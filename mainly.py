import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def click_checkin():
    call(["python", "checkin.py"])


def click_list():
    call(["python", "listgui.py"])


def click_checkout():
    call(["python", "checkoutgui.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''The top evel window is configured'''
        _backgroundcolor = '#d9d9d9'  # X11 color: 'gray85'
        _foregroundcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff'  # X11 color: 'white'
        _colorcode1 = '#ffffff'  # X11 color: 'white'
        _colorcode2 = '#ffffff'  # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        root.geometry("963x549+540+110")
        root.title("ZOSTEL ROOM MANAGEMENT")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.menubar = Menu(root, font=font9, bg=_backgroundcolor, fg=_foregroundcolor)
        root.configure(menu=self.menubar)

        self.firstFrame = Frame(root)
        self.firstFrame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.firstFrame.configure(relief=GROOVE)
        self.firstFrame.configure(borderwidth="2")
        self.firstFrame.configure(relief=GROOVE)
        self.firstFrame.configure(background="#E5E2E7")
        self.firstFrame.configure(highlightbackground="#d9d9d9")
        self.firstFrame.configure(highlightcolor="black")
        self.firstFrame.configure(width=925)

        self.WelcomeLabel = Message(self.firstFrame)
        self.WelcomeLabel.place(relx=0.067, rely=0.01, relheight=0.15, relwidth=0.86)
        self.WelcomeLabel.configure(background="#E5E2E7")
        self.WelcomeLabel.configure(font=font16)
        self.WelcomeLabel.configure(foreground="#000000")
        self.WelcomeLabel.configure(highlightbackground="#c0b8c3")
        self.WelcomeLabel.configure(highlightcolor="black")
        self.WelcomeLabel.configure(text='''ZOSTEL PANCHGANI''')
        self.WelcomeLabel.configure(width=791)

        self.firstButton = Button(self.firstFrame)
        self.firstButton.place(relx=0.206, rely=0.19, height=93, width=566)
        self.firstButton.configure(activebackground="#d9d9d9")
        self.firstButton.configure(activeforeground="#000000")
        self.firstButton.configure(background="#d9d9d9")
        self.firstButton.configure(disabledforeground="#bfbfbf")
        self.firstButton.configure(font=font14)
        self.firstButton.configure(foreground="#000000")
        self.firstButton.configure(highlightbackground="#d9d9d9")
        self.firstButton.configure(highlightcolor="black")
        self.firstButton.configure(pady="0")
        self.firstButton.configure(text='''Check-In''')
        self.firstButton.configure(width=566)
        self.firstButton.configure(command=click_checkin)

        self.secondButton = Button(self.firstFrame)
        self.secondButton.place(relx=0.206, rely=0.38, height=93, width=566)
        self.secondButton.configure(activebackground="#d9d9d9")
        self.secondButton.configure(activeforeground="#000000")
        self.secondButton.configure(background="#d9d9d9")
        self.secondButton.configure(disabledforeground="#bfbfbf")
        self.secondButton.configure(font=font14)
        self.secondButton.configure(foreground="#000000")
        self.secondButton.configure(highlightbackground="#d9d9d9")
        self.secondButton.configure(highlightcolor="black")
        self.secondButton.configure(pady="0")
        self.secondButton.configure(text='''Guest List''')
        self.secondButton.configure(width=566)
        self.secondButton.configure(command=click_list)

        self.thirdButton = Button(self.firstFrame)
        self.thirdButton.place(relx=0.206, rely=0.58, height=93, width=566)
        self.thirdButton.configure(activebackground="#d9d9d9")
        self.thirdButton.configure(activeforeground="#000000")
        self.thirdButton.configure(background="#d9d9d9")
        self.thirdButton.configure(disabledforeground="#bfbfbf")
        self.thirdButton.configure(font=font14)
        self.thirdButton.configure(foreground="#000000")
        self.thirdButton.configure(highlightbackground="#d9d9d9")
        self.thirdButton.configure(highlightcolor="black")
        self.thirdButton.configure(pady="0")
        self.thirdButton.configure(text='''Check-Out''')
        self.thirdButton.configure(width=566)
        self.thirdButton.configure(command=click_checkout)



        self.fifthButton = Button(self.firstFrame)
        self.fifthButton.place(relx=0.6, rely=0.8, height=51, width=283)
        self.fifthButton.configure(activebackground="#d9d9d9")
        self.fifthButton.configure(activeforeground="#000000")
        self.fifthButton.configure(background="#d9d9d9")
        self.fifthButton.configure(disabledforeground="#bfbfbf")
        self.fifthButton.configure(font=font14)
        self.fifthButton.configure(foreground="#000000")
        self.fifthButton.configure(highlightbackground="#d9d9d9")
        self.fifthButton.configure(highlightcolor="black")
        self.fifthButton.configure(pady="0")
        self.fifthButton.configure(text='''Quit''')
        self.fifthButton.configure(width=566)
        self.fifthButton.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST = HOTEL_MANAGEMENT()


