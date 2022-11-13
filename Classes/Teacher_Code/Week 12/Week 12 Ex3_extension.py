# Create a GUI with called “Fortune teller”
# GUI should contain a label and a button with green font
# When the button is pressed, show a positive fortune 80% of the time and a negative fortune the other 20%
# When hovering over the label, show a yellow background label with Arial 10 italicized and bolded font

# EXTENSION - show the extra label when hovering, and hide it when the hover ends

import tkinter
import tkinter.messagebox
import random

def label_hover(event):
    """Show an informational label when hovering."""
    global new_label
    new_label.grid(row = 1, column = 0) # add label to the grid
    
def label_hover_end(event):
    """Remove the informational label when hovering ends."""
    global new_label
    new_label.grid_remove() # remove label from the grid
    
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
info_label.bind("<Leave>", label_hover_end)

# Create label but don't add it to the grid yet
# Label will be invisible until added to the grid upon hover
# Label defined outside the functions to make sure they can both access it
new_label = tkinter.Label(root, text = "You have an 80% chance to win!")
new_label.configure(bg = "yellow")
new_label.configure(font = "Arial 10 italic bold")

fortune_button = tkinter.Button(root, text = "Show fortune", command = get_fortune)
fortune_button.configure(fg = "green")
fortune_button.grid(row = 0, column = 1)

root.mainloop()
