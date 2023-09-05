from tkinter import *
import string
import random
import pyperclip
#generate a password
def generator():
    small_alphabet = string.ascii_lowercase
    capital_alphabet = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation
    all = small_alphabet + capital_alphabet + numbers + punctuation
    password_length = int(length_Box.get())
    if choice.get() == 1:
        passwordField.insert(0,random.sample(small_alphabet,password_length))
    if choice.get() == 2:
        passwordField.insert(0,random.sample(small_alphabet+capital_alphabet,password_length))
    if choice.get() == 3:
        passwordField.insert(0,random.sample(all,password_length))        
    password = random.sample(all,password_length)
    passwordField.insert(0,password)
#Copy Function
def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)

 #GUI CODE FOR PASSWORD GENERATOR   
root = Tk()
root.config(bg ="gray28")
choice = IntVar()
Font = ('arial',13,'bold')
passwordLabel = Label(root,text = 'Password Generator',font = ('times new roman',28,'bold'),bg = 'gray20',fg = 'white')
passwordLabel.grid(pady=5)
weakradioButton = Radiobutton(root,text = "Weak",value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)
mediumradioButton = Radiobutton(root,text = "Medium",value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)
strongradioButton = Radiobutton(root,text = "Strong",value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

length_Box = Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton = Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root,width=25,bd=2)
passwordField.grid(pady=10)

copyButton = Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()