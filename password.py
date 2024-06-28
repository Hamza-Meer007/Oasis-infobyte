from tkinter import *
import string , pyperclip
import random
from tkinter import messagebox
def copy_text():
    
    res = entry_field.get()
    if res == '':
        messagebox.showerror('Error','Password field is empty')
    else:
        pyperclip.copy(res)
        messagebox.showinfo('Success',"Message copied Successfully!!")

    
     
def generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit=string.digits
    punc = string.punctuation
    size = int(get_len.get())
    if entry_field.get() == '':
            
        if choice.get()==1:
            add1 = lower + upper
            res =random.sample(add1,size)
            entry_field.insert(0,res)
        elif choice.get()==2:
            add1 = lower + upper +digit
            res =random.sample(add1,size)
            entry_field.insert(0,res)
        else:
            add1 = lower + upper +digit + punc
            res =random.sample(add1,size)
            entry_field.insert(0,res)
    else:
        entry_field.delete(0,END)
        if choice.get()==1:
            add1 = lower + upper
            res =random.sample(add1,size)
            entry_field.insert(0,res)
        elif choice.get()==2:
            add1 = lower + upper +digit
            res =random.sample(add1,size)
            entry_field.insert(0,res)
        else:
            add1 = lower + upper +digit + punc
            res =random.sample(add1,size)
            entry_field.insert(0,res)



root = Tk()

root.geometry('400x500+300+100')
root.title('Password Generator')
root.iconbitmap('lock.ico')
root.resizable(0,0)
root.configure(bg='#D8EFD3')

pass_label = Label(root,text='Password Generator',font='puppins 25 bold',bg='#D8EFD3',fg='#55AD9B')
pass_label.place(x=45,y=15)
complexity = Label(root,text='\u2023 Select Complexity Level',font='Arial 13 bold',bg='#D8EFD3')
complexity.place(x=0,y=70)
choice = IntVar()
simple = Radiobutton(root,text='Weak',value=1,variable=choice,bg='#D8EFD3',font='Times 17 bold',activebackground='#D8EFD3')
simple.place(x=45,y=110)
normal = Radiobutton(root,text='Medium',value=2,variable=choice,bg='#D8EFD3',font='Times 17 bold',activebackground='#D8EFD3')
normal.place(x=200,y=110)
high = Radiobutton(root,text='Strong',value=3,variable=choice,bg='#D8EFD3',font='Times 17 bold',activebackground='#D8EFD3')
high.place(x=130,y=150)


length = Label(root,text='\u2023 Select Length',font='Arial 13 bold',bg='#D8EFD3')
length.place(x=0,y=210)

get_len = Spinbox(root,from_=5,to=15,font='Helvetice 15 bold',justify=CENTER,width=10,bg='#D8EFD3',relief='groove')
get_len.place(x=105,y=250)

length = Label(root,text='\u2023 Your Password',font='Arial 13 bold',bg='#D8EFD3')
length.place(x=0,y=310)

entry_field = Entry(root,font='Times 17 bold',justify=CENTER,bd=5,relief='groove',width=25)
entry_field.place(x=10,y=350)

copy = Button(root,text='Copy',font='Arial 12 bold',bg='gray20',activebackground='gray20',activeforeground='gold',fg='gold',bd=5,relief='groove',padx=3,command=copy_text)
copy.place(x=330,y=347)

generate = Button(root,text='Generate',font='Arial 15 bold',bg='gray20',activebackground='gray20',activeforeground='gold',fg='gold',bd=5,relief='groove',padx=25,command=generator)
generate.place(x=120,y=410)


root.mainloop()