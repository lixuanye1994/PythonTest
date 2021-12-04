from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_pdf(input_dir):
    file_list = filter(lambda x: str(x).endswith('pdf') and not str(x).endswith('output.pdf'), Path(input_dir).iterdir())
    output_file = Path(input_dir).joinpath('output.pdf').absolute()
    pdf_output = PdfFileWriter()
    for in_fn in list(file_list):
        pdf_input = PdfFileReader(open(str(in_fn), 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(str(output_file), 'wb'))
    return '合并成功: {}'.format(output_file)
