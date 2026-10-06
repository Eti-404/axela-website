import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Desktop
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://axelaglobal.com/", wait_until="networkidle", timeout=60000)
        await page.evaluate("""() => new Promise(resolve => {
            const img = new Image();
            img.onload = img.onerror = resolve;
            img.src = 'https://axelaglobal.com/wp-content/uploads/2026/10/port-terminal-infrastructure.webp';
        })""")
        await page.wait_for_timeout(2000)

        # Full page
        await page.screenshot(path="final_verified_desktop.png", full_page=True)
        print("Saved final_verified_desktop.png")

        # Section-specific crops
        sections = [
            ("about", "final_about.png"),
            ("services", "final_services.png"),
            ("products", "final_products.png"),
            ("approach", "final_approach.png"),
            ("network", "final_routes_map.png"),
            ("investment", "final_investment.png"),
            ("ethics", "final_ethics.png"),
            ("contact", "final_contact.png")
        ]

        for sec_id, filename in sections:
            loc = page.locator(f"#{sec_id}")
            if await loc.count() > 0:
                await loc.first.screenshot(path=filename)
                print(f"Saved {filename}")

        # Header crop (scroll to top)
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(600)
        await page.screenshot(path="final_header.png", clip={"x": 0, "y": 0, "width": 1440, "height": 140})
        print("Saved final_header.png")

        # Hero crop
        await page.screenshot(path="final_hero.png", clip={"x": 0, "y": 140, "width": 1440, "height": 650})
        print("Saved final_hero.png")

        # Scrolled Sticky Header check (scroll to 800px)
        await page.evaluate("window.scrollTo(0, 800)")
        await page.wait_for_timeout(600)
        await page.screenshot(path="final_sticky_scrolled.png", clip={"x": 0, "y": 0, "width": 1440, "height": 140})
        print("Saved final_sticky_scrolled.png")

        # Footer crop
        footer_loc = page.locator(".axela-slim-footer, .axela-footer-section")
        if await footer_loc.count() > 0:
            await footer_loc.first.screenshot(path="final_footer.png")
            print("Saved final_footer.png")

        # Mobile
        page_m = await browser.new_page(viewport={"width": 390, "height": 844})
        await page_m.goto("https://axelaglobal.com/", wait_until="domcontentloaded", timeout=60000)
        await page_m.wait_for_timeout(3500)
        await page_m.screenshot(path="final_verified_mobile.png", full_page=True)
        print("Saved final_verified_mobile.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(verify())
