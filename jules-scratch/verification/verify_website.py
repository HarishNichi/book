import asyncio
from playwright.async_api import async_playwright
import pathlib

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Get the absolute path to the index.html file
        file_path = pathlib.Path("index.html").resolve()

        # Navigate to the local file
        await page.goto(f"file://{file_path}")

        # Wait for the page to load and the fade-in animation to complete
        await page.wait_for_timeout(1000)

        # Take a screenshot
        await page.screenshot(path="jules-scratch/verification/verification_toc.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
