from PyPDF2 import PdfWriter, PdfReader

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

inputpdf = PdfReader(open("Appreciation.pdf", "rb"))


for i in range(len(inputpdf.pages)):

    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open(f"output/{fileName[i]}.pdf","wb") as outputStream:
        output.write(outputStream)