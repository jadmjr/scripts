import PyPDF2

merger = PyPDF2.PdfMerger()

merger.append("IMG_20230821_0001.pdf")
merger.append("IMG_20230821_0002.pdf")
merger.append("IMG_20230821_0003.pdf")
merger.append("IMG_20230821_0004.pdf")

merger.write("vivo_documento.pdf")