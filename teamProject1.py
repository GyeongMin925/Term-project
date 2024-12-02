import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows의 경우 경로 설정

image = cv2.imread('./image/answk56.jpg') 

if image is None:
    print("Image Could Not Be Opened.")
    exit()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_image = clahe.apply(gray_image)

_, thresh_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blurred_image = cv2.GaussianBlur(thresh_image, (5, 5), 0)

custom_config = r'--oem 1 --psm 6'  
lang = 'eng' 

text = pytesseract.image_to_string(blurred_image, config=custom_config, lang=lang)

print("<인식된 텍스트>")
print(text)

scale_percent = 50 
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

resized_original = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
resized_processed = cv2.resize(blurred_image, dim, interpolation=cv2.INTER_AREA)

cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Processed Image', cv2.WINDOW_NORMAL)

cv2.imshow('Original Image', resized_original)
cv2.imshow('Processed Image', resized_processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
