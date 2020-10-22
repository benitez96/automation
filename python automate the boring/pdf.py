## Modules --> pip install PyPDF2
import PyPDF2
import os

os.chdir('.')

pdfFile = open('example.pdf', 'rb')     # Must open in 'Read Binary'
reader = PyPDF2.PdfFileReader(pdfFile)
reader.numPages   #Returns number of pages

page = reader.getPage(0)    #Catches document's page 1 
page.extractText() #Extracts text as string type

# Extract the entire text from document
for numPage in range(reader.numPages):
    print(reader.getPage(numPage).extractText())


# Combining 2 PDF documents

pdfFile1 = open('example1.pdf', 'rb')
pdfFile2 = open('example2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)


outputFile = open('cominedPDFs.pdf', 'wb')      # Open it in Binary

writer.write(outputFile)

outputFile.close()
pdfFile1.close()
pdfFile2.close()