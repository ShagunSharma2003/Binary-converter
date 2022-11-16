# Import all the required modules
from tkinter import Tk, Label
from data import data


# Create a function for the explanation window
def explanation(check_val, option):
    # Create the explanation window
    window = Tk()
    # Set the title of the window
    window.title("Explanation")
    # Set the size of the window
    window.geometry("800x650")

    # Create a label for the explanation
    for i in range(len(check_val)):
        # Create a label for the explanation
        expn_label = Label(window, text=data[option.get()][i])
        expn_label.place(x=100, y=50 + (i * 150))

    # Create mainloop
    window.mainloop()
