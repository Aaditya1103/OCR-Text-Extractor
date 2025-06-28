import numpy as np
from PIL import Image
from aadhar2a import backaadhar_extract1
from aadhar2b import backaadhar_extract2
import pytesseract

def aadharb_extractor(photo_path, languages=['eng', 'hin']):
    try:
        with Image.open(photo_path) as img:
            text = pytesseract.image_to_string(img, lang='+'.join(languages))
            return text
    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = 'backaadharimages/aadharb_1.jpg'

extracted_text = aadharb_extractor(image_path)
for i, (text) in enumerate(extracted_text):
    append_text = text
    
result_list = [extracted_text]
result_list.append({
    'text': append_text,
})

data = [result_list]
def extract_strings(data):
    strings = []
    if isinstance(data, str):
        strings.append(data)
    elif isinstance(data, list):
        for item in data:
            strings.extend(extract_strings(item))
    elif isinstance(data, dict):
        for value in data.items():
            strings.extend(extract_strings(value))
    return strings

strings_only = extract_strings(data)
data = strings_only
strings = [word for phrase in data for word in phrase.split()]
print("Words list:", strings)

detect_address = ["Address", "Address:"]
for element in detect_address:
    index = strings.index(element) if element in strings else -1
    
    if index != -1 and index + 2 < len(strings):
        next_element_1 = strings[index + 1]
        next_element_2 = strings[index + 2]        
        next_element_3 = strings[index + 3]        
        next_element_4 = strings[index + 4]        
        next_element_5 = strings[index + 5]
        is_hindi = any(any('\u0900' <= char <= '\u097F' for char in element) for element in [next_element_1, next_element_2, next_element_3, next_element_4, next_element_5])
        
        if is_hindi:
            backaadhar_extract1(image_path)
        else:
            backaadhar_extract2(image_path)


    
    
    
    
    

