import fitz # PyMuPDF
import os

pdf_path = r"C:\Users\Franc\Downloads\SmartAccess_AirCom.pdf"
output_dir = r"C:\Users\Franc\Mercadeo_IOTSYS\slides"

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    page = doc.load_page(i)
    # zoom factor for high quality (2 = 200%)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) 
    pix.save(os.path.join(output_dir, f"slide_{i+1}.png"))
    print(f"Saved slide_{i+1}.png")

print("Done!")
