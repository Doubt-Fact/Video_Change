# from sys import getdlopenflags
from fileinput import filename
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ffmpy
import calendar
import time


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 270)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        # 固定窗口大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height()); 
        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "音视频转换工具箱-v1.1"))
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 200, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("选择要转换的视频")
        self.pushButton.clicked.connect(self.openfile)

        self.labelA = QtWidgets.QLabel(MainWindow)
        self.labelA.setText('此工具可一键转换视频格式（复制\n音视频，在保持音视频质量基本不\n变的情况下改变音视频格式。注意，\n音视频分离功能仅支持音频aac编码\n的素材）')
        self.labelA.setGeometry(QtCore.QRect(240, 30, 250, 80))

        self.labelB = QtWidgets.QLabel(MainWindow)
        self.labelB.setText('Copyright 2022 Doubt-Fact All Rights Reserved')
        self.labelB.setOpenExternalLinks(True)
        self.labelB.setGeometry(QtCore.QRect(10, 200, 380, 80))
        
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(10, 80, 200, 30))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setText("选择要音视频分离的文件")
        self.pushButton2.clicked.connect(self.openfile2)

        self.labelC = QtWidgets.QLabel(MainWindow)
        self.labelC.setText('<a href="https://www.doubt-fact.top">''官网链接</a>')
        self.labelC.setOpenExternalLinks(True)
        self.labelC.setGeometry(QtCore.QRect(10, 180, 380, 80))

        self.labelD = QtWidgets.QLabel(MainWindow)
        self.labelD.setText('<a href="https://github.com/Doubt-Fact/Video_Change">''GitHub</a>')
        self.labelD.setOpenExternalLinks(True)
        self.labelD.setGeometry(QtCore.QRect(100, 180, 380, 80))

    def openfile(self):
        global dizhi
        ts1 = time.strftime('%H%M%S')
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    '', # 起始路径 
                                    "All Files (*.*)")
        dizhi = fileName_choose
        ff = ffmpy.FFmpeg(
            inputs={dizhi: None},
            # outputs={mingming+'.mp4': None}
            outputs={dizhi+ts1+'.mp4': '-c:v copy -c:a copy'}
            )
        ff.run() 

    def openfile2(self):
        ts1 = time.strftime('%H%M%S')
        global dizhi2
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    '', # 起始路径 
                                    "All Files (*.*)")
        dizhi2 = fileName_choose
        ff = ffmpy.FFmpeg(
            inputs={dizhi2: None},
            outputs={dizhi2+ts1+'.aac': '-c:a copy -vn',dizhi2+ts1+'.mp4':'-c:v copy -an'}
            )
        ff.run() 
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
