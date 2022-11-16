# Import all the required modules
from tkinter import Tk, Button
from fields import fields
from result import result
from explanation import explanation


# Create the main window
def main():
    # Create the main window
    window = Tk()
    # Set the title of the main window
    window.title("Number Conversion")
    # Set the size of the main window
    window.geometry("450x350")
    
    # Call the fields function
    check_val, option, num_entry = fields(window)
    
    # Create a button for result
    result_btn = Button(window, text="Result", width=20, command=lambda: result(check_val, option, num_entry))
    result_btn.place(x=100, y=250)
    
    # Create a button for explanation
    exp_btn = Button(window, text="Explanation", width=20, command=lambda: explanation(check_val, option))
    exp_btn.place(x=100, y=275)
    
    # Start the main loop
    window.mainloop()
    
    
# Run the main function
if __name__ == "__main__":
    main()
