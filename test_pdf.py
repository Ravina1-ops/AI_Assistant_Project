import pdf_tools
pdf_path = "C:/Users/hema1/Downloads/selfstudys_com_file.pdf"
text = pdf_tools.extract_text_from_pdf(pdf_path)

print(text[:1000])