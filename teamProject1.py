# 영어 텍스트 인식 프로그램
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread('image.png') 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

extracted_text = pytesseract.image_to_string(gray_image)

if extracted_text.strip():  
    print("<추출된 텍스트>")
    print(extracted_text)
else:
    print("텍스트를 추출 불가능.")