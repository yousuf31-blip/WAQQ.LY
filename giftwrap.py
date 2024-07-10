from tkinter import * #tkinter needs to be imported
window = Tk()   #window is created everything under this will go into to the window
window.title("Gift Wrapping Menu") # Title created
window.geometry('5000x5500') #setting the size of the window
window.configure(background="light blue") #Background colour

#label for title
label_0 = Label(window, text="Gift Wrapping Service:", width=23, font=("bold", 22), bg="white")
label_0.place(x=200, y=10)

label_1 = Label(window, text="Customer Name:",width=20, font=("bold", 15))
label_1.place(x=30,y=70)

label_1 = StringVar() #StringVar used for text
entry_1 = Entry(textvariable=label_1, width=25) #Entry creates an entry field for text
entry_1.place(x=250,y=70) #place is the grid


#canvas1.create_rectangle(x1, y1, x2, y2, fill="colour")
canvas1 = Canvas(window, width=100, height=100) #creating a canvas to draw shapes
canvas1.place(x=250,y=110)
canvas1.create_polygon(80, 0, 100, 0, 100, 20, fill="purple") # first cordinates to create pattern
canvas1.create_polygon(40, 0, 60, 0, 100, 40, 100, 60,  fill="purple")
canvas1.create_polygon(0, 0, 20, 0, 100, 80, 100, 100,  fill="purple")
canvas1.create_polygon(0, 20, 80, 100, 60, 100, 0, 40,  fill="purple")
canvas1.create_polygon(0, 60, 40, 100, 20, 100, 0, 80,  fill="purple")


canvas7 = Canvas(window, width=100, height=100)
canvas7.place(x=430,y=110)
canvas7.create_rectangle(0, 20, 20, 0, fill="purple")
canvas7.create_rectangle(20, 40, 40, 20, fill="purple")
canvas7.create_rectangle(40, 60, 60, 40, fill="purple")
canvas7.create_rectangle(60, 80, 80, 60, fill="purple")
canvas7.create_rectangle(80, 100, 100, 80, fill="purple")
canvas7.create_rectangle(60, 20, 40, 0, fill="purple")
canvas7.create_rectangle(100, 20, 80, 0, fill="purple")
canvas7.create_rectangle(80, 40, 60, 20, fill="purple")
canvas7.create_rectangle(40, 80, 20, 60, fill="purple")
canvas7.create_rectangle(20, 100, 0, 80, fill="purple")
canvas7.create_rectangle(60, 100, 40, 80, fill="purple")
canvas7.create_rectangle(100, 60, 80, 40, fill="purple")
canvas7.create_rectangle(20, 60, 0, 40, fill="purple")




def selection():
    selected = "You have selected " + str(radio.get())

#radio = IntVar() creates radio box
radio = IntVar()
Label(text="Choose Pattern:",width=20, font=("bold", 15), bg="white").place(x=30, y=110)

r1 = Radiobutton(window, text="Polygon Paper",width=15, variable=radio, value=1, command=selection) #radio button created for pattern
r1.place(x=250, y=220)

r2 = Radiobutton(window, text="Square Paper",width=15, variable=radio, value=2, command=selection)
r2.place(x=420, y=220)

label_2 = Label(text="Choose Material:", width=20, font=("bold", 15), bg="white").place(x=30, y=270)

radio = IntVar()

r3 = Radiobutton(window, text="Standard(£0.40)",width=15, variable=radio, value=1, command=selection)
r3.place(x=250, y=270)

r4 = Radiobutton(window, text="Premium (£0.75)",width=15, variable=radio, value=2, command=selection)
r4.place(x=420, y=270)


label_3 = Label(text="Choose Colour:", width=20, font=("bold", 15), bg="white").place(x=30, y=330)

list_1 =["Purple", "DarkSlateGray4", "Deep Sky Blue", "Light Sea Green","Gold"] #dropdown menu options
c=StringVar()
droplist=OptionMenu(window,c, *list_1) #dropdown menu created
droplist.config(width=40)
c.set('Select colour...')
droplist.place(x=250,y=330)

label_4 = Label(text="Choose Extras:", width=20, font=("bold", 15), bg="white").place(x=30, y=390) #Label created for check list

CheckVar1 = IntVar() # variable created to make it a checklist
CheckVar2 = IntVar()
c_1 = Checkbutton(window, text="Gift Tag (£0.50)",width=15, variable=CheckVar1, onvalue=1).place(x=250, y=390)
c_2 = Checkbutton(window, text="Bow (£1.50)",width=15, variable=CheckVar2, onvalue=1).place(x=420, y=390)

label_5 = Label(text="Total Cost:", width=20, font=("bold", 15), bg="white").place(x=30, y=440)


def callback():
    label_6 = Label(window, text="Thank You For Your Order!")
    label_6.place(x=480, y=550)

button_1 = Button(window, text="Submit", width=10, command=callback)
button_1.place(x=480, y=520)

mybutton_2 = Button(window, text="Cancel")
mybutton_2.place(x=400, y=520)

#window.mainloop() creates the window
window.mainloop()