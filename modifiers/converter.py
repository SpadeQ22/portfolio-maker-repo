from docx2pdf import convert
import os
from PIL import Image


# Configure API key authorization: Apikey


def word_to_pdf(input_file):
    convert(input_file)
    os.remove(input_file)


def img_to_pdf(input_file):
    img = Image.open(input_file)
    img = img.convert('RGB')
    img.save(input_file.rsplit(".", 1)[0] + '.pdf')
    os.remove(input_file)


def convert_to_pdf(input_files):
    for input_file in input_files:
        try:
            print(input_file)
            if input_file.endswith('docx') or input_file.endswith('doc'):
                word_to_pdf(input_file)
            elif input_file.endswith('png') or input_file.endswith('jpg'):
                img_to_pdf(input_file)

        except IOError:
            print("file doesn't end with: docx, doc, png or jpg!")


# convert_to_pdf('Autofill/img.jpg')
