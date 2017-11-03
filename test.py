from tkinter import *
# frame_магазинов = Frame(root,bd=5)
# frame_покупок   = Frame(root,bd=5)
# frame_отчета    = Frame(root,bd=5)
# frame_магазинов.grid(row=0, column=1) 
# frame_покупок.grid(row=0, column=2)   
# frame_отчета.grid(row=1, column=0, columnspan=3)

def создать_frame_людей(parent,
						row, #мое
						column, #мое
						поле_фамилии,
						поле_имени,
						поле_даты,
						поле_адреса,
						функция_добавления_людей):
	
	frame_людей     = Frame(root,bd=5)
	frame_людей.grid(row=row, column=column)     
                    #его      его
	Label(frame_людей, text = "Фамилия:"          ).grid(row=0, column=0)
	Entry(frame_людей, textvariable = поле_фамилии).grid(row=0, column=1)

	Label(frame_людей, text = "Имя:"              ).grid(row=1, column=0)
	Entry(frame_людей, textvariable = поле_имени  ).grid(row=1, column=1)

	Label(frame_людей, text = "Дата рождения:"    ).grid(row=2, column=0)
	Entry(frame_людей, textvariable = поле_даты   ).grid(row=2, column=1)

	Label(frame_людей, text = "Адрес:"            ).grid(row=3, column=0)
	Entry(frame_людей, textvariable = поле_адреса ).grid(row=3, column=1)

	Button(frame_людей, text='добавить покупателя', command = функция_добавления_людей).grid(row=4, column=0)

def создать_frame_магазина(parent,
						   row, #мое
						   column,#мое
						   поле_названия,
						   поле_адреса,
						   функция_добавления_магазина):
	
	frame_магазина     = Frame(root,bd=5)
	frame_магазина.grid(row=row, column=column)     

	Label(frame_магазина, text = "Название:"            ).grid(row=0, column=0)
	Entry(frame_магазина, textvariable = поле_названия  ).grid(row=0, column=1)

	Label(frame_магазина, text = "Адрес:"               ).grid(row=1, column=0)
	Entry(frame_магазина, textvariable = поле_адреса    ).grid(row=1, column=1)

	Button(frame_магазина, text='добавить магазин', command = функция_добавления_магазина).grid(row=2, column=0)

def создать_frame_покупок(parent,
						  row, #мое
						  column, #мое
						  поле_фамилии,
						  поле_названия,
						  поле_товара,
						  поле_цены,
						  поле_колва,
						  функция_добавления_покупок):
	
	frame_покупок     = Frame(root,bd=5)
	frame_покупок.grid(row=row, column=column)     
                    #его      его
	Label(frame_покупок, text = "Фамилия:"            ).grid(row=0, column=0)
	Entry(frame_покупок, textvariable = поле_фамилии  ).grid(row=0, column=1)

	Label(frame_покупок, text = "Магазин:"            ).grid(row=1, column=0)
	Entry(frame_покупок, textvariable = поле_названия ).grid(row=1, column=1)

	Label(frame_покупок, text = "Товар:"              ).grid(row=2, column=0)
	Entry(frame_покупок, textvariable = поле_товара   ).grid(row=2, column=1)

	Label(frame_покупок, text = "Цена (коп.):"        ).grid(row=3, column=0)
	Entry(frame_покупок, textvariable = поле_цены     ).grid(row=3, column=1)

	Label(frame_покупок, text = "Количество (шт.):"   ).grid(row=4, column=0)
	Entry(frame_покупок, textvariable = поле_колва    ).grid(row=4, column=1)
	
	Button(frame_покупок, text='добавить покупку', command = функция_добавления_покупок).grid(row=5, column=0)

def создать_frame_отчета(parent,
						 row, #мое
						 column, #мое
						 columnspan,
						 список_отчета=[
						 	"'сидоров^семья^чай': {'цена': 4400, 'кол-во': 1}",
							"'петров^пятерочка^яблоко': {'кол-во': 12, 'цена': 2350}"
							]):
	pass


# button1=Button(frame1,text=u'Первая кнопка')
# button2=Button(frame2,text=u'Вторая кнопка')
# frame1.pack()
# frame2.pack()
# button1.pack()
# button2.pack()

def f():
	pass

if __name__ == '__main__':
	root=Tk()
	создать_frame_людей(parent=root,
						row=0, #мое
						column=0, #мое
						поле_фамилии=StringVar(),
						поле_имени=StringVar(),
						поле_даты=StringVar(),
						поле_адреса=StringVar(),
						функция_добавления_людей=f)
	создать_frame_магазина(parent=root,
						   row=0, #мое
						   column=1,#мое
						   поле_названия=StringVar(),
						   поле_адреса=StringVar(),
						   функция_добавления_магазина=f)

	создать_frame_покупок(parent=root,
						  row=0, #мое
						  column=2, #мое
						  поле_фамилии=StringVar(),
						  поле_названия=StringVar(),
						  поле_товара=StringVar(),
						  поле_цены=StringVar(),
						  поле_колва=StringVar(),
						  функция_добавления_покупок=f)

	создать_frame_отчета(parent=root,
						 row=1, #мое
						 column=0, #мое
						 columnspan=3,
						 список_отчета=["'сидоров^семья^чай': {'цена': 4400, 'кол-во': 1}",
"'петров^пятерочка^яблоко': {'кол-во': 12, 'цена': 2350}"])


	root.mainloop()

["'сидоров^семья^чай': {'цена': 4400, 'кол-во': 1}",
"'петров^пятерочка^яблоко': {'кол-во': 12, 'цена': 2350}"]
