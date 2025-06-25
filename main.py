from appium import webdriver
from config.config import settings
from tests.app_test import run_full_flow

def main():
    from appium.options.android import UiAutomator2Options

    options = UiAutomator2Options()
    options.platform_name = settings["platformName"]
    options.platform_version = settings["platformVersion"]
    options.device_name = settings["deviceName"]
    options.udid = settings["udid"]
    options.app_package = settings["appPackage"]
    options.app_activity = settings["appActivity"]
    options.no_reset = settings["noReset"]
    options.dont_stop_app_on_reset = settings["dontStopAppOnReset"]

    driver = webdriver.Remote(
        command_executor=settings["appium_server_url"],
        options=options
    )

    print("App launched. Please complete login process, then press Enter...")
    input()  # Wait for your manual login completion

    run_full_flow(driver)

    driver.quit()

if __name__ == "__main__":
    main()
