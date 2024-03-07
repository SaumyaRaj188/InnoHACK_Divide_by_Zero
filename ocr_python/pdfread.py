# import module
from pdf2image import convert_from_path
from pytesseract import pytesseract

# Store Pdf with convert_from_path function
images = convert_from_path('nsut.pdf')

with open("ocr.txt", "w") as myfile:
        myfile.write("")

myfile.close()

for i in range(len(images)):
    text = pytesseract.image_to_string(images[i])

    with open("ocr.txt", "a") as myfile:
        myfile.write(text)
	# Save pages as images in the pdf
    myfile.close()
