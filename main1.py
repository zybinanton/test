from cProfile import label
from distutils import command
import tkinter as tk

def click():
    btn_text.set("Измененый текст")

def replaceText():
    label_text.set(btn_text.get())


root = tk.Tk()
root.title("Python11")
root.geometry("400x600")

btn_text = tk.StringVar() # IntVar, BooleanVar, DoubleVar
label_text = tk.StringVar()
btn_text.set("Старый текст")
btn1 = tk.Button(text="Это кнопка1",
                textvariable= btn_text,
                command=click, 
                background="red", 
                foreground="blue", 
                padx="20", 
                pady="40", 
                width="100",
                height="200",
                font="Arial 20",
                activebackground="blue",
                activeforeground="red",
                state="active") 

lb = tk.Label(textvariable=label_text)
lb.pack()

entry = tk.Entry(textvariable=btn_text)
entry.pack()
entry.setvar()

btn2 = tk.Button(text="Это кнопка2", 
                command=replaceText)
btn3 = tk.Button(text="Это кнопка3") 

txt = tk.Text()
# txt.pack()

# btn1.grid(column=2, row=2)
btn2.grid( row=0, column=0)
btn3.grid( row=1, column=1)


root.mainloop()