from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")


        #background image
        img = Image.open("D:/Attendance Managment System/Image/p-1.jpg")
        img = img.resize((1540,900),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1540,height=900)

        
        #title
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)


        #Buttons-1(studnet details)
        img1 = Image.open("D:/Attendance Managment System/Image/student-profile.png")
        img1 = img1.resize((180,180),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        btn = Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        btn.place(x=100,y=130,width=180,height=180)

        btn_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=100,y=310,width=180,height=40)




        #Button-2(face detection)
        img2 = Image.open("D:/Attendance Managment System/Image/facial-recognition.png")
        img2 = img2.resize((180,180),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        btn = Button(bg_img,image=self.photoimg2,cursor="hand2",command=self.recognition_details)
        btn.place(x=500,y=130,width=180,height=180)

        btn_1= Button(bg_img,text="Face Detection",cursor="hand2",command=self.recognition_details,font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=500,y=310,width=180,height=40)



        #Button-3(Attendance)
        img3 = Image.open("D:/Attendance Managment System/Image/attendance.png")
        img3 = img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        btn = Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.attendance_details)
        btn.place(x=900,y=130,width=180,height=180)

        btn_1= Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_details,font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=900,y=310,width=180,height=40)


        #Button-4(HELP DESK)
        img4 = Image.open("D:/Attendance Managment System/Image/help-desk.png")
        img4 = img4.resize((180,180),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn = Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.help_details)
        btn.place(x=1300,y=130,width=180,height=180)

        btn_1= Button(bg_img,text="Help",command=self.help_details,cursor="hand2",font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=1300,y=310,width=180,height=40)



        #Button-5(train data)
        img5 = Image.open("D:/Attendance Managment System/Image/robot.png")
        img5 = img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_details)
        btn.place(x=100,y=450,width=180,height=180)

        btn_1= Button(bg_img,text="Train Data",cursor="hand2",command=self.train_details,font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=100,y=620,width=180,height=40)


        #Button-6(photo)
        img6 = Image.open("D:/Attendance Managment System/Image/image.png")
        img6 = img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        btn.place(x=500,y=450,width=180,height=180)

        btn_1= Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=500,y=620,width=180,height=40)


        #Button-7(Attendance)
        img7 = Image.open("D:/Attendance Managment System/Image/coding.png")
        img7 = img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.developer_details)
        btn.place(x=900,y=450,width=180,height=180)

        btn_1= Button(bg_img,text="Developer",command=self.developer_details,cursor="hand2",font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=900,y=620,width=180,height=40)


        #Button-8(EXIT)
        img8 = Image.open("D:/Attendance Managment System/Image/exit.png")
        img8 = img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.iexit)
        btn.place(x=1300,y=450,width=180,height=180)

        btn_1= Button(bg_img,text="Exit",command=self.iexit,cursor="hand2",font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=1300,y=620,width=180,height=40)


    def open_img(self):
        os.startfile("data")


    def iexit(self):
        # self.iexit = tkinter.Message.askyesno("Face Recognition","Do you want to exit the window")
        # if self.iexit>0:
        #     self.root.destroy()
        # else:
        #     return
        self.root.destroy()
    #################### Function Buttons ###########################
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def recognition_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)


    def attendance_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()