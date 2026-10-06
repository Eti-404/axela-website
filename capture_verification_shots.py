import asyncio
from playwright.async_api import async_playwright

async def snap():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("https://axelaglobal.com/", wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # Products section
        prod_el = await page.query_selector("#products")
        if prod_el:
            await prod_el.screenshot(path="verified_products_blend.png")
            print("Saved verified_products_blend.png")

        # Services section
        svc_el = await page.query_selector("#services")
        if svc_el:
            await svc_el.screenshot(path="verified_services_gold.png")
            print("Saved verified_services_gold.png")

        # Ethics section
        eth_el = await page.query_selector("#ethics")
        if eth_el:
            await eth_el.screenshot(path="verified_ethics_lock.png")
            print("Saved verified_ethics_lock.png")

        # Contact section
        cnt_el = await page.query_selector("#contact")
        if cnt_el:
            await cnt_el.screenshot(path="verified_contact_form.png")
            print("Saved verified_contact_form.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(snap())
