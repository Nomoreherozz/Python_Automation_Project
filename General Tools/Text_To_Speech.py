# importing the modules 
import PyPDF2 
import pyttsx3 
  
# path of the PDF file 
pdf_file = input("Please input path for PDF file: ")
path = open(pdf_file, 'rb') 
  
# creating a PdfFileReader object 
pdfReader = PyPDF2.PdfReader(path) 
  
# the page with which you want to start 
# this will read the page of 25th page. 

page=input("Please input page number of choice: ")
page = int(page)-1
from_page = pdfReader.pages[page] 
  
# extracting the text from the PDF 
text = from_page.extract_text() 
  
# reading the text 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait()