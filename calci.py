# coding: utf-8
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

def calci_dimensions(window):
   
   window.setWindowTitle('Calculator')
   window.setGeometry(500,300,600,600)
   window.move(50,20)
   

def create_buttons(window):
      btn = QPushButton("Quit",window)
      btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
      btn.resize(100,100)
      btn.move(100,100)
      window.show()
   
	
def main():
   calci = QApplication(sys.argv)
   window = QWidget()
   calci_dimensions(window)
   create_buttons(window)
   window.show()
   sys.exit(calci.exec_())

if __name__ == '__main__':
   main()