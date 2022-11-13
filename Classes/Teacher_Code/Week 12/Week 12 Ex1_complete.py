# Create a GUI named “Coffee analyzer” with an orange background
# Make a label that says “Temperature:” and a box for the user to type in the temperature
# When the user presses the “Analyze” button, show the appropriate messagebox
# <120 -> too cold; >140 -> too hot; 120-140 -> just right

import tkinter
import tkinter.messagebox

def analyze_temp():
    """Shows an appropriate messagebox based on the temperature."""

    global temp_box
    temp = float(temp_box.get())

    if temp < 120:
        tkinter.messagebox.showwarning("Bad coffee", "The coffee is too cold!")
    elif temp > 140:
        tkinter.messagebox.showwarning("Bad coffee", "The coffee is too hot!")
    else:
        tkinter.messagebox.showinfo("Good coffee", "The coffee is just right!")

root = tkinter.Tk()
root.title("Coffee analyzer")
root.configure(bg = "orange")

temp_label = tkinter.Label(root, text = "Temperature:")
temp_label.configure(bg = "orange")
temp_label.grid(row = 0, column = 0)

temp_box = tkinter.Entry(root, width = 5)
temp_box.grid(row = 0, column = 1)

temp_button = tkinter.Button(root, text = "Analyze", command = analyze_temp)
temp_button.grid(row = 0, column = 2)

root.mainloop()
