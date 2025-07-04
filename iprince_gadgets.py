import numpy as np
from fpdf import FPDF

pdf = FPDF(orientation='p', unit='pt', format='A4')
pdf.add_page()
pdf.set_font('Times', 'B', 30)
pdf.cell(0, 10, txt='TikTok Products', ln=1, align='C')
pdf.ln(20)
pdf.set_font('Times', size=20)
products = np.arange(1,11)
for i in range(2,15):
    pdf.cell(0,10, txt= f'For Day {i}, post the following product:', ln=1)
    pdf.ln(15)
    for i in np.random.choice(products, size=5, replace=False):
        pdf.cell(0,10,f'Product {i}',ln=1)
        pdf.ln(10)
    pdf.ln(20)
pdf.output(r'C:\Users\Precious\Desktop\Personal Development\Business Folder\iprince gadgets\tiktok_products.pdf')
print('PDF done')
    