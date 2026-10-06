import os
import time
from playwright.sync_api import sync_playwright

def verify():
    artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\2a73addf-6cd1-49aa-9fa0-d4cdbd82ea1e"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # -------------------------------------------------------------
        # 1. Desktop Verification
        # -------------------------------------------------------------
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()
        print("Navigating to https://axelaglobal.com/ (Desktop)...", flush=True)
        page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        page.wait_for_timeout(3000)
        
        # Test Sticky Header on Scroll
        page.evaluate("window.scrollTo(0, 1000);")
        page.wait_for_timeout(1000)
        
        header_scrolled_info = page.evaluate("""() => {
            const hdr = document.querySelector('.elementor-element-hdr_container_main, .axela-sticky-header');
            if (!hdr) return { found: false };
            const rect = hdr.getBoundingClientRect();
            const cs = window.getComputedStyle(hdr);
            return {
                found: true,
                position: cs.position,
                top: cs.top,
                rectTop: rect.top,
                rectHeight: rect.height,
                isStickyAtTop: rect.top === 0
            };
        }""")
        print("HEADER_SCROLLED_DESKTOP:", header_scrolled_info, flush=True)
        
        # Screenshot of scrolled desktop showing sticky header
        scrolled_img = os.path.join(artifact_dir, "verified_sticky_header_scrolled.png")
        page.screenshot(path=scrolled_img, clip={'x': 0, 'y': 0, 'width': 1440, 'height': 400})
        print(f"Saved: {scrolled_img}", flush=True)
        
        # Test Products Banner Overlay
        page.evaluate("document.querySelector('#products').scrollIntoView();")
        page.wait_for_timeout(1500)
        prod_loc = page.locator(".elementor-element-prod_split_banner, .axela-products-split-banner")
        prod_img = os.path.join(artifact_dir, "verified_products_banner_soft_overlay.png")
        prod_loc.screenshot(path=prod_img)
        print(f"Saved: {prod_img}", flush=True)
        
        # Test Footer
        footer_loc = page.locator(".axela-slim-footer")
        footer_loc.scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        
        footer_info = page.evaluate("""() => {
            const ftr = document.querySelector('.axela-slim-footer');
            if (!ftr) return { found: false };
            const logo = ftr.querySelector('.axela-footer-logo');
            const services = ftr.querySelector('.axela-footer-services-text');
            const copy = ftr.querySelector('.axela-footer-copy');
            const nav = ftr.querySelector('.axela-footer-nav');
            
            return {
                found: true,
                logoHeight: logo ? logo.clientHeight : null,
                servicesText: services ? services.innerText.trim() : null,
                servicesMaxWidth: services ? window.getComputedStyle(services).maxWidth : null,
                copyText: copy ? copy.innerText.trim() : null,
                navDisplay: nav ? window.getComputedStyle(nav).display : null,
                navGridCols: nav ? window.getComputedStyle(nav).gridTemplateColumns : null
            };
        }""")
        print("FOOTER_INFO_DESKTOP:", footer_info, flush=True)
        
        footer_img = os.path.join(artifact_dir, "verified_footer_reorganized.png")
        footer_loc.screenshot(path=footer_img)
        print(f"Saved: {footer_img}", flush=True)
        
        # -------------------------------------------------------------
        # 2. Mobile Verification
        # -------------------------------------------------------------
        print("Navigating to https://axelaglobal.com/ (Mobile)...", flush=True)
        m_context = browser.new_context(viewport={'width': 375, 'height': 812}, is_mobile=True, user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1")
        m_page = m_context.new_page()
        m_page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        m_page.wait_for_timeout(3000)
        
        # Scroll down and test sticky header
        m_page.evaluate("window.scrollTo(0, 800);")
        m_page.wait_for_timeout(1000)
        
        m_header_info = m_page.evaluate("""() => {
            const hdr = document.querySelector('.elementor-element-hdr_container_main, .axela-sticky-header');
            if (!hdr) return { found: false };
            const rect = hdr.getBoundingClientRect();
            const cs = window.getComputedStyle(hdr);
            return {
                found: true,
                position: cs.position,
                rectTop: rect.top,
                rectHeight: rect.height,
                isStickyAtTop: rect.top === 0
            };
        }""")
        print("HEADER_SCROLLED_MOBILE:", m_header_info, flush=True)
        
        # Click hamburger menu while scrolled to test menu accessibility
        toggle = m_page.locator(".elementor-menu-toggle").first
        if toggle.is_visible():
            toggle.click()
            m_page.wait_for_timeout(1000)
            
        m_scrolled_img = os.path.join(artifact_dir, "verified_mobile_sticky_header.png")
        m_page.screenshot(path=m_scrolled_img, clip={'x': 0, 'y': 0, 'width': 375, 'height': 500})
        print(f"Saved: {m_scrolled_img}", flush=True)
        
        # Mobile footer screenshot
        m_ftr = m_page.locator(".axela-slim-footer")
        m_ftr.scroll_into_view_if_needed()
        m_page.wait_for_timeout(1000)
        m_ftr_img = os.path.join(artifact_dir, "verified_mobile_footer_reorganized.png")
        m_ftr.screenshot(path=m_ftr_img)
        print(f"Saved: {m_ftr_img}", flush=True)
        
        browser.close()
        print("ALL_VERIFICATIONS_COMPLETE", flush=True)

if __name__ == '__main__':
    verify()
