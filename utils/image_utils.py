# utils/image_utils.py

def capture_screenshot(driver, filename):
    driver.get_screenshot_as_file(filename)

def compare_images(img1, img2):# Compare two images using Structural Similarity Index (SSIM)

    from skimage.metrics import structural_similarity as ssim
    import cv2

    # Convert images to grayscale as it is more efficient for comparison
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, _ = ssim(gray1, gray2, full=True)
    return score
