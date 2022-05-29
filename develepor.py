from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv

class Develepor:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")

     # background image
    img=Image.open("images/train_3.png") 
    img=img.resize((1300,650),Image.ANTIALIAS) 
    self.photoimg=ImageTk.PhotoImage(img)

    bg_img=Label(self.home,image=self.photoimg)
    bg_img.place(x=-4,y=0)

    # title develepor
    title_lbl=Label(bg_img,text="Project  Information",font=("Pristina",55,"underline"),fg="white",bg="black")
    title_lbl.place(x=350,y=55,width=660,height=90)

    main_frame=Frame(bg_img,bd=2,bg="black")
    main_frame.place(x=350,y=170,width=660,height=450)

    # develepor info
    info1=Label(main_frame,bg="black",text="Hello !!   My name is Harshita. ",font=("century",14),fg="white")
    info1.grid(row=0,column=0,padx=5,sticky=W)

    info2=Label(main_frame,bg="black",text="This is Face Recognition Project using which we have marked the",font=("century",14),fg="white")
    info2.grid(row=1,column=0,padx=5,sticky=W)

    info3=Label(main_frame,bg="black",text="attendance of students. ",font=("century",14),fg="white")
    info3.grid(row=2,column=0,padx=5,sticky=W)

    info4=Label(main_frame,bg="black",text="This project has been made using python via VS Code. I have used ",font=("century",14),fg="white")
    info4.grid(row=3,column=0,padx=5,sticky=W)

    info5=Label(main_frame,bg="black",text="OpenCV with Tkinter GUI and MySQL database. ",font=("century",14),fg="white")
    info5.grid(row=4,column=0,padx=5,sticky=W)

    info6=Label(main_frame,bg="black",text="Some libraries and algorithm used in this project are :- ",font=("century",14),fg="white")
    info6.grid(row=5,column=0,padx=5,sticky=W)

    info7=Label(main_frame,bg="black",text="1) Pilow library ",font=("century",14),fg="white")
    info7.grid(row=6,column=0,padx=5,sticky=W)

    info8=Label(main_frame,bg="black",text="2) Tkinter ",font=("century",14),fg="white")
    info8.grid(row=7,column=0,padx=5,sticky=W)

    info9=Label(main_frame,bg="black",text="3) OS ",font=("century",14),fg="white")
    info9.grid(row=8,column=0,padx=5,sticky=W)

    info10=Label(main_frame,bg="black",text="4) haarcascade classifier and LBPH face recognizer algorithm ",font=("century",14),fg="white")
    info10.grid(row=9,column=0,padx=5,sticky=W)

    info11=Label(main_frame,bg="black",text="=========================================",font=("century",14),fg="white")
    info11.grid(row=10,column=0,padx=5,sticky=W)

    info12=Label(main_frame,bg="black",text="Hope You Like This Project !!!",font=("century",14),fg="white")
    info12.grid(row=11,column=0,padx=0,sticky=W)

    info13=Label(main_frame,bg="black",text="THANK YOU !!",font=("century",14),fg="white")
    info13.grid(row=12,column=0,padx=5,sticky=W)

    

    
    
    




if __name__=="__main__":
  home=Tk() 
  obj=Develepor(home)
  home.mainloop()
