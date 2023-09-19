from pytesseract import pytesseract
from PIL import Image

img = Image.open('/home/my_image.png')

text = pytesseract.image_to_string(img, lang='eng').lower()
print(text)
