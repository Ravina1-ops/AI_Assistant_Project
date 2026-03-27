from tkinter import*
from PIL import Image , ImageTk
root = Tk()
root.title("My Assistant")
root.geometry("550x675")
root.resizable(False, False )
root.config(bg= "sky blue")

# frame

frame = LabelFrame(root, padx = 100, pady = 7, borderwidth= 3, relief="ridge")
frame.config(bg = "light Green")
frame.grid(row = 0, column = 1, padx= 55, pady= 10)

# add text label
text_label = Label(frame, text = "AI Boss", font = ("Lucida Calligraphy", 26, "bold",),bg = "Beige" )
text_label.grid(row = 0, column = 0, padx= 20, pady= 10)


# add image
image = ImageTk.PhotoImage(Image.open("image/image.png"))
image_Label = Label(frame , image = image)
image_Label.grid(row = 1, column = 0, pady= 20)

# adding a text widget
text = Text(root , font = ('courier 10 bold'), bg = "beige")
text.grid(row = 2, column = 0, )
text.place(x= 60, y = 300, width = 400, height= 100)

# entry widget

entry = Entry(root, justify = CENTER)
entry.place(x = 60, y = 450, width= 400, height = 30)





root.mainloop()
