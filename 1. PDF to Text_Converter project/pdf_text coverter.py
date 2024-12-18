import PyPDF2

input_pdf = "sample.pdf"
output_txt = "output_text.txt"

with open(input_pdf, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

with open(output_txt, "w", encoding="utf-8") as output_file:
    output_file.write(text)

print(f"Text extracted and saved to {output_txt}")
