from tkinter import *
root=Tk()

listbox1=Listbox(root,height=5,width=15,selectmode=SINGLE)
listbox2=Listbox(root,height=5,width=15,selectmode=SINGLE)


for i in ["Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]:
    listbox1.insert(END,i)
for i in [u"Канберра",u"Сидней",u"Мельбурн",u"Аделаида"]:
    listbox2.insert(END,i)
    
listbox1.pack()
listbox2.pack()
root.mainloop()