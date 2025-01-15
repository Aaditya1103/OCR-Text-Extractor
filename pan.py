import re
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def pan_extractor(photo_path, languages=['eng', 'hin']):
    try:
        with Image.open(photo_path) as img:
            text = pytesseract.image_to_string(img, lang='+'.join(languages))
            boxes = pytesseract.image_to_boxes(img, lang='+'.join(languages))
            return text, boxes
    except Exception as e:
        print(f"Error in pan_extractor: {e}")
        return "", ""

def pan_face_detector():
    # Use tkinter to select the image file
    Tk().withdraw()  # Hide the root tkinter window
    image_path = askopenfilename(title="Select PAN/Aadhaar Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    
    if not image_path:  # Handle case where no file is selected
        print("No file selected. Exiting.")
        return

    # Read the image using OpenCV
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Extract text and bounding boxes using pan_extractor
    text, boxes = pan_extractor(image_path)
    if boxes:
        for b in boxes.splitlines():
            b = b.split()
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, img.shape[0] - y), (w, img.shape[0] - h), (0, 255, 0), 2)

    # Display the processed image with rectangles
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()

    # Save each detected face as a separate image
    for i, (x, y, w, h) in enumerate(faces):
        face_img = img[y:y + h, x:x + w]
        face_with_box = cv2.rectangle(face_img.copy(), (0, 0), (w, h), (255, 0, 0), 2)
        plt.imshow(face_with_box)
        plt.axis('off')
        plt.savefig(f'face_{i + 1}.jpg')
        plt.show()

    return text

# Extract text from image
extracted_text = pan_face_detector()

# Process extracted text
if extracted_text:
    result_list = [extracted_text]
    result_list.append({'text': extracted_text})

    data = [result_list]

    def extract_strings(data):
        strings = []
        if isinstance(data, str):
            strings.append(data)
        elif isinstance(data, list):
            for item in data:
                strings.extend(extract_strings(item))
        elif isinstance(data, dict):
            for value in data.values():
                strings.extend(extract_strings(value))
        return strings


    # Define unwanted characters
    not_required = [':', '-', '/', '—', '*', '|', '=', '1', '2', '3', '4', '5', '6', '7', '9', '0']

    # Extract only the strings
    strings_only = extract_strings(data)
    data = strings_only
    strings = [word for phrase in data for word in phrase.split()]
    strings_filtered = [element for element in strings if element not in not_required]

    print("Words list:", strings_filtered)      

############################################### Account Number ###############################################

    my_list = strings
    d_fact = 'Card'
    if d_fact in my_list:
        number = my_list[my_list.index(d_fact)+1]
    print(number)

############################################### Name ###############################################

    my_list2 = strings_filtered
    english_name = [element for element in my_list2 if element.isalpha() and all(char.isascii() for char in element)]
    names = ["Name", "Nate", "NaTe"]
    for element in names:
        if element in my_list2:
            index_of_name = my_list2.index(element)
    name_string = my_list2[index_of_name+1:index_of_name+5]
    english_name = [item for item in name_string if not any(ord(char) > 127 for char in item)]
    string3 = ' '.join(english_name)
    print(string3)

############################################### Father Name ###############################################

    my_list3 = strings_filtered[index_of_name+5:]
    english_fname = [element for element in my_list3 if element.isalpha() and all(char.isascii() for char in element)]
    fnames = ["Name", "Nate", "NaTe", "Fathers", "Gender"]
    for element in names:
        if element in my_list3:
            index_of_fname = my_list3.index(element)
    name_string = my_list3[index_of_fname+1:index_of_fname+4]
    english_fname_string = [item for item in name_string if not any(ord(char) > 127 for char in item)]
    english_fname = [element for element in english_fname_string if element not in fnames]
    final_fname = [item for item in english_fname if not any(char.isdigit() for char in item)]
    string4 = ' '.join(final_fname)
    print(string4)

############################################### DOB ###############################################

    my_list4 = strings
    date_pattern = re.compile(r'\b(\d{2}/\d{2}/\d{4})\b')
    for item in my_list4:
        match = re.search(date_pattern, item)
        if match:
            date_of_birth = match.group(1)
            print(date_of_birth)
            break

