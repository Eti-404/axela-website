import os
import sys
import time
from playwright.sync_api import sync_playwright

def verify_hero():
    artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\2a73addf-6cd1-49aa-9fa0-d4cdbd82ea1e"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # 1. Desktop Verification
        context = browser.new_context(viewport={'width': 1440, 'height': 900})
        page = context.new_page()
        print("Navigating to https://axelaglobal.com/ (Desktop)...", flush=True)
        page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        page.wait_for_timeout(4000) # allow video to play and render
        
        video_info = page.evaluate("""() => {
            const hero = document.querySelector('#home, .axela-hero-section');
            if (!hero) return { found: false, error: 'Hero section not found' };
            
            const video = hero.querySelector('video');
            const overlay = hero.querySelector('.elementor-background-overlay');
            const heading = hero.querySelector('.axela-hero-title h1, .axela-hero-title .elementor-heading-title');
            const buttons = Array.from(hero.querySelectorAll('.axela-hero-btn a, .axela-hero-btn .elementor-button')).map(b => b.innerText.trim());
            
            let overlayStyle = null;
            if (overlay) {
                const cs = window.getComputedStyle(overlay);
                overlayStyle = {
                    backgroundColor: cs.backgroundColor,
                    backgroundImage: cs.backgroundImage,
                    zIndex: cs.zIndex,
                    opacity: cs.opacity
                };
            }
            
            return {
                found: true,
                hasVideo: !!video,
                videoSrc: video ? (video.currentSrc || video.src || (video.querySelector('source') ? video.querySelector('source').src : '')) : null,
                videoAutoplay: video ? video.autoplay : null,
                videoLoop: video ? video.loop : null,
                videoMuted: video ? video.muted : null,
                videoPaused: video ? video.paused : null,
                videoReadyState: video ? video.readyState : null,
                overlayStyle: overlayStyle,
                headingText: heading ? heading.innerText.trim() : null,
                buttons: buttons
            };
        }""")
        
        print("HERO_VIDEO_INFO_DESKTOP:", video_info, flush=True)
        
        # Take desktop screenshot
        desktop_img_path = os.path.join(artifact_dir, "verified_hero_video_desktop.png")
        page.screenshot(path=desktop_img_path, clip={'x': 0, 'y': 0, 'width': 1440, 'height': 850})
        print(f"Saved desktop screenshot: {desktop_img_path}", flush=True)
        
        # 2. Mobile Verification
        print("Navigating to https://axelaglobal.com/ (Mobile)...", flush=True)
        m_context = browser.new_context(viewport={'width': 375, 'height': 812}, is_mobile=True, user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1")
        m_page = m_context.new_page()
        m_page.goto('https://axelaglobal.com/?nocache=' + str(int(time.time())), wait_until='load', timeout=45000)
        m_page.wait_for_timeout(4000)
        
        mobile_info = m_page.evaluate("""() => {
            const hero = document.querySelector('#home, .axela-hero-section');
            if (!hero) return { found: false };
            const video = hero.querySelector('video');
            return {
                hasVideo: !!video,
                videoSrc: video ? (video.currentSrc || video.src || (video.querySelector('source') ? video.querySelector('source').src : '')) : null,
                videoPlaying: video ? !video.paused : null
            };
        }""")
        print("HERO_VIDEO_INFO_MOBILE:", mobile_info, flush=True)
        
        mobile_img_path = os.path.join(artifact_dir, "verified_hero_video_mobile.png")
        m_page.screenshot(path=mobile_img_path, clip={'x': 0, 'y': 0, 'width': 375, 'height': 780})
        print(f"Saved mobile screenshot: {mobile_img_path}", flush=True)
        
        browser.close()
        print("VERIFICATION_COMPLETE", flush=True)

if __name__ == '__main__':
    verify_hero()
