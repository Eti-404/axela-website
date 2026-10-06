import os
import time
from playwright.sync_api import sync_playwright

def verify_footer():
    artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\2a73addf-6cd1-49aa-9fa0-d4cdbd82ea1e"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Desktop Verification
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()
        print("Navigating to https://axelaglobal.com/ (Desktop)...", flush=True)
        page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        page.wait_for_timeout(3000)
        
        footer_loc = page.locator(".axela-slim-footer")
        footer_loc.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        
        footer_info = page.evaluate("""() => {
            const footer = document.querySelector('.axela-slim-footer, footer');
            if (!footer) return { found: false };
            
            const logo = footer.querySelector('.axela-footer-logo');
            const servicesText = footer.querySelector('.axela-footer-services-text');
            
            let servicesStyle = null;
            if (servicesText) {
                const cs = window.getComputedStyle(servicesText);
                servicesStyle = {
                    fontSize: cs.fontSize,
                    color: cs.color,
                    letterSpacing: cs.letterSpacing,
                    textTransform: cs.textTransform,
                    fontFamily: cs.fontFamily,
                    lineHeight: cs.lineHeight
                };
            }
            
            return {
                found: true,
                hasLogo: !!logo,
                logoSrc: logo ? logo.src : null,
                hasServicesText: !!servicesText,
                text: servicesText ? servicesText.innerText.trim() : null,
                style: servicesStyle
            };
        }""")
        
        print("FOOTER_INFO_DESKTOP:", footer_info, flush=True)
        
        desktop_img_path = os.path.join(artifact_dir, "verified_footer_services_desktop.png")
        footer_loc.screenshot(path=desktop_img_path)
        print(f"Saved desktop footer screenshot: {desktop_img_path}", flush=True)
        
        # 2. Mobile Verification
        print("Navigating to https://axelaglobal.com/ (Mobile)...", flush=True)
        m_context = browser.new_context(viewport={'width': 375, 'height': 812}, is_mobile=True, user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1")
        m_page = m_context.new_page()
        m_page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        m_page.wait_for_timeout(3000)
        
        m_footer_loc = m_page.locator(".axela-slim-footer")
        m_footer_loc.scroll_into_view_if_needed()
        m_page.wait_for_timeout(1000)
        
        mobile_img_path = os.path.join(artifact_dir, "verified_footer_services_mobile.png")
        m_footer_loc.screenshot(path=mobile_img_path)
        print(f"Saved mobile footer screenshot: {mobile_img_path}", flush=True)
        
        browser.close()
        print("FOOTER_VERIFICATION_COMPLETE", flush=True)

if __name__ == '__main__':
    verify_footer()
