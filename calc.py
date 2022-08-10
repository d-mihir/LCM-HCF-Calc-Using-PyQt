# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcm_hcf.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 374)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.answer = QtWidgets.QPushButton(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(150, 250, 87, 33))
        self.answer.setObjectName("answer")
        # calls the function that calculates the answer and repopulates the textEdit with answer
        self.answer.clicked.connect(self.answering)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 291, 20))
        self.label.setObjectName("label")
        self.lcm = QtWidgets.QRadioButton(self.centralwidget)
        self.lcm.setGeometry(QtCore.QRect(170, 200, 104, 21))
        self.lcm.setChecked(True)
        self.lcm.setObjectName("lcm")
        self.hcf = QtWidgets.QRadioButton(self.centralwidget)
        self.hcf.setGeometry(QtCore.QRect(300, 200, 104, 21))
        self.hcf.setObjectName("hcf")
        self.input_text = QtWidgets.QTextEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(133, 90, 261, 87))
        self.input_text.setObjectName("input_text")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(280, 250, 87, 33))
        self.clear.setObjectName("clear")
        # clear the screen when clicked
        self.clear.clicked.connect(self.clear_screen)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.answer.connect(self.getInfo)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # clear the screen
    def clear_screen(self):
        self.input_text.setPlainText("")
    def answering(self):
        mytext = self.input_text.toPlainText()
        # if nothing is entered
        if(len(mytext)==0):
            return

        # if any string is entered
        try:
            numbers = list(map(int,mytext.split(',')))
        except:
            return


        # if only one number is entered
        if(len(numbers)==1):
            return
        numbers = sorted(numbers)
        
        # check if we are to calculate lcm or hcf
        if(self.lcm.isChecked()):
            self.cal_lcm(numbers)
        else:
            self.cal_hcf(numbers)
    
    # lcm subfunction
    def find_lcm(self,num1,num2):
        if(num1>num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num%den
        while(rem!=0):
            num=den
            den = rem
            rem = num%den
        gcd = den
        lcm = int(int(num1*num2)/int(gcd))
        return lcm

    def cal_lcm(self,numbers):
        num1 = numbers[0]
        num2 = numbers[1]
        lcm = self.find_lcm(num1,num2)
        
        for i in range(2,len(numbers)):
            lcm = self.find_lcm(lcm,numbers[i])
        
        self.input_text.setPlainText(str(f"LCM : {lcm}"))

    # hcf subfunction
    def find_hcf(self,num1,num2):
        while(num2):
            num1,num2 = num2,num1%num2
        return num1


    def cal_hcf(self,numbers):
        num1 = numbers[0]
        num2 = numbers[1]
        hcf = self.find_hcf(num1,num2)

        for i in range(2,len(numbers)):
            hcf = self.find_hcf(hcf,numbers[i])
        
        self.input_text.setPlainText(str(f"HCF : {hcf}"))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LCM & HCF Calculator"))
        self.answer.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Enter the numbers separated with commas"))
        self.lcm.setText(_translate("MainWindow", "LCM"))
        self.hcf.setText(_translate("MainWindow", "HCF"))
        self.clear.setText(_translate("MainWindow","Clear"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
