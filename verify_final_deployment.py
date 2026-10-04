import asyncio
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Desktop
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://axelaglobal.com/", wait_until="networkidle")
        await page.wait_for_timeout(2500)

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

        # Footer crop
        footer_loc = page.locator(".axela-slim-footer, .axela-footer-section")
        if await footer_loc.count() > 0:
            await footer_loc.first.screenshot(path="final_footer.png")
            print("Saved final_footer.png")

        # Mobile
        page_m = await browser.new_page(viewport={"width": 390, "height": 844})
        await page_m.goto("https://axelaglobal.com/", wait_until="networkidle")
        await page_m.wait_for_timeout(2500)
        await page_m.screenshot(path="final_verified_mobile.png", full_page=True)
        print("Saved final_verified_mobile.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(verify())
