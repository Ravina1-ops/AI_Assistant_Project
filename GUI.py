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







root.mainloop()
