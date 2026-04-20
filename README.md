# AI Boss - Desktop Virtual Assistant 🤖

AI Boss is a Python-based desktop virtual assistant featuring a graphical user interface (GUI) built with Tkinter. It uses speech recognition to listen to your commands and text-to-speech to reply back. You can also interact with it using text input!

![Screnshot]({EB720745-3161-47DC-95AB-0D047F687025}.png)

## ✨ Features
* **Interactive GUI**: A clean and simple user interface to interact with the assistant.
* **Voice Command Support**: Uses a microphone to listen to your voice commands.
* **Text Input**: If you don't want to speak, you can type your commands in the entry box.
* **Text-to-Speech**: The assistant speaks back its responses to you.
* **Task Automation**: Can perform various tasks like:
  * Telling the current time.
  * Opening YouTube, Google, LinkedIn, and Spotify.
  * Casual greetings and conversation.

## 🛠️ Tech Stack & Libraries Used
* **Python 3.x**
* **Tkinter**: For the Graphical User Interface.
* **Pillow (PIL)**: For handling and displaying images in the GUI.
* **SpeechRecognition**: To convert user voice input into text.
* **pyttsx3**: For offline text-to-speech conversion.
* **webbrowser**: To open links in the default browser.

## ⚙️ Prerequisites & Installation

To run this project on your system:

[x]- Make sure you create virtual environemt for installin all libraries easily

[x]-  You just need to run below cmd

pip install -r requirements.txt

🤖 AI Boss – Student Utility Assistant (Desktop + Web)

AI Boss is a Python-based assistant project built in two versions:

✅ Desktop Assistant (Tkinter + Voice Commands)
✅ Web App (Streamlit + PDF/Image Text Extractor)

This project was created to explore real-world student productivity features like PDF text extraction, OCR, automation, and web deployment.

🚀 Web Version (Streamlit)

A browser-based student utility tool where users can upload study material and extract text instantly.

Features
📄 Upload PDF → Extract Text
🖼️ Upload Image → Extract Text (OCR)
📥 Download extracted text as .txt
🌐 Works in browser (easy to share)
Run Web App Locally
pip install -r requirements.txt
streamlit run app.py
🖥️ Desktop Version (Tkinter)

A desktop voice assistant with a GUI that can take voice/text commands and perform basic tasks.

Features
🎤 Voice commands (Speech Recognition)
⌨️ Text input support
🔊 Text-to-speech responses
🌍 Opens websites like YouTube, Google, Spotify, LinkedIn
Run Desktop App Locally
pip install -r requirements_desktop.txt
python GUI.py
🌐 Live Demo (Web Version)

🔗 Streamlit App Link: PASTE_YOUR_LINK_HERE

🛠️ Tech Stack
Python
Tkinter (Desktop UI)
Streamlit (Web UI)
pypdf (PDF extraction)
pytesseract (OCR)
Pillow (Image processing)
📌 Author

Ravina
GitHub: PASTE_YOUR_GITHUB_LINK_HERE
LinkedIn: PASTE_YOUR_LINKEDIN_LINK_HERE

⭐ Note

This project is continuously improving. Future updates may include translation, question extraction, and advanced note tools.

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
🔗 **Streamlit App:** `PASTE_YOUR_STREAMLIT_LINK_HERE`

Example:
https://your-app-name.streamlit.app

---

## 🖼️ Screenshots

### Desktop Version (Tkinter)
![Desktop Screenshot](PASTE_YOUR_DESKTOP_SCREENSHOT_PATH_HERE)

### Web Version (Streamlit)
![Web Screenshot](PASTE_YOUR_WEB_SCREENSHOT_PATH_HERE)

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