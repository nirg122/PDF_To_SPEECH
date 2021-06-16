# Working version

import PyPDF2
import pyttsx3

# path of the PDF file
path = open('my_file.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.

# from_page = pdfReader.getPage(0) # Get specific page
# text = from_page.extractText()
# speak = pyttsx3.init()
# speak.say(text)
# speak.runAndWait()

num_of_pages = pdfReader.getNumPages()
# extracting the text from the PDF
for page in range(num_of_pages):
    from_page = pdfReader.getPage(page)
    text = from_page.extractText()

    # reading the text
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

