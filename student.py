from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")
        ################################ variables ####################################
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_studentID = StringVar()
        self.var_studentName = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_branch = StringVar()
        self.var_registration = StringVar()

        #background image
        img = Image.open("D:/Attendance Managment System/Image/p-1.jpg")
        img = img.resize((1540,900),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root,image = self.photoimg)
        bg_img.place(x=0,y=0,width=1540,height=900)

        
        #title
        title_lbl = Label(bg_img,text="STUDENT DETAILS",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)



        main_frame = Frame(bg_img,bd=4,bg="#66347F")
        main_frame.place(x=13,y=100,width=1500,height=650)


        #left side frame
        left_frame = LabelFrame(main_frame,bd=4,bg="#AA77FF",relief=RIDGE,text="Student Details",font=("Verdana",15,"bold"))
        left_frame.place(x=50,y=15,width=650,height=610)

        #Current Course information
        currentCourse_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Course Information",font=("Verdana",10,"bold"))
        currentCourse_frame.place(x=20,y=10,width=600,height=120)

        #Department
        dept_lbl = Label(currentCourse_frame,text="Department:",font=("Verdana",10,"bold"))
        dept_lbl.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo = ttk.Combobox(currentCourse_frame,textvariable=self.var_dept,font=("Verdana",10,"bold"),width=17,state="readonly")
        dept_combo["values"] = ("Select Department","Computer Science","IT","Civil","Mechnical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_lbl = Label(currentCourse_frame,text="Course:",font=("Verdana",10,"bold"))
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(currentCourse_frame,textvariable=self.var_course,font=("Verdana",10,"bold"),width=17,state="readonly")
        course_combo["values"] = ("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_lbl = Label(currentCourse_frame,text="Year:",font=("Verdana",10,"bold"))
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(currentCourse_frame,textvariable=self.var_year,font=("Verdana",10,"bold"),width=17,state="readonly")
        year_combo["values"] = ("Select Year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_lbl = Label(currentCourse_frame,text="Semester:",font=("Verdana",10,"bold"))
        semester_lbl.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(currentCourse_frame,textvariable=self.var_semester,font=("Verdana",10,"bold"),width=17,state="readonly")
        semester_combo["values"] = ("Select Semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #class student Information
        classStudent_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Information",font=("Verdana",10,"bold"))
        classStudent_frame.place(x=20,y=140,width=600,height=430)


    

        #Student name
        StudentName_lbl = Label(classStudent_frame,text="Name:",font=("Verdana",10,"bold"))
        StudentName_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        StudentName_entry = ttk.Entry(classStudent_frame,textvariable=self.var_studentName,width=17,font=("Verdana",13,"bold"))
        StudentName_entry.grid(row=0,column=1,pady=10,sticky=W)
        #Student Id
        StudentId_lbl = Label(classStudent_frame,text="ID:",font=("Verdana",10,"bold"))
        StudentId_lbl.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        StudentId_entry = ttk.Entry(classStudent_frame,textvariable=self.var_studentID,font=("Verdana",13,"bold"))
        StudentId_entry.grid(row=0,column=3,pady=10,sticky=W)

        #Branch
        Branch_lbl = Label(classStudent_frame,text="Branch:",font=("Verdana",10,"bold"))
        Branch_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        Branch_entry = ttk.Entry(classStudent_frame,textvariable=self.var_branch,width=17,font=("Verdana",13,"bold"))
        Branch_entry.grid(row=1,column=1,pady=5,sticky=W)

        #Student Registration
        registration_lbl = Label(classStudent_frame,text="Reg-ID:",font=("Verdana",10,"bold"))
        registration_lbl.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        registration_entry = ttk.Entry(classStudent_frame,textvariable=self.var_registration,width=17,font=("Verdana",13,"bold"))
        registration_entry.grid(row=1,column=3,pady=10,sticky=W)

        #Student email
        email_lbl = Label(classStudent_frame,text="mail-ID:",font=("Verdana",10,"bold"))
        email_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        email_entry = ttk.Entry(classStudent_frame,textvariable=self.var_email,width=17,font=("Verdana",13,"bold"))
        email_entry.grid(row=2,column=1,pady=10,sticky=W)

        #Student Gender
        gender_lbl = Label(classStudent_frame,text="Gender:",font=("Verdana",10,"bold"))
        gender_lbl.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        # gender_entry = ttk.Entry(classStudent_frame,textvariable=self.var_gender,width=17,font=("Verdana",13,"bold"))
        # gender_entry.grid(row=2,column=3,pady=10,sticky=W)


        gender_combo = ttk.Combobox(classStudent_frame,textvariable=self.var_gender,font=("Verdana",10,"bold"),width=15,state="readonly")
        gender_combo["values"] = ("Select gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,pady=10,sticky=W)

        #Student address
        address_lbl = Label(classStudent_frame,text="Address:",font=("Verdana",10,"bold"))
        address_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        address_entry = ttk.Entry(classStudent_frame,textvariable=self.var_address,width=17,font=("Verdana",13,"bold"))
        address_entry.grid(row=3,column=1,pady=10,sticky=W)

        #Student phone no
        phone_lbl = Label(classStudent_frame,text="Phone-no:",font=("Verdana",10,"bold"))
        phone_lbl.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        phone_entry = ttk.Entry(classStudent_frame,textvariable=self.var_phone,width=17,font=("Verdana",13,"bold"))
        phone_entry.grid(row=3,column=3,pady=10,sticky=W)


        #Radio Buttons
        self.radio_btn1 = StringVar()
        btn_1 = ttk.Radiobutton(classStudent_frame,variable=self.radio_btn1,text="Take Photo Sample",value="Yes")
        btn_1.grid(row = 4,column=0)


        btn_2 = ttk.Radiobutton(classStudent_frame,variable=self.radio_btn1,text="No Photo Sample",value="No")
        btn_2.grid(row = 4,column=1)


        #Buttons Frame
        btn_frame = Frame(classStudent_frame,bd=2,relief=RIDGE,bg="#66347F")
        btn_frame.place(x=0,y=310,width=600,height=40)

        save_btn = Button(btn_frame,command=self.add_data,text="Save",font=("Verdana",13,"bold"),width=12)
        save_btn.grid(row=0,column=0)


        update_btn = Button(btn_frame,command=self.update_data,text="Update",font=("Verdana",13,"bold"),width=12)
        update_btn.grid(row=0,column=1)


        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",font=("Verdana",13,"bold"),width=12)
        delete_btn.grid(row=0,column=2)



        reset_btn = Button(btn_frame,command=self.reser_data,text="Reset",font=("Verdana",13,"bold"),width=12)
        reset_btn.grid(row=0,column=3)




        btn_frame1 = Frame(classStudent_frame,bd=2,relief=RIDGE,bg="#66347F")
        btn_frame1.place(x=0,y=350,width=600,height=40)


        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",font=("Verdana",13,"bold"),width=25)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo Sample",font=("Verdana",13,"bold"),width=25)
        update_photo_btn.grid(row=0,column=1)







        #right side frame
        right_frame = LabelFrame(main_frame,bd=4,bg="#AA77FF",relief=RIDGE,text="Student Details",font=("Verdana",15,"bold"))
        right_frame.place(x=770,y=15,width=650,height=610)


        ################## Search SYStem ########################
        #class student Information
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search Information",font=("Verdana",10,"bold"))
        search_frame.place(x=20,y=20,width=600,height=100)


        search_lbl = Label(search_frame,text="Search:",font=("Verdana",10,"bold"),bg="#66347F",fg="white")
        search_lbl.grid(row=0,column=0,padx=15,pady=10,sticky=W)

        search_combo = ttk.Combobox(search_frame,font=("Verdana",10,"bold"),width=10,state="readonly")
        search_combo["values"] = ("Select","Name","Roll no","ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,width=15,font=("Verdana",12,"bold"))
        search_entry.grid(row=0,column=2,pady=10,sticky=W)

        search_btn = Button(search_frame,text="Search",font=("Verdana",10),width=10,bg="#AA77FF",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showAll_btn = Button(search_frame,text="Show",font=("Verdana",10),width=10,bg="#AA77FF",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)

        ######################## Table Frame ######################
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=20,y=150,width=600,height=350)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","branch","reg-id","email","phone","address","gender","photo"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("branch",text="Branch")
        self.student_table.heading("reg-id",text="Reg-ID")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSampleSatstus")

        self.student_table["show"] = "headings"


        self.student_table.pack(fill=BOTH,expand=1)


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("branch",width=100)
        self.student_table.column("reg-id",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.column("gender",width=100)


        self.student_table.bind("<ButtonRelease>",self.get_curs)

        self.fetch_data()
    ########################### function declaretion ##################################
    def add_data(self):
        if(self.var_dept.get() == "Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()==""):
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_studentID.get(),
                self.var_studentName.get(),
                self.var_branch.get(),
                self.var_registration.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_gender.get(),
                self.radio_btn1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    #=====================================FETCHING DATA======================================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from student")
        data = my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #===========================================GET CURSUR====================================================
    def get_curs(self,event=" "):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_studentID.set(data[4]),
        self.var_studentName.set(data[5]),
        self.var_branch.set(data[6]),
        self.var_registration.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_gender.set(data[11]),
        self.radio_btn1.set(data[12])
    #===========================================UPDATE FUNCTION===================================================
    def update_data(self):
        if(self.var_dept.get() == "Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()==""):
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this student details",parent = self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,branch=%s,Reg_no=%s,email=%s,phone=%s,address=%s,gender=%s,photosample=%s where student_id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_studentName.get(),
                        self.var_branch.get(),
                        self.var_registration.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.radio_btn1.get(),
                        self.var_studentID.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #==========================Delete Function=========================================
    def delete_data(self):
        if self.var_studentID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete student info",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
                    my_cursur=conn.cursor()
                    sql="delete from student where student_id = %s"
                    val = (self.var_studentID.get(),)
                    my_cursur.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","Successfully deleted student information",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    #=============================Reset Function=======================================================
    def reser_data(self):
     
        self.var_dept.set("Select Deparment"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_studentID.set(""),
        self.var_studentName.set(""),
        self.var_branch.set(""),
        self.var_registration.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_gender.set("Select gender"),
        self.radio_btn1.set("")

    #========================== Generate data set or take photo sample====================================
    def generate_dataset(self):
        if(self.var_dept.get() == "Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()==""):
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="9668128936",database="attendance_system")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from student")
                my_result = my_cursur.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursur.execute("update student set dept=%s,course=%s,year=%s,semester=%s,name=%s,branch=%s,Reg_no=%s,email=%s,phone=%s,address=%s,gender=%s,photosample=%s where student_id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_studentName.get(),
                        self.var_branch.get(),
                        self.var_registration.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_gender.get(),
                        self.radio_btn1.get(),
                        self.var_studentID.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reser_data()
                conn.close()
                #============================= Load Predifind data from face frontal from opencv======================================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour = 5


                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                capture = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame_face=capture.read()
                    if face_cropped(frame_face) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(frame_face),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(img_id)==100:
                        break

                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            
            

    

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()