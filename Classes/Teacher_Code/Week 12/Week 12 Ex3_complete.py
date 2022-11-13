# Create a GUI with called “Fortune teller”
# GUI should contain a label and a button with green font
# When the button is pressed, show a positive fortune 80% of the time and a negative fortune the other 20%
# When hovering over the label, show a yellow background label with Arial 10 italicized and bolded font

import tkinter
import tkinter.messagebox
import random

def label_hover(event):
    """Show an informational label when hovering."""
    global root
    new_label = tkinter.Label(root, text = "You have an 80% chance to win!")
    new_label.configure(bg = "yellow")
    new_label.configure(font = "Arial 10 italic bold")
    new_label.grid(row = 1, column = 0)

def get_fortune():
    """Gives a positive fortune 80% of the time, negative 20% of the time."""
    fortune = random.randrange(1, 6)
    if fortune <= 4:
        tkinter.messagebox.showinfo("Yay!", "You will be fortunate today :)")
    else:
        tkinter.messagebox.showwarning("Oh no!", "Today will not be a good day :(")

root = tkinter.Tk()
root.title("Fortune teller")

info_label = tkinter.Label(root, text = "Click on the button to see your fortune.")
info_label.grid(row = 0, column = 0)
info_label.bind("<Enter>", label_hover)

fortune_button = tkinter.Button(root, text = "Show fortune", command = get_fortune)
fortune_button.configure(fg = "green")
fortune_button.grid(row = 0, column = 1)

root.mainloop()
