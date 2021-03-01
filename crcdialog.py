# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:18:06 2020

@author: Ejderya
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from crccoding import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()