from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 as cv
import os
import numpy as np

class Face_Recognization:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")

    img_top=Image.open("images/recog_4.png") 
    img_top=img_top.resize((1282,650),Image.ANTIALIAS) 
    self.photoimg_top=ImageTk.PhotoImage(img_top)

    f_lbl=Label(self.home,image=self.photoimg_top)
    f_lbl.place(x=-3,y=-2)

    # button
    b1_1=Button(f_lbl,text="DETECT  FACE",command=self.face_recog,cursor="hand2",font=("georgia",35,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=98,y=489,width=480,height=90)


  # ======== attendance =========
  def mark_attendance(self,ro,n,d,s):
    with open("attendance.csv","r+",newline="\n") as f:
      myDataList=f.readlines()
      name_list=[]
      for line in myDataList:
        entry=line.split((","))
        name_list.append(entry[0])
      if ((ro not in name_list) and (n not in name_list) and (d not in name_list) and (s not in name_list)):
        now=datetime.now()
        d1=now.strftime("%d/%m/%Y")
        dtString=now.strftime("%H:%M:%S")
        f.writelines(f"\n{ro},{n},{d},{s},{dtString},{d1},Present")






  # ===== FACE RECOGNIZATION======
  def face_recog(self):
    def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
      gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
      features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

      coord=[]

      for(x,y,w,h) in features:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        id,predict=clf.predict(gray_image[y:y+h,x:x+w])
        confidence=int((100*(1-predict/300)))

        conn=mysql.connector.connect(host="localhost",username="root",password="harshita1234@",database="face_recognization")
        my_cursor=conn.cursor()

        my_cursor.execute("select name from student where roll="+str(id))
        n=my_cursor.fetchone()
        n="+".join(n)

        my_cursor.execute("select dep from student where roll="+str(id))
        d=my_cursor.fetchone()
        d="+".join(d)

        my_cursor.execute("select sem from student where roll="+str(id))
        s=my_cursor.fetchone()
        s="+".join(s)

        my_cursor.execute("select roll from student where roll="+str(id))
        ro=my_cursor.fetchone()
        ro="+".join(ro)




        if confidence>77:
          cv.putText(img,f"ROLL: {ro}",(x,y-105),cv.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
          cv.putText(img,f"Name: {n}",(x,y-75),cv.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
          cv.putText(img,f"Department: {d}",(x,y-50),cv.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
          cv.putText(img,f"Semester: {s}",(x,y-20),cv.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
          self.mark_attendance(ro, n, d, s)
        else:
          cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
          cv.putText(img,"Unknown Face",(x,y-35),cv.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        
        coord=[x,y,w,h]

      return coord
    
    def recognize(img,clf,faceCascade):
      coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
      return img
    
    faceCascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf=cv.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_cap=cv.VideoCapture(0)

    while True:
      ret,img=video_cap.read()
      img=recognize(img,clf,faceCascade)
      cv.imshow("Welcome to Face Recognization",img)

      if cv.waitKey(1)==13:
        break
    video_cap.release()
    cv.destroyAllWindows()



if __name__=="__main__":
  home=Tk() 
  obj=Face_Recognization(home)
  home.mainloop()