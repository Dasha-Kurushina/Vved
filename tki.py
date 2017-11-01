from tkinter import *

def f():
	print(ttt.get())

def t():
	ttt.set('hello')

root = Tk()
fam = StringVar()
ima = StringVar()
dat = StringVar()
adr = StringVar()

Label(root, text = "Фамилия:"        ).grid(row=0, column=0)
Entry(root, textvariable = fam       ).grid(row=0, column=1)

Label(root, text = "Имя:"            ).grid(row=1, column=0)
Entry(root, textvariable = ima       ).grid(row=1, column=1)

Label(root, text = "Дата рождения:"  ).grid(row=2, column=0)
Entry(root, textvariable = dat       ).grid(row=2, column=1)

Label(root, text = "Адрес:"          ).grid(row=3, column=0)
Entry(root, textvariable = adr       ).grid(row=3, column=1)

Button(root, text='ok', command = f).grid(row=4, column=0)

# Label(root, text="1111111", bg="red", fg="white").pack()
# Label(root, text="2222222", bg="green", fg="white").pack(side=LEFT)
# Label(root, text="3333333", bg="black", fg="white").pack()
# Label(root, text="4444444", bg="red", fg="white").pack(side=LEFT)

# grid(row=0, column=1)

# button1 = Button(root, text='ok', command = f)
# button1.pack()

# entry1 = Entry(root, textvariable = ttt)
# entry1.pack()

# button2 = Button(root, text='ok2', command = t)
# button2.pack()

root.mainloop()


#for i in range(20):
    #listbox.insert(END, str(i))

#pack(fill=X)
#w = Label(root, text="Green", bg="green", fg="black")

