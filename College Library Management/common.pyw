#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 09:06:38 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from Tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import common_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.resizable(0,0)
    top = LIBRARY_PANEL (root)
    common_support.init(root, top)
    root.mainloop()

w = None
def create_LIBRARY_PANEL(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = LIBRARY_PANEL (w)
    common_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LIBRARY_PANEL():
    global w
    w.destroy()
    w = None


class LIBRARY_PANEL:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 1 -overstrike 0"

        top.geometry("600x345+665+223")
        top.title("LIBRARY PANEL")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.15, rely=0.09, height=76, width=432)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#f0f0f0")
        self.Label1.configure(highlightcolor="#646464")
        self.Label1.configure(text='''COLLEGE LIBRARY PANEL''')

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.12, rely=0.29, relheight=0.59, relwidth=0.77)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=463)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.19, rely=0.1, height=34, width=294)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Choose your login portal''')

        self.emp = Button(self.Canvas1)
        self.emp.place(relx=0.15, rely=0.49, height=63, width=126)
        self.emp.configure(activebackground="#d9d9d9")
        self.emp.configure(activeforeground="#000000")
        self.emp.configure(background="#d9d9d9")
        self.emp.configure(command=common_support.empcall)
        self.emp.configure(disabledforeground="#a3a3a3")
        self.emp.configure(font=font10)
        self.emp.configure(foreground="#000000")
        self.emp.configure(highlightbackground="#d9d9d9")
        self.emp.configure(highlightcolor="black")
        self.emp.configure(pady="0")
        self.emp.configure(text='''EMPLOYEE''')

        self.stu = Button(self.Canvas1)
        self.stu.place(relx=0.6, rely=0.49, height=63, width=126)
        self.stu.configure(activebackground="#d9d9d9")
        self.stu.configure(activeforeground="#000000")
        self.stu.configure(background="#d9d9d9")
        self.stu.configure(command=common_support.stucall)
        self.stu.configure(disabledforeground="#a3a3a3")
        self.stu.configure(font=font10)
        self.stu.configure(foreground="#000000")
        self.stu.configure(highlightbackground="#d9d9d9")
        self.stu.configure(highlightcolor="black")
        self.stu.configure(pady="0")
        self.stu.configure(text='''STUDENT''')






if __name__ == '__main__':
    vp_start_gui()



