from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")


        #title
        title_lbl = Label(self.root,text="Help Desk",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)

        main_frame = Frame(self.root,bd=2,bg="#66347F")
        main_frame.place(x=50,y=100,width=1450,height=200)


        dev_label=Label(main_frame,text="For More Query Please Contact:",font=("Verdana",13,"bold"),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=20,y=20)

        dev_label=Label(main_frame,text="19btcse21@suiit.ac.in",font=("Verdana",13,"bold"),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=350,y=20)

        dev_label=Label(main_frame,text="19btcse64@suiit.ac.in",font=("Verdana",13,"bold"),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=650,y=20)


        dev_label=Label(main_frame,text="19btcse68@suiit.ac.in",font=("Verdana",13,"bold"),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=950,y=20)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()