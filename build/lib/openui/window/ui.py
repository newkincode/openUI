import tkinter

class Oui():
    def __init__(self) -> None:
        self.win = tkinter.Tk()
        self.win.title("OpenUI")
        self.win.geometry("800x600")
        
    def show(self):
        self.win.mainloop()