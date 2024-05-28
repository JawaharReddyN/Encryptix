import tkinter as tk
from tkinter import messagebox
import random

def play(userchoice):
    compchoice = random.choice(["rock","paper","scissors"])
    result = winner(userchoice, compchoice)
    displayres(userchoice, compchoice, result) 

def winner(userchoice, compchoice):
    if userchoice == compchoice:
        return "It's a tie..!"
    elif (userchoice =="rock"and compchoice == "scissors") or \
         (userchoice =="scissors" and compchoice == "paper") or \
         (userchoice =="paper" and compchoice =="rock"):
         return "Congrats! You Won"
    else: 
        return "You Lost! Better Luck next time"

def displayres (userchoice, compchoice, result):
    result_label.config(text=f"Your choice: {userchoice}\nComputer's choice: {compchoice}\nResult:{result}")    

def playagain():
    result_label.config(text="")
    messagebox.showinfo("Rock, Paper, Scissors","Choose Rock , Paper, or Scissors to play!")

root = tk.Tk()
root.title("Rock, Paper, Scissors")

instruction_label = tk.Label(root, text="Choose rock , paper, or scissors:")
instruction_label.pack()

rock_button = tk.Button(root,text="Rock", command=lambda: play("rock") )
rock_button.pack()

paper_button = tk.Button(root,text="Paper", command=lambda: play("paper") )
paper_button.pack()

scissors_button = tk.Button(root,text="Scissors", command=lambda: play("scissors") )
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

playagain_button = tk.Button(root, text="Play Again", command=playagain )
playagain_button.pack()

root.mainloop()