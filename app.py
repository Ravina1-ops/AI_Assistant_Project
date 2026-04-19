import streamlit as st
import pdf_tools
import ocr_tools

st.set_page_config(page_title="Student Utility Assistant", layout="wide")

st.title("📚 Student Utility Assistant (PDF + OCR Tool)")
st.write("Upload a PDF or Image to extract text (No AI).")

# Tabs
tab1, tab2 = st.tabs(["📄 PDF to Text", "🖼️ Image to Text (OCR)"])

# ---------------- PDF SECTION ----------------
with tab1:
    st.header("📄 Upload PDF and Extract Text")

    pdf_file = st.file_uploader("Upload PDF File", type=["pdf"])

    if pdf_file is not None:
        # Save uploaded PDF temporarily
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.read())

        extracted_text = pdf_tools.extract_text_from_pdf("temp.pdf")

        st.subheader("✅ Extracted Text")
        st.text_area("PDF Output", extracted_text, height=300)

        st.download_button(
            label="⬇️ Download Extracted Text",
            data=extracted_text,
            file_name="pdf_extracted_text.txt",
            mime="text/plain"
        )

# ---------------- IMAGE OCR SECTION ----------------
with tab2:
    st.header("🖼️ Upload Image and Extract Text (OCR)")

    img_file = st.file_uploader("Upload Image File", type=["png", "jpg", "jpeg"])

    if img_file is not None:
        # Save uploaded image temporarily
        with open("temp_image.png", "wb") as f:
            f.write(img_file.read())

        st.image("temp_image.png", caption="Uploaded Image", width='stretch')

        extracted_text = ocr_tools.extract_text_from_image("temp_image.png")

        st.subheader("✅ OCR Extracted Text")
        st.text_area("OCR Output", extracted_text, height=300)

        st.download_button(
            label="⬇️ Download OCR Text",
            data=extracted_text,
            file_name="ocr_extracted_text.txt",
            mime="text/plain"
        )