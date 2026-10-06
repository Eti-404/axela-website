import re
import json
import base64
import urllib.request

BASE_URL = "https://axelaglobal.com"
AUTH_STR = "admin:FYCY 52pM wknI 1nOf 4RA2 t8zP"
AUTH_B64 = base64.b64encode(AUTH_STR.encode("ascii")).decode("ascii")
headers = {
    "Authorization": f"Basic {AUTH_B64}",
    "Content-Type": "application/json"
}

def run_wp_cli(cmd):
    url = f"{BASE_URL}/wp-json/wpvibe/v1/cli/run"
    payload = json.dumps({"command": cmd}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error ({cmd}):", e)
        return None

def main():
    with open('update_master_css.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Section Spacing and Scroll-Margin-Top
    old_spacing = re.search(r'/\* Universal Section Spacing.*?\n\.axela-section,[\s\S]*?padding:\s*50px\s*0\s*!important;[\s\S]*?box-sizing:\s*border-box\s*!important;\s*\}', content)
    if old_spacing:
        new_spacing = """/* Universal Section Spacing & Menu Scroll Margin Offset */
#about, #services, #products, #approach, #network, #routes, #investment, #ethics, #contact,
.axela-section,
.axela-services-section,
.axela-products-section,
.axela-approach-section,
.axela-network-section,
.axela-invest-section,
.axela-ethics-section,
.axela-contact-section,
.axela-about-section {
  padding-top: 105px !important;
  padding-bottom: 105px !important;
  scroll-margin-top: 90px !important;
  position: relative !important;
  width: 100% !important;
  border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
  box-sizing: border-box !important;
}

@media (max-width: 767px) {
  #about, #services, #products, #approach, #network, #routes, #investment, #ethics, #contact,
  .axela-section,
  .axela-services-section,
  .axela-products-section,
  .axela-approach-section,
  .axela-network-section,
  .axela-invest-section,
  .axela-ethics-section,
  .axela-contact-section,
  .axela-about-section {
    padding-top: 60px !important;
    padding-bottom: 60px !important;
    scroll-margin-top: 70px !important;
  }
}"""
        content = content.replace(old_spacing.group(0), new_spacing)
        print("Updated section spacing and scroll-margin-top.")
    else:
        print("Warning: old spacing pattern not matched.")

    # 2. Update Products Split-Blend Banner (Natural overlay & soft mask)
    old_banner = re.search(r'/\* Split Blend Warehouse Banner.*?\.axela-products-split-banner,[\s\S]*?\.axela-prod-banner-text', content)
    if old_banner:
        new_banner = """/* Split Blend Warehouse Banner (Petrotraders / Screenshot 2026-10-06 142745.jpg Spec) */
.axela-products-split-banner,
.elementor-element-prod_split_banner {
  position: relative !important;
  min-height: 420px !important;
  border-radius: 6px !important;
  overflow: hidden !important;
  margin-bottom: 24px !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5) !important;
  box-sizing: border-box !important;
  display: flex !important;
  align-items: center !important;
  background: url('https://axelaglobal.com/wp-content/uploads/2026/10/port-terminal-infrastructure.webp') no-repeat center right / cover !important;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 10%, black 90%, transparent 100%) !important;
  mask-image: linear-gradient(to bottom, transparent 0%, black 10%, black 90%, transparent 100%) !important;
}

.axela-products-split-banner::before,
.elementor-element-prod_split_banner::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(
    to right,
    #040911 0%,
    #040911 38%,
    rgba(4, 9, 17, 0.85) 50%,
    rgba(4, 9, 17, 0.45) 68%,
    transparent 100%
  ) !important;
  z-index: 1 !important;
  pointer-events: none !important;
}

.axela-prod-banner-text"""
        content = content.replace(old_banner.group(0), new_banner)
        print("Updated products split banner styling.")
    else:
        print("Warning: old banner pattern not matched.")

    # 3. Update icon colors to Strict Standard Golden #D4AF37
    # Service card icon
    content = re.sub(
        r'(\.service-card-icon-sleek[\s\S]*?background:\s*)rgba\(218,\s*66,\s*60,\s*0\.12\)(\s*!important;\s*border:\s*1px\s*solid\s*)rgba\(218,\s*66,\s*60,\s*0\.30\)(\s*!important;\s*color:\s*)#DA423C(\s*!important;)',
        r'\1rgba(212, 175, 55, 0.12)\2rgba(212, 175, 55, 0.30)\3#D4AF37\4',
        content
    )
    # Category icon inline
    content = re.sub(
        r'(\.category-icon-inline\s*\.elementor-icon\s*\{[\s\S]*?color:\s*)#DA423C(\s*!important;)',
        r'\1#D4AF37\2',
        content
    )
    # Ethics icon sleek
    content = re.sub(
        r'(\.ethics-icon-sleek[\s\S]*?color:\s*)#DA423C(\s*!important;)',
        r'\1#D4AF37\2',
        content
    )
    print("Updated icon colors to #D4AF37.")

    # 4. Remove all font-family: ... !important; from css_rules
    # Client requirement: Exclude all hardcoded !important on font-family so Elementor Global Typography governs styles
    before_count = len(re.findall(r'font-family:[^;]+!important;', content))
    content = re.sub(r'font-family:\s*([^;!]+)\s*!important;', r'/* font-family: \1; */', content)
    after_count = len(re.findall(r'font-family:[^;]+!important;', content))
    print(f"Removed font-family !important rules: {before_count} before -> {after_count} after.")

    # Save update_master_css.py
    with open('update_master_css.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Saved update_master_css.py.")

    # Also update custom-css/global-dark-theme.css
    with open('custom-css/global-dark-theme.css', 'w', encoding='utf-8') as f:
        # extract css_rules from update_master_css.py
        m = re.search(r'css_rules\s*=\s*"""([\s\S]*?)"""', content)
        if m:
            f.write(m.group(1).strip())
            print("Updated custom-css/global-dark-theme.css.")

    # Run update_master_css.py to deploy to Post 40 and regenerate Elementor CSS
    print("\nExecuting update_master_css.py to push to Post 40 and flush caches...")

if __name__ == '__main__':
    main()
