import ocr_tools

img_path = "{06D088EB-C88F-47D3-9238-8ED4240CA97A}.png"
text = ocr_tools.extract_text_from_image(img_path)

print(text)