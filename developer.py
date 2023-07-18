from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")


        #title
        title_lbl = Label(self.root,text="Developere",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)

        main_frame = Frame(self.root,bd=2,bg="#66347F")
        main_frame.place(x=50,y=100,width=1450,height=200)

        img = Image.open(r"D:/Attendance Managment System/Image/Alina.jpg")
        img = img.resize((200,200),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(main_frame,image = self.photoimg)
        bg_img.place(x=0,y=0,width=200,height=200)


        dev_label=Label(main_frame,text="Name-Alina Soy",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=5)

        dev_label=Label(main_frame,text="Roll-19btcse64",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=30)

        dev_label=Label(main_frame,text="Dept-CSE Btech 8th sem",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=55)



        main_frame1 = Frame(self.root,bd=2,bg="#66347F")
        main_frame1.place(x=50,y=350,width=1450,height=200)

        img1 = Image.open(r"D:/Attendance Managment System/Image/DSC_0135.jpg")
        img1 = img1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img1 = Label(main_frame1,image = self.photoimg1)
        bg_img1.place(x=0,y=0,width=200,height=200)


        dev_label=Label(main_frame1,text="Name-Mukti Satabdi",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=5)

        dev_label=Label(main_frame1,text="Roll-19btcse68",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=30)

        dev_label=Label(main_frame1,text="Dept-CSE Btech 8th sem",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=55)




        main_frame2 = Frame(self.root,bd=2,bg="#66347F")
        main_frame2.place(x=50,y=600,width=1450,height=200)

        img2 = Image.open(r"D:/Attendance Managment System/Image/pari.jpg")
        img2 = img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img2 = Label(main_frame2,image = self.photoimg2)
        bg_img2.place(x=0,y=0,width=200,height=200)


        dev_label=Label(main_frame2,text="Name-Parween Khan",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=5)

        dev_label=Label(main_frame2,text="Roll-19btcse21",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=30)

        dev_label=Label(main_frame2,text="Dept-CSE Btech 8th sem",font=("Verdana",10),bg="#AA77FF",fg="#66347F")
        dev_label.place(x=250,y=55)










if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()