	#Задание 1.
	#1)создать базу данных
	#2)создать 3 таблицы:
	#	покупатель(ф,и,о,адрес)
	#	магазин(название,адрес)
	#	продажа(товар,кол-во,цена)
	#3)создать формы заполнения для каждой таблицы
	#4)заполнить таблицы данными(мин.20)
	#5)создать отчет.

from tkinter import *

from bd import загрузить, сохранить, добавить_продажу, список_покупок, добавить_покупателя, добавить_магазин

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
	
	frame_людей     = Frame(parent,bd=5)
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
	
	frame_магазина     = Frame(parent,bd=5)
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
	
	frame_покупок     = Frame(parent,bd=5)
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
						 columnspan):
	def обновить_отчет():
		отчет.delete(0, END)
		x = список_покупок()
		for i in x.keys():
			#{'сидоров^семья^чай': {'кол-во': 1, 'цена': 4400}}
			фамилия, магазин, товар = i.split("^")
			цена = x[i]['цена']
			количество = x[i]['кол-во']
			отчет.insert(END,"%s, %s, %s, %s, %s" % (фамилия, магазин, товар, цена, количество))

	frame_отчета     = Frame(parent,bd=5)
	frame_отчета.grid(row=row, column=column, columnspan=columnspan)

	отчет = Listbox(frame_отчета,height=15, width=50)

	обновить_отчет()

	отчет.pack(fill = 'both', expand = 1)

	Button(frame_отчета, text='обновить', command = обновить_отчет).pack()

# button1=Button(frame1,text=u'Первая кнопка')
# button2=Button(frame2,text=u'Вторая кнопка')
# frame1.pack()
# frame2.pack()
# button1.pack()
# button2.pack()

def функция_добавления_покупок():
	добавить_продажу(
		фамилия = покупки_поле_фамилии.get(), 
		название_магазина = покупки_поле_названия.get(), 
		товар = покупки_поле_товара.get(), 
		цена = покупки_поле_цены.get(), 
		количество = покупки_поле_колва.get()
	)

	сохранить()

def функция_добавления_людей():
	добавить_покупателя(
		фамилия = люди_поле_фамилии.get(), 
		имя = люди_поле_имени.get(), 
		дата_рождения = люди_поле_даты.get(), 
		адрес = люди_поле_адреса.get()
	)
	
	сохранить()

def функция_добавления_магазина():
	добавить_магазин(название = магазины_поле_названия.get(), 
					адрес = магазины_поле_адреса.get()
					)

	сохранить()

def f():
	pass

if __name__ == '__main__':
	root=Tk()

	загрузить()

	покупки_поле_фамилии  = StringVar()
	покупки_поле_названия = StringVar()
	покупки_поле_товара   = StringVar()
	покупки_поле_цены     = IntVar()
	покупки_поле_колва    = IntVar()

	люди_поле_фамилии     = StringVar()
	люди_поле_имени       = StringVar()
	люди_поле_даты        = StringVar()
	люди_поле_адреса      = StringVar()

	магазины_поле_названия= StringVar()
	магазины_поле_адреса  = StringVar()

	создать_frame_людей(parent=root,
						row=0, #мое
						column=0, #мое
						поле_фамилии  = люди_поле_фамилии,
						поле_имени    = люди_поле_имени,
						поле_даты     = люди_поле_даты,
						поле_адреса   = люди_поле_адреса,
						функция_добавления_людей=функция_добавления_людей)

	создать_frame_магазина(parent=root,
						   row=0, #мое
						   column=1,#мое
						   поле_названия  = магазины_поле_названия,
						   поле_адреса    = магазины_поле_адреса,
						   функция_добавления_магазина=функция_добавления_магазина)

	создать_frame_покупок(parent=root,
						  row=0, #мое
						  column=2, #мое
						  поле_фамилии	= покупки_поле_фамилии,
						  поле_названия	= покупки_поле_названия,
						  поле_товара	= покупки_поле_товара,
						  поле_цены		= покупки_поле_цены,
						  поле_колва	= покупки_поле_колва,
						  функция_добавления_покупок=функция_добавления_покупок)

	создать_frame_отчета(parent=root,
						 row=1, #мое
						 column=0, #мое
						 columnspan=3)


	root.mainloop()

