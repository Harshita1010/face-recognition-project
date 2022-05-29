from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")


    #====== variables ===========
    self.var_atten_roll=StringVar()
    self.var_atten_name=StringVar()
    self.var_atten_dep=StringVar()
    self.var_atten_sem=StringVar()
    self.var_atten_time=StringVar()
    self.var_atten_date=StringVar()
    self.var_atten_attendance=StringVar()

    

    # background image
    img=Image.open("images/background/background_21.jpg") 
    img=img.resize((1909,700),Image.ANTIALIAS) 
    self.photoimg=ImageTk.PhotoImage(img)

    bg_img=Label(self.home,image=self.photoimg)
    bg_img.place(x=-3,y=0)

    # title face recognization attendance system
    title_lbl=Label(bg_img,text="STUDENT  ATTENDANCE",font=("Pristina",50,"underline"),fg="white",bg="black")
    title_lbl.place(x=-300,y=0,width=1909,height=70)

    main_frame=Frame(bg_img,bd=2,bg="black")
    main_frame.place(x=130,y=90,width=1050,height=530)

     # left label frame
    Left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"),fg="white")
    Left_frame.place(x=10,y=10,width=520,height=500)
    
    img_left_1=Image.open("images/attendance_image4.jpg") 
    img_left_1=img_left_1.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_left_1=ImageTk.PhotoImage(img_left_1)

    f_lbl=Label(Left_frame,image=self.photoimg_left_1)
    f_lbl.place(x=0,y=0,width=260,height=100)

    img_left_2=Image.open("images/attendance_image5.jpg") 
    img_left_2=img_left_2.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_left_2=ImageTk.PhotoImage(img_left_2)

    f_lbl=Label(Left_frame,image=self.photoimg_left_2)
    f_lbl.place(x=260,y=0,width=260,height=100)

    left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="black")
    left_inside_frame.place(x=0,y=120,width=517,height=200)

    # labels and entries

    # Roll
    Roll_label=Label(left_inside_frame,bg="black",text="Roll Number :",font=("times new roman",12,"bold"),fg="white")
    Roll_label.grid(row=0,column=0,padx=5,sticky=W)

    atten_roll=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
    atten_roll.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    # student Name
    name_label=Label(left_inside_frame,bg="black",text="Student Name :",font=("times new roman",12,"bold"),fg="white")
    name_label.grid(row=0,column=2,padx=5,sticky=W)

    atten_name=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
    atten_name.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    # department
    dep_label=Label(left_inside_frame,bg="black",text="Department :",font=("times new roman",12,"bold"),fg="white")
    dep_label.grid(row=1,column=0,padx=2,sticky=W)

    atten_dep=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
    atten_dep.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    # semester
    sem_label=Label(left_inside_frame,bg="black",text="Semester :",font=("times new roman",12,"bold"),fg="white")
    sem_label.grid(row=1,column=2,padx=5,sticky=W)

    atten_sem=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_sem,font=("times new roman",12,"bold"))
    atten_sem.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    # Time
    time_label=Label(left_inside_frame,bg="black",text="Time :",font=("times new roman",12,"bold"),fg="white")
    time_label.grid(row=2,column=0,padx=5,sticky=W)

    atten_time=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
    atten_time.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    # Date
    date_label=Label(left_inside_frame,bg="black",text="Date :",font=("times new roman",12,"bold"),fg="white")
    date_label.grid(row=2,column=2,padx=5,sticky=W)

    atten_date=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
    atten_date.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    #  Attendance
    atten_label=Label(left_inside_frame,bg="black",text="Attendance :",font=("times new roman",12,"bold"),fg="white")
    atten_label.grid(row=4,column=0,padx=5,sticky=W)

    self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=14)
    self.atten_status["values"]=("Status","Present","Absent")
    self.atten_status.grid(row=4,column=1,padx=5,pady=5,sticky=W)
    self.atten_status.current(0)


    # button frame
    btn_frame=Frame(Left_frame,bd=2,bg="black",relief=RIDGE)
    btn_frame.place(x=-2,y=330,width=517,height=70)

    import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=28,font=("times new roman",12,"bold"),bg="lightgreen",fg="black")
    import_btn.grid(row=0,column=0)

    export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=30,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
    export_btn.grid(row=0,column=1)

    reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=28,font=("times new roman",12,"bold"),bg="lightblue",fg="black")
    reset_btn.grid(row=2,column=0)

    reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=30,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
    reset_btn.grid(row=2,column=1)

   
    




    # right label frame
    Right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Attendance",font=("times new roman",12,"bold"),fg="white")
    Right_frame.place(x=540,y=10,width=500,height=500)

    img_right_1=Image.open("images/attendance_image7.jpg") 
    img_right_1=img_right_1.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_right_1=ImageTk.PhotoImage(img_right_1)

    f_lbl=Label(Right_frame,image=self.photoimg_right_1)
    f_lbl.place(x=0,y=0,width=260,height=100)

    img_right_2=Image.open("images/attendance_image1.jpg") 
    img_right_2=img_right_2.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_right_2=ImageTk.PhotoImage(img_right_2)

    f_lbl=Label(Right_frame,image=self.photoimg_right_2)
    f_lbl.place(x=260,y=0,width=260,height=100)

    table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="black")
    table_frame.place(x=0,y=120,width=499,height=320)

    # ======== scroll bar ==========
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("roll","name","department","semester","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=self.AttendanceReportTable.xview)
    scroll_y.config(command=self.AttendanceReportTable.yview)

    self.AttendanceReportTable.heading("roll",text="Roll Number")
    self.AttendanceReportTable.heading("name",text="Student Name")
    self.AttendanceReportTable.heading("department",text="Department")
    self.AttendanceReportTable.heading("semester",text="Semester")
    self.AttendanceReportTable.heading("time",text="Time")
    self.AttendanceReportTable.heading("date",text="Date")
    self.AttendanceReportTable.heading("attendance",text="Attendance")

    self.AttendanceReportTable["show"]="headings"

    self.AttendanceReportTable.column("roll",width=150)
    self.AttendanceReportTable.column("name",width=150)
    self.AttendanceReportTable.column("department",width=150)
    self.AttendanceReportTable.column("semester",width=150)
    self.AttendanceReportTable.column("time",width=150)
    self.AttendanceReportTable.column("date",width=150)
    self.AttendanceReportTable.column("attendance",width=200)

    self.AttendanceReportTable.pack(fill=BOTH,expand=1)

    self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
  

  # ======== fetch data=============
  def fetchData(self,rows):
    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
    for i in rows:
      self.AttendanceReportTable.insert("",END,values=i)
  

  # import csv
  def importCsv(self):
    global mydata
    mydata.clear()
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.home)
    with open(fln) as myfile:
      csvread=csv.reader(myfile,delimiter=",")
      for i in csvread:
        mydata.append(i)
      self.fetchData(mydata)

  # export csv
  def exportCsv(self):
    try:
      if len(mydata)<1:
        messagebox.showerror("No Data","No data found to export",parent=self.home)
        return false
      fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.home)
      with open(fln,mode="w",newline="") as myfile:
        exp_write=csv.writer(myfile,delimiter=",")
        for i in mydata:
          exp_write.writerow(i)
        messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
    except Exception as es:
        messagebox.showerror("ERROR!!",f"Due To :{str(es)}",parent=self.home)
  

  def get_cursor(self,event=""):
    cursor_row=self.AttendanceReportTable.focus()
    content=self.AttendanceReportTable.item(cursor_row)
    rows=content['values']
    self.var_atten_roll.set(rows[0])
    self.var_atten_name.set(rows[1])
    self.var_atten_dep.set(rows[2])
    self.var_atten_sem.set(rows[3])
    self.var_atten_time.set(rows[4])
    self.var_atten_date.set(rows[5])
    self.var_atten_attendance.set(rows[6])

  
  def reset_data(self):
    self.var_atten_roll.set("")
    self.var_atten_name.set("")
    self.var_atten_dep.set("")
    self.var_atten_sem.set("")
    self.var_atten_time.set("")
    self.var_atten_date.set("")
    self.var_atten_attendance.set("")








if __name__=="__main__":
  home=Tk() 
  obj=Attendance(home)
  home.mainloop()
