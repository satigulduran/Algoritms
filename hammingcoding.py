# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:50:53 2020

@author: Ejderya
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from hamming import Ui_Dialog



class MainWindow(QWidget,Ui_Dialog):

    dataset_file_path = ""
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hamming)
        """hamming kodlaması belirli kısımlarına girilen bitleri işlemlere alarak eşlik biti seçimine göre r1 de birici bitten başlayarak
        birer birer gider r2 de ikinci bitten başlayarak iki tane alır ve iki tane de boşluk bırakır
        r4 ise dördüncü bitten başlayarak dört tane alır ve 4 boşluk bırakır
        r8 ise sekizinci bitten başlayarak 8 tane alır eğer okadar biit yoksa olduğu kadarını alır 
        alınan bitlere göre eşlik biti istediğine göre 1 ler sayılır.""""
    def hamming(self):
        if len(self.lineEdit.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_20.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_19.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_22.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_23.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_21.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_25.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_26.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_24.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_28.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        if len(self.lineEdit_29.text())>1:
            self.label_4.setStyleSheet("QWidget{color: darkred}")
            self.label_4.setText("Her kutucuğa 1 bit veri yazınız")
        else:
            if self.radioButton.isChecked()== False and self.radioButton_2.isChecked()==False:
                self.label_4.setStyleSheet("QWidget{color: darkred}")
                self.label_4.setText("Eşlik Biti Seçimi Yapınız..")
                
            if self.radioButton.isChecked() == True: #tek eşlik biti
                self.label_4.setText("")
                sayac=0
                sayacr2=0
                sayacr4=0
                sayacr8=0
                
                veri=""
                veri2=""
                veri4=""
                veri8=""
                
                veri11=self.lineEdit.text()
                veri10=self.lineEdit_20.text()
                veri9=self.lineEdit_19.text()
                veri8=self.lineEdit_22.text()
                veri7=self.lineEdit_23.text()
                veri6=self.lineEdit_21.text()
                veri5=self.lineEdit_25.text()
                veri4=self.lineEdit_26.text()
                veri3=self.lineEdit_24.text()
                veri2=self.lineEdit_28.text()
                veri1=self.lineEdit_29.text()
                
                # r1 için işlem yap
             
                if veri1=="1":
                    sayac=sayac+1
                if veri1=="0":
                    sayac= sayac + 0
                if veri3=="1":
                    sayac=sayac+1
                if veri3=="0":
                    sayac= sayac + 0
                if veri5=="1":
                    sayac=sayac+1
                if veri5=="0":
                    sayac= sayac + 0
                if veri7=="1":
                    sayac=sayac+1
                if veri7=="0":
                    sayac= sayac + 0
                if veri9=="1":
                    sayac=sayac+1
                if veri9=="0":
                    sayac= sayac + 0
                if veri11=="1":
                    sayac = sayac +1 
                if veri11=="0":
                    sayac = sayac + 0
                
                if(sayac % 2 == 1 ):
                    veri="0"
                if( sayac % 2 == 0 ):
                    veri="1"
                
                self.lineEdit_2.setText(veri11)
                self.lineEdit_37.setText(veri10)
                self.lineEdit_31.setText(veri9)
                self.lineEdit_34.setText(veri8)
                self.lineEdit_30.setText(veri7)
                self.lineEdit_38.setText(veri6)
                self.lineEdit_35.setText(veri5)
                self.lineEdit_32.setText(veri4)
                self.lineEdit_27.setText(veri3)
                self.lineEdit_36.setText(veri2)
                self.lineEdit_33.setText(veri1)
                
                
                if(veri1==""):
                    self.lineEdit_33.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_33.setText(veri)
                if(veri3==""):
                   self.lineEdit_27.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_27.setText(veri)
                if(veri5==""):
                    self.lineEdit_35.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_35.setText(veri)
                if(veri7==""):
                    self.lineEdit_30.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_30.setText(veri)
                if(veri9==""):
                    self.lineEdit_31.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_31.setText(veri)
                if(veri11==""):
                    self.lineEdit_2.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_2.setText(veri)
                    
                #r2 için işlem yap
               
                veri11=self.lineEdit_2.text()
                veri10=self.lineEdit_37.text()
                veri9=self.lineEdit_31.text()
                veri8=self.lineEdit_34.text()
                veri7=self.lineEdit_30.text()
                veri6=self.lineEdit_38.text()
                veri5=self.lineEdit_35.text()
                veri4=self.lineEdit_32.text()
                veri3=self.lineEdit_27.text()
                veri2=self.lineEdit_36.text()
                veri1=self.lineEdit_33.text()      
                
                if(veri2=="1"):
                    sayacr2 +=1
                if veri3=="1":
                    sayacr2+=1
                if veri6=="1":
                    sayacr2+=1
                if veri7=="1":
                    sayacr2+=1
                if veri10=="1":
                    sayacr2+="1"
                if veri11=="1":
                    sayacr2+=1
                    
                if sayacr2 % 2 == 0:
                    veri2="1"
                if sayacr2 % 2 == 1:
                    veri2="0"
                
                
                self.lineEdit_3.setText(veri11)
                self.lineEdit_47.setText(veri10)
                self.lineEdit_41.setText(veri9)
                self.lineEdit_44.setText(veri8)
                self.lineEdit_40.setText(veri7)
                self.lineEdit_48.setText(veri6)
                self.lineEdit_45.setText(veri5)
                self.lineEdit_42.setText(veri4)
                self.lineEdit_39.setText(veri3)
                self.lineEdit_46.setText(veri2)
                self.lineEdit_43.setText(veri1)   
                
                if(veri2==""):
                    self.lineEdit_46.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_46.setText(veri2)
                if(veri3==""):
                   self.lineEdit_39.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_39.setText(veri2)
                if(veri6==""):
                    self.lineEdit_48.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_48.setText(veri2)
                if(veri7==""):
                    self.lineEdit_40.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_40.setText(veri2)
                if(veri10==""):
                    self.lineEdit_47.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_47.setText(veri2)
                if(veri11==""):
                    self.lineEdit_3.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_3.setText(veri2)
                
                
            
                
                #r4  için işlem yap
                veri11=self.lineEdit_3.text()
                veri10=self.lineEdit_47.text()
                veri9=self.lineEdit_41.text()
                veri8=self.lineEdit_44.text()
                veri7=self.lineEdit_40.text()
                veri6=self.lineEdit_48.text()
                veri5=self.lineEdit_45.text()
                veri4=self.lineEdit_42.text()
                veri3=self.lineEdit_39.text()
                veri2=self.lineEdit_46.text()
                veri1=self.lineEdit_43.text()
                
                if veri4 =="1":
                    sayacr4+=1
                if veri5 =="1":
                    sayacr4+=1
                if veri6 =="1":
                    sayacr4+=1
                if veri7 =="1":
                    sayacr4+=1
                    
                    
                if sayacr4 % 2 == 0:
                    veri3="1"
                if sayacr4 % 1 ==1:
                    veri3="0"
                    
                self.lineEdit_4.setText(veri11)
                self.lineEdit_57.setText(veri10)
                self.lineEdit_54.setText(veri9)
                self.lineEdit_50.setText(veri8)
                self.lineEdit_55.setText(veri7)
                self.lineEdit_51.setText(veri6)
                self.lineEdit_56.setText(veri5)
                self.lineEdit_49.setText(veri4)
                self.lineEdit_53.setText(veri3)
                self.lineEdit_52.setText(veri2)
                self.lineEdit_58.setText(veri1)   
                    
            
                if(veri4==""):
                    self.lineEdit_49.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_49.setText(veri3)
                if(veri5==""):
                   self.lineEdit_56.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_56.setText(veri3)
                if(veri6==""):
                    self.lineEdit_51.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_51.setText(veri3)
                if(veri7==""):
                    self.lineEdit_55.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_55.setText(veri3)
                    
                    #r8 için
                veri11=self.lineEdit_4.text()
                veri10=self.lineEdit_57.text()
                veri9=self.lineEdit_54.text()
                veri8=self.lineEdit_50.text()
                veri7=self.lineEdit_55.text()
                veri6=self.lineEdit_51.text()
                veri5=self.lineEdit_56.text()
                veri4=self.lineEdit_49.text()
                veri3=self.lineEdit_53.text()
                veri2=self.lineEdit_52.text()
                veri1=self.lineEdit_58.text()
                
                if veri8=="1":
                    sayacr8+=1
                
                if veri9 =="1":
                    sayacr8+=1
                if veri10 =="1":
                    sayacr8+=1
                if veri11 =="1":
                    sayacr8+=1
                    
                if (sayacr8 % 2 == 0):
                    verii="1"
                if (sayacr8 % 2 == 1):
                    verii="0"
                
                
                self.lineEdit_5.setText(veri11)
                self.lineEdit_67.setText(veri10)
                self.lineEdit_64.setText(veri9)
                self.lineEdit_60.setText(veri8)
                self.lineEdit_65.setText(veri7)
                self.lineEdit_61.setText(veri6)
                self.lineEdit_66.setText(veri5)
                self.lineEdit_59.setText(veri4)
                self.lineEdit_63.setText(veri3)
                self.lineEdit_62.setText(veri2)
                self.lineEdit_68.setText(veri1) 
                
                
                if(veri8==""):
                    self.lineEdit_60.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_60.setText(verii)
                if(veri9==""):
                   self.lineEdit_64.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_64.setText(verii)
                if(veri10==""):
                    self.lineEdit_67.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_67.setText(verii)
                if(veri11==""):
                    self.lineEdit_5.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_5.setText(verii)
        
        if self.radioButton_2.isChecked() == True: #çift eşlik biti
                self.label_4.setText("")
                sayac=0
                sayacr2=0
                sayacr4=0
                sayacr8=0
                
                veri=""
                veri2=""
                veri4=""
                veri8=""
                
                veri11=self.lineEdit.text()
                veri10=self.lineEdit_20.text()
                veri9=self.lineEdit_19.text()
                veri8=self.lineEdit_22.text()
                veri7=self.lineEdit_23.text()
                veri6=self.lineEdit_21.text()
                veri5=self.lineEdit_25.text()
                veri4=self.lineEdit_26.text()
                veri3=self.lineEdit_24.text()
                veri2=self.lineEdit_28.text()
                veri1=self.lineEdit_29.text()
                
                # r1 için işlem yap
             
                if veri1=="1":
                    sayac=sayac+1
                if veri1=="0":
                    sayac= sayac + 0
                if veri3=="1":
                    sayac=sayac+1
                if veri3=="0":
                    sayac= sayac + 0
                if veri5=="1":
                    sayac=sayac+1
                if veri5=="0":
                    sayac= sayac + 0
                if veri7=="1":
                    sayac=sayac+1
                if veri7=="0":
                    sayac= sayac + 0
                if veri9=="1":
                    sayac=sayac+1
                if veri9=="0":
                    sayac= sayac + 0
                if veri11=="1":
                    sayac = sayac +1 
                if veri11=="0":
                    sayac = sayac + 0
                
                if(sayac % 2 == 1 ):
                    veri="1"
                if( sayac % 2 == 0 ):
                    veri="0"
                
                self.lineEdit_2.setText(veri11)
                self.lineEdit_37.setText(veri10)
                self.lineEdit_31.setText(veri9)
                self.lineEdit_34.setText(veri8)
                self.lineEdit_30.setText(veri7)
                self.lineEdit_38.setText(veri6)
                self.lineEdit_35.setText(veri5)
                self.lineEdit_32.setText(veri4)
                self.lineEdit_27.setText(veri3)
                self.lineEdit_36.setText(veri2)
                self.lineEdit_33.setText(veri1)
                
                
                if(veri1==""):
                    self.lineEdit_33.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_33.setText(veri)
                if(veri3==""):
                   self.lineEdit_27.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_27.setText(veri)
                if(veri5==""):
                    self.lineEdit_35.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_35.setText(veri)
                if(veri7==""):
                    self.lineEdit_30.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_30.setText(veri)
                if(veri9==""):
                    self.lineEdit_31.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_31.setText(veri)
                if(veri11==""):
                    self.lineEdit_2.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_2.setText(veri)
                    
                #r2 için işlem yap
               
                veri11=self.lineEdit_2.text()
                veri10=self.lineEdit_37.text()
                veri9=self.lineEdit_31.text()
                veri8=self.lineEdit_34.text()
                veri7=self.lineEdit_30.text()
                veri6=self.lineEdit_38.text()
                veri5=self.lineEdit_35.text()
                veri4=self.lineEdit_32.text()
                veri3=self.lineEdit_27.text()
                veri2=self.lineEdit_36.text()
                veri1=self.lineEdit_33.text()      
                
                if(veri2=="1"):
                    sayacr2 +=1
                if veri3=="1":
                    sayacr2+=1
                if veri6=="1":
                    sayacr2+=1
                if veri7=="1":
                    sayacr2+=1
                if veri10=="1":
                    sayacr2+="1"
                if veri11=="1":
                    sayacr2+=1
                    
                if sayacr2 % 2 == 0:
                    veri2="0"
                if sayacr2 % 2 == 1:
                    veri2="1"
                
                
                self.lineEdit_3.setText(veri11)
                self.lineEdit_47.setText(veri10)
                self.lineEdit_41.setText(veri9)
                self.lineEdit_44.setText(veri8)
                self.lineEdit_40.setText(veri7)
                self.lineEdit_48.setText(veri6)
                self.lineEdit_45.setText(veri5)
                self.lineEdit_42.setText(veri4)
                self.lineEdit_39.setText(veri3)
                self.lineEdit_46.setText(veri2)
                self.lineEdit_43.setText(veri1)   
                
                if(veri2==""):
                    self.lineEdit_46.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_46.setText(veri2)
                if(veri3==""):
                   self.lineEdit_39.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_39.setText(veri2)
                if(veri6==""):
                    self.lineEdit_48.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_48.setText(veri2)
                if(veri7==""):
                    self.lineEdit_40.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_40.setText(veri2)
                if(veri10==""):
                    self.lineEdit_47.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_47.setText(veri2)
                if(veri11==""):
                    self.lineEdit_3.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_3.setText(veri2)
                
                verii3=""
                #r4  için işlem yap
                veri11=self.lineEdit_3.text()
                veri10=self.lineEdit_47.text()
                veri9=self.lineEdit_41.text()
                veri8=self.lineEdit_44.text()
                veri7=self.lineEdit_40.text()
                veri6=self.lineEdit_48.text()
                veri5=self.lineEdit_45.text()
                veri4=self.lineEdit_42.text()
                veri3=self.lineEdit_39.text()
                veri2=self.lineEdit_46.text()
                veri1=self.lineEdit_43.text()
                
                if veri4 =="1":
                    sayacr4+=1
                if veri5 =="1":
                    sayacr4+=1
                if veri6 =="1":
                    sayacr4+=1
                if veri7 =="1":
                    sayacr4+=1
                    
                    
                if sayacr4 % 2 == 0:
                    verii3="0"
                if sayacr4 % 1 ==1:
                    verii3="1"
                    
                self.lineEdit_4.setText(veri11)
                self.lineEdit_57.setText(veri10)
                self.lineEdit_54.setText(veri9)
                self.lineEdit_50.setText(veri8)
                self.lineEdit_55.setText(veri7)
                self.lineEdit_51.setText(veri6)
                self.lineEdit_56.setText(veri5)
                self.lineEdit_49.setText(veri4)
                self.lineEdit_53.setText(veri3)
                self.lineEdit_52.setText(veri2)
                self.lineEdit_58.setText(veri1)   
                  
            
                if(veri4==""):
                    self.lineEdit_49.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_49.setText(verii3)
                if(veri5==""):
                   self.lineEdit_56.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_56.setText(verii3)
                if(veri6==""):
                    self.lineEdit_51.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_51.setText(verii3)
                if(veri7==""):
                    self.lineEdit_55.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_55.setText(verii3)
                    
                    #r8 için
                veri11=self.lineEdit_4.text()
                veri10=self.lineEdit_57.text()
                veri9=self.lineEdit_54.text()
                veri8=self.lineEdit_50.text()
                veri7=self.lineEdit_55.text()
                veri6=self.lineEdit_51.text()
                veri5=self.lineEdit_56.text()
                veri4=self.lineEdit_49.text()
                veri3=self.lineEdit_53.text()
                veri2=self.lineEdit_52.text()
                veri1=self.lineEdit_58.text()
                
                if veri8=="1":
                    sayacr8+=1
                
                if veri9 =="1":
                    sayacr8+=1
                if veri10 =="1":
                    sayacr8+=1
                if veri11 =="1":
                    sayacr8+=1
                    
                if (sayacr8 % 2 == 0):
                    verii="0"
                if (sayacr8 % 2 == 1):
                    verii="1"
                
                
                self.lineEdit_5.setText(veri11)
                self.lineEdit_67.setText(veri10)
                self.lineEdit_64.setText(veri9)
                self.lineEdit_60.setText(veri8)
                self.lineEdit_65.setText(veri7)
                self.lineEdit_61.setText(veri6)
                self.lineEdit_66.setText(veri5)
                self.lineEdit_59.setText(veri4)
                self.lineEdit_63.setText(veri3)
                self.lineEdit_62.setText(veri2)
                self.lineEdit_68.setText(veri1) 
                
                
                if(veri8==""):
                    self.lineEdit_60.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_60.setText(verii)
                if(veri9==""):
                   self.lineEdit_64.setStyleSheet("QWidget{color: darkred}")
                   self.lineEdit_64.setText(verii)
                if(veri10==""):
                    self.lineEdit_67.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_67.setText(verii)
                if(veri11==""):
                    self.lineEdit_5.setStyleSheet("QWidget{color: darkred}")
                    self.lineEdit_5.setText(verii)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        