# 🤖 AI Boss - Student Utility Assistant (Desktop + Web)

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Tkinter](https://img.shields.io/badge/Tkinter-Desktop_App-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

AI Boss is a **Python-based Student Utility Assistant** built in **two versions**:

✅ **Desktop Assistant (Tkinter GUI + Voice Commands)**  
✅ **Web Assistant (Streamlit App for PDF & OCR tools)**  

This project helps students with productivity tasks like **PDF text extraction, image-to-text conversion (OCR), and basic assistant automation**.

---

## 🌟 Project Versions

### 🖥️ 1) Desktop Version (Tkinter Assistant)
A GUI-based virtual assistant that supports **voice and text commands**.

#### ✨ Features
- 🎤 Speech Recognition (Voice Commands)
- ⌨️ Text Input Support
- 🔊 Text-to-Speech Replies
- 🌐 Opens websites (YouTube, Google, Spotify, LinkedIn)
- ⏰ Tells current time
- 💬 Simple chatbot style responses

---

### 🌐 2) Web Version (Streamlit Student Utility App)
A web-based tool where students can upload study material and extract text easily.

#### ✨ Features
- 📄 Upload PDF → Extract Text
- 🖼️ Upload Image → Extract Text (OCR)
- 📥 Download extracted text as `.txt`
- 🌍 Works on Browser (easy to share)

---

## 🚀 Live Demo (Web Version)
🔗 **Streamlit App:** `https://student-utility-assistant.streamlit.app`

Example:
https://your-app-name.streamlit.app

---

## 🖼️ Screenshots

### Desktop Version (Tkinter)
![Desktop Screenshot](desktop.png)

### Web Version (Streamlit)
![Web Screenshot](web.png)

---

## 🛠️ Tech Stack

### 🔹 Languages
- Python 3.10+

### 🔹 Frameworks / UI
- Tkinter (Desktop GUI)
- Streamlit (Web UI)

### 🔹 Libraries Used
- SpeechRecognition (speech-to-text)
- pyttsx3 (text-to-speech)
- pypdf (PDF text extraction)
- pytesseract (OCR extraction)
- Pillow (Image processing)
- OpenCV (image handling)

---

## 📂 Project Structure

```txt
AI_Assistant_Project/
│
├── GUI.py                  # Desktop Tkinter GUI
├── action.py               # Desktop assistant logic
├── Speech_To_text.py       # Speech recognition module
├── Text_to_Speech.py       # Text-to-speech module
│
├── app.py                  # Streamlit Web App
├── pdf_tools.py            # PDF extraction module
├── ocr_tools.py            # OCR extraction module
│
├── requirements.txt        # Web requirements (Streamlit)
├── requirements_desktop.txt# Desktop requirements (Tkinter)
└── README.md


⭐ Note

This project is continuously improving. Future updates may include translation, question extraction, and advanced note tools.