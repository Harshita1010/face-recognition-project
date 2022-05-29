# Face Recognition Project
 
## Requirements :

Mandatory 👉 Python version must be above or 3.8

## Algorithm Use:
Haarcascade Opencv (Object Detection)
LBPH Opencv (Face Recognition)

## Features of Project:
Real time face detection
- 1] Home Page
-- i) Student management system (Save, Take Photo Samples, Update, Delete, Clear) 
--ii) Train Photo Samples 
--iii) Take Attendance with Face Detection 
--iv) Attendance Report (Excel file & MySql database) 
--v) Developer Page


## Libraries to install :
- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` or `pip install opencv-contrib-python --user`
- `pip install Pillow`
- `pip install tkinter`
- `pip install numpy` 

## MySQL Workbench to install to store and create the table. All the students information has been stored using MySQL workbench and mysql connector
- `import mysql.connector`

## NOTE
The project has been created by using the above libraries and packages so it must be installed on the system to run it. The Roll to be given by the user it 
must be sequential i.e 1,2,3,4... and so on. The project will then successfully run on any system.

## STEPS
- `File-main.py` : 
It takes us to the home page of face recognition project using which we mark the attendance of students. It includes the Student details button, face detector, 
attendance , train data , photos and develepor buttons. These buttons lead us to different windows respectively.

- `File-student_details.py` :
It collects the student information by using which we add new data , update the existing data, delete a student's data and reset the data. It also takes the photo
sample which will further be used to train our model. There ara several button and labels created in this file to enter student information. `MySQL Connector`
is also added is this file to connect the data with sql and save the changes made in accordance with time.

- `File-train.py` :
In this file we will train our classifier to detect the face. We used haar cascade classifier to detect the object and LBPH algorithm to detect the image or face
Once the training of data is done it also generates the message "Training Datasets completed !!". Once dataset is trained we are ready to detect our face 
and mark attendance.

- `File-face_recognization.py` :
It finally detects our image and shows the details which we have given like Roll, Name, Department and Semester. In addition to this it also calculates the time 
and date at which the system recognize our face. This was made possible by importing `time` and `datetime` modules . It also used the haar cascade classifier 
and lbph algorithm to detect faces. 

- `File-attendance.py` :
This marks the attendance of the registered students. As soon as the face is being detected the information about the student and the attendance status is being
stored in a csv file or excel sheet. On opening this window we can import or export csv file. To perform these function `csv module` has been imported and
attendance of the students is marked successfully.

- `File-photos` :
This button on home page simply leads us to the training images. About 100 images were used to train the dataset.

- `File-Develepor.py` :
This was just created to give a brief idea about the project.


## REFERENCES
- `Code with Kiran (You Tube) Face Recognition playlist`
- `Sample Face Recognition Project Git Hub`
- `Face Detection and Recognition git hub project by Neha Yadav`
- `OpenCV tutorial by Freecodecamp on You Tube`
- `Traversy Media Face Recognition project tutorial` 
- `Krish Naik Face REcognition tutorials`




## =============== THANK YOU =================





`





 
