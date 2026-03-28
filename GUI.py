from tkinter import*
from PIL import Image , ImageTk
import Speech_To_text
import action

root = Tk()
root.title("My Assistant")
root.geometry("550x675")
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

# Button 1
Button1 = Button(root, text = "ASK", bg = "Light Green", pady = 16, padx = 40, borderwidth=3, relief="sunken", command=ask)
Button1.place(x = 70, y = 575)

# Button 2
Button2 = Button(root, text = "Send", bg = "Light Green", pady = 16, padx = 40, borderwidth=3, relief="sunken", command=send)
Button2.place(x = 400, y = 575)

# Button 3
Button3 = Button(root, text = "Delete", bg = "Light Green", pady = 16, padx = 40, borderwidth=3, relief="sunken", command=del_txt)
Button3.place(x =225 , y = 575)




root.mainloop()
