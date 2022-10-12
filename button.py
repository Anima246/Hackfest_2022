# importing tkinter library for making GUI
import tkinter as tk

#calling Tk() function
#this will create the top level window with a frame
#of title bar, control box with the minimize and close buttons
#className will change the title bar of the box
top = tk.Tk(className=' Button and Label')

# The geometry() method defines the width, height and coordinates
# of the top left corner of the frame
# as window.geometry("widthxheight+XPOS+YPOS")
top.geometry("300x100+300+300")

# Syntax for label is Label(window, attributes)
# here we have created a window of name 'top'
w = tk.Label(top, text="Enter your password")

# Syntax for button is Button(window, attribute)
B = tk.Button(top, text ="Play", bg="blue", fg="white")

# The pack method tells Tk to fit the size of the window to the given text.
# Otherwise text won't appear.
w.pack()
B.pack()

#The window won't appear until we enter the Tkinter event loop
#The script will remain in the event loop until we close the window.
top.mainloop()


