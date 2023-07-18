from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
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
        title_lbl = Label(bg_img,text="Train Data",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)


        b1_1=Button(bg_img, text= "Train" ,command=self.train_classifier,cursor= "hand2",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        b1_1.place(x=650, y=400, width=220, height=50)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path. join(data_dir, file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np. array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids. append(id)
            cv2.imshow( "Training", imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #=========================== Train the classifier And save===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

 







if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
    