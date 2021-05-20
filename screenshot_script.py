# run in vscode terminal: .\screenshot_script.py URLs
# run in command prompt: python -m screenshot_script URLs
# "usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: 
# A device attached to the system is not functioning. (0x1F)" can safely be ignored

# .\screenshot_script.py https://bcs.livingskysd.ca/ https://bready.livingskysd.ca/ https://cando.livingskysd.ca/ https://connaught.livingskysd.ca/ https://ckcs.livingskysd.ca/ https://hafford.livingskysd.ca/ https://hces.livingskysd.ca/ https://heritage.livingskysd.ca/ https://kerrobert.livingskysd.ca/ https://lawrence.livingskysd.ca/ https://leoville.livingskysd.ca/ https://lssdvirtual.livingskysd.ca/ https://luseland.livingskysd.ca/ https://macklin.livingskysd.ca/ https://maymont.livingskysd.ca/ https://mckitrick.livingskysd.ca/ https://mclurg.livingskysd.ca/ https://medstead.livingskysd.ca/ https://nces.livingskysd.ca/ https://nbchs.livingskysd.ca/ https://shs.livingskysd.ca/ https://stvital.livingskysd.ca/ https://uchs.livingskysd.ca/ https://ups.livingskysd.ca/ https://www.livingskysd.ca/
# python -m screenshot_script https://bcs.livingskysd.ca/ https://bready.livingskysd.ca/ https://cando.livingskysd.ca/ https://connaught.livingskysd.ca/ https://ckcs.livingskysd.ca/ https://hafford.livingskysd.ca/ https://hces.livingskysd.ca/ https://heritage.livingskysd.ca/ https://kerrobert.livingskysd.ca/ https://lawrence.livingskysd.ca/ https://leoville.livingskysd.ca/ https://lssdvirtual.livingskysd.ca/ https://luseland.livingskysd.ca/ https://macklin.livingskysd.ca/ https://maymont.livingskysd.ca/ https://mckitrick.livingskysd.ca/ https://mclurg.livingskysd.ca/ https://medstead.livingskysd.ca/ https://nces.livingskysd.ca/ https://nbchs.livingskysd.ca/ https://shs.livingskysd.ca/ https://stvital.livingskysd.ca/ https://uchs.livingskysd.ca/ https://ups.livingskysd.ca/ https://www.livingskysd.ca/

import sys
from selenium import webdriver
from PIL import ImageGrab
from PIL import Image
import time


driver = webdriver.Chrome() #open chrome
driver.maximize_window()
for _ in sys.argv:
    if _ != sys.argv[0]: #the first argument is this file, so skip it
        name = str(_)
        if name == "https://www.livingskysd.ca/":
            name = "lskysd"
        elif len(name) <= 24: #this should not happen with school URLs, just for preventing errors
            name = "".join( x for x in name if (x.isalnum()))
        else:
            name = name[8:-16] #converts URL to schoolname
            name = "".join( x for x in name if (x.isalnum()))
        name = name + ".jpg"
        try:
            driver.get(str(_))
            time.sleep(2) #webdriver waits for the page to load but sometimes they need longer
            image = ImageGrab.grab()
            image = image.crop((0, 0, image.width, image.height - 40)) #crop off the taskbar
            image = image.resize((400, 300))
            image.save(name) 
        except:
            print(str(_), "is an invalid address or there was an error saving the image")
            try:
                error_image = Image.open("error_img.jpg")
                error_image.save(name)
            except:
                print("There was an error updating the image for", str(_))

driver.close() #closes chrome after all sites have been visited
