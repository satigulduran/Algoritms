# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:19:56 2020

@author: Ejderya
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from crcalgoritmasi import Ui_Dialog


class MainWindow(QWidget,Ui_Dialog):

    dataset_file_path = ""
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hesapla)
        """
        kullanıcıdan divisor değeri alınıyor 
        alttada data değeri alınıyor datanın ilk karakteri 1 ise divisorla 0 ise 0000 ile xor işlemi yapılıyor"
        """
        
        
    def hesapla(self):
        
        if(self.lineEdit.text()==""):
            self.label_5.setStyleSheet("QWidget{color: darkred}")
            self.label_5.setText("DIVISOR Bilgisini Giriniz.")
        if(self.lineEdit_2.text()==""):
            self.label_5.setStyleSheet("QWidget{color: darkred}")
            self.label_5.setText("DATAWORD Bilgisini Giriniz.")
        
        else:
            
            yenidata=""
            divisor = self.lineEdit.text()
            dataword = self.lineEdit_2.text()
            for i in range (0,3):
                yenidata=""
                if dataword[0] == "1":
                    for i in range(0,4):
                        if divisor[i]==dataword[i]:
                            yenidata+="0"
                        if divisor[i] != dataword[i]:
                            yenidata+="1"
                    yenidata+="0"            
               
              #  dataword=yenidata[1:]
                
                if(dataword[0]=="0"): 
                    yenidivisor="0000"
                    for i in range(0,4):
                        
                        if(yenidivisor[i]==dataword[i]):
                            
                            yenidata+="0"
                        if yenidivisor[i] != dataword[i]:
                                yenidata+="1"
                    yenidata+="0"
            
                dataword=yenidata[1:]
                print("dataword",dataword)
            olusancodeword=self.lineEdit_2.text()+dataword[1:]       
            self.lineEdit_7.setText(olusancodeword)
            self.label_9.setStyleSheet("QWidget{color:green}")
            self.label_9.setText("CODEWORD BAŞARIYLA OLUŞTURULDU")
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        