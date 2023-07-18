from PyPDF2 import PdfMerger

pdf_list = ["one.pdf", "two.pdf", "three.pdf"]
margePdf = PdfMerger();

for newPdf in pdf_list:
   margePdf.append(newPdf)

margePdf.write('New2.pdf')   
margePdf.close()