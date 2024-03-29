from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    
    root.mainloop()



if __name__ == "__main__":
    main() 