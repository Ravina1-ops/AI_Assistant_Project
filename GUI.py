from tkinter import*
from tkinter import filedialog
from PIL import Image , ImageTk
import Speech_To_text
import action
import pdf_tools
import ocr_tools

root = Tk()
root.title("My Assistant")
root.geometry("800x700")
root.resizable(False, False )
root.config(bg= "sky blue")

# ask function 
def ask ():
    user_val = Speech_To_text.speech_to_txt()
    bot_val = action.Action(user_val)
    text.insert(END, 'User-----> ' + user_val+"\n")
    if bot_val != None:
        text.insert(END, "Bot <-----"+str(bot_val)+"\n")
    if bot_val == "Okay ma'am":
        root.destroy()

# send function
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User-----> ' + send+"\n")
    if bot != None:
        text.insert(END, "Bot <-----"+str(bot)+"\n")
    if bot == "Okay ma'am":
        root.destroy()


# delete function
def del_txt():
    text.delete('1.0',"end")

# pdf upload function
def upload_pdf():
    file_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        extracted_text = pdf_tools.extract_text_from_pdf(file_path)
        text.insert(END, "\n--- PDF Extracted Text ---\n")
        text.insert(END, extracted_text + "\n")

# image upload function
def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )

    if file_path:
        extracted_text = ocr_tools.extract_text_from_image(file_path)
        text.insert(END, "\n--- Image OCR Text ---\n")
        text.insert(END, extracted_text + "\n")

# frame

frame = LabelFrame(root, padx = 20, pady = 10, borderwidth= 3, relief="ridge")
frame.config(bg = "light Green")
frame.grid(row = 0, column = 1, padx= 55, pady= 10)
frame.place(x=200, y=10, width=400, height=280)

# add text label
text_label = Label(frame, text = "AI Boss", font = ("Lucida Calligraphy", 26, "bold",),bg = "Beige" )
text_label.grid(row = 0, column = 0, padx= 20, pady= 10)


# add image
image = ImageTk.PhotoImage(Image.open("image/image.png"))
image_Label = Label(frame , image = image, bg ="light Yellow")
image_Label.grid(row = 1, column = 0, pady= 20,padx = 120)

# adding a text widget with scrollbar

scrollbar = Scrollbar(root)
scrollbar.place(x=750, y=320, height=250)

text = Text(root , font = ('courier 10 bold'), bg = "beige")
text.place(x= 50, y = 320, width = 700, height= 250)

text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

# entry widget

entry = Entry(root, justify = CENTER)
entry.place(x = 50, y = 590, width= 700, height = 35)

# Button 1
Button1 = Button(root, text = "ASK", bg = "Light Green", pady = 10, padx = 25, borderwidth=3, relief="sunken", command=ask)
Button1.place(x = 60, y = 640)

# Button 2
Button2 = Button(root, text = "Send", bg = "Light Green", pady = 10, padx = 25, borderwidth=3, relief="sunken", command=send)
Button2.place(x = 170, y = 640)

# Button 3
Button3 = Button(root, text = "Delete", bg = "Light Green", pady = 10, padx = 25, borderwidth=3, relief="sunken", command=del_txt)
Button3.place(x =290 , y = 640)

# Button 4
Button4 = Button(root, text="Upload PDF", bg="Light Yellow", pady=10, padx=25, borderwidth=3, relief="sunken", command=upload_pdf)
Button4.place(x=430, y=640)

# Button 5
Button5 = Button(root, text="Upload Image", bg="Light Yellow", pady=10, padx=25, borderwidth=3, relief="sunken", command=upload_image)
Button5.place(x=600, y=640)




root.mainloop()
