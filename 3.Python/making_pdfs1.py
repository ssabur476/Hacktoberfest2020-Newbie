#creating a pdf file 
#then using a text file to create a pdf
#setting font name/style and size of text

from fpdf import FPDF 

pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)
pdf.cell(200,15,txt="welcome I know python very well",ln=1,align="C")
pdf.cell(200,12,txt="I will just replace the text",ln=8,align="C")
pdf.cell()
pdf.output("MyPDF.pdf")
#File1.pdf will be the file name and extension