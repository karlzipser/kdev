import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def create_page_num_pdf(page_num, filename):
    """Create a temporary PDF to overlay page number."""
    packet = io.BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(300, 20, str(page_num))  # Adjust positioning as necessary
    can.save()
    
    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)
    # Add the "watermark" (which is the new pdf) to the existing page
    existing_page = PyPDF2.PdfFileReader(filename).getPage(0)
    existing_page.mergePage(new_pdf.getPage(0))
    output = PyPDF2.PdfFileWriter()
    output.addPage(existing_page)
    
    # Write to a real file
    with open(f"page_{page_num}.pdf", "wb") as outputStream:
        output.write(outputStream)

def merge_pdfs(files, output_filename):
    pdf_writer = PyPDF2.PdfWriter()

    for page_num, file_path in enumerate(files, start=1):
        pdf_reader = PyPDF2.PdfReader(file_path)
        for page in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page]
            if page == 0:  # Add page numbers to the first page of each file
                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)
                can.drawString(300, 20, f"Page {page_num}")
                can.save()
                packet.seek(0)
                number_pdf = PyPDF2.PdfReader(packet)
                pdf_page.merge_page(number_pdf.pages[0])
            pdf_writer.add_page(pdf_page)

    with open(output_filename, "wb") as out:
        pdf_writer.write(out)

# Example usage:
files = sggo(opjD('pdfs/Part 1/*.pdf'))
merge_pdfs(files, 'merged_numbered.pdf')
