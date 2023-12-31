import tkinter as tk

# Create a function that will be called when the button is clicked
def button_click():
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Click Example")

# Create a button and attach the button_click function to it
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

# Create a label to display a message
label = tk.Label(root, text="")
label.pack()

# Start the tkinter main loop
root.mainloop()



