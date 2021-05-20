# Web Screenshot Script
Web Screenshot Script is a Python script that takes screenshots of websites given their URLs to ensure they are working properly. 

# Prerequisites
## Supported Browsers
Chrome is the only supported browser. Only Chrome version 90.0.4430.212 has been tested.

## Libraries
### Selenium
Selenium's installation instructions can be found [here](https://selenium-python.readthedocs.io/installation.html). Ensure you install the correct version of the driver for your version of Chrome and add it to your PATH, as described in the Selenium installation instructions.

### Pillow
To install Pillow with pip, open the terminal and type `pip install Pillow`

# Running the Script
1. Clone the repository or download error_img.jpg and screenshot_script.py.
2. Open the terminal and navigate to the directory containing screenshot_script.py and error_img.jpg.
3. Type `python -m screenshot_script` followed by each URL that needs to be visited. i.e. `python -m screenshot_script URL1 URL2 URL3 etc.`. There is no limit on the number of URLs that can be entered as arguments. *Note: some installations of Python may require `py -m ...` or similar to be typed instead of `python -m ...`*.
3. Chrome will open a new window and visit each site. **Do not touch your computer during this process.** When all URLs have been visited, Chrome will close automatically. 
5. The screenshots the script takes can be found in the same folder as the script. Screenshots are resized to 400x300 pixels and will be named based off of their respective URLs. The name of the screenshot for a specific URL will be the same each time the program runs, meaning the old screenshot of the website will be replaced.

# Errors and Warnings
- "usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)" can be ignored and will not affect the functionality of the script.
- If there is a problem with a URL, the script will save a default image "error_img.jpg" in place of a screenshot of the site.
- This script was created for certain, short URLs; if the name generated from the URL for the screenshot is longer than the filename character limit, the screenshot will not be saved.