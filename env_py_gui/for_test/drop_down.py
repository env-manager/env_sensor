from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title('Drop Down Button')

root.geometry("400x400")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
e1 = Entry(root)
e1.grid(row=0, column=0, columnspan=2)
def temp_click_e1(event):
    print('e1 clicked')
    
e1.bind('<FocusIn>',temp_click_e1)
e1.focus()
e2 = Entry(root)
e2.grid(row=1, column=0, columnspan=2)
def temp_click_e2(event):
    print('e2 clicked')
    
e2.bind('<FocusIn>',temp_click_e2)

e3 = Entry(root)
e3.grid(row=2, column=0, columnspan=2)
def temp_click_e3(event):
    print('e3 clicked')
    
e3.bind('<FocusIn>',temp_click_e3)


btn_1 = Label(root, text='1', bg='red')
btn_1.grid(row=3, column=0,sticky='NEWS')
def temp_click_1(event):
    print('1')
btn_1.bind('<Button-1>', temp_click_1)

btn_2 = Label(root, text='2', bg='green')
btn_2.grid(row=3, column=1,sticky='NEWS')
def temp_click_2(event):
    print('2')
btn_2.bind('<Button-1>', temp_click_2)




root.mainloop()