# add GUI for the code
import tkinter as ttk
from tkinter import messagebox
import customtkinter as tk

class GUI:
    def __init__(self) -> None:
	    # set a title & higth and width
        self.root = ttk.Tk()
        self.root.geometry('800x450')
        self.root.title(" ")
        self.label = ttk.Label(self.root,text="Welcome",font=(18))
        self.label.pack(padx=10,pady=10)

        # make a buttons fraem
        self.fraem = ttk.Frame(self.root)
        self.butoon = ttk.Button(self.fraem,text="butoon",command=self.butto)
        self.butoon.grid(row=0,column=0)
        self.butoon2 = ttk.Button(self.fraem,text="more button",command=self.butto)
        self.butoon2.grid(row=0,column=3)
        self.fraem.pack(padx=10,pady=10)
        
        # now enable the window
        self.root.protocol("WM_DELETE_WINDOW",self.Quit)
        self.root.mainloop()
    
    def butto(self) -> None:
        print("you click me")
        return
    
    def Quit(self) -> None:
        if not messagebox.askyesno(message="Are you sore?"):
            return
        self.root.destroy()
    
    def turtle(self) -> None:
        from turtle import fd,lt,speed,color,bgcolor,done
        from colorsys import hsv_to_rgb as rgb
        speed(99)
        bgcolor('black')
        h = 1
        for x in range(300):
            rggb = rgb(h,1,1)
            h = h + 0.004
            fd(x)
            lt(91)
            color(rggb)
        done()

    def server(self):
        pass
# now lets run the code
try:
    GUI()
except Exception as code:
    print(f'some error we found :{code}:')