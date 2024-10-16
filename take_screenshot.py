import asyncio
import logging
from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def take_screenshot():
    logger.info("Starting screenshot process")
    async with async_playwright() as p:
        logger.info("Launching browser")
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        logger.info("Navigating to https://vercel3d.vercel.app/")
        await page.goto("https://vercel3d.vercel.app/")
        
        logger.info("Waiting for model-viewer to load")
        await page.wait_for_selector("model-viewer")
        
        logger.info("Waiting additional 5 seconds for 3D model to render")
        await asyncio.sleep(5)
        
        logger.info("Taking screenshot")
        await page.screenshot(path="social_share_image.png", full_page=True)
        
        logger.info("Closing browser")
        await browser.close()
    
    logger.info("Screenshot process completed")

if __name__ == "__main__":
    asyncio.run(take_screenshot())
