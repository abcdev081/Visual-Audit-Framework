# config/config.py

settings = {
    # Appium Server & Device Capabilities
    "appium_server_url": "http://127.0.0.1:4723", # Appium server URL, replace with your server address (this is default)
    #For the below 4, change according to your device
    "deviceName": "Android Emulator", 
    "udid": "emulator-5554",
    "platformName": "Android",#
    "platformVersion": "16.0",

    # Application Details
    "appPackage": "com.sample.app.sampleapp",#Change this to your app's package name
    "appActivity": ".MainActivity",# Change this to your app's main activity

    # Behavior Flags
    "noReset": True,
    "fullReset": False,
    
    # Misc
    "screenshotDir": "screenshots",# Directory to save screenshots
    "ocrLanguage": "eng" # Language for OCR, change if needed
}
