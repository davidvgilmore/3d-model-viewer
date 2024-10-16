import asyncio
from playwright.async_api import async_playwright

async def test_model_viewer():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Navigate to the local file
        await page.goto(f"http://localhost:63356")
        
        # Wait for the model-viewer to load
        await page.wait_for_selector("model-viewer")
        
        # Check if the model-viewer is visible
        model_viewer = await page.query_selector("model-viewer")
        is_visible = await model_viewer.is_visible()
        
        if is_visible:
            print("3D Model Viewer loaded successfully!")
        else:
            print("Error: 3D Model Viewer not visible.")
        
        # Take a screenshot
        await page.screenshot(path="model_viewer_screenshot.png")
        print("Screenshot saved as model_viewer_screenshot.png")
        
        await browser.close()

asyncio.run(test_model_viewer())
