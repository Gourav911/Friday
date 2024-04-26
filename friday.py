import tkinter as tk
import requests

def check_internet_connection():
  """Checks if the internet connection is available."""
  try:
    response = requests.get("https://www.google.com", timeout=5)
    return response.status_code == 200
  except requests.ConnectionError:
    return False

def main():
  """Checks the internet connection and prints a message accordingly."""
  is_connected = check_internet_connection()

  if not is_connected:
    # Create a tkinter window
    window = tk.Tk()
    window.geometry("500x500")
    window.resizable(False, False)
    icon = tk.PhotoImage(file="src/icon.png")
    window.iconphoto(True, icon)

    # Set the title of the window
    window.title("F.R.I.D.A.Y")
    
    window.config(bg="black")
    image = tk.PhotoImage(file="src/logo.png")
    label1=tk.Label(image=image)
    label1.config(bg='black')
    label1.pack(pady=50)
    
    # Create a label widget
    label = tk.Label(text="Please connect to the internet.", bg="black", fg="skyblue", font=("DejaVu Sans", 18))

    # Pack the label widget
    label.pack()

    # Start the mainloop of the tkinter window
    window.mainloop()
  else:
    # Add your other functions here

    
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QApplication, QWidget, QScrollBar, QPlainTextEdit
    from PyQt5.QtCore import QThread,QPropertyAnimation, QPoint
    from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

    from googletrans import Translator

    import pyttsx3
    import speech_recognition as sr
    import datetime
    from time import sleep
    import time
    import os
    import pathlib
    import subprocess
    import random
    import requests
    import webbrowser
    import wikipedia
    import pywhatkit
    import pyautogui
    import pyjokes



    class Ui_Form(object):
        def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.setWindowIcon(QtGui.QIcon('src/icon.png'))
            
            Form.setFixedSize(1380, 720)
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            Form.setFont(font)
            Form.setStyleSheet("background-color: rgb(0, 0, 0);")
            

            
            self.label = QtWidgets.QLabel(Form)
            self.label.setGeometry(QtCore.QRect(10, -80, 351, 300))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("src/logo.png"))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            
            
            self.label_4 = QtWidgets.QLabel(Form)
            self.label_4.setGeometry(QtCore.QRect(880, 250, 300, 200))
            self.label_4.setText("")
            self.label_4.setPixmap(QtGui.QPixmap("src/main.gif"))
            self.label_4.setScaledContents(True)
            self.label_4.setObjectName("label_4")

            self.status=QtWidgets.QPlainTextEdit(Form)
            self.status.setGeometry(QtCore.QRect(700,30,631,40))
            self.status.setReadOnly(True)
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.status.setFont(font)
            self.status.setStyleSheet("border:2px inset #4D61FF;\n"
    "color:whitesmoke;\n"
    "border-right:2px;\n"
    "border-top:2px;\n"                                         
    ##"border-radius:8px;\n"       
    "background-color: #0015FF30;\n"
    ##"QScrollBar:vertical{background-color:red;}"                                         

                                            )
            scr=self.status.verticalScrollBar()
            scr.setStyleSheet(    "width:0px\n"                          )
            self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
            self.plainTextEdit.setGeometry(QtCore.QRect(700, 70, 631, 500))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.plainTextEdit.setFont(font)
            self.plainTextEdit.setStyleSheet("border:2px solid #4D61FF;\n"
    "color:whitesmoke;\n"
    "border-right:2px;\n"
    "border-top:2px;\n"                                         
    ##"border-radius:8px;\n"       
    "background-color: #0015FF30;\n"
    ##"QScrollBar:vertical{background-color:red;}"                                         

                                            )
            scrollbar = self.plainTextEdit.verticalScrollBar()
            scrollbar.setStyleSheet("background-color: #0047ab;\n"
    "width:7px;"                                )
            self.plainTextEdit.setReadOnly(True)
            self.plainTextEdit.setCenterOnScroll(False)
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.lineEdit = QtWidgets.QLineEdit(Form)
            self.lineEdit.setGeometry(QtCore.QRect(700, 600, 500, 31))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(12)
            self.lineEdit.setFont(font)
            self.lineEdit.setStyleSheet("background-color: transparent;\n"
    "color: #DBCFFF;\n"
                                        
                                        
    "border:2px outset rgb(0, 85, 255);"
    "border-right:2px;\n"
    "border-top:2px;\n"                                    )
            self.lineEdit.setClearButtonEnabled(True)
            self.lineEdit.setObjectName("lineEdit")
            
            self.pushButton = QtWidgets.QPushButton(Form)
            self.pushButton.setGeometry(QtCore.QRect(1190, 600, 141, 31))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("color: rgb(0, 85, 255);\n"
    "background-color: transparent;\n"

    "border-color: rgb(0, 85, 255);\n"
    "border:2px outset rgb(0, 85, 255);"
    "border-left:2px;\n"                                      )
            self.pushButton.setObjectName("pushButton")
            
            self.pushButton_2 = QtWidgets.QPushButton(Form)
            self.pushButton_2.setGeometry(QtCore.QRect(20, 660, 151, 30))
            font = QtGui.QFont()
            font.setPointSize(16)
            self.pushButton_2.setFont(font)
            self.pushButton_2.setStyleSheet("color: rgb(0, 85, 255);\n"
    "background-color: transparent;\n"
    "border-color: rgb(0, 85, 255);\n"                                        
    "border:2px outset rgb(0, 85, 255);"                                        )
            self.pushButton_2.setObjectName("pushButton_2")

          

            self.label_8 = QtWidgets.QLabel(Form)
            self.label_8.setGeometry(QtCore.QRect(80, 150, 492, 492))
            self.label_8.setText("")
            self.label_8.setPixmap(QtGui.QPixmap("src/left_main.gif"))
            self.label_8.setScaledContents(True)
            self.label_8.setObjectName("label_8")

      

            self.label_9 = QtWidgets.QLabel(Form)
            self.label_9.setGeometry(QtCore.QRect(300, 670, 720, 50))
            self.label_9.setText("")
            self.label_9.setPixmap(QtGui.QPixmap("src/bot.gif"))
            self.label_9.setScaledContents(True)
            self.label_9.setObjectName("label_9")

            self.showabout = QtWidgets.QPushButton(Form)
            self.showabout.setGeometry(QtCore.QRect(20, 580, 150, 51))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.showabout.setFont(font)
            self.showabout.setStyleSheet("color: rgb(0, 85, 255);\n"
    "background-color: transparent;\n"

    "border-color: rgb(0, 85, 255);\n"
    "border:2px outset rgb(0, 85, 255);"
                                          )
            self.showabout.setObjectName("showabout")
            self.showabout.clicked.connect(self.showAbout)
            
            
            self.about = QtWidgets.QLabel(Form)
            self.about.setGeometry(QtCore.QRect(1900, 0,1380, 720))
            self.about.setText("")
            self.about.setPixmap(QtGui.QPixmap("src/body.jpg"))
            self.about.setScaledContents(True)
            self.about.setObjectName("about")

            

            self.about_logo = QtWidgets.QLabel(Form)
            self.about_logo.setGeometry(QtCore.QRect(1530, -30,300, 200))
            self.about_logo.setText("")
            self.about_logo.setPixmap(QtGui.QPixmap("src/logo.png"))
            self.about_logo.setScaledContents(True)
            self.about_logo.setObjectName("about_logo")
            self.about_logo.setStyleSheet('background-color:transparent;\n')


            self.about_desc = QtWidgets.QPushButton(Form)
            self.about_desc.setGeometry(QtCore.QRect(1950, 130, 500, 100))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(28)
            self.about_desc.setFont(font)
            self.about_desc.setStyleSheet("color: whitesmoke;\n"
    "background-color: transparent;\n"
    "font-style:italic ;\n "
                                          )
            self.about_desc.setObjectName("about_desc")
            self.about_card = QtWidgets.QLabel(Form)
            self.about_card.setGeometry(QtCore.QRect(1930, 250,500, 300))
            self.about_card.setText("")
            self.about_card.setPixmap(QtGui.QPixmap("src/body.jpg"))
            self.about_card.setScaledContents(True)
            self.about_card.setObjectName("about_card")
            self.about_card.setStyleSheet('background-color:transparent;\n'
    "border:3px outset rgb(0, 85, 255);\n"
                                          
                         )


            self.about_img=QtWidgets.QLabel(Form)
            self.about_img.setGeometry(QtCore.QRect(3910,170,130,130))
            self.about_img.setPixmap(QtGui.QPixmap("src/gg.jpeg"))
            self.about_img.setScaledContents(True)
            self.about_img.setObjectName("about_img")
            self.about_img.setStyleSheet("border-radius:80px;\n"
    "border:transparent ;\n"
    "background-color:transparent;\n"
                                         )

                            
            self.plainTextEdit1 = QtWidgets.QPlainTextEdit(Form)
            self.plainTextEdit1.setGeometry(QtCore.QRect(1950, 310, 450, 190))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(15)
            
            self.plainTextEdit1.setFont(font)
            self.plainTextEdit1.setStyleSheet("color:white;\n"
    "border:2px solid transparent;\n"
    "font-style:italic;\n"                                          
    "background-color:transparent;\n"
    "text-align:center;\n "                                                                                                                         
                                            )                     
            self.plainTextEdit1.setReadOnly(True)
            self.plainTextEdit1.setCenterOnScroll(False)
            self.plainTextEdit1.setObjectName("plainTextEdit1")
            string=' '*7
            self.plainTextEdit1.insertPlainText(f"\t {string}|{string}GOURAV\t|\n")
            self.plainTextEdit1.insertPlainText("\nPython Developer\n")
            self.plainTextEdit1.insertPlainText("\nRole in Project: Project design & GUI\n")
            self.plainTextEdit1.insertPlainText("\nE-mail: gouravmahindra313@gmail.com")

            self.about_card2 = QtWidgets.QLabel(Form)
            self.about_card2.setGeometry(QtCore.QRect(1730, 250,500, 300))
            self.about_card2.setText("")
            self.about_card2.setPixmap(QtGui.QPixmap("src/body.jpg"))
            self.about_card2.setScaledContents(True)
            self.about_card2.setObjectName("about_card2")
    ##        self.about_card.setText("gourav")
            self.about_card2.setStyleSheet('background-color:transparent;\n'
    "border:3px outset rgb(0, 85, 255);\n"
                         )

            self.about_img2=QtWidgets.QLabel(Form)
            self.about_img2.setGeometry(QtCore.QRect(1900,170,130,130))
            self.about_img2.setPixmap(QtGui.QPixmap("src/mani.jpeg"))
            self.about_img2.setScaledContents(True)
            self.about_img2.setObjectName("about_img2")
            self.about_img2.setStyleSheet("border-radius:80px;\n"
    "border:transparent ;\n"
    "background-color:transparent;\n"
                                         )

            self.plainTextEdit2 = QtWidgets.QPlainTextEdit(Form)
            self.plainTextEdit2.setGeometry(QtCore.QRect(1750, 310, 480, 190))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(15)
            
            self.plainTextEdit2.setFont(font)
            self.plainTextEdit2.setStyleSheet("color:white;\n"
    "font-style:italic;\n"                                           
    "border:2px solid transparent;\n"
    "background-color:transparent;\n"
    "text-align:center;\n "                                                                                                                         
                                            )                     
            self.plainTextEdit2.setReadOnly(True)
            self.plainTextEdit2.setCenterOnScroll(False)
            self.plainTextEdit2.setObjectName("plainTextEdit2")
            self.plainTextEdit2.insertPlainText("\t  |\tMANISHA\t|\n")
            self.plainTextEdit2.insertPlainText("\nPython Developer\n")
            self.plainTextEdit2.insertPlainText("\nRole in project: Scripting and Logic\n")            
            self.plainTextEdit2.insertPlainText("\nE-mail: sachdevamanisha1407@gmail.com")


            self.hidebtn=QtWidgets.QPushButton(Form)
            self.hidebtn.setGeometry(QtCore.QRect(1550, 630, 220, 51))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.hidebtn.setFont(font)
            self.hidebtn.setStyleSheet("color: rgb(0,87,255);\n"
    "background-color: transparent;\n"
    "font-weight:700;\n"                                   

    "border-color: cyan;\n"
    "border:5px outset rgb(0, 85, 255);"                                    )
            self.hidebtn.setObjectName("hidebtn")
            self.hidebtn.clicked.connect(self.hideAbout)
            


            self.label_gif = QtWidgets.QLabel(Form)
            self.label_gif.setGeometry(QtCore.QRect(0,0, 1380,720))
            self.label_gif.setText("")
            self.label_gif.setPixmap(QtGui.QPixmap(""))
            self.label_gif.setScaledContents(True)
            self.label_gif.setObjectName("label_gif")

            self.label_gif_movie=QtGui.QMovie("")
            self.label_gif.setMovie(self.label_gif_movie)
            self.label_gif_movie.start()

            self.label_gif1 = QtWidgets.QLabel(Form)
            self.label_gif1.setGeometry(QtCore.QRect(530,200, 300,300))
            self.label_gif1.setText("")
            self.label_gif1.setPixmap(QtGui.QPixmap("src/33.gif"))
            self.label_gif1.setScaledContents(True)
            self.label_gif1.setObjectName("label_gif1")

            self.label_gif1_movie=QtGui.QMovie("src/33.gif")
            self.label_gif1.setMovie(self.label_gif1_movie)
            self.label_gif1_movie.start()

            self.logo = QtWidgets.QLabel(Form)
            self.logo.setGeometry(QtCore.QRect(470, -50,400, 250))
            self.logo.setText("")
            self.logo.setPixmap(QtGui.QPixmap("src/logo.png"))
            self.logo.setScaledContents(True)
            self.logo.setObjectName("logo")
            self.logo.setStyleSheet('background-color:transparent;\n')


            
            

            self.pushButton3 = QtWidgets.QPushButton(Form)
            self.pushButton3.setGeometry(QtCore.QRect(550, 600, 241, 51))
            font = QtGui.QFont()
            font.setFamily("DejaVu Sans")
            font.setPointSize(16)
            self.pushButton3.setFont(font)
            self.pushButton3.setStyleSheet("color: cyan;\n"
    "background-color: transparent;\n"

    "border-color: cyan;\n"
    "border:2px inset rgb(0, 85, 255);"                                    )
            self.pushButton3.setObjectName("pushButton3")

            self.pushButton3.clicked.connect(self.hide_label)


            self.pushButton3.clicked.connect(self.hide_label)

            # Connect the animation finished signal to the slot
            

            
            
            
    ##        self.lineEdit.pushButton.clicked.connect(self.manualcodefromterminal)
            

            

            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)
            

        def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "F.R.I.D.A.Y"))
            self.plainTextEdit.setPlaceholderText(_translate("Form", "F.R.I.D.A.Y :"))
            self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Command..."))
            self.status.setPlaceholderText(_translate("Form", "F.R.I.D.A.Y status: SLEEPING......"))
            self.pushButton.setText(_translate("Form", "Submit"))
            self.pushButton_2.setText(_translate("Form", "EXIT"))
            self.showabout.setText(_translate("Form", "About"))
            self.pushButton3.setText(_translate("Form", "Start"))
            self.hidebtn.setText(_translate("Form", "X"))
            self.about_desc.setText(_translate("Form","DEVELOPERS"))
    ##        self.about_card.setPlaceholderText(_translate("Form","gourav"))
        def hide_label(self):
            self.anim = QPropertyAnimation(self.label_gif, b"pos")
            self.anim.setEndValue(QPoint(0, -1200))
            self.anim.setDuration(200)

            self.animlogo = QPropertyAnimation(self.logo, b"pos")
            self.animlogo.setEndValue(QPoint(0, -1200))
            self.animlogo.setDuration(200)

            self.animload = QPropertyAnimation(self.label_gif1, b"pos")
            self.animload.setEndValue(QPoint(-1900,0))
            self.animload.setDuration(500)
            self.animbtn = QPropertyAnimation(self.pushButton3, b"pos")
            self.animbtn.setEndValue(QPoint(550,800))
            self.animbtn.setDuration(1000)
            self.animbtn.start()
            self.anim.start()
            self.animload.start()
            self.animlogo.start()
            
        def hideAbout(self):
            self.anim = QPropertyAnimation(self.plainTextEdit1, b"pos")
            self.anim.setEndValue(QPoint(-1900, 0))
            self.anim.setDuration(700)

            self.anim1 = QPropertyAnimation(self.plainTextEdit2, b"pos")
            self.anim1.setEndValue(QPoint(0, -1200))
            self.anim1.setDuration(700)

            self.anim2 = QPropertyAnimation(self.about_card, b"pos")
            self.anim2.setEndValue(QPoint(-1900, 0))
            self.anim2.setDuration(700)

            self.anim3 = QPropertyAnimation(self.about_img, b"pos")
            self.anim3.setEndValue(QPoint(0, -1200))
            self.anim3.setDuration(700)

            self.anim4 = QPropertyAnimation(self.about_card2, b"pos")
            self.anim4.setEndValue(QPoint(-1900, 0))
            self.anim4.setDuration(700)

            self.anim5 = QPropertyAnimation(self.about_img2, b"pos")
            self.anim5.setEndValue(QPoint(0, -1200))
            self.anim5.setDuration(700)

            self.anim6 = QPropertyAnimation(self.hidebtn, b"pos")
            self.anim6.setEndValue(QPoint(-1900, 0))
            self.anim6.setDuration(700)

            self.anim7 = QPropertyAnimation(self.about, b"pos")
            self.anim7.setEndValue(QPoint(0, -1200))
            self.anim7.setDuration(700)

            self.anim8 = QPropertyAnimation(self.about_logo, b"pos")
            self.anim8.setEndValue(QPoint(-1900, 0))
            self.anim8.setDuration(700)

            self.anim9 = QPropertyAnimation(self.about_desc, b"pos")
            self.anim9.setEndValue(QPoint(0, -1200))
            self.anim9.setDuration(700)
            
            

            
            
            self.anim.start()
            self.anim1.start()
            self.anim2.start()
            self.anim3.start()
            self.anim4.start()
            self.anim5.start()
            self.anim6.start()
            self.anim7.start()
            self.anim8.start()
            self.anim9.start()
        def showAbout(self):

            
            self.anim = QPropertyAnimation(self.plainTextEdit1, b"pos")
            self.anim.setEndValue(QPoint(150, 310))
            self.anim.setDuration(1000)

            self.anim1 = QPropertyAnimation(self.plainTextEdit2, b"pos")
            self.anim1.setEndValue(QPoint(750, 310))
            self.anim1.setDuration(700)

            self.anim2 = QPropertyAnimation(self.about_card, b"pos")
            self.anim2.setEndValue(QPoint(130, 250))
            self.anim2.setDuration(1000)

            self.anim3 = QPropertyAnimation(self.about_img, b"pos")
            self.anim3.setEndValue(QPoint(310, 170))
            self.anim3.setDuration(700)

            self.anim4 = QPropertyAnimation(self.about_card2, b"pos")
            self.anim4.setEndValue(QPoint(730, 250))
            self.anim4.setDuration(1000)

            self.anim5 = QPropertyAnimation(self.about_img2, b"pos")
            self.anim5.setEndValue(QPoint(900, 170))
            self.anim5.setDuration(700)

            self.anim6 = QPropertyAnimation(self.hidebtn, b"pos")
            self.anim6.setEndValue(QPoint(550, 630))
            self.anim6.setDuration(1000)

            self.anim7 = QPropertyAnimation(self.about, b"pos")
            self.anim7.setEndValue(QPoint(0,0))
            self.anim7.setDuration(700)

            self.anim8 = QPropertyAnimation(self.about_logo, b"pos")
            self.anim8.setEndValue(QPoint(530, -30))
            self.anim8.setDuration(1000)

            self.anim9 = QPropertyAnimation(self.about_desc, b"pos")
            self.anim9.setEndValue(QPoint(450, 130))
            self.anim9.setDuration(700)
            
            
            self.anim.start()
            self.anim1.start()
            self.anim2.start()
            self.anim3.start()
            self.anim4.start()
            self.anim5.start()
            self.anim6.start()
            self.anim7.start()
            self.anim8.start()
            self.anim9.start()


    ##        self.label_gif.hide()
    ##        self.pushButton3.hide()
        def clear_terminal(self,text):
            self.plainTextEdit.clear(text)
        def status_print(self,text):
            self.status.insertPlainText(text)
        def terminal_print(self,text):
            self.plainTextEdit.insertPlainText(text)

        def manualcodefromterminal(self):
            cmd=self.lineEdit.text()
            if cmd:
                self.lineEdit.clear()
                self.terminal_self.fridayUi.terminal_print(f"you just typed : {cmd}")

           



    engine= pyttsx3.init()

    voices = engine.getProperty("voices")

    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate",150)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def wishings():
        hour = int(datetime.datetime.now().hour)
        if hour >=0 and hour <12:
            print("Good Morning")
            speak("Good Morning")
        elif hour >=12 and hour <17:
            print("Good afternoon")
            speak("Good afternoon")
        elif hour >=17 and hour <21:
            print("Good evening")
            speak("Good evening")
        else:
            print("goooood night")
            speak("gooooooood Night")

        

    def get_time():
        now = time.localtime()
        current_time = time.strftime("%H:%M:%S", now)
        return current_time


    def get_current_date():
        now = datetime.datetime.now()
        current_date = now.strftime("%d %B %Y")
        return current_date

    def Translatetoeng(text):
        line= str(text)
        translate=Translator()
        result=translate.translate(line)
        data = result.text
        Ui.terminalPrint(f"you said : {data}")
        return data
    def get_brightness_level_from_speech():
        recognizer = sr.Recognizer()
        with sr.Microphone() as microphone:
            recognizer.pause_threadshold=1
    ##        recognizer.adjust_for_ambient_noise(microphone)

            audio = recognizer.listen(microphone,0,5)

        try:
            speech_text = recognizer.recognize_google(audio)
            brightness_level = int(speech_text)
        except sr.UnknownValueError:
            speak("I didn't understand that.")
            return None
        except sr.RequestError:
            speak("There was an error with the speech recognizer.")
            return None

        if brightness_level < 0 or brightness_level > 100:
            speak("Brightness level must be between 0 and 100.")
            return None

        return brightness_level

    def change_brightness(brightness):
        command = ["powershell", "-Command", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + str(brightness) + ")"]
        subprocess.run(command)

    class FridayMain(QThread):
         def __init__(self):
            super(FridayMain,self).__init__()

            


         def run(self):
             self.runfriday()
         def commands(self):
            r= sr.Recognizer()
            with sr.Microphone() as source:
                Ui.statusPrint("F.R.I.D.A.Y Status: ACTIVE....")
                Ui.terminalPrint("listening....")
                r.pause_threadshold=1
    ##            r.adjust_for_ambient_noise(source,duration=3)
                audio=r.listen(source,0,5)
            try:
                Ui.terminalPrint("Recognizing...")
                query=r.recognize_google(audio,language='en-in')
    ##            Translatetoeng(query)
                Ui.terminalPrint(f"[USER] :-{query}\n")
            except Exception as e:
                print(e)
                
                query="none"
            if query is not None:
                query = query.lower()
                
                
            return  query
        


         def wakeup(self):
             r= sr.Recognizer()
             with sr.Microphone() as source:
    ##            Ui.statusPrint("hii")
                r.pause_threadshold=1
                audio=r.listen(source,0,5)
             try:
    ##            Ui.statusPrint("sdfs")
                query=r.recognize_google(audio,language='en-in')
                Ui.terminalPrint(f"<USER> :-{query}\n")
             except Exception as e:
                print(e)
                
                query="none"
             if query is not None:
                query = query.lower()
             return query

         def runfriday(self):

             while True:
                 query=self.wakeup()
                 if "wake up" in query or "wakeup" in query or "hey friday" in query or "hi friday" in query or "hello friday" in query:
                     wishings()
                     speak("hi, I am FRIDAY, what can i do for you !?")
                     while True:
                         query=self.commands()
                         if 'mute' in query or 'go to sleep' in query or 'soja' in query or 'so ja' in query:
                             speak("going to sleep...")
                             Ui.statusPrint("F.R.I.D.A.Y status: SLEEPING....")
                             break
                             
                         if 'how are you'in query or'how you doing' in query:
                             Ui.terminalPrint("I'm doing well, thanks for asking!")
                             speak("I'm doing well, thanks for asking!")
                         if "what's your name" in query or "tell me your name" in query or "who are you" in query or 'what is your name' in query:
                             Ui.terminalPrint("I am Friday, Your Assistant!")
                             speak("I am Friday, Your Assistant!")
                         if 'time' in query:
                            current_time = get_time()
                            Ui.terminalPrint(current_time)
                            speak(f"The time is {current_time}")
                         if 'date' in query:
                            current_date = get_current_date()
                            speak(current_date)
                         if 'task manager' in query:
                             speak("opening, Task Manager!")
                             os.system('taskmgr')
                         if 'settings' in query:
                             speak("opening, settings")
                             os.system("start ms-settings:")
                         if 'camera' in query:
                             speak("opening, Camera Application")
                             subprocess.run('start microsoft.windows.camera:', shell=True)
    ##                         os.system("start ms-windows-camera:")
                         if 'google chrome' in query or 'google' in query or 'chrome' in query:
                            speak("Opening Google chrome Application ...")
                            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                            while True:
                                chromequery=self.commands()
                                if "search" in chromequery:
                                    chromequery=chromequery.replace("search",'')
                                    pyautogui.write(chromequery)
                                    pyautogui.press('enter')
                                    speak('searching')
                                if 'close chrome' in chromequery or 'exit chrome' in chromequery:
                                    pyautogui.hotkey('alt','f4')
                                    speak('closing, google chrome application!')                                  
                                    break
                         if 'open edge'  in query or 'edge' in query or 'microsoft edge' in query or 'Open Microsoft Edge' in query or 'Microsoft Edge'in query:
                            speak("Opening Micro Soft Edge Application ...")
                            os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                            while True:
                                edgequery=self.commands()
                                if "search" in edgequery:
                                    edgequery=edgequery.replace("search",'')
                                    pyautogui.write(edgequery)
                                    pyautogui.press('enter')
                                    speak('searching')
                                if 'close edge' in edgequery or 'exit edge' in edgequery or 'close Microsoft Edge' in edgequery or 'exit Microsoft Edge' in edgequery:
                                    pyautogui.hotkey('alt','f4')
                                    speak('closing, Microsoft Edge application!')
                                    break
                         if 'brightness' in query or 'set brigtness' in query:
                             speak("speak the level of brightness in digits, between 0 to 100")
                             brightness_level = get_brightness_level_from_speech()
                             if brightness_level is not None:
                                 change_brightness(brightness_level)
                          

                                 
                         if 'why your name is friday' in query or 'why is your name friday' in query or 'what is the inspiration behind your name friday' in query :
                            speak("The name,'FRIDAY' is inspired by the role of the first AI Virtual assistant of Tony Stark in iron man movie.")
                            Ui.terminalPrint("The name,'FRIDAY' is inspired by the role of the first AI Virtual assistant of Tony Stark in iron man movie.")
                         if 'vs code'  in query or 'visual studio code' in query:
                            speak("Opening Visual Studio Code ...")
                            os.startfile("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                         if 'open notepad' in query or 'notepad' in query or 'Open Notepad' in query:
                            speak("Opening Notepad ...")
                            subprocess.Popen("notepad.exe")
                         if 'close notepad' in query  or 'exit notepad' in query:
                            speak("closing notepad")
                            pyautogui.hotkey('ctrl','w')
                         if 'play song' in query or 'play music' in query:
                            speak('Playing song you might like')
                            path = pathlib.Path("songs")
                            d = random.choice(os.listdir(path))
                            os.startfile(os.path.join("songs",d))
                            Ui.statusPrint("F.R.I.D.A.Y status: SLEEPING....")
                            break
                         if 'play' in query:
                           query=query.replace('play','')
                           pywhatkit.playonyt(query)
                           Ui.statusPrint("F.R.I.D.A.Y status: SLEEPING....")
                           break
                            
                         if 'wikipedia' in query:
                            try:
                                speak('Searching Wikipedia...')
                                query = query.replace("wikipedia", "")
                                results = wikipedia.summary(query, sentences=2)
                                speak("According to Wikipedia")
                                Ui.terminalPrint(results)
                                speak(results)
                            except:
                                speak('no results found')
                                Ui.terminalPrint('no results found')
                         if 'i want to know about ' in query or 'want to know about' in query or 'to know about' in query:
                            try:
                                speak('Searching Wikipedia...')
                                query = query.replace("wikipedia", "")
                                results = wikipedia.summary(query, sentences=2)
                                speak("According to Wikipedia")
                                Ui.terminalPrint(results)
                                speak(results)
                            except:
                                speak('no results found')
                                Ui.terminalPrint('no results found')

                            

                         if 'who is' in query:
                            try:
                                speak('Searching Wikipedia...')
                                query = query.replace("wikipedia", "")
                                results = wikipedia.summary(query, sentences=2)
                                speak("According to Wikipedia")
                                Ui.terminalPrint(results)
                                speak(results)
                            except:
                                speak('no results found')
                                Ui.terminalPrint('no results found')
                         if 'open youtube' in query or "open YouTube" in query or 'open you tube' in query or 'open You Tube' in query:
                            speak("opening, youtube..")
                            webbrowser.open('youtube.com')
                            while True:
                                ytquery=self.commands()
                                if 'close youtube' in ytquery or 'exit youtube' in ytquery:
                                    pyautogui.hotkey('alt','f4')
                                    speak('closing, YouTube!')
                                    
                                    break
                                
                         if 'stackoverflow' in query or 'stack overflow' in query or 'stack over flow' in query:
                            speak("opening, stackoverflow..")
                            webbrowser.open('stackoverflow.com')
                         if 'instagram' in query:
                             speak('opening, instagram')
                             webbrowser.open('instagram.com')
                         if 'facebook' in query:
                             speak('opening, facebook')
                             webbrowser.open('facebook.com')
                         if 'gmail' in query:
                             speak('opening, gmail')
                             webbrowser.open('mail.google.com')

                         if 'geeksforgeeks' in query or 'geeks for geeks' in query:
                            speak('opening,geeksforgeeks..')
                            webbrowser.open('geeksforgeeks.com')
                         if 'type' in query or 'start typing' in query or 'write' in query or 'make a note' in query:
                            speak('What should i write..?')
                            subprocess.Popen("notepad.exe")
                            while True:
                                writeInNotepad=self.commands()
                                if writeInNotepad=='exit typing':
                                    speak("done sir!")
                                    break
                                else:
                                    pyautogui.write(writeInNotepad)
  
                         if 'introduce' in query or 'yourself' in query or 'your self' in query :
                             Ui.terminalPrint('i am, FRIDAY, a desktop virtual assistant, i am designed to assist you with varius tasks, information and more. I am still under development, but My developers are constantly working to make me more efficient and helpful. In the future, I will be able to do even more things, so stay tuned!"')
                             speak('i am, FRIDAY, a desktop virtual assistant, i am designed to assist you with varius tasks, information and more. I am still under development, but My developers are constantly working to make me more efficient and helpful. In the future, I will be able to do even more things, so stay tuned!"')
                             
                         if 'your developers' in query or 'who created you' in query or 'who designed you' in query or 'who built you' in query or 'developers' in query or 'developer' in query:
                             speak("i was created by mr. Gourav Mahindra and Miss Manisha Sachdevaa ")
                             Ui.terminalPrint("i was created by mr. Gourav Mahindra and Miss Manisha Sachdeva ")
                             Ui.terminalPrint("They are software engineer with experience in Python and other programming languages. They are skilled and dedicated to creating an assistant that is helpful and informative.")
                             speak("They are software engineer with experience in Python and other programming languages. They are skilled and dedicated to creating an assistant that is helpful and informative.")
                             
                         if 'joke' in query or 'tell me a joke' in query:
                            joke=pyjokes.get_joke()
                            Ui.terminalPrint(joke)
                            speak(joke)
                         if 'shut down' in query or 'shutdown' in query:
                             speak("shutting down,system")
                             os.system("shutdown /s /t 0")
                         if 'bye' in query or 'by' in query or 'see you later' in query or 'catch you later' in query:
                            lines=['good bye..','catch you later','see you later','bye']
                            select_line=random.choice(lines)
                            speak(select_line)
                            pyautogui.hotkey('alt','f4')
                            pyautogui.press('enter')
                            quit()



    startExecution=FridayMain()      
       

    class guiofFriday(QWidget):
        def __init__(self):
            super(guiofFriday,self).__init__()
            

      

            self.fridayUi=Ui_Form()
    ##        self.startExecution=FridayMain()
            self.fridayUi.setupUi(self)
            self.fridayUi.pushButton_2.clicked.connect(self.close)
            self.fridayUi.pushButton.clicked.connect(self.manualcodefromterminal)
            self.runAllMovies()
        

           
        def manualcodefromterminal(self):
            cmd=self.fridayUi.lineEdit.text()
            if cmd:
                self.fridayUi.lineEdit.clear()
                self.fridayUi.terminal_print(f"User Said:{cmd}\n")

                if cmd == "exit" or cmd=='by' or cmd=='bye' or cmd=='see yaa' or cmd=='see you' or cmd=='good bye' or cmd=='good by' :
                    lines=['good bye..','catch you later','see you later','bye']
                    select_line=random.choice(lines)
                    speak(select_line)
                    self.close()
                    pyautogui.hotkey('alt','f4')
                    pyautogui.press('enter')
                if cmd=="time" or cmd=="what's the time" or cmd =="tell me the time" or cmd=="what is the time" or cmd=="tell me the current time":
                    current_time = get_time()
                    Ui.terminalPrint(current_time)
                    speak(f"The time is {current_time}")
                if cmd=="date" or cmd=="what's the date" or cmd =="tell me the date" or cmd=="what is the date" or cmd=="tell me the current date" :
                    current_date = get_current_date()
                    speak(current_date)
                if cmd =='google chrome'  or cmd == 'google' or cmd =='chrome' :
                    speak("Opening Google chrome Application ...")
                    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                if cmd =='open edge'   or cmd == 'edge'  or cmd =='microsoft edge' :
                    speak("Opening Micro Soft Edge Application ...")
                    os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                if cmd =='vs code'   or cmd =='visual studio code' :
                    speak("Opening Visual Studio Code ...")
                    os.startfile("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                if  cmd=='open notepad' :
                    speak("Opening Notepad ...")
                    subprocess.Popen("notepad.exe")
                if cmd=='open youtube' or 'youtube' in cmd:
                    speak("opening, youtube..")
                    webbrowser.open('youtube.com')
                if cmd =='introduce'  or cmd =='yourself' or cmd == 'your self' :
                    Ui.terminalPrint('i am, FRIDAY, a desktop virtual assistant, i am designed to assist you with varius tasks, information and more. I am still under development, but My developers are constantly working to make me more efficient and helpful. In the future, I will be able to do even more things, so stay tuned!"')
                    speak('i am, FRIDAY, a desktop virtual assistant, i am designed to assist you with varius tasks, information and more. I am still under development, but My developers are constantly working to make me more efficient and helpful. In the future, I will be able to do even more things, so stay tuned!"')
                if 'why your name is friday' in cmd or 'why is your name friday' in cmd or 'what is the inspiration behind your name friday' in cmd :
                    speak("The name,'FRIDAY' is inspired by the role of the first AI Virtual assistant of Tony Stark in iron man movie.")
                    Ui.terminalPrint("The name,'FRIDAY' is inspired by the role of the first AI Virtual assistant of Tony Stark in iron man movie.")      
                 
                    
                



                    
        
        def runAllMovies(self):

            
            
            
            self.fridayUi.label4_movie=QtGui.QMovie("src/main.gif")
            self.fridayUi.label_4.setMovie(self.fridayUi.label4_movie)
            self.fridayUi.label4_movie.start()

            self.fridayUi.label8_movie=QtGui.QMovie("src/left_main.gif")
            self.fridayUi.label_8.setMovie(self.fridayUi.label8_movie)
            self.fridayUi.label8_movie.start()

                
            self.fridayUi.label9_movie=QtGui.QMovie("src/end.gif")
            self.fridayUi.label_9.setMovie(self.fridayUi.label9_movie)
            self.fridayUi.label9_movie.start()

            startExecution.start()

        def terminalPrint(self,text):
            self.fridayUi.plainTextEdit.insertPlainText(text+"\n")
        def statusPrint(self,text):
            self.fridayUi.status.clear()
            self.fridayUi.status.insertPlainText(text+"\n")
        def clear_terminal(self):
            self.plainTextEdit.clear()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
##    Form.show()
    Ui=guiofFriday()
    Ui.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
