from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from student_details import Student
from train import Train
from face_recognization import Face_Recognization
from attendance import Attendance
from develepor import Develepor



class Face_Recognization_System:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")

    
    # image 1
    img_1=Image.open("images/face_1.png") 
    img_1=img_1.resize((400,170),Image.ANTIALIAS) 
    self.photoimg_1=ImageTk.PhotoImage(img_1)

    f_lbl=Label(self.home,image=self.photoimg_1)
    f_lbl.place(x=0,y=0,width=400,height=170)

    # image 2
    img_2=Image.open("images/face.png") 
    img_2=img_2.resize((400,170),Image.ANTIALIAS) 
    self.photoimg_2=ImageTk.PhotoImage(img_2)

    f_lbl=Label(self.home,image=self.photoimg_2)
    f_lbl.place(x=400,y=0,width=400,height=170)
    
    
    # image 3
    img_3=Image.open("images/face_2.png") 
    img_3=img_3.resize((500,170),Image.ANTIALIAS) 
    self.photoimg_3=ImageTk.PhotoImage(img_3)

    f_lbl=Label(self.home,image=self.photoimg_3)
    f_lbl.place(x=800,y=0,width=500,height=170)


    # background image
    img=Image.open("images/background/background_22.jpg") 
    img=img.resize((1350,736),Image.ANTIALIAS) 
    self.photoimg=ImageTk.PhotoImage(img)

    bg_img=Label(self.home,image=self.photoimg)
    bg_img.place(x=0,y=170,width=1350,height=736)

    # title face recognization attendance system
    title_lbl=Label(bg_img,text="FACE  RECOGNIZATION  ATTENDANCE  SYSTEM",font=("times new roman",26,"bold"),bg="black",fg="white")
    title_lbl.place(x=-300,y=-5,width=1909,height=35)

    # student button
    img_4=Image.open("images/student_details.png") 
    img_4=img_4.resize((150,130),Image.ANTIALIAS) 
    self.photoimg_4=ImageTk.PhotoImage(img_4)

    b1=Button(bg_img,image=self.photoimg_4,command=self.student_details,cursor="hand2")
    b1.place(x=300,y=100,width=150,height=130)

    b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=300,y=230,width=150,height=20)

    # face detect
    img_5=Image.open("images/face_detect.png") 
    img_5=img_5.resize((150,100),Image.ANTIALIAS) 
    self.photoimg_5=ImageTk.PhotoImage(img_5)

    b1=Button(bg_img,image=self.photoimg_5,cursor="hand2",command=self.face_data)
    b1.place(x=600,y=100,width=150,height=130)

    b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=600,y=230,width=150,height=20)

    # Attendance
    img_6=Image.open("images/attendance_1.png") 
    img_6=img_6.resize((150,100),Image.ANTIALIAS) 
    self.photoimg_6=ImageTk.PhotoImage(img_6)

    b1=Button(bg_img,image=self.photoimg_6,cursor="hand2",command=self.attendance_data)
    b1.place(x=900,y=100,width=150,height=130)

    b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=900,y=230,width=150,height=20)


    # train face
    img_8=Image.open("images/train_1.png") 
    img_8=img_8.resize((150,130),Image.ANTIALIAS) 
    self.photoimg_8=ImageTk.PhotoImage(img_8)

    b1=Button(bg_img,image=self.photoimg_8,cursor="hand2",command=self.train_data)
    b1.place(x=300,y=300,width=150,height=130)

    b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=300,y=430,width=150,height=20)

    # photos
    img_9=Image.open("images/photos.png") 
    img_9=img_9.resize((150,100),Image.ANTIALIAS) 
    self.photoimg_9=ImageTk.PhotoImage(img_9)

    b1=Button(bg_img,image=self.photoimg_9,cursor="hand2",command=self.open_img)
    b1.place(x=600,y=300,width=150,height=130)

    b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=600,y=430,width=150,height=20)

    # develepor
    img_10=Image.open("images/develepor.png") 
    img_10=img_10.resize((150,100),Image.ANTIALIAS) 
    self.photoimg_10=ImageTk.PhotoImage(img_10)

    b1=Button(bg_img,image=self.photoimg_10,cursor="hand2",command=self.develepor_data)
    b1.place(x=900,y=300,width=150,height=130)

    b1_1=Button(bg_img,text="Develepor",cursor="hand2",command=self.develepor_data,font=("times new roman",10,"bold"),bg="black",fg="lightblue")
    b1_1.place(x=900,y=430,width=150,height=20)

    

  def open_img(self):
    os.startfile("data")


  # ================= functions buttons ===================
  def student_details(self):
    self.new_window=Toplevel(self.home)
    self.app=Student(self.new_window)

  
  def train_data(self):
    self.new_window=Toplevel(self.home)
    self.app=Train(self.new_window)

  
  def face_data(self):
    self.new_window=Toplevel(self.home)
    self.app=Face_Recognization(self.new_window)


  def attendance_data(self):
    self.new_window=Toplevel(self.home)
    self.app=Attendance(self.new_window)

  def develepor_data(self):
    self.new_window=Toplevel(self.home)
    self.app=Develepor(self.new_window)





if __name__=="__main__":
  home=Tk() 
  obj=Face_Recognization_System(home)
  home.mainloop()