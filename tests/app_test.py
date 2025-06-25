import os
import time
import cv2
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import settings
from utils.image_utils import capture_screenshot, compare_images
from utils.ocr_utils import extract_text_from_image
from utils.spellcheckertool import check_spelling
from utils.gestures import swipe_down, swipe_up



################################################################################
# Core “Sweep” Routine: Scroll, capture screenshots until the bottom is reached,
# perform OCR and spell-check, then scroll back up.
################################################################################
def perform_sweep(driver, screenshot_prefix):
    screenshot_dir = settings["screenshotDir"]
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    screenshots = []
    max_scrolls = 10
    scroll_count = 0
    reached_end = False

    while not reached_end and scroll_count < max_scrolls:
        filename = os.path.join(screenshot_dir, f"{screenshot_prefix}_{scroll_count}.png")
        capture_screenshot(driver, filename)
        screenshots.append(filename)
        print(f"Captured screenshot: {filename}")

        if scroll_count > 0:
            img_prev = cv2.imread(screenshots[scroll_count - 1])
            img_curr = cv2.imread(screenshots[scroll_count])
            similarity = compare_images(img_prev, img_curr)
            print(f"Similarity between screenshots: {similarity:.2f}")
            if similarity >= 0.95:
                print("Reached end of scrollable content.")
                reached_end = True
                break

        swipe_down(driver)
        scroll_count += 1
        time.sleep(2)  # Allow UI to settle

    # Process OCR and spell-check for each captured screenshot.
    for ss in screenshots:
        text = extract_text_from_image(ss, lang=settings["ocrLanguage"])
        errors = check_spelling(text)
        if errors:
            print(f"Spelling errors in {ss}: {errors}")
        else:
            print(f"No spelling errors found in {ss}")

    # Scroll back up to the top.
    for _ in range(10):  # The number of times to swipe up can be adjusted.
        swipe_up(driver)
        time.sleep(1)
    print("Scrolled back to top.")

################################################################################
# Universal Navigation and Sweep Function
# This function receives:
#  • entry_xpath: The XPath of the button that starts the navigation.
#  • depth: The number of additional buttons to press (each representing one level) to reach the target page.
#  • screenshot_prefix: A prefix used when saving the screenshots.
#
# The function works as follows:
#  1. Click the entry button.
#  2. For each level (depth), ask for the next button’s XPath (in the universal version).
#  3. Once at the deepest level, perform the sweep routine.
#  4. Then, for each level, press the native Android back button (driver.back()),
#     performing a sweep after each back press until you return to the home page.
################################################################################
def universal_navigate_and_sweep(driver, entry_xpath, depth, screenshot_prefix="SS"):
    # Step 1: Click the entry button.
    try:
        entry_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, entry_xpath))
        )
        entry_element.click()
        print(f"Clicked entry element: {entry_xpath}")
    except Exception as e:
        print(f"Failed to click entry element: {entry_xpath}. Error: {e}")
        return
    time.sleep(2)

    # Step 2: For each depth level, get the corresponding button XPath.
    for i in range(depth):
        button_xpath = input(f"Enter the XPath for button level {i+1}: ")
        try:
            button_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, button_xpath))
            )
            button_element.click()
            print(f"Clicked button level {i+1}: {button_xpath}")
        except Exception as e:
            print(f"Failed to click button level {i+1}: {button_xpath}. Error: {e}")
            return
        time.sleep(2)

    # Step 3: At the deepest level, perform the sweep.
    print("Performing sweep at deepest level...")
    perform_sweep(driver, screenshot_prefix)

    # Step 4: Navigate back to the home page using the native back button.
    for i in range(depth):
        driver.back()  # Use the native Android back button.
        print(f"Pressed native back button (iteration {i+1}).")
        time.sleep(2)
        # Optionally perform a sweep at each back level.
        perform_sweep(driver, f"{screenshot_prefix}_back{i+1}")

    print("Returned to home page using native back navigation.")

################################################################################
# Helper: Run the Universal Test
# Prompts the user for the necessary input (except the screenshot prefix,
# depending on the SS_PREFIX_OPTION flag), then calls universal_navigate_and_sweep().
################################################################################

SS_PREFIX_OPTION = False # Set to True if you want to prompt for screenshot prefix.

def run_universal_test(driver):
    entry_xpath = input("Enter the entry XPath for the universal test: ")
    depth = int(input("Enter the number of buttons (depth) to press: "))
    if SS_PREFIX_OPTION:
        screenshot_prefix = input("Enter the screenshot prefix for this test: ")
    else:
        screenshot_prefix = "SS"
    universal_navigate_and_sweep(driver, entry_xpath, depth, screenshot_prefix)

################################################################################
# Full Flow: For this example, the full flow simply runs the universal test.
################################################################################
def run_full_flow(driver):
    run_universal_test(driver)
