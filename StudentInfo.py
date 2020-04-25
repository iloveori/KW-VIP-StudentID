import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import qimage2ndarray
import numpy as np
import cv2

basic_ui = uic.loadUiType("StudentInfo.ui")[0]

class WindowClass(QMainWindow, basic_ui) :
    image = QImage()

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(lambda : self.ShowInfo(1))
        self.pushButton_2.clicked.connect(lambda : self.ShowInfo(2))
        self.pushButton_3.clicked.connect(lambda : self.ShowInfo(3))
        self.pushButton_4.clicked.connect(lambda : self.ShowInfo(4))
        self.pushButton_5.clicked.connect(lambda : self.ShowInfo(5))
        self.pushButton_6.clicked.connect(lambda : self.ShowInfo(6))
        self.pushButton_7.clicked.connect(lambda : self.ShowInfo(7))
        self.pushButton_8.clicked.connect(lambda : self.ShowInfo(8))
        self.pushButton_9.clicked.connect(lambda : self.ShowInfo(9))
        self.pushButton_10.clicked.connect(lambda : self.ShowInfo(10))

    def ShowInfo(self, num):
        studentid = ''

        if num == 1: #이로사
            studentid = ""

        elif num == 2: #권나성
            studentid = "미니언즈"

        elif num == 3: #김나현
            studentid = "고양이"

        elif num == 4: #서성원
            studentid = ""

        elif num == 5: #황승언
            studentid = ""

        elif num == 6: #이성호
            studentid = "밥잘챙"

        elif num == 7: #권동욱
            studentid = ""

        elif num == 8: #한정수
            studentid = ""

        elif num == 9: #손정현
            studentid = ""

        else :         #금빛나
            studentid = ""
            

        buttonReply = QMessageBox.information(
            self, "StudentInfo", studentid, 
            QMessageBox.Yes)
 
    
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')

        self.show()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()

