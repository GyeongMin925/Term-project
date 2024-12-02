from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng+kor')
        return text
    except Exception as e:
        return f"Error: {e}"

image_path = "image.png"

extracted_text = extract_text_from_image(image_path)
print("Extracted Text:")
print(extracted_text)
