import PyPDF2
import os


def merge_pdfs(files, path):
    if not bool(files):
        return
    # Create a new PdfFileWriter object which represents a blank PDF document
    pdf_writer = PyPDF2.PdfFileWriter()
    # Open the files that have to be merged one by one
    # Read the files that you have opened
    for file in files:
        print(file)
        pdf_file = open(file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Loop through all the page numbers for the first document
        for pageNum in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(pageNum)
            pdf_writer.addPage(page_obj)

        # Now that you have copied all the pages in both the documents, write them into the a new document
        pdf_output_file = open(path + '/My Portfolio.pdf', 'wb')
        pdf_writer.write(pdf_output_file)
        #pdf_output_file.name.replace(path, "")
        # Close all the files - Created as well as opened
        pdf_file.close()
        pdf_output_file.close()


# merge_pdfs(['Autofill/AutofillResults/My Assignment1.pdf', 'Autofill/AutofillResults/My Assignment2.pdf'],
#            'Autofill/AutofillResults')
