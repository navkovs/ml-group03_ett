import os
import glob
import asyncio
import pyppdf.patch_pyppeteer
from pyppeteer import launch
from datetime import datetime
import random


async def main():

    # delete all previous files in screenshots folder
    files = glob.glob('screenshots/*')
    for f in files:
        os.remove(f)

    # create timestamp for screenshots
    timestamp = str(datetime.now())

    # open browser page with website
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto('file:///Users/vanessa/group03_ett/html/index.html')

    # take screenshot of initial website
    await page.waitFor(1000)
    await page.screenshot({'path': 'screenshots/01_homepage_' + timestamp + '.png', 'fullPage': True})

    # select route in dropdown menu (does not work) and take a screenshot
    await page.click('#route')
    await page.keyboard.press('ArrowDown')
    await page.keyboard.press('Enter')

    await page.waitFor(1000)
    await page.screenshot({'path': 'screenshots/02_selectPort_' + timestamp + '.png', 'fullPage': True})

    # create random inputs
    latitude = str(random.randint(30, 70))
    longitude = str(random.randint(-10, 30))
    # speed = str(random.randint(0, 150))
    length = str(random.randint(0, 500))
    breadth = str(random.randint(0, 100))

    # put random values into input forms, calculate, take screenshot
    await page.focus('#latitude')
    await page.keyboard.type(latitude)

    await page.focus('#longitude')
    await page.keyboard.type(longitude)

    # await page.focus('#speed')
    # await page.keyboard.type(speed)

    await page.focus('#length')
    await page.keyboard.type(length)

    await page.focus('#breadth')
    await page.keyboard.type(breadth)

    await page.click('#calculateETT')

    await page.waitFor(1000)
    await page.screenshot({'path': 'screenshots/03_ETTCalculated_' + timestamp + '.png', 'fullPage': True})

    # zoom out on map, take screenshot
    await page.focus('#osm')
    await page.click('[title="Zoom out"]')

    await page.waitFor(2000)
    await page.screenshot({'path': 'screenshots/04_zoomOut_' + timestamp + '.png', 'fullPage': True})

    # close browser
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
