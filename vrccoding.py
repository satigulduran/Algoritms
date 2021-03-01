# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:06:42 2020

@author: Ejderya
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from vrc import Ui_Dialog



class MainWindow(QWidget,Ui_Dialog):

    dataset_file_path = ""
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.vrc)
        """ vrc algortiması dikay olarak yazılan bitleri seçilen eşlik bitine göre yatay olarak bitleri sıralar"""
        
    def vrc(self):
         
         if self.radioButton_2.isChecked()== False | self.radioButton.isChecked()==False:
            self.label_2.setStyleSheet("QWidget{color: darkred}")
            self.label_2.setText("LÜTFEN  EŞLİK BİTİ SEÇİMİ YAPINIZ!..")
         
         if(self.radioButton_2.isChecked() == True): # çift eşlik biti seçildiyse yapılacaklar
             self.lineEdit_2.setText("")
             self.label_2.setText("")
             data=""
             data1=""
             data2=""
             data3=""
             veri=""
             datasayac=0
             uzunluk=0
             uzunluk1=0
             uzunluk2=0
             uzunluk3=0
             yaz=""
             self.label_2.setText("")
             
             data=self.plainTextEdit.toPlainText()
             uzunluk=len(data)
             sonuc=self.cifteslikbiti(data,uzunluk)
             yaz+=str(sonuc)
             
             
             data1=self.plainTextEdit_4.toPlainText()
             uzunluk1=len(data1)
             sonuc1=self.cifteslikbiti(data1,uzunluk1)
             yaz+=str(sonuc1)
             
             
             data2=self.plainTextEdit_3.toPlainText()
             uzunluk2=len(data2)
             sonuc2=self.cifteslikbiti(data2,uzunluk2)
             yaz+=str(sonuc2)
             
             
             data3=self.plainTextEdit_2.toPlainText()
             uzunluk3=len(data3)
             sonuc3=self.cifteslikbiti(data3,uzunluk3)
             yaz+=str(sonuc3)
             
             
             self.lineEdit_2.setText(yaz)
             self.label_2.setStyleSheet("QWidget{color: green}")
             self.label_2.setText(" ÇİFT EŞLİK BİTİ İÇİN SONUÇ BAŞARIYLA HESAPLANDI..")
        
         if(self.radioButton.isChecked() == True): #tek eşlik biti seçildiyse yapılacaklar
             self.lineEdit_2.setText("")
             self.label_2.setText("")
             tsonuc=""
             tdata=""
             tdata1=""
             tdata2=""
             tdata3=""
             tuzunluk=0
             tuzunluk1=0
             tuzunluk2=0
             tuzunluk3=0
             yazdir=""
             self.label_2.setText("")
             
             tdata=self.plainTextEdit.toPlainText()
             tuzunluk=len(tdata)
             tsonuc=self.tekeslikbiti(tdata,tuzunluk)
             yazdir+=str(tsonuc)
             
             
             tdata1=self.plainTextEdit_4.toPlainText()
             tuzunluk1=len(tdata1)
             tsonuc1=self.tekeslikbiti(tdata1,tuzunluk1)
             yazdir+=str(tsonuc1)
             
             
             tdata2=self.plainTextEdit_3.toPlainText()
             tuzunluk2=len(tdata2)
             tsonuc2=self.tekeslikbiti(tdata2,tuzunluk2)
             yazdir+=str(tsonuc2)
             
             
             tdata3=self.plainTextEdit_2.toPlainText()
             tuzunluk3=len(tdata3)
             tsonuc3=self.tekeslikbiti(tdata3,tuzunluk3)
             yazdir+=str(tsonuc3)
             
             
             self.lineEdit_2.setText(yazdir)
             self.label_2.setStyleSheet("QWidget{color: green}")
             self.label_2.setText(" TEK EŞLİK BİTİ İÇİN SONUÇ BAŞARIYLA HESAPLANDI..")
            
      
    def cifteslikbiti(self,veri,uznlk): # çift eşlik biti seçildiğinde bu fonksiyona yollanır ve içindeki birler sayılarak 1 ve 0 yazılacağına karar verilir.
        syc=0
        for i in range(0,uznlk):
                 if veri[i]=="1":
                     syc=syc+1
                 if veri[i]=="0":
                     syc=syc+0
                 else:
                     continue
        if(syc%2==0):
            syc=0
            return syc
        if(syc%2==1):
            syc=1
            return syc
    
    def tekeslikbiti(self,word,lenght):#tek eşlik biti seçildiğinde bu fonksiyon aynı seilde 1leri sayar ve ona göre 1 veya 0 eklemesi yapar
        say=0
        for i in range(0,lenght):
            if word[i]=="1":
                say=say+1
            if word[i]=="0":
                say=say+0
            else:
                continue
        if(say%2==1):
            say=0
            return say
        if(say%2==0):
            say=1
            return say
             
        
             
             
   
        
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
             