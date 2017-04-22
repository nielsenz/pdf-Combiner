import PyPDF2 as pdf

#All files have to be in current directory

file1 = input("What is the first PDF file you would like to combine (with .pdf)? ")
file2 = input("What is the second PDF file you would like to combine (with .pdf)? ")

pdf1File = open(file1, 'rb')
pdf2File = open(file2, 'rb')
pdf1Reader = pdf.PdfFileReader(pdf1File)
pdf2Reader = pdf.PdfFileReader(pdf2File)
pdfWriter = pdf.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
	pageObj = pdf1Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
	pageObj = pdf2Reader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedFile.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
