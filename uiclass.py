from tkinter import *


class ganeshbutton:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printbutton=Button(frame,text="print message",command=self.printmessage)
        self.printbutton.pack(side=LEFT)

        self.quitbutton = Button(frame,text="quit",command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("this actually works")

root = Tk()
b = ganeshbutton(root)
root.mainloop()
