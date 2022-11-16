# Import all the required modules
from tkinter import Frame, Label, Entry, IntVar, Radiobutton, Checkbutton


# Create a function for fields
def fields(window):
    # Create a frame for fields
    field_frame = Frame(window)
    field_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Create a label for user entry
    num_label = Label(field_frame, text="Enter a number: ")
    num_label.grid(row=0, column=0, pady=10, sticky="w")
    # Create an entry for user input
    num_entry = Entry(field_frame)
    num_entry.grid(row=0, column=1)
    
    # Create a variable to store the option selected
    option = IntVar()
    
    # Create a label for the radio buttons
    option_label = Label(field_frame, text="Select the type of number: ")
    option_label.grid(row=1, column=0, pady=10, sticky="w")
    
    # Create radio for binary
    bin_radio = Radiobutton(field_frame, text="Binary", variable=option, value=1)
    bin_radio.grid(row=2, column=0, sticky="w")
    
    # Create radio for octal
    oct_radio = Radiobutton(field_frame, text="Octal", variable=option, value=2)
    oct_radio.grid(row=3, column=0, sticky="w")
    
    # Create radio for hexadecimal
    hex_radio = Radiobutton(field_frame, text="Hexadecimal", variable=option, value=3)
    hex_radio.grid(row=4, column=0, sticky="w")
    
    # Create a radio for decimal
    dec_radio = Radiobutton(field_frame, text="Decimal", variable=option, value=4)
    dec_radio.grid(row=5, column=0, sticky="w")
    
    # Create a label for the numbers to be converted
    conversion_label = Label(field_frame, text="Select the conversion: ")
    conversion_label.grid(row=1, column=1, padx=30, pady=10, sticky="w")

    # Create a list to store the check buttons
    check_val = []
    
    # Create a check button for binary
    bin_val = IntVar()
    bin_check = Checkbutton(field_frame, text="Binary", variable=bin_val)
    bin_check.grid(row=2, column=1, sticky="w", padx=30)
    # Append the value to the list
    check_val.append(bin_val)
    
    # Create a check button for octal
    oct_val = IntVar()
    oct_check = Checkbutton(field_frame, text="Octal", variable=oct_val)
    oct_check.grid(row=3, column=1, sticky="w", padx=30)
    # Append the value to the list
    check_val.append(oct_val)
    
    # Create a check button for hexadecimal
    hex_val = IntVar()
    hex_check = Checkbutton(field_frame, text="Hexadecimal", variable=hex_val)
    hex_check.grid(row=4, column=1, sticky="w", padx=30)
    # Append the value to the list
    check_val.append(hex_val)
    
    # Create a check button for decimal
    dec_val = IntVar()
    dec_check = Checkbutton(field_frame, text="Decimal", variable=dec_val)
    dec_check.grid(row=5, column=1, sticky="w", padx=30)
    # Append the value to the list
    check_val.append(dec_val)
    
    # Return the list of checkbutton values, the option selected and the entry
    return check_val, option, num_entry
