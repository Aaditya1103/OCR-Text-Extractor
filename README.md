# OCR-Text-Extractor
An entry-level Python tool using Tesseract OCR to extract text from Aadhaar, PAN, and Voter ID cards. Simplistic implementation, suitable for beginners exploring OCR concepts and basic document data extraction workflows.
# Aadhaar and PAN Image Processing Tool

This repository contains two Python scripts for processing Aadhaar and PAN card images. These tools leverage Optical Character Recognition (OCR) to extract textual information and detect faces from the images. The tools also provide functionality to display and annotate the processed images with bounding boxes.

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation and Setup](#installation-and-setup)
4. [Usage Instructions](#usage-instructions)
    - [Aadhaar OCR Tool](#aadhaar-ocr-tool)
    - [PAN Face Detector and OCR](#pan-face-detector-and-ocr)
5. [Example Outputs](#example-outputs)
6. [Folder Structure](#folder-structure)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)
10. [Author](#author)

---

## Features

### Aadhaar OCR Tool
- **Multilingual OCR**: Extracts text in both English and Hindi using EasyOCR.
- **Face Detection**: Detects and highlights faces within the Aadhaar card image using Haar cascades.
- **Text Highlighting**: Annotates the image with bounding boxes around detected text.
- **Dynamic Input**: Allows users to select Aadhaar card images dynamically via a file dialog.
- **Filtered Text Output**: Cleans the extracted text to remove unwanted characters and numbers.

### PAN Face Detector and OCR
- **Face Detection**: Uses Haar cascades to identify and highlight faces in PAN card images.
- **OCR with Bounding Boxes**: Utilizes Tesseract OCR to extract text and mark bounding boxes around individual characters.
- **Face Cropping and Saving**: Crops detected faces and saves them as separate image files.
- **Dynamic Input**: Prompts users to select PAN card images dynamically.
- **Filtered Text Output**: Processes and filters the extracted text to ensure cleaner results.

---

## Technologies Used

- **Python**: Programming language for scripting and processing.
- **Libraries**:
  - [OpenCV](https://opencv.org/): Image processing and face detection.
  - [EasyOCR](https://github.com/JaidedAI/EasyOCR): OCR engine for multilingual text recognition.
  - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract): OCR engine for text extraction.
  - [Pillow](https://python-pillow.org/): Image handling and manipulation.
  - [Matplotlib](https://matplotlib.org/): Visualization and annotation of processed images.
  - [Tkinter](https://docs.python.org/3/library/tkinter.html): GUI for file dialog to select images.

---

## Installation and Setup

### Prerequisites
1. **Python 3.8+**: Install Python from [here](https://www.python.org/downloads/).
2. **Tesseract OCR**:
   - Install Tesseract OCR on your system:
     - **Windows**: [Download Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
     - **Linux**: Use `sudo apt install tesseract-ocr`.
     - **macOS**: Use Homebrew: `brew install tesseract`.
3. **Install Python Libraries**:
   - Install the required libraries using pip:
     ```bash
     pip install opencv-python-headless matplotlib pytesseract pillow easyocr
     ```

### Setting Up the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aadhaar-pan-processing.git
   cd aadhaar-pan-processing

