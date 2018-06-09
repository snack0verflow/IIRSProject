from Tkinter import *
class MyFirstGUI:
def __init__(self, master):
self.master = master
master.title("A simple GUI")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
raw_input()