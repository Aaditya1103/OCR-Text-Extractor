from PIL import Image
from matplotlib import pyplot as plt
import pytesseract
import cv2

def backaadhar_extract2(image_path, languages=['eng']):
    image = cv2.imread(image_path)
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    text = pytesseract.image_to_string(image_pil, lang='+'.join(languages))
    strings_only = [line.strip() for line in text.split('\n')]
    data = strings_only
    strings = [word for phrase in data for word in phrase.split()]
    
    my_list = strings
    detect_address = ["Address", "Address:"]
    detect_pincode = [word for word in strings if word.isdigit() and len(word) == 6]

    index_of_address = None
    for element in detect_address:
        if element in my_list:
            index_of_address = my_list.index(element)
            break

    if index_of_address is not None:
        final_address = my_list[index_of_address + 1:]

        index_of_pincode = None
        for element in detect_pincode:
            if element in final_address:
                index_of_pincode = final_address.index(element)
                break
        if index_of_pincode is not None:
            final_address2 = final_address[:index_of_pincode+1]
        Address = ' '.join(final_address2)
        print(Address)
            
            