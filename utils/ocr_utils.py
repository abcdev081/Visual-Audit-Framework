import pytesseract
import os
import cv2

os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"# Ensure the Tesseract data path is set correctly to your Tesseract installation directory, this is hardcoded to avoid errors

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"#Same as above

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding for better OCR accuracy
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extract_text_from_image(image_path, lang="eng"):
    processed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_img, lang=lang)
    return text
