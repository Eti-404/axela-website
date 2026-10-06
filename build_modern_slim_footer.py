import json
import urllib.request
import base64

BASE_URL = "https://axelaglobal.com"
AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
headers = {
    "Authorization": f"Basic {AUTH_B64}",
    "Content-Type": "application/json"
}

def run_cli(command):
    url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
    payload = json.dumps({"command": command}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def update_footer():
    # Modern slim footer HTML matching petrotraders.com
    footer_html = """
<footer class="axela-slim-footer">
  <style>
    .axela-slim-footer {
      background: #04070D;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 56px 0 34px 0;
      color: #94A3B8;
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      width: 100%;
    }
    .axela-footer-inner {
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
    }
    .axela-footer-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 40px;
      margin-bottom: 34px;
    }
    .axela-footer-brand {
      display: flex;
      flex-direction: column;
      gap: 14px;
      max-width: 380px;
    }
    .axela-footer-logo {
      height: 40px;
      max-height: 42px !important;
      width: auto !important;
      max-width: 220px !important;
      display: block;
    }
    .axela-footer-services-text {
      font-size: 11px;
      font-weight: 500;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #94A3B8;
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      line-height: 1.6;
      max-width: 360px;
      margin: 0;
      text-align: left;
    }
    .axela-footer-tagline {
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #64748B;
      font-family: 'Barlow Condensed', sans-serif;
      font-weight: 600;
    }
    .axela-footer-nav {
      display: grid;
      grid-template-columns: repeat(3, auto);
      gap: 12px 36px;
      list-style: none;
      margin: 0;
      padding: 0;
      justify-content: end;
    }
    .axela-footer-nav a {
      color: #94A3B8;
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: color 0.2s ease;
    }
    .axela-footer-nav a:hover {
      color: #DA423C;
    }
    .axela-footer-divider {
      border: 0;
      height: 1px;
      background: rgba(255, 255, 255, 0.18);
      margin: 0 0 22px 0;
    }
    .axela-footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 12px;
      color: #64748B;
    }
    .axela-footer-bottom-links {
      display: flex;
      gap: 20px;
      align-items: center;
      flex-wrap: wrap;
    }
    .axela-footer-bottom-links a {
      color: #64748B;
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .axela-footer-bottom-links a:hover {
      color: #D4AF37;
    }
    @media (max-width: 768px) {
      .axela-footer-top {
        flex-direction: column;
        align-items: flex-start;
        gap: 24px;
      }
      .axela-footer-brand {
        max-width: 100%;
        gap: 12px;
      }
      .axela-footer-services-text {
        max-width: 100%;
        font-size: 11px;
        line-height: 1.6;
      }
      .axela-footer-nav {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px 24px;
        width: 100%;
        justify-content: start;
      }
      .axela-footer-bottom {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
      }
    }
  </style>

  <div class="axela-footer-inner">
    <div class="axela-footer-top">
      <div class="axela-footer-brand">
        <a href="#home" style="display:inline-block;">
          <img src="https://axelaglobal.com/wp-content/uploads/2026/10/cropped-Axela-Limited-Transparent-Logo.png" alt="AXELA Limited" class="axela-footer-logo" />
        </a>
        <div class="axela-footer-services-text">ENERGY • COMMODITIES • TRADING • SUPPLY • PROJECT DEVELOPMENT • INVESTMENT ADVISORY</div>
      </div>

      <ul class="axela-footer-nav">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#products">Products</a></li>
        <li><a href="#approach">Approach</a></li>
        <li><a href="#network">Routes</a></li>
        <li><a href="#investment">Investment</a></li>
        <li><a href="#ethics">Ethics</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </div>

    <hr class="axela-footer-divider" />

    <div class="axela-footer-bottom">
      <div>
        <p class="axela-footer-copy" style="margin:0; font-size: 12px; color: #94A3B8;">© 2026 AXELA LTD. All rights reserved | Digital Growth Partner: E-GUIDER</p>
      </div>
      <div class="axela-footer-bottom-links">
        <a href="#ethics">Privacy &amp; Compliance</a>
        <a href="#approach">Terms of Trade</a>
      </div>
    </div>
  </div>
</footer>
"""

    footer_data = [
        {
            "id": "axela_slim_footer_root",
            "elType": "container",
            "settings": {
                "content_width": "full",
                "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
                "_css_classes": "axela-footer-slim-root"
            },
            "elements": [
                {
                    "id": "axela_slim_footer_html",
                    "elType": "widget",
                    "widgetType": "html",
                    "settings": {
                        "html": footer_html
                    },
                    "elements": []
                }
            ],
            "isInner": False
        }
    ]

    print("Updating Post 38 (Global Dark Footer) via WPVibe save-page...")
    payload = {
        "id": 38,
        "title": "AXELA LTD. — Global Dark Footer",
        "status": "publish",
        "data": footer_data
    }
    req = urllib.request.Request(
        f"{BASE_URL}/wp-json/wpvibe/v1/elementor/save-page",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("Footer update result:", res)

    print("\nFlushing Elementor CSS...")
    run_cli("elementor flush-css --regenerate")
    print("Purging LiteSpeed...")
    run_cli("litespeed-purge all")
    print("Footer updated and flushed successfully!")

if __name__ == '__main__':
    update_footer()
