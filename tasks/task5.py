# importing the modules
import PyPDF2
import pyttsx3
import re

# function: PDF to Voice
def pdf_to_voice(pdf):
    # path of the PDF file
    path = open(pdf, 'rb')

    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(path)

    # the page with which you want to start
    from_page = pdfReader.getPage(0)

    # extracting the text from the PDF
    text = from_page.extractText()

    # reading the text
    speak = pyttsx3.init() # gives reference to the engine
    speak.say(text)
    print("Reading Starts. . . .")
    speak.runAndWait()
    print("Done Reading, Bye")

# Function: Check the PDF path format 
def check_pdf_format(img):
     # Regex to check valid PDF file extension.
    regex = "([^\\s]+(\\.(?i)(pdf))$)"
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    if (img == ""):
        print("Path can't be empty")
        exit()
    elif(re.search(p, img)):
        return True
    else:
        print("Wrong Path Format! try again")
        exit()

# calling functions
pdf= input("Enter PDF path: ")
    
check_pdf_format(pdf)

pdf_to_voice(pdf)