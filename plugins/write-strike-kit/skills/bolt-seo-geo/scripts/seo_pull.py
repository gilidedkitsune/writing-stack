#!/usr/bin/env python3
"""bolt-seo-geo: live SEO data puller for bolt.new (GA4 + Google Search Console).

Reads via OAuth, signed in AS the user (not a service account). That matters because
"Full" access in Search Console and "Editor" in Analytics can READ through the API but
cannot grant a service-account user. Signing in as the user reads through whatever access
that user already has.

CREDENTIALS live OUTSIDE this skill, in ~/.config/claude-seo/ (per-user, never shared):
  oauth_client.json   the Desktop OAuth client you download from Google Cloud Console
  token.json          created on first `auth`; your saved sign-in
  config.json         (optional) overrides the baked-in bolt.new defaults below

Defaults are baked in for bolt.new, so the data commands work with no config file.

Commands:
  auth                                  one-time browser sign-in; saves token.json
  properties                            list GA4 properties this account can see (find the right ID)
  ga4 [--property <id>] [--days 28]     GA4 traffic by channel (sessions, users, engagement, views)
  gsc [--site <url>] [--dimension query|page] [--days 28] [--limit 25]   GSC search performance

Setup is documented in the skill's SKILL.md. Python deps:
  pip install google-auth google-auth-oauthlib google-api-python-client
"""
import argparse, json, os, sys, http.server, urllib.parse, webbrowser
from datetime import date, timedelta

CONFIG_DIR = os.path.expanduser("~/.config/claude-seo")
CLIENT = os.path.join(CONFIG_DIR, "oauth_client.json")
TOKEN = os.path.join(CONFIG_DIR, "token.json")
AUTH_URL_FILE = os.path.join(CONFIG_DIR, "auth_url.txt")
SCOPES = [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/webmasters.readonly",
]
REDIRECT_PORT = 8765
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/"

# Baked-in defaults for bolt.new. A config.json in CONFIG_DIR can override either key.
#   ga4_property: the GA4 property literally named "bolt.new" (NOT 102991586, which has no access)
#   gsc_site:     a Search Console *Domain* property, so the sc-domain: form is required
#                 (the https://bolt.new/ URL-prefix form returns 403)
DEFAULTS = {
    "ga4_property": "properties/464310328",
    "gsc_site": "sc-domain:bolt.new",
}


def _config():
    p = os.path.join(CONFIG_DIR, "config.json")
    return json.load(open(p)) if os.path.exists(p) else {}


def _default(key):
    """CLI arg (handled by caller) > config.json override > baked-in bolt.new default."""
    return _config().get(key) or DEFAULTS.get(key)


def _load_creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not os.path.exists(TOKEN):
        sys.exit("No saved sign-in. Run the `auth` command first.")
    creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN, "w") as f:
            f.write(creds.to_json())
    return creds


def cmd_auth(args):
    if not os.path.exists(CLIENT):
        sys.exit(f"Missing OAuth client. Download the Desktop client from Google Cloud "
                 f"Console and save it as {CLIENT} (see the skill's SKILL.md setup steps).")
    from google_auth_oauthlib.flow import Flow
    flow = Flow.from_client_secrets_file(CLIENT, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    auth_url, _ = flow.authorization_url(access_type="offline", prompt="consent", include_granted_scopes="true")
    with open(AUTH_URL_FILE, "w") as f:
        f.write(auth_url)
    print("AUTH_URL: " + auth_url, flush=True)
    holder = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if "code" in params:
                holder["code"] = params["code"][0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Connected. You can close this tab and return to Claude.</h2>")

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("localhost", REDIRECT_PORT), H)
    try:
        webbrowser.open(auth_url)
    except Exception:
        pass
    while "code" not in holder:
        srv.handle_request()
    flow.fetch_token(code=holder["code"])
    with open(TOKEN, "w") as f:
        f.write(flow.credentials.to_json())
    print("OK: signed in, token saved to " + TOKEN)


def cmd_properties(args):
    from googleapiclient.discovery import build
    admin = build("analyticsadmin", "v1beta", credentials=_load_creds(), cache_discovery=False)
    res = admin.accountSummaries().list().execute()
    out = []
    for acct in res.get("accountSummaries", []):
        for p in acct.get("propertySummaries", []):
            out.append({"property": p.get("property"), "name": p.get("displayName"), "account": acct.get("displayName")})
    print(json.dumps(out, indent=2))


def cmd_ga4(args):
    from googleapiclient.discovery import build
    prop_id = args.property or _default("ga4_property")
    if not prop_id:
        sys.exit("No GA4 property. Pass --property or set ga4_property in config.json")
    data = build("analyticsdata", "v1beta", credentials=_load_creds(), cache_discovery=False)
    prop = str(prop_id) if str(prop_id).startswith("properties/") else f"properties/{prop_id}"
    body = {
        "dateRanges": [{"startDate": f"{args.days}daysAgo", "endDate": "yesterday"}],
        "dimensions": [{"name": "sessionDefaultChannelGroup"}],
        "metrics": [{"name": "sessions"}, {"name": "totalUsers"}, {"name": "engagementRate"}, {"name": "screenPageViews"}],
        "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}],
    }
    print(json.dumps(data.properties().runReport(property=prop, body=body).execute(), indent=2))


def cmd_gsc(args):
    from googleapiclient.discovery import build
    site = args.site or _default("gsc_site")
    if not site:
        sys.exit("No GSC site. Pass --site or set gsc_site in config.json")
    sc = build("webmasters", "v3", credentials=_load_creds(), cache_discovery=False)
    end = date.today() - timedelta(days=3)   # GSC data lags 2-3 days
    start = end - timedelta(days=args.days)
    body = {"startDate": str(start), "endDate": str(end), "dimensions": [args.dimension], "rowLimit": args.limit}
    print(json.dumps(sc.searchanalytics().query(siteUrl=site, body=body).execute(), indent=2))


def main():
    ap = argparse.ArgumentParser(description="bolt-seo-geo data puller (GA4 + GSC), signed in as the user")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth")
    sub.add_parser("properties")
    g = sub.add_parser("ga4")
    g.add_argument("--property")
    g.add_argument("--days", type=int, default=28)
    s = sub.add_parser("gsc")
    s.add_argument("--site")
    s.add_argument("--dimension", default="query")
    s.add_argument("--days", type=int, default=28)
    s.add_argument("--limit", type=int, default=25)
    args = ap.parse_args()
    {"auth": cmd_auth, "properties": cmd_properties, "ga4": cmd_ga4, "gsc": cmd_gsc}[args.cmd](args)


if __name__ == "__main__":
    main()
