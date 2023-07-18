from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")


        #title
        title_lbl = Label(self.root,text="Face Recognition",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)


        img1 = Image.open(r"Image/face-recognizer.png")
        img1 = img1.resize((300,250),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image = self.photoimg1)
        bg_img.place(x=600,y=300,width=300,height=250)


        btn_1 = Button(self.root,text="Face Recognize",command=self.face_recog,cursor="hand2",font=("Verdana",10,"bold"),bg="#AA77FF",fg="white")
        btn_1.place(x=660,y=550,width=180,height=40)
    #===============================Attendance=====================================
    def mark_attendance(self,n,d,e,r):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]

            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list) and (d not in name_list) and (e not in name_list) and (r not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{d},{e},{r},{dtString},{d1},Present")



    #=================function========================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor ,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
                my_cursur=conn.cursor()

                my_cursur.execute("select student_id from student where student_id="+str(id))
                i = my_cursur.fetchone()
                i = "+".join(i)

                my_cursur.execute("select name from student where student_id="+str(id))
                n = my_cursur.fetchone()
                n = "+".join(n)

                my_cursur.execute("select dept from student where student_id="+str(id))
                d = my_cursur.fetchone()
                d = "+".join(d)

                my_cursur.execute("select email from student where student_id="+str(id))
                e = my_cursur.fetchone()
                e = "+".join(e)

                if confidence>77:
                    cv2.putText (img, f"Roll:{i}", (x,y-75),cv2. FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText (img, f"Name:{n}", (x,y-55),cv2. FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText (img, f"Department:{d}", (x,y-30),cv2. FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText (img, f"Email:{e}", (x,y-5),cv2. FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,d,e)
                else:
                    cv2.rectangle(img,(x,y),(x+w, y+h), (0,0,255),3)
                    cv2.putText (img, "Unknown", (x,y-5),cv2. FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,y]
            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img, faceCascade,1.1,10,(255,25, 255),"Face",clf)
            return img
        

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf, faceCascade)
            cv2.imshow("Welcome to face recognizer",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
    