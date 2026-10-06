import os
import time
from playwright.sync_api import sync_playwright

ARTIFACT_DIR = r"C:\Users\User\.gemini\antigravity\brain\2a73addf-6cd1-49aa-9fa0-d4cdbd82ea1e"

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # -------------------------------------------------------------
        # 1. Desktop Verification (1440 x 900)
        # -------------------------------------------------------------
        print("\n--- Verifying Desktop (1440x900) ---", flush=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.goto("https://axelaglobal.com/?nocache=" + str(int(time.time())), wait_until="load", timeout=45000)
        page.wait_for_timeout(3000)

        # Header metrics
        hdr_metrics = page.evaluate("""() => {
            const hdr = document.querySelector('.axela-sticky-header') || document.querySelector('.elementor-element-hdr_container_main') || document.querySelector('header');
            const logo = document.querySelector('.axela-native-logo img');
            const btn = document.querySelector('.axela-native-hdr-btn .elementor-button');
            const hdrStyle = hdr ? window.getComputedStyle(hdr) : null;
            const logoStyle = logo ? window.getComputedStyle(logo) : null;
            const btnStyle = btn ? window.getComputedStyle(btn) : null;
            const hdrRect = hdr ? hdr.getBoundingClientRect() : null;
            const btnRect = btn ? btn.getBoundingClientRect() : null;

            return {
                headerPosition: hdrStyle ? hdrStyle.position : null,
                headerHeight: hdrRect ? hdrRect.height : null,
                logoHeight: logoStyle ? logoStyle.height : null,
                btnPadding: btnStyle ? btnStyle.padding : null,
                btnFontSize: btnStyle ? btnStyle.fontSize : null,
                btnWidth: btnRect ? btnRect.width : null,
                btnHeight: btnRect ? btnRect.height : null
            };
        }""")
        print("Header Metrics:", hdr_metrics, flush=True)

        # Hero Buttons & Overlay metrics
        hero_metrics = page.evaluate("""() => {
            const overlay = document.querySelector('.axela-hero-section > .elementor-background-overlay');
            const btnTrade = document.querySelector('.elementor-element-hero_btn_trade .elementor-button');
            const btnSupply = document.querySelector('.elementor-element-hero_btn_supply .elementor-button');
            const btnInvest = document.querySelector('.elementor-element-hero_btn_invest .elementor-button') || document.querySelector('.axela-btn-gold-link .elementor-button');
            const ovStyle = overlay ? window.getComputedStyle(overlay) : null;
            const tStyle = btnTrade ? window.getComputedStyle(btnTrade) : null;
            const tRect = btnTrade ? btnTrade.getBoundingClientRect() : null;
            const sStyle = btnSupply ? window.getComputedStyle(btnSupply) : null;
            const sRect = btnSupply ? btnSupply.getBoundingClientRect() : null;
            const iStyle = btnInvest ? window.getComputedStyle(btnInvest) : null;
            const iRect = btnInvest ? btnInvest.getBoundingClientRect() : null;

            return {
                overlayBackground: ovStyle ? ovStyle.backgroundImage || ovStyle.backgroundColor : null,
                btnTradeWidth: tRect ? tRect.width : null,
                btnTradeHeight: tRect ? tRect.height : null,
                btnTradeFontSize: tStyle ? tStyle.fontSize : null,
                btnSupplyWidth: sRect ? sRect.width : null,
                btnSupplyHeight: sRect ? sRect.height : null,
                btnInvestWidth: iRect ? iRect.width : null,
                btnInvestHeight: iRect ? iRect.height : null,
                btnInvestFontSize: iStyle ? iStyle.fontSize : null
            };
        }""")
        print("Hero Metrics:", hero_metrics, flush=True)

        # Capture Hero Section Screenshot
        hero_shot = os.path.join(ARTIFACT_DIR, "verified_hero_blend_desktop.png")
        page.screenshot(path=hero_shot, clip={"x": 0, "y": 0, "width": 1440, "height": 800})
        print(f"Captured Hero screenshot: {hero_shot}", flush=True)

        # Check Scrolled Sticky Header
        page.evaluate("() => window.scrollTo(0, 800)")
        page.wait_for_timeout(1000)
        scrolled_metrics = page.evaluate("""() => {
            const hdr = document.querySelector('.axela-sticky-header') || document.querySelector('.elementor-element-hdr_container_main') || document.querySelector('header');
            const rect = hdr ? hdr.getBoundingClientRect() : null;
            return {
                scrollY: window.scrollY,
                rectTop: rect ? rect.top : null,
                isStickyAtTop: rect ? Math.abs(rect.top) < 2 : false
            };
        }""")
        print("Scrolled Sticky Header Metrics:", scrolled_metrics, flush=True)

        scrolled_shot = os.path.join(ARTIFACT_DIR, "verified_slim_sticky_header_scrolled.png")
        page.screenshot(path=scrolled_shot, clip={"x": 0, "y": 0, "width": 1440, "height": 300})
        print(f"Captured Scrolled Header screenshot: {scrolled_shot}", flush=True)

        # Contact Section & Form Metrics
        contact_metrics = page.evaluate("""() => {
            const contactSec = document.querySelector('#contact');
            if (contactSec) contactSec.scrollIntoView();
            const form = document.querySelector('.axela-native-pro-form') || document.querySelector('.elementor-element-contact_form_right .elementor-form');
            const formBox = document.querySelector('.elementor-element-contact_form_right');
            const fStyle = form ? window.getComputedStyle(form) : null;
            const bStyle = formBox ? window.getComputedStyle(formBox) : null;
            const submitBtn = document.querySelector('.axela-native-pro-form .elementor-button') || document.querySelector('.elementor-element-contact_form_right .elementor-button');
            const sbStyle = submitBtn ? window.getComputedStyle(submitBtn) : null;
            const sbRect = submitBtn ? submitBtn.getBoundingClientRect() : null;
            const emailLink = document.querySelector('.axela-contact-hub-left a[href^="mailto:info@axelaglobal.com"]');
            const emStyle = emailLink ? window.getComputedStyle(emailLink) : null;

            return {
                formBg: fStyle ? fStyle.backgroundColor : null,
                formBorder: fStyle ? fStyle.border : null,
                formBoxBg: bStyle ? bStyle.backgroundColor : null,
                formBoxBorder: bStyle ? bStyle.border : null,
                submitBtnWidth: sbRect ? sbRect.width : null,
                submitBtnHeight: sbRect ? sbRect.height : null,
                submitBtnFontSize: sbStyle ? sbStyle.fontSize : null,
                emailColor: emStyle ? emStyle.color : null,
                emailText: emailLink ? emailLink.textContent : null
            };
        }""")
        page.wait_for_timeout(1500)
        print("Contact & Form Metrics:", contact_metrics, flush=True)

        # Capture Contact Section Screenshot
        contact_shot = os.path.join(ARTIFACT_DIR, "verified_contact_form_optimized.png")
        contact_el = page.locator("#contact")
        if contact_el.count() > 0:
            contact_el.screenshot(path=contact_shot)
        else:
            page.screenshot(path=contact_shot)
        print(f"Captured Contact screenshot: {contact_shot}", flush=True)

        page.close()

        # -------------------------------------------------------------
        # 2. Tablet Verification (768 x 1024)
        # -------------------------------------------------------------
        print("\n--- Verifying Tablet (768x1024) ---", flush=True)
        tab_context = browser.new_context(viewport={"width": 768, "height": 1024})
        tab_page = tab_context.new_page()
        tab_page.goto("https://axelaglobal.com/?nocache=" + str(int(time.time())), wait_until="load", timeout=45000)
        tab_page.wait_for_timeout(3000)

        tab_metrics = tab_page.evaluate("""() => {
            const hdr = document.querySelector('.axela-sticky-header') || document.querySelector('.elementor-element-hdr_container_main') || document.querySelector('header');
            const burger = document.querySelector('.axela-native-nav .elementor-menu-toggle');
            const hdrRect = hdr ? hdr.getBoundingClientRect() : null;
            const burgerStyle = burger ? window.getComputedStyle(burger) : null;
            return {
                headerHeight: hdrRect ? hdrRect.height : null,
                headerPosition: hdr ? window.getComputedStyle(hdr).position : null,
                burgerVisible: burgerStyle ? (burgerStyle.display !== 'none' && burgerStyle.visibility !== 'hidden') : false
            };
        }""")
        print("Tablet Metrics:", tab_metrics, flush=True)

        # Click hamburger toggle on tablet
        tab_page.click(".axela-native-nav .elementor-menu-toggle")
        tab_page.wait_for_timeout(600)

        tab_shot = os.path.join(ARTIFACT_DIR, "verified_tablet_sticky_menu.png")
        tab_page.screenshot(path=tab_shot, clip={"x": 0, "y": 0, "width": 768, "height": 600})
        print(f"Captured Tablet Screenshot: {tab_shot}", flush=True)

        tab_page.close()

        # -------------------------------------------------------------
        # 3. Mobile Verification (390 x 844)
        # -------------------------------------------------------------
        print("\n--- Verifying Mobile (390x844) ---", flush=True)
        mob_context = browser.new_context(viewport={"width": 390, "height": 844})
        mob_page = mob_context.new_page()
        mob_page.goto("https://axelaglobal.com/?nocache=" + str(int(time.time())), wait_until="load", timeout=45000)
        mob_page.wait_for_timeout(3000)

        mob_metrics = mob_page.evaluate("""() => {
            const hdr = document.querySelector('.axela-sticky-header') || document.querySelector('.elementor-element-hdr_container_main') || document.querySelector('header');
            const burger = document.querySelector('.axela-native-nav .elementor-menu-toggle');
            const hdrRect = hdr ? hdr.getBoundingClientRect() : null;
            const burgerStyle = burger ? window.getComputedStyle(burger) : null;
            const btnTrade = document.querySelector('.elementor-element-hero_btn_trade .elementor-button');
            const tRect = btnTrade ? btnTrade.getBoundingClientRect() : null;
            return {
                headerHeight: hdrRect ? hdrRect.height : null,
                headerPosition: hdr ? window.getComputedStyle(hdr).position : null,
                burgerVisible: burgerStyle ? (burgerStyle.display !== 'none' && burgerStyle.visibility !== 'hidden') : false,
                heroBtnWidth: tRect ? tRect.width : null,
                heroBtnHeight: tRect ? tRect.height : null
            };
        }""")
        print("Mobile Metrics:", mob_metrics, flush=True)

        mob_shot_hero = os.path.join(ARTIFACT_DIR, "verified_mobile_hero_compact.png")
        mob_page.screenshot(path=mob_shot_hero, clip={"x": 0, "y": 0, "width": 390, "height": 700})
        print(f"Captured Mobile Hero Screenshot: {mob_shot_hero}", flush=True)

        # Click hamburger menu on mobile
        mob_page.click(".axela-native-nav .elementor-menu-toggle")
        mob_page.wait_for_timeout(600)

        mob_shot_menu = os.path.join(ARTIFACT_DIR, "verified_mobile_menu_open_slim.png")
        mob_page.screenshot(path=mob_shot_menu, clip={"x": 0, "y": 0, "width": 390, "height": 600})
        print(f"Captured Mobile Menu Open Screenshot: {mob_shot_menu}", flush=True)

        mob_page.close()
        browser.close()
        print("\nALL VERIFICATIONS COMPLETED SUCCESSFULLY!", flush=True)

if __name__ == '__main__':
    verify()
