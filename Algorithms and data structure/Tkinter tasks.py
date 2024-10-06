import tkinter as tk
from tkinter import *



# ----------Exercise 1
click = 0
def click_button_plus():
    global click
    click+=1
    btn2["text"] = click
def click_button_minus():
    global click
    click-=1
    btn2["text"] = click
window = Tk()
window.title('Test')
window.geometry("250x50")
btn = tk.Button(text="-", command=click_button_minus)
btn.grid(row = 1, column = 0, ipadx = 2, ipady = 2)
btn2 = tk.Button(text=click)
btn2.grid(row = 1, column = 1, ipadx = 2, ipady = 2)
btn3 = tk.Button(text="+", command=click_button_plus)
btn3.grid(row = 1, column = 2, ipadx = 2, ipady = 2)

window.mainloop()


#----------Exercise 2
import random
rand_numb: int = 0
def insert_value_in_entry():
    rand_numb =random.randint(0,10000)
    entry.delete(0, tk.END)
    entry.insert(0, int(rand_numb))
window = Tk()
window.title("Random number")
window.geometry("100x50")
btn = tk.Button(text="Бросить", command=insert_value_in_entry)
btn.grid(row = 0, column = 0)
entry = Entry()
entry.insert(0,"Случайное число")
entry.grid(row = 1, column = 0)
window.mainloop()

#----------Exercise 3
def faringate_to_celsium():
    faringate = int(entry.get())
    cls : float = round((faringate - 32)*(5/9), 2)
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", cls)

window = Tk()
window.title("Converter to celsium")
window.geometry("200x200")

text_box = Text(width=5, height=1)
entry = Entry(width=5)
entry.insert(0, "")
btn = tk.Button(text="-->", command=faringate_to_celsium)
text_box.insert("1.0", "")
lb_f = Label(text=u"\u00b0""F")
lb_C = Label(text=u"\u00b0""C")
entry.grid(row = 0, column = 0, padx = 1, pady =1)
lb_f.grid(row = 0, column = 1, padx = 1, pady =1)
btn.grid(row = 0, column = 2, padx = 1, pady =1)
text_box.grid(row = 0, column = 3, padx = 1, pady =1)
lb_C.grid(row = 0, column = 4, padx = 1, pady =1)

window.mainloop()

#----------Exercise 4
import json as js
window = Tk()
window.title("Fill the form")
window.geometry("400x250")
form_ready = {}
def get_data():
    form_ready["Имя"]= entry_name.get()
    form_ready["ФИО"]= entry_lastname.get()
    form_ready["Адрес 1"]= entry_adress1.get()
    form_ready["Адрес 2"] = entry_adress2.get()
    form_ready["Город"]= entry_city.get()
    form_ready["Регион"] =entry_region.get()
    form_ready["Почтовый индекс"] =entry_postind.get()
    form_ready["Страна"]=entry_country.get()
    form = js.dumps(form_ready, ensure_ascii=False, indent=4)
    print (form)
def delete_data():
    entry_name.delete(0, tk.END)
    entry_lastname.delete(0, tk.END)
    entry_adress1.delete(0, tk.END)
    entry_adress2.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_region.delete(0, tk.END)
    entry_postind.delete(0, tk.END)
    entry_country.delete(0, tk.END)
#Имя
label_name = Label(text="Имя:",anchor="e", justify="right", width=15)
entry_name = Entry(width=45)
label_name.grid(row = 0, column = 0, padx = 1, pady =1)
entry_name.grid(row = 0, column = 1, padx = 1, pady =1)

#ФИО
label_lastname = Label(text="ФИО:",anchor="e", justify="right", width=15)
entry_lastname = Entry(width=45)
label_lastname.grid(row = 1, column = 0, padx = 1, pady =1)
entry_lastname.grid(row = 1, column = 1, padx = 1, pady =1)

#Адрес 1
label_adress1 = Label(text="Адрес 1:", anchor="e", justify="right", width=15)
entry_adress1 = Entry(width=45)
label_adress1.grid(row = 2, column = 0, padx = 1, pady =1)
entry_adress1.grid(row = 2, column = 1, padx = 1, pady =1)
#Адрес 2
label_adress2 = Label(text="Адрес 2:",anchor="e", justify="right", width=15)
entry_adress2 = Entry(width=45)
label_adress2.grid(row = 3, column = 0, padx = 1, pady =1)
entry_adress2.grid(row = 3, column = 1, padx = 1, pady =1)
#Город
label_city = Label(text="Город:",anchor="e", justify="right", width=15)
entry_city = Entry(width=45)
label_city.grid(row = 4, column = 0, padx = 1, pady =1)
entry_city.grid(row = 4, column = 1, padx = 1, pady =1)
#Регион
label_region = Label(text="Регион:", anchor="e", justify="right", width=15)
entry_region = Entry(width=45)
label_region.grid(row = 5, column = 0, padx = 1, pady =1)
entry_region.grid(row = 5, column = 1, padx = 1, pady =1)
#Почтовый индекс
label_postind = Label(text="Почтовый индекс:",anchor="e", justify="right", width=15)
entry_postind = Entry(width=45)
label_postind.grid(row = 6, column = 0, padx = 1, pady =1)
entry_postind.grid(row = 6, column = 1, padx = 1, pady =1)
#Страна
label_country = Label(text="Страна:",anchor="e", justify="right", width=15)
entry_country = Entry(width=45)
label_country.grid(row = 7, column = 0, padx = 1, pady =1)
entry_country.grid(row = 7, column = 1, padx = 1, pady =1)

btn = Button(text="Отправить", command=get_data, width=15)
btn_del = Button(text="Очистить", command=delete_data, width=15)
btn.place(x = 250, y = 190)
btn_del.place(x = 130, y = 190)
window.mainloop()
