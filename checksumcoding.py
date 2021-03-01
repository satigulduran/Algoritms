# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:35:04 2020

@author: Ejderya
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from checksum import Ui_Dialog



class MainWindow(QWidget,Ui_Dialog):

    dataset_file_path = ""
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.checksum)
        """
        Checksum algoritmasında 4 adet hexadecimal data alınıp toplanıyor toplanma sonucu ortaya çıkan hexadecimal verinin elde biti varsa o tekrar çıkan sonuçla toplanır.
        En son çıkan sonuç 16 lık sisteme göre tümleyeni alınarak codewordü oluşturulur."""
        
        
    def checksum(self):#data girilip girilmediğini ve girilen datanın 4 bit olup olmadığını kontrol ediyor.Daha sonra verileri binnary toplayıp hexadecimale çevirerek fonksiyonlara yolluyor.
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        
        if(self.lineEdit.text()==""):
            self.label_3.setStyleSheet("QWidget{color: darkred}")
            self.label_3.setText("DATA GİRİNİZ")
        if(self.lineEdit_2.text()==""):
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("DATA GİRİNİZ")
        if(self.lineEdit_3.text()==""):
            self.label_5.setStyleSheet("QWidget{color: darkred}")
            self.label_5.setText("DATA GİRİNİZ")
        if(self.lineEdit_4.text()==""):
            self.label_6.setStyleSheet("QWidget{color: darkred}")
            self.label_6.setText("DATA GİRİNİZ")
        if(len(self.lineEdit.text())>4):
            self.label_3.setStyleSheet("QWidget{color: darkred}")
            self.label_3.setText(" 4 BİT DATA GİRİNİZ")
        if(len(self.lineEdit_2.text())>4):
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText(" 4 BİT DATA GİRİNİZ")
        if(len(self.lineEdit_3.text())>4):
            self.label_5.setStyleSheet("QWidget{color: darkred}")
            self.label_5.setText(" 4 BİT DATA GİRİNİZ")
        if(len(self.lineEdit_4.text())>4):
            self.label_6.setStyleSheet("QWidget{color: darkred}")
            self.label_6.setText("4 BİT DATA GİRİNİZ")
        else:
                
            self.label_7.setText("")
            veri1=self.lineEdit.text()
            binary1= self.hextobinary(veri1)
            #print(binary1)
            veri2=self.lineEdit_2.text()
            binary2=self.hextobinary(veri2)
            veri3=self.lineEdit_3.text()
            binary3=self.hextobinary(veri3)
            veri4 = self.lineEdit_4.text()
            binary4=self.hextobinary(veri4)
            integer_sum = int(binary1, 2) + int(binary2, 2) + int(binary3, 2) + int(binary4, 2)#binary toplama yapılıyor
            binary_sum = bin(integer_sum)
            #print(binary_sum)
            decimal_representation = int(binary_sum, 2)
            hexadecimal_string = hex(decimal_representation)#binary hexadecimale çevriliyor
            #print(hexadecimal_string)
            if(hexadecimal_string[2]=="1"):
                hexadecimal_string=hexadecimal_string[0:2]+hexadecimal_string[3:]
                son=self.hextobinary(hexadecimal_string)
                #print(son)
                son=int(son,2)+int("1",2)
                binarry_sum=bin(son)
                decimal_representation = int(binarry_sum, 2)
                hexadecimal_string = hex(decimal_representation)
                #print(binarry_sum)
                #print(hexadecimal_string)
                hexadecimal_string=self.tumleyenal(hexadecimal_string)
                #print(hexadecimal_string)
                self.lineEdit_5.setText(hexadecimal_string)
                self.label_7.setStyleSheet("QWidget{color: green}")
                self.label_7.setText("DATAWORD HESAPLANDI.")
       
        
        
    def hextobinary(self,deger): #hexadecimali binarye çevirme işlemi yapıyor
        ini_string =deger
        scale = 16
        
        res = bin(int(ini_string, scale)).zfill(8) 
        return(str(res))
        
    def tumleyenal(self,hexadecimal_strin):# 16 lık sisteme göre tumleyenini alır 
        yenistring=""
        uzunluk=len(hexadecimal_strin)-2
        hexadecimal_string=str(hexadecimal_strin[2:])
        hexadecimal_string=str(hexadecimal_string)
        print(hexadecimal_string)
        
        for i in range(0,uzunluk):
            if(hexadecimal_string[i]=="f" or hexadecimal_string[i]=="F" ):
                
                yenistring+="0"
            if(hexadecimal_string[i]=="e" or hexadecimal_string[i]=="E" ):
                
                yenistring+="1"
            if(hexadecimal_string[i]=="d" or hexadecimal_string[i]=="D" ):
                
                yenistring+="2"
            if(hexadecimal_string[i]=="c" or hexadecimal_string[i]=="C" ):
                
                yenistring+="3"
            if(hexadecimal_string[i]=="b" or hexadecimal_string[i]=="B" ):
                
                yenistring+="4"
            if(hexadecimal_string[i]=="a" or hexadecimal_string[i]=="A" ):
               
                yenistring+="5"

            if(hexadecimal_string[i]=="9"):
                
                yenistring+="6"
            if(hexadecimal_string[i]=="8" ):
                
                yenistring+="7"
            if(hexadecimal_string[i]=="7" ):
                
                yenistring+="8"
            if(hexadecimal_string[i]=="6" ):
                
                yenistring+="9"
            if(hexadecimal_string[i]=="5" ):
              
               yenistring+="A"
            if(hexadecimal_string[i]=="4" ):
               
                yenistring+="B"
            if(hexadecimal_string[i]=="3" ):
               
                yenistring+="C"
            if(hexadecimal_string[i]=="2" ):
                
                yenistring+="D"
            if(hexadecimal_string[i]=="1" ):
                yenistring+="E"
              
            if(hexadecimal_string[i]=="0" ):
                
                yenistring+="F"
        return yenistring
                
            
            
            
            
            
            
            
            