from tkinter import *


class MyButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Button", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit Button", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("It worked")

root = Tk()
b = MyButtons(root)
root.mainloop()
