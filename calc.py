import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title('Calculator')
app.minsize(400, 480)
app.geometry('500x600')
app.maxsize(550, 660)
app.config(bg='#241F1A')
# app.iconbitmap(r"C:\Users\RAAJ\Desktop\code\python\dist\32officeicons-16_89723.ico")


font_1 = ('Arial',20,'bold')
butbg = '#3F3A36'


def clear():
    equation_entry.delete(0,END)

def calculate():
    try:
        equation = equation_entry.get()
        result = eval(equation)
        clear()
        equation_entry.insert(0,result)
    except ZeroDivisionError:
        messagebox.showerror('Error404','Cannot divide by zero')
    except :
        messagebox.showerror('Error404','Invalid Input')

def back():
    equation = equation_entry.get()
    equation_entry.delete(0,END) #clearing the entry
    equation_entry.insert(0,equation[:-1]) #inserting the equation again except the last character

def root():
    equation = equation_entry.get()
    equation_entry.delete(0,END)
    equation_entry.insert(0,eval(equation)**0.5)

def percent():
    equation = equation_entry.get()
    equation_entry.delete(0,END)
    equation_entry.insert(0,eval(equation)/50)

equation_entry = customtkinter.CTkEntry(app,font=font_1,text_color='#fff',fg_color='#241F1A')
b7 = customtkinter.CTkButton(app,text='7',font=font_1,command=lambda:equation_entry.insert(END,'7'),fg_color=butbg)
b8 = customtkinter.CTkButton(app,text='8',font=font_1,command=lambda:equation_entry.insert(END,'8'),fg_color=butbg)
b9 = customtkinter.CTkButton(app,text='9',font=font_1,command=lambda:equation_entry.insert(END,'9'),fg_color=butbg)
b4 = customtkinter.CTkButton(app,text='4',font=font_1,command=lambda:equation_entry.insert(END,'4'),fg_color=butbg)
b5 = customtkinter.CTkButton(app,text='5',font=font_1,command=lambda:equation_entry.insert(END,'5'),fg_color=butbg)
b6 = customtkinter.CTkButton(app,text='6',font=font_1,command=lambda:equation_entry.insert(END,'6'),fg_color=butbg)
b1 = customtkinter.CTkButton(app,text='1',font=font_1,command=lambda:equation_entry.insert(END,'1'),fg_color=butbg)
b2 = customtkinter.CTkButton(app,text='2',font=font_1,command=lambda:equation_entry.insert(END,'2'),fg_color=butbg)
b3 = customtkinter.CTkButton(app,text='3',font=font_1,command=lambda:equation_entry.insert(END,'3'),fg_color=butbg)
b_0 = customtkinter.CTkButton(app,text='0',font=font_1,command=lambda:equation_entry.insert(END,'0'),fg_color=butbg)
b_div = customtkinter.CTkButton(app,text='/',font=font_1,command=lambda:equation_entry.insert(END,'/'),fg_color=butbg)
b_into = customtkinter.CTkButton(app,text='*',font=font_1,command=lambda:equation_entry.insert(END,'*'),fg_color=butbg)
b_sub = customtkinter.CTkButton(app,text='-',font=font_1,command=lambda:equation_entry.insert(END,'-'),fg_color=butbg)
b_pls = customtkinter.CTkButton(app,text='+',font=font_1,command=lambda:equation_entry.insert(END,'+'),fg_color=butbg)
b_eqls = customtkinter.CTkButton(app,text='=',font=font_1,command=calculate,fg_color=butbg)
b_dot= customtkinter.CTkButton(app,text='.',font=font_1,command=lambda:equation_entry.insert(END,'.'),fg_color=butbg)
b_clr = customtkinter.CTkButton(app,text='C',font=font_1,command=clear,fg_color=butbg)
b_back = customtkinter.CTkButton(app,text='🔙',font=font_1,command=back,fg_color=butbg)
b_root = customtkinter.CTkButton(app,text='√',font=font_1,command=root,fg_color=butbg)
b_percent = customtkinter.CTkButton(app,text='%',font=font_1,command=percent,fg_color=butbg)

app.grid_columnconfigure((0,1,2,3),weight=1)
app.grid_rowconfigure((5,0,1,2,3,4),weight=1)

equation_entry.grid(row=0,columnspan=4, column=0,padx=5,pady=5, sticky= "nsew")
b7.grid(row=1,column=0,padx=5,pady=5, sticky= "nsew")
b8.grid(row=1,column=1,padx=5,pady=5, sticky= "nsew")
b9.grid(row=1,column=2,padx=5,pady=5, sticky= "nsew")
b4.grid(row=2,column=0,padx=5,pady=5, sticky= "nsew")
b5.grid(row=2,column=1,padx=5,pady=5, sticky= "nsew")
b6.grid(row=2,column=2,padx=5,pady=5, sticky= "nsew")
b1.grid(row=3,column=0,padx=5,pady=5, sticky= "nsew")
b2.grid(row=3,column=1,padx=5,pady=5, sticky= "nsew")
b3.grid(row=3,column=2,padx=5,pady=5, sticky= "nsew")
b_0.grid(row=4,column=1,padx=5,pady=5, sticky= "nsew")
b_div.grid(row=1,column=3,padx=5,pady=5, sticky= "nsew")
b_into.grid(row=2,column=3,padx=5,pady=5, sticky= "nsew")
b_sub.grid(row=3,column=3,padx=5,pady=5, sticky= "nsew")
b_pls.grid(row=4,column=3,padx=5,pady=5, sticky= "nsew")
b_dot.grid(row=4,column=0,padx=5,pady=5, sticky= "nsew")
b_eqls.grid(row=5,column=3,padx=5,pady=5, sticky= "nsew")
b_clr.grid(row=5,column=0,padx=5,pady=5, sticky= "nsew")
b_back.grid(row=5,column=1,padx=5,pady=5, sticky= "nsew")
b_root.grid(row=5,column=2,padx=5,pady=5, sticky= "nsew")
b_percent.grid(row=4,column=2,padx=5,pady=5, sticky= "nsew")


app.mainloop()