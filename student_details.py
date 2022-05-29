from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv

class Student:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")

    # variables
    self.var_dep=StringVar()
    self.var_course=StringVar()
    self.var_year=StringVar()
    self.var_sem=StringVar()
    self.var_roll=StringVar()
    self.var_name=StringVar()
    self.var_phone=StringVar()
    self.var_RegNo=StringVar()
    self.var_dob=StringVar()
    self.var_gender=StringVar()
    


    # background image
    img=Image.open("images/background/background_11.jpg") 
    img=img.resize((1909,700),Image.ANTIALIAS) 
    self.photoimg=ImageTk.PhotoImage(img)

    bg_img=Label(self.home,image=self.photoimg)
    bg_img.place(x=0,y=0)

    # title face recognization attendance system
    title_lbl=Label(bg_img,text="STUDENT  INFORMATION",font=("Pristina",50,"underline"),fg="white",bg="black")
    title_lbl.place(x=-300,y=3,width=1909,height=70)


    main_frame=Frame(bg_img,bd=2,bg="black")
    main_frame.place(x=130,y=90,width=1050,height=530)

    # left label frame
    Left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="white")
    Left_frame.place(x=10,y=10,width=520,height=500)
    
    img_left_1=Image.open("images/student_details/student_icon_1.jpg") 
    img_left_1=img_left_1.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_left_1=ImageTk.PhotoImage(img_left_1)

    f_lbl=Label(Left_frame,image=self.photoimg_left_1)
    f_lbl.place(x=0,y=0,width=260,height=100)

    img_left_2=Image.open("images/student_details/student_icon_2.jpg") 
    img_left_2=img_left_2.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_left_2=ImageTk.PhotoImage(img_left_2)

    f_lbl=Label(Left_frame,image=self.photoimg_left_2)
    f_lbl.place(x=260,y=0,width=260,height=100)


    # current course
    current_course_frame=LabelFrame(Left_frame,bd=2,bg="black",relief=RIDGE,text="CURRENT COURSE",font=("times new roman",12,"bold"),fg="white")
    current_course_frame.place(x=0,y=120,width=520,height=100)
    
    # department
    dep_label=Label(current_course_frame,bg="black",text="Department",font=("times new roman",12,"bold"),fg="white")
    dep_label.grid(row=0,column=0,padx=2,sticky=W)

    dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
    dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
    dep_combo.current(0)
    dep_combo.grid(row=0,column=1,padx=0,pady=5,sticky=W)

    # course
    course_label=Label(current_course_frame,bg="black",text="Courses",font=("times new roman",12,"bold"),fg="white")
    course_label.grid(row=0,column=2,padx=5,sticky=W)

    course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
    course_combo["values"]=("Select Course","DSA","DBMS","OS","PDC","AFL","COA")
    course_combo.current(0)
    course_combo.grid(row=0,column=3,padx=0,pady=5,sticky=W)

    # year
    year_label=Label(current_course_frame,bg="black",text="Year",font=("times new roman",12,"bold"),fg="white")
    year_label.grid(row=1,column=0,padx=5,sticky=W)

    year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
    year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
    year_combo.current(0)
    year_combo.grid(row=1,column=1,padx=0,pady=5,sticky=W)

    # semester
    semester_label=Label(current_course_frame,bg="black",text="Semester",font=("times new roman",12,"bold"),fg="white")
    semester_label.grid(row=1,column=2,padx=5,sticky=W)

    semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=17)
    semester_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
    semester_combo.current(0)
    semester_combo.grid(row=1,column=3,padx=0,pady=5,sticky=W)

    # Student Information
    student_info_frame=LabelFrame(Left_frame,bd=2,bg="black",relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"),fg="white")
    student_info_frame.place(x=0,y=240,width=520,height=237)

    # student Roll
    student_Roll_label=Label(student_info_frame,bg="black",text="Roll Number :",font=("times new roman",12,"bold"),fg="white")
    student_Roll_label.grid(row=0,column=0,padx=5,sticky=W)

    student_Roll_entry=ttk.Entry(student_info_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
    student_Roll_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    # student Name
    student_name_label=Label(student_info_frame,bg="black",text="Student Name :",font=("times new roman",12,"bold"),fg="white")
    student_name_label.grid(row=0,column=3,padx=5,sticky=W)

    student_name_entry=ttk.Entry(student_info_frame,textvariable=self.var_name,width=15,font=("times new roman",12,"bold"))
    student_name_entry.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    # student phone
    student_phone_label=Label(student_info_frame,bg="black",text="Phone Number :",font=("times new roman",12,"bold"),fg="white")
    student_phone_label.grid(row=1,column=0,padx=5,sticky=W)

    student_phone_entry=ttk.Entry(student_info_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
    student_phone_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    # student Reg no
    student_Reg_label=Label(student_info_frame,bg="black",text="Reg No :",font=("times new roman",12,"bold"),fg="white")
    student_Reg_label.grid(row=1,column=3,padx=5,sticky=W)

    student_Reg_entry=ttk.Entry(student_info_frame,textvariable=self.var_RegNo,width=15,font=("times new roman",12,"bold"))
    student_Reg_entry.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    # student dob
    student_dob_label=Label(student_info_frame,bg="black",text="DOB :",font=("times new roman",12,"bold"),fg="white")
    student_dob_label.grid(row=2,column=0,padx=5,sticky=W)

    student_dob_entry=ttk.Entry(student_info_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
    student_dob_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    # student gender
    student_gender_label=Label(student_info_frame,bg="black",text="Gender :",font=("times new roman",12,"bold"),fg="white")
    student_gender_label.grid(row=2,column=3,padx=5,sticky=W)

    # student_gender_entry=ttk.Entry(student_info_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"))
    # student_gender_entry.grid(row=2,column=4,padx=5,pady=5,sticky=W)

    gender_combo=ttk.Combobox(student_info_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=13)
    gender_combo["values"]=("Male","Female","others")
    gender_combo.current(0)
    gender_combo.grid(row=2,column=4,padx=5,pady=5,sticky=W)

    # radio buttons
    self.var_radio1=StringVar()
    radiobtn1=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="take photo sample",value="Yes",padding="normal")
    radiobtn1.grid(row=6,column=0)


    radiobtn2=ttk.Radiobutton(student_info_frame,variable=self.var_radio1,text="NO photo sample",value="No",padding="normal")
    radiobtn2.grid(row=6,column=3)

    # button frame
    btn_frame=Frame(student_info_frame,bd=2,bg="black",relief=RIDGE)
    btn_frame.place(x=0,y=130,width=520,height=79)

    save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
    save_btn.grid(row=0,column=0)

    update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",12,"bold"),bg="orange",fg="white")
    update_btn.grid(row=0,column=1)

    delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",12,"bold"),bg="red",fg="white")
    delete_btn.grid(row=0,column=2)

    reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
    reset_btn.grid(row=0,column=3)

    btn_frame1=Frame(student_info_frame,bd=2,relief=RIDGE,bg="black")
    btn_frame1.place(x=0,y=170,width=520,height=40)

    take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=27,font=("times new roman",12,"bold"),bg="pink",fg="white")
    take_photo_btn.grid(row=0,column=3)

    update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=28,font=("times new roman",12,"bold"),bg="purple",fg="white")
    update_photo_btn.grid(row=0,column=5)
    
    
    # right label frame
    Right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="white")
    Right_frame.place(x=540,y=10,width=500,height=500)

    img_right_1=Image.open("images/student_details/student_icon_5.jpg") 
    img_right_1=img_right_1.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_right_1=ImageTk.PhotoImage(img_right_1)

    f_lbl=Label(Right_frame,image=self.photoimg_right_1)
    f_lbl.place(x=0,y=0,width=260,height=100)

    img_right_2=Image.open("images/student_details/student_icon_9.jpg") 
    img_right_2=img_right_2.resize((260,100),Image.ANTIALIAS) 
    self.photoimg_right_2=ImageTk.PhotoImage(img_right_2)

    f_lbl=Label(Right_frame,image=self.photoimg_right_2)
    f_lbl.place(x=260,y=0,width=260,height=100)

    # search system===========
    search_frame=LabelFrame(Right_frame,bd=2,bg="black",relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"),fg="white")
    search_frame.place(x=-1,y=120,width=520,height=70)

    search_label=Label(search_frame,bg="black",text="Search By :",font=("times new roman",12,"bold"),fg="white")
    search_label.grid(row=0,column=0,padx=4,pady=5,sticky=W)

    search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=12)
    search_combo["values"]=("Select","Roll No","Phone No")
    search_combo.current(0)
    search_combo.grid(row=0,column=1,padx=0,pady=5,sticky=W)

    search_entry=ttk.Entry(search_frame,width=10,font=("times new roman",12,"bold"))
    search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
    
    
    search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",12,"bold"),bg="white",fg="black")
    search_btn.grid(row=0,column=3,padx=1.5)

    showAll_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",12,"bold"),bg="white",fg="black")
    showAll_btn.grid(row=0,column=4,padx=1.5)

    # ====== table frame ======
    table_frame=Frame(Right_frame,bd=2,bg="black",relief=RIDGE)
    table_frame.place(x=0,y=200,width=520,height=270)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","roll","name","phone","RegNo","dob","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.config(command=self.student_table.yview)


    self.student_table.heading("dep",text="Department")
    self.student_table.heading("course",text="Course")
    self.student_table.heading("year",text="Year")
    self.student_table.heading("sem",text="Semester")
    self.student_table.heading("roll",text="Roll No")
    self.student_table.heading("name",text="Name")
    self.student_table.heading("phone",text="Phone No")
    self.student_table.heading("RegNo",text="Registration No")
    self.student_table.heading("dob",text="Date Of Birth")
    self.student_table.heading("gender",text="Gender")
    self.student_table.heading("photo",text="Photo Status")
    self.student_table["show"]="headings"

    self.student_table.column("dep",width=130)
    self.student_table.column("course",width=100)
    self.student_table.column("year",width=100)
    self.student_table.column("sem",width=100)
    self.student_table.column("roll",width=100)
    self.student_table.column("name",width=130)
    self.student_table.column("phone",width=130)
    self.student_table.column("RegNo",width=130)
    self.student_table.column("dob",width=100)
    self.student_table.column("gender",width=100)
    self.student_table.column("photo",width=130)

    self.student_table.pack(fill=BOTH,expand=1)
    self.student_table.bind("<ButtonRelease>",self.get_cursor)
    self.fetch_data()

  # ==== function declare ====
  def add_data(self):
    if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
      messagebox.showerror("Error","All Field are required",parent=self.home)
    else:
      try:
        conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_RegNo.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_radio1.get()

                                                                                      ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("SUCCESS!!","Students details has been added successfully",parent=self.home)
      except Exception as es:
        messagebox.showerror("ERROR!!",f"Due To :{str(es)}",parent=self.home)

  
  # =========== fetch data ===========
  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from student")
    data=my_cursor.fetchall()

    if len(data)!=0:
      self.student_table.delete(*self.student_table.get_children())
      for i in data:
        self.student_table.insert("",END,values=i)
      conn.commit()
    conn.close()
  

  # ============= get cursor ===========
  def get_cursor(self,event=""):
    cursor_focus=self.student_table.focus()
    content=self.student_table.item(cursor_focus)
    data=content["values"]

    self.var_dep.set(data[0])
    self.var_course.set(data[1])
    self.var_year.set(data[2])
    self.var_sem.set(data[3])
    self.var_roll.set(data[4])
    self.var_name.set(data[5])
    self.var_phone.set(data[6])
    self.var_RegNo.set(data[7])
    self.var_dob.set(data[8])
    self.var_gender.set(data[9])
    self.var_radio1.set(data[10])

  # update function
  def update_data(self):
    if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
      messagebox.showerror("Error","All Field are required",parent=self.home)
    else:
      try:
        update=messagebox.askyesno("Update","Do you want to update",parent=self.home)
        if update>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
          my_cursor=conn.cursor()
          my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,phone=%s,RegNo=%s,dob=%s,gender=%s,photo=%s where roll=%s",(

                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_RegNo.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_radio1.get(),
                                                                                                                            self.var_roll.get()    


                                                                                                                          ))
        else:
          if not update:
            return
        messagebox.showinfo("Success","Student Details sucessfully updated",parent=self.home)
        conn.commit()
        self.fetch_data()
        conn.close()
      except Exception as es:
        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.home)

  # ====== delete ======
  def delete_data(self):
    if self.var_roll.get()=="":
      messagebox.showerror("Error","Student Roll Number is required",parent=self.home)
    else:
      try:
        delete=messagebox.askyesno("Student Delete Page","Do you want to delete this information",parent=self.home)
        if delete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
          my_cursor=conn.cursor()
          sql="delete from student where roll=%s"
          val=(self.var_roll.get(),)
          my_cursor.execute(sql,val)
        else:
          if not delete:
            return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root)
      except Exception as es:
        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.home)
  
  # ======== reset ========
  def reset_data(self):
    self.var_dep.set("Select Department")
    self.var_course.set("Select Course")
    self.var_year.set("Select Year")
    self.var_sem.set("Select Semester")
    self.var_roll.set("")
    self.var_name.set("")
    self.var_phone.set("")
    self.var_RegNo.set("")
    self.var_dob.set("")
    self.var_gender.set("Male")
    self.var_radio1.set("")


  # take photo sample or geneerate dataset
  def generate_dataset(self):
    if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_roll.get()=="":
      messagebox.showerror("Error","All Field are required",parent=self.home)
    else:
      try:
        conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        myresult=my_cursor.fetchall()
        id=0
        for x in myresult:
          id+=1
        my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,name=%s,phone=%s,RegNo=%s,dob=%s,gender=%s,photo=%s where roll=%s",(

                                                                                                                            self.var_dep.get(),
                                                                                                                            self.var_course.get(),
                                                                                                                            self.var_year.get(),
                                                                                                                            self.var_sem.get(),
                                                                                                                            self.var_name.get(),
                                                                                                                            self.var_phone.get(),
                                                                                                                            self.var_RegNo.get(),
                                                                                                                            self.var_dob.get(),
                                                                                                                            self.var_gender.get(),
                                                                                                                            self.var_radio1.get(),
                                                                                                                            self.var_roll.get()==id+1    


                                                                                                                          ))
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()     
        # ===== load pre defined data on face frontals from openCV =====
        face_classifier=cv.CascadeClassifier("haarcascade_frontalface_default.xml")                                                                                                             
        
        def face_cropped(img):
          gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
          faces=face_classifier.detectMultiScale(gray,1.3,5)
          # scaling factor=1.3
          # minimum neighbour=5

          for (x,y,w,h) in faces:
            face_cropped=img[y:y+h,x:x+w]
            return face_cropped

        cap=cv.VideoCapture(0)
        img_id=0
        while True:
          ret,my_frame=cap.read()
          if face_cropped(my_frame) is not None:
            img_id+=1
            face=cv.resize(face_cropped(my_frame),(450,450))
            face=cv.cvtColor(face, cv.COLOR_BGR2GRAY)
            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
            cv.imwrite(file_name_path,face)
            cv.putText(face, str(img_id),(50,50),cv.FONT_HERSHEY_COMPLEX, 2,(0,255,0),2)
            cv.imshow("Cropped Face", face)

          if cv.waitKey(1)==13 or int(img_id)==100:
            break
        cap.release()
        cv.destroyAllWindows()
        messagebox.showinfo("Result","Generating datasets completed !!!")
      except Exception as es:
        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.home)



if __name__=="__main__":
  home=Tk() 
  obj=Student(home)
  home.mainloop()

 
