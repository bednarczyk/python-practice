import PyPDF2

with open("resume.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    write = PyPDF2.PdfFileWriter()
    write.addPage(page)
    with open("rotated.pdf", "wb") as output:
        write.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["resume.pdf", "cert.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")