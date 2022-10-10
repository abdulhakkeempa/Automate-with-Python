from PyPDF2 import PdfFileWriter, PdfFileReader

fileName = [
    "Dr.Anil Raj" ,
    "Dr.Deepak Padmanabhan" ,
    "Dr. Joemon M Jose" ,
    "Dr. S. D. Anitha Kumari" ,
    "Mr. Rajeev M Azhuvath" ,
    "Mr.Abhijith A" ,
    "Ms.Hashmy Hassan" ,
    "Ms.Bineetha Vijayan" ,
    "Dr. Madhu S. Nair" ,
    "Dr. Bindu Krishnan" ,
    "Mr.Santhosh Kumar K. P" ,
    "Mr.Midhun Haridas T P" ,
    "Ms.Haritha K" ,
    "Mr.Muhammed Anees V"
]

inputpdf = PdfFileReader(open("Appreciation.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(f"output/{fileName[i]}.pdf","wb") as outputStream:
        output.write(outputStream)
