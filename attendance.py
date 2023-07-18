from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog



myData=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x900+0+0")
        self.root.title("Attendance Managment System")


        #============Variables======================
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_time=StringVar()

        self.var_date=StringVar()

        self.var_atten=StringVar()



        #title
        title_lbl = Label(self.root,text="Attendance Managment System",font=("Verdana",35,"bold"),bg="#AA77FF",fg="#66347F")
        title_lbl.place(x=0,y=10,width=1540,height=55)


        main_frame = Frame(self.root,bd=4,bg="#66347F")
        main_frame.place(x=13,y=100,width=1500,height=650)

        #left side frame
        left_frame = LabelFrame(main_frame,bd=4,bg="#AA77FF",relief=RIDGE,text="Student Attendance Details",font=("Verdana",15,"bold"))
        left_frame.place(x=50,y=15,width=650,height=610)

        
        left_side_frame = Frame(left_frame,bd=4,relief=RIDGE,bg="#66347F")
        left_side_frame.place(x=15,y=20,width=600,height=500)

        #Student name
        attendance_id_lbl = Label(left_side_frame,text="Student ID:",font=("Verdana",10,"bold"))
        attendance_id_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendance_id_entry = ttk.Entry(left_side_frame,textvariable=self.var_id,width=17,font=("Verdana",13,"bold"))
        attendance_id_entry.grid(row=0,column=1,pady=10,sticky=W)

        attendance_name_lbl = Label(left_side_frame,text="Student Name:",font=("Verdana",10,"bold"))
        attendance_name_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        attendance_name_entry = ttk.Entry(left_side_frame,textvariable=self.var_name,width=17,font=("Verdana",13,"bold"))
        attendance_name_entry.grid(row=1,column=1,pady=10,sticky=W)


        attendance_dept_lbl = Label(left_side_frame,text="Department :",font=("Verdana",10,"bold"))
        attendance_dept_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        attendance_dept_entry = ttk.Entry(left_side_frame,textvariable=self.var_dept,width=17,font=("Verdana",13,"bold"))
        attendance_dept_entry.grid(row=2,column=1,pady=10,sticky=W)


        time_lbl = Label(left_side_frame,text="Time:",font=("Verdana",10,"bold"))
        time_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        time_entry = ttk.Entry(left_side_frame,textvariable=self.var_time,width=17,font=("Verdana",13,"bold"))
        time_entry.grid(row=3,column=1,pady=10,sticky=W)


        date_lbl = Label(left_side_frame,text="Date:",font=("Verdana",10,"bold"))
        date_lbl.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        date_entry = ttk.Entry(left_side_frame,textvariable=self.var_date,width=17,font=("Verdana",13,"bold"))
        date_entry.grid(row=4,column=1,pady=10,sticky=W)

        attendance_lbl = Label(left_side_frame,text="Attendance Status:",font=("Verdana",10,"bold"))
        attendance_lbl.grid(row=5,column=0,padx=10,pady=10,sticky=W)

        attendance_combo = ttk.Combobox(left_side_frame,textvariable=self.var_atten,font=("Verdana",10,"bold"),width=16,state="readonly")
        attendance_combo["values"] = ("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=5,column=1,padx=2,pady=10,sticky=W)


        #Buttons Frame
        btn_frame = Frame(left_side_frame,bd=2,relief=RIDGE,bg="#66347F")
        btn_frame.place(x=0,y=310,width=600,height=40)

        save_btn = Button(btn_frame,text="Import Csv",command=self.import_csv,font=("Verdana",13,"bold"),width=25)
        save_btn.grid(row=0,column=0)


        update_btn = Button(btn_frame,text="Export Csv",command=self.export_csv,font=("Verdana",13,"bold"),width=25)
        update_btn.grid(row=0,column=1)

        btn_frame1 = Frame(left_side_frame,bd=2,relief=RIDGE,bg="#66347F")
        btn_frame1.place(x=0,y=350,width=600,height=40)

        delete_btn = Button(btn_frame1,text="Reset",command=self.reset,font=("Verdana",13,"bold"),width=25)
        delete_btn.grid(row=1,column=0)



        reset_btn = Button(btn_frame1,text="Update",font=("Verdana",13,"bold"),width=25)
        reset_btn.grid(row=1,column=1)

















        
        right_frame = LabelFrame(main_frame,bd=4,bg="#AA77FF",relief=RIDGE,text="Attendance Details",font=("Verdana",15,"bold"))
        right_frame.place(x=770,y=15,width=650,height=610)

        table_frame = LabelFrame(right_frame,bg="#AA77FF",relief=RIDGE,font=("Verdana",10,"bold"))
        table_frame.place(x=5,y=5,width=630,height=445)


        #=========================Scroll Bar=============================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable=ttk.Treeview(table_frame,column=("Id","Name","Department","Time","Date","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.xview)


        self.attendanceReportTable.heading("Id",text="Attendance ID")
        self.attendanceReportTable.heading("Name",text="Attendance Name")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Time",text="time")
        self.attendanceReportTable.heading("Date",text="date")
        self.attendanceReportTable.heading("Status",text="Attendance")


        self.attendanceReportTable['show']="headings"
        self.attendanceReportTable.column("Id",width=100)
        self.attendanceReportTable.column("Name",width=100)
        self.attendanceReportTable.column("Department",width=100)
        self.attendanceReportTable.column("Time",width=100)
        self.attendanceReportTable.column("Date",width=100)
        self.attendanceReportTable.column("Status",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)


        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #==========================Fetch data===============================
    def fetch_data(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)

    def import_csv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetch_data(myData)

    #==============================Export csv====================================
    def export_csv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data Found",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open Csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                export = csv.writer(myfile,delimiter=",")
                for i in myData:
                    export.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    def get_cursor(self,event=""):
        cursor_row = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_atten.set(rows[5])

    def reset(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

