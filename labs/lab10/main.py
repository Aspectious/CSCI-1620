import tkinter as tk
from gui import GUI

def main():
    root = tk.Tk()
    root.title("Lab 10")
    root.geometry("240x220")
    root.resizable(False,False)


    gui = GUI(root)

    root.mainloop()
    


if __name__ == "__main__":
    main()
