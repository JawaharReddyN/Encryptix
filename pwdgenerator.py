import tkinter as tk
from tkinter import messagebox
import string
import random

def passgenerater(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    specialchars = string.punctuation

    allchars =lower_case + upper_case + digits + specialchars

    password = ''.join(random.choice(allchars) for _ in range(length))

    return password

def displaypass():
    length = length_entry.get() 
    try:
        length = int(length)
        if length <=0:
             raise ValueError
    except ValueError:
        messagebox.showerror("Error","Plz enter a positive integer for password length. ")
        return 

    password = passgenerater(length)
    password_display_label.config(text ="Generated Password is:" + password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the length of password:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_buttton = tk.Button(root,text="Generate Password", command=displaypass)
generate_buttton.pack()

password_display_label = tk.Label(root, text="")
password_display_label.pack()

root.mainloop()