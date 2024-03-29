from tkinter import *
from tkinter import ttk




def main():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="MP3 Player!!!").grid(column=10, row=10)
    
    root.mainloop()



if __name__ == "__main__":
    main() 