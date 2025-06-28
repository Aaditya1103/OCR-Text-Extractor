import numpy as np
from PIL import Image
import re
import pytesseract

def aadhar_extractor(photo_path, languages=['eng', 'hin']):
    try:
        with Image.open(photo_path) as img:
            text = pytesseract.image_to_string(img, lang='+'.join(languages))
            return text
    except Exception as e:
        print(f"Error: {e}")
        return None

image_path = 'VOTERID.jpg'

extracted_text = aadhar_extractor(image_path)
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

not_required = [':','-','/','—']
strings_only = extract_strings(data)
data = strings_only
strings = [word for phrase in data for word in phrase.split()]
strings2 = [element for element in strings if element not in not_required]

print("Words list:", strings2)

# ############################################### Name ###############################################

# my_list = strings2
# english_name = [element for element in my_list if element.isalpha() and all(char.isascii() for char in element)]
# names = ["Name", "Nate", "NaTe"]
# for element in names:
#     if element in my_list:
#         index_of_name = my_list.index(element)
# name_string = my_list[index_of_name+1:index_of_name+5]
# english_name = [item for item in name_string if not any(ord(char) > 127 for char in item)]
# string3 = ' '.join(english_name)
# print(string3)

# ############################################### Father Name ###############################################

# my_list2 = strings2[index_of_name+5:]
# english_fname = [element for element in my_list2 if element.isalpha() and all(char.isascii() for char in element)]
# fnames = ["Name", "Nate", "NaTe", "Fathers", "Gender"]
# for element in names:
#     if element in my_list2:
#         index_of_fname = my_list2.index(element)
# name_string = my_list2[index_of_fname+1:index_of_fname+5]
# english_fname_string = [item for item in name_string if not any(ord(char) > 127 for char in item)]
# english_fname = [element for element in english_fname_string if element not in fnames]
# string4 = ' '.join(english_fname)
# print(string4)

# ############################################### DOB ###############################################

# my_list5 = strings2
# date_pattern = re.compile(r'\b(\d{2}-\d{2}-\d{4})\b')
# for item in my_list5:
#     match = re.search(date_pattern, item)
#     if match:
#         date_of_birth = match.group(1)
#         print(date_of_birth)
#         break

# ############################################### Gender ###############################################

# my_list6 = strings2
# gender = "Male" or "Female"
# if gender in my_list6:
#     print(gender)
