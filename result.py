# Import all the required modules
from tkinter import Tk, Label, Entry, messagebox


# Create a function for the result window
def result(check_val, option, num_entry):
    # Get all the values from the check buttons
    check_val = [val.get() for val in check_val]
    
    # Check if the user entered a number
    if (num_entry.get() != "") and (option.get() in list(range(1, 5))) and (1 in check_val):
        # Create new window
        window = Tk()
        # Set the title of the window
        window.title("Result")
        # Set the size of the window
        window.geometry("450x350")
        
        # Get the results
        results, types = get_result(check_val, option, num_entry)
        
        # Create labels for the results
        for i in range(len(results)):
            # Create an entry for the types
            type_label = Label(window, text=types[i])
            type_label.place(x=100, y=50 + (i * 25))
            
            # Create an entry for the result
            result_entry = Entry(window)
            result_entry.place(x=200, y=50 + (i * 25))
            # Insert the result
            result_entry.insert(0, results[i])
            
        # Create mainloop
        window.mainloop()
            
    else:
        # Show an error message
        messagebox.showerror("Error", "Please enter a number and select the type of number and the conversion")


def get_result(check_val, option, num_entry):
    # Get the number entered by the user
    num = num_entry.get()
    # Get the option selected by the user
    option = option.get()
    # Create a list to store the results
    results = []
    # Create a list to store the types of numbers
    types = []
    
    # Check if the user wants to convert to binary
    if check_val[0]:
        # Convert the number to binary
        binary = bin(eval(num))[2:]
        # Append the result to the list
        results.append(binary)
        # Append the type of number to the list
        types.append("Binary")
        
    # Check if the user wants to convert to octal
    if check_val[1]:
        # Convert the number to octal
        octal = oct(eval(num))[2:]
        # Append the result to the list
        results.append(octal)
        # Append the type of number to the list
        types.append("Octal")
        
    # Check if the user wants to convert to hexadecimal
    if check_val[2]:
        # Convert the number to hexadecimal
        hexadecimal = hex(eval(num))[2:]
        # Append the result to the list
        results.append(hexadecimal)
        # Append the type of number to the list
        types.append("Hexadecimal")
        
    # Check if the user wants to convert to decimal
    if check_val[3]:
        # Convert the number to decimal
        decimal = int(num)
        # Append the result to the list
        results.append(decimal)
        # Append the type of number to the list
        types.append("Decimal")

    # Return the results and the types of numbers
    return results, types
