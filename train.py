from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import os
import numpy as np

class Train:
  def __init__(self,home):
    self.home=home
    self.home.geometry("1920x1080+0+0")#set width and height
    self.home.title("Face Recognization System")

    # title_lbl=Label(self.home,text="TRAIN  DATASET",font=("Pristina",50,"underline"),fg="white",bg="darkblue")
    # title_lbl.place(x=-300,y=0,width=1909,height=90)

    img_top=Image.open("images/train_4.png") 
    img_top=img_top.resize((1282,650),Image.ANTIALIAS) 
    self.photoimg_top=ImageTk.PhotoImage(img_top)

    f_lbl=Label(self.home,image=self.photoimg_top)
    f_lbl.place(x=-3,y=-2)
    
    # button
    b1_1=Button(self.home,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("georgia",30,"bold"),bg="darkblue",fg="white")
    b1_1.place(x=23,y=400,width=500,height=70)


  def train_classifier(self):
    data_dir=("data")
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    faces=[]
    ids=[]

    for image in path:
      img=Image.open(image).convert('L') # gray scale image
      imageNp=np.array(img,'uint8')
      id=int(os.path.split(image)[1].split('.')[1])

      faces.append(imageNp)
      ids.append(id)
      cv.imshow("Training",imageNp)
      cv.waitKey(1)==13
    ids=np.array(ids)

    # ====== train the classifier and save ===========
    clf=cv.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv.destroyAllWindows()
    messagebox.showinfo("Result","Training Datasets completed !!")





if __name__=="__main__":
  home=Tk() 
  obj=Train(home)
  home.mainloop()