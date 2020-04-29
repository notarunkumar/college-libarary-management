#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 11:45:10 PM

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

import student_registration_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.resizable(0, 0)
    student_registration_support.set_Tk_var()
    top = Student_Registration (root)
    student_registration_support.init(root, top)
    root.mainloop()

w = None
def create_Student_Registration(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    student_registration_support.set_Tk_var()
    top = Student_Registration (w)
    student_registration_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_Registration():
    global w
    w.destroy()
    w = None


class Student_Registration:
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
        font11 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 18 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x522+651+252")
        top.title("Student Registration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.07, rely=0.06, height=47, width=367)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''New Student Registration''')

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.07, rely=0.19, relheight=0.75, relwidth=0.86)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=513)

        self.Label2 = Label(self.Canvas1)
        self.Label2.place(relx=0.18, rely=0.08, height=34, width=58)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Name''')

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.12, rely=0.2, height=34, width=111)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Department''')

        self.Label4 = Label(self.Canvas1)
        self.Label4.place(relx=0.15, rely=0.33, height=34, width=86)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Semester''')

        self.Label5 = Label(self.Canvas1)
        self.Label5.place(relx=0.18, rely=0.46, height=34, width=54)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Batch''')

        self.Label6 = Label(self.Canvas1)
        self.Label6.place(relx=0.16, rely=0.6, height=34, width=76)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font10)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Roll No.''')

        self.Label7 = Label(self.Canvas1)
        self.Label7.place(relx=0.14, rely=0.73, height=34, width=88)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font10)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Password''')

        self.name = Entry(self.Canvas1)
        self.name.place(relx=0.49, rely=0.1,height=24, relwidth=0.44)
        self.name.configure(background="white")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="TkFixedFont")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="black")
        self.name.configure(insertbackground="black")
        self.name.configure(selectbackground="#c4c4c4")
        self.name.configure(selectforeground="black")
        self.name.configure(textvariable=student_registration_support.uname)

        self.department = Entry(self.Canvas1)
        self.department.place(relx=0.49, rely=0.23,height=24, relwidth=0.44)
        self.department.configure(background="white")
        self.department.configure(disabledforeground="#a3a3a3")
        self.department.configure(font="TkFixedFont")
        self.department.configure(foreground="#000000")
        self.department.configure(highlightbackground="#d9d9d9")
        self.department.configure(highlightcolor="black")
        self.department.configure(insertbackground="black")
        self.department.configure(selectbackground="#c4c4c4")
        self.department.configure(selectforeground="black")
        self.department.configure(textvariable=student_registration_support.udepart)

        self.semester = Entry(self.Canvas1)
        self.semester.place(relx=0.49, rely=0.36,height=24, relwidth=0.44)
        self.semester.configure(background="white")
        self.semester.configure(disabledforeground="#a3a3a3")
        self.semester.configure(font="TkFixedFont")
        self.semester.configure(foreground="#000000")
        self.semester.configure(highlightbackground="#d9d9d9")
        self.semester.configure(highlightcolor="black")
        self.semester.configure(insertbackground="black")
        self.semester.configure(selectbackground="#c4c4c4")
        self.semester.configure(selectforeground="black")
        self.semester.configure(textvariable=student_registration_support.usem)

        self.batch = Entry(self.Canvas1)
        self.batch.place(relx=0.49, rely=0.48,height=24, relwidth=0.44)
        self.batch.configure(background="white")
        self.batch.configure(disabledforeground="#a3a3a3")
        self.batch.configure(font="TkFixedFont")
        self.batch.configure(foreground="#000000")
        self.batch.configure(highlightbackground="#d9d9d9")
        self.batch.configure(highlightcolor="black")
        self.batch.configure(insertbackground="black")
        self.batch.configure(selectbackground="#c4c4c4")
        self.batch.configure(selectforeground="black")
        self.batch.configure(textvariable=student_registration_support.ubatch)

        self.srollno = Entry(self.Canvas1)
        self.srollno.place(relx=0.49, rely=0.61,height=24, relwidth=0.44)
        self.srollno.configure(background="white")
        self.srollno.configure(disabledforeground="#a3a3a3")
        self.srollno.configure(font="TkFixedFont")
        self.srollno.configure(foreground="#000000")
        self.srollno.configure(highlightbackground="#d9d9d9")
        self.srollno.configure(highlightcolor="black")
        self.srollno.configure(insertbackground="black")
        self.srollno.configure(selectbackground="#c4c4c4")
        self.srollno.configure(selectforeground="black")
        self.srollno.configure(textvariable=student_registration_support.uroll)

        self.password = Entry(self.Canvas1)
        self.password.place(relx=0.49, rely=0.74,height=24, relwidth=0.44)
        self.password.configure(background="white")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(font="TkFixedFont")
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(insertbackground="black")
        self.password.configure(selectbackground="#c4c4c4")
        self.password.configure(selectforeground="black")
        self.password.configure(textvariable=student_registration_support.upass)

        self.backbutton = Button(self.Canvas1)
        self.backbutton.place(relx=0.14, rely=0.87, height=33, width=76)
        self.backbutton.configure(activebackground="#d9d9d9")
        self.backbutton.configure(activeforeground="#000000")
        self.backbutton.configure(background="#d9d9d9")
        self.backbutton.configure(command=student_registration_support.back_Function)
        self.backbutton.configure(disabledforeground="#a3a3a3")
        self.backbutton.configure(foreground="#000000")
        self.backbutton.configure(highlightbackground="#d9d9d9")
        self.backbutton.configure(highlightcolor="black")
        self.backbutton.configure(pady="0")
        self.backbutton.configure(text='''BACK''')

        self.clearbutton = Button(self.Canvas1)
        self.clearbutton.place(relx=0.45, rely=0.87, height=33, width=75)
        self.clearbutton.configure(activebackground="#d9d9d9")
        self.clearbutton.configure(activeforeground="#000000")
        self.clearbutton.configure(background="#d9d9d9")
        self.clearbutton.configure(command=student_registration_support.clear_Function)
        self.clearbutton.configure(disabledforeground="#a3a3a3")
        self.clearbutton.configure(foreground="#000000")
        self.clearbutton.configure(highlightbackground="#d9d9d9")
        self.clearbutton.configure(highlightcolor="black")
        self.clearbutton.configure(pady="0")
        self.clearbutton.configure(text='''CLEAR''')

        self.submitButton = Button(self.Canvas1)
        self.submitButton.place(relx=0.78, rely=0.87, height=33, width=74)
        self.submitButton.configure(activebackground="#d9d9d9")
        self.submitButton.configure(activeforeground="#000000")
        self.submitButton.configure(background="#d9d9d9")
        self.submitButton.configure(command=student_registration_support.submit_Function)
        self.submitButton.configure(disabledforeground="#a3a3a3")
        self.submitButton.configure(font=font11)
        self.submitButton.configure(foreground="#000000")
        self.submitButton.configure(highlightbackground="#d9d9d9")
        self.submitButton.configure(highlightcolor="black")
        self.submitButton.configure(pady="0")
        self.submitButton.configure(text='''SUBMIT''')






#if __name__ == '__main__':
#    vp_start_gui()


