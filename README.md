# Term-project
# OCR Image Text Recognition with Tesseract and OpenCV

This project demonstrates how to perform Optical Character Recognition (OCR) on images using Tesseract and OpenCV in Python. The program processes an input image, applies image enhancement techniques, and extracts text using the Tesseract OCR engine.

![image](https://github.com/user-attachments/assets/cd9174ab-17f7-4019-a1e1-68fa6befaf28)
![image](https://github.com/user-attachments/assets/48f828bf-7da1-4657-a078-cce32597c210)
![image](https://github.com/user-attachments/assets/7b7eee31-b9e0-4844-b699-7f51e4242b58)


## Features
- **Image Preprocessing**:
  - Converts the image to grayscale.
  - Enhances contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization).
  - Removes noise using Gaussian Blur.
  - Applies binarization (Otsu's thresholding) for improved text recognition.
- **Text Recognition**:
  - Extracts text from the processed image using Tesseract OCR.
  - Supports customization through OCR configuration options (`--oem` and `--psm`).
- **Visual Output**:
  - Displays the original and processed images in resizable windows.

---

## Prerequisites

### Software Requirements
1. Python 3.7 or later
2. Tesseract OCR engine installed on your system
3. Python packages:
   - `opencv-python`
   - `pytesseract`

### Installation
1. Install Python dependencies:
   ```bash
   pip install opencv-python pytesseract
