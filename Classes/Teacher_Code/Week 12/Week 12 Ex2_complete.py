# Create a GUI called “Original window” with a “Click me” button
# Each button press should open another window
# Each window is called “New window” with a label “Hello!”

import tkinter

def new_window():
    """Creates and shows a new window."""
    new_window = tkinter.Toplevel()
    new_window.title("New window")
    new_label = tkinter.Label(new_window, text = "Hello!")
    new_label.pack()

root = tkinter.Tk()
root.title("Original window")

new_window_button = tkinter.Button(root, text = "Click me", command = new_window)
new_window_button.pack()

root.mainloop()