#project2 number guessing game using tkinter

import tkinter as Tk
import random
from tkinter import messagebox


def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    entry_guess.delete(0, Tk.END)
    entry_guess.focus()


def check_guess():
    global secret_number
    user_guess = entry_guess.get()
    
    if not user_guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return
    guess = int(user_guess)
    
    if guess < secret_number:
        messagebox.showinfo("Result", "Too low! Try again.")
    elif guess > secret_number:
        messagebox.showinfo("Result", "Too high! Try again.")
    else:
        messagebox.showinfo("Result", "Congratulations! You've guessed it!")
        reset_game()

secret_number = random.randint(1, 100)

# create the main window
root = Tk.Tk()
root.title("Number Guessing Game")

# create a label to display the secret number
label = Tk.Label(root, text="Guess a number between 1 and 100:")
label.pack()

# create an entry field for the user to enter their guess
entry_guess = Tk.Entry(root)
entry_guess.pack()

# create a button to check the user's guess
button_check = Tk.Button(root, text="Check", command=check_guess)
button_check.pack()

# start the main event loop
root.mainloop()