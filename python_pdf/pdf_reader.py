from PyPDF2 import PdfFileReader


def extract_info(input_file):
    pdf_input = PdfFileReader(open(input_file, 'rb'))
    information = pdf_input.getDocumentInfo()
    pages = pdf_input.getNumPages()
    txt = f"""
        Information of {input_file}:

        Author:{information.author}
        Creator:{information.creator}
        Producer:{information.producer}
        Subject:{information.subject}
        Title:{information.title}
        Number of pages:{pages}
        """
    return txt
