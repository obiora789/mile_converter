from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)
calculate_unit = ""


def calculate_km():
    """Method to convert miles to Kilometres"""
    input_value = float(input_number.get())
    output_value = round(input_value * 1.60934, 2)
    unit_value.config(text=f"{output_value}")


def calculate_nm():
    """Method to convert miles to Nautical Miles"""
    input_value = float(input_number.get())
    output_value = round(input_value * 0.868976, 2)
    unit_value.config(text=f"{output_value}")


def calculate_yards():
    """Method to convert miles to Yards"""
    input_value = float(input_number.get())
    output_value = round(input_value * 1760)
    unit_value.config(text=f"{output_value}")


def calculate_feet():
    """Method to convert miles to Feet"""
    input_value = float(input_number.get())
    output_value = round(input_value * 5280)
    unit_value.config(text=f"{output_value}")


def calculate_inches():
    """Method to convert miles to Inches"""
    input_value = float(input_number.get())
    output_value = round(input_value * 63360)
    unit_value.config(text=f"{output_value}")


def unit_box_used(event):
    """Get the unit selected by the user to be converted."""
    global calculate_unit
    calculate_unit = unit_box.get(unit_box.curselection())


def calculate_value():
    """Determine the method to run based on user selection"""
    if calculate_unit == "Km":
        calculate_km()
    elif calculate_unit == "Nm":
        calculate_nm()
    elif calculate_unit == "Yards":
        calculate_yards()
    elif calculate_unit == "Feet":
        calculate_feet()
    elif calculate_unit == "Inches":
        calculate_inches()


input_number = Entry(width=7)
input_number.insert(END, "0")
input_number.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 14))
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 14))
is_equal_to.config(pady=10, padx=10)
is_equal_to.grid(column=0, row=1)

unit_value = Label(text="0", font=("Arial", 14))
unit_value.grid(column=1, row=1)

# kilometres = Label(text="Km", font=("Arial", 14))
unit_box = Listbox(height=5, width=7)
units = ["Km", "Nm", "Yards", "Feet", "Inches"]
for unit in units:
    unit_box.insert(units.index(unit), unit)
unit_box.bind("<<ListboxSelect>>", unit_box_used)
unit_box.grid(column=2, row=1)

calculate = Button(text="Calculate", command=calculate_value, width=4)
calculate.grid(column=1, row=2)

window.mainloop()
