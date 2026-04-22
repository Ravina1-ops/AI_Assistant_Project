import streamlit as st
import translate_tools
import pdf_tools
import ocr_tools

st.set_page_config(page_title="Student Utility Assistant", layout="wide")

st.title("📚 Student Utility Assistant (PDF + OCR Tool)")
st.write("Upload a PDF or Image to extract text (No AI).")

# Tabs
tab1 = st.container()

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

# ----------------translate----------------

st.subheader("🌍 Translate Extracted Text")

lang = st.selectbox("Choose Language", ["Hindi", "English"])

if st.button("Translate"):
    target = "hi" if lang == "Hindi" else "en"
    translated = translate_tools.translate_text(extracted_text, target_lang=target)
    st.text_area("Translated Output", translated, height=300)


