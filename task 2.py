from fpdf import FPDF

# Analyze text from a file
with open('sample_data.txt', 'r') as f:
    content = f.read()
word_count = len(content.split())
line_count = len(content.splitlines())

# Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Text File Analysis Report", ln=True, align='C')
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Words: {word_count}", ln=True)
pdf.cell(200, 10, txt=f"Total Lines: {line_count}", ln=True)

pdf.output("report.pdf")
