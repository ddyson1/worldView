from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo/c_lewis_dot.png', 20, 12, 24)
        # Helevetica Bold 12
        pdf.set_font('Helvetica', 'B', 16)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 24, 'ALLOTROPE LLC', 0, 1, 'C')
        # Line break
        self.ln(25)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', '', 8)
        # Page number
        self.cell(0, 10, str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Helvetica', '', 12)
name = 'plots/realgdp.png'
pdf.image(name, x = None, y = None, w = 120, h = 90, type = '', link = '')
'''
for i in range(1, 21):
    pdf.cell(0, 20, 'printing line number ' + str(i), 0, 1)
'''
pdf.output('reports/test.pdf', 'F')
