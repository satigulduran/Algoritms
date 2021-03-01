# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:50:53 2020

@author: Ejderya
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from hammingcoding import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()