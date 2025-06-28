# import re
# import cv2
# import easyocr
# import matplotlib.pyplot as plt

# def aadhar_extractor(image_path):

#     reader = easyocr.Reader(['en', 'hi'])

#     img = cv2.imread(image_path, cv2.COLOR_BGR2HLS)

#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

#     result = reader.readtext(img, paragraph=True)

#     for box, text in result:
#         top_left = tuple(box[0])
#         bottom_right = tuple(box[2])
#         cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)
#         cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        
#     for i, (text) in enumerate(result):
#         result_list = [result]
#         result_list.append({
#             'text': text,
#         })

#     data = [result_list]
#     def extract_strings(data):
#         strings = []
#         if isinstance(data, str):
#             strings.append(data)
#         elif isinstance(data, list):
#             for item in data:
#                 strings.extend(extract_strings(item))
#         elif isinstance(data, dict):
#             for value in data.items():
#                 strings.extend(extract_strings(value))
#         return strings

#     strings_only = extract_strings(data)

#     data = strings_only
#     strings = [word for phrase in data for word in phrase.split()]

#     print("Words list:", strings)
    
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     plt.title('Face and Text Recognition')
#     plt.axis('off') 
#     plt.show()

# ############################################### Name ###############################################

#     my_list4 = strings[7:11]
#     english_name = [element for element in my_list4 if element.isalpha() and all(char.isascii() for char in element)]
#     english_string4 = ' '.join(english_name)
#     print(english_string4)

# ############################################### DOB ###############################################

#     my_list5 = strings[11:18]
#     dob = [":", "DOB", "DOB:", "Birth", "Binth"]
#     for element in dob:
#         if element in my_list5:
#             dob = my_list5[my_list5.index(element)+1]
#     print(dob)

# ############################################### Gender ###############################################

#     my_list6 = strings
#     gender = "Male" or "Female" or "MALE" or "FEMALE"
#     if gender in my_list6:
#         print(gender)

# ############################################### Aadhar Number ###############################################

#     my_list7 = strings
#     element = my_list7.index('Male' or 'Female' or 'MALE' or 'FEMALE')
#     updated_value = [value.replace(':', ' ') for value in my_list7[element + 1:]]
#     updated_value2 = [value.replace('_', ' ') for value in updated_value[0:4]]
#     aadhar_no_seperate = [word for phrase in updated_value2 for word in phrase.split()]
#     aadhar_no = [value for value in aadhar_no_seperate if value.isnumeric()]
#     string7 = ' '.join(aadhar_no)
#     print(string7[:14])

# aadhar_extractor("aadharimages/aadhar1.jpg")

import re
import cv2
import easyocr
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def aadhar_extractor():
    # Use Tkinter to open a file dialog for selecting the image
    Tk().withdraw()  # Hide the root Tkinter window
    image_path = askopenfilename(title="Select Aadhaar Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    if not image_path:  # Check if no file is selected
        print("No file selected. Exiting.")
        return

    # Initialize the EasyOCR Reader
    reader = easyocr.Reader(['en', 'hi'])

    # Read the image
    img = cv2.imread(image_path, cv2.COLOR_BGR2HLS)

    # Detect faces in the image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Perform OCR on the image
    result = reader.readtext(img, paragraph=True)

    # Highlight the recognized text in the image
    for box, text in result:
        top_left = tuple(box[0])
        bottom_right = tuple(box[2])
        cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)
        cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

    # Extract text from the OCR results
    result_list = []
    for _, text in result:
        result_list.append({'text': text})

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

    strings_only = extract_strings(result_list)

    # Process the strings
    strings = [word for phrase in strings_only for word in phrase.split()]
    print("Words list:", strings)

    # Display the image with annotations
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Face and Text Recognition')
    plt.axis('off')
    plt.show()

# Call the function
aadhar_extractor()
