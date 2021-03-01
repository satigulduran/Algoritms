# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:06:42 2020

@author: Ejderya
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from vrccoding import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()