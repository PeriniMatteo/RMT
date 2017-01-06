

import sys

import gui_magazzino
import gui_trasformati
import gui_venduti
import gui_report_magazzino
import gui_report_venduti

from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
#from PyQt5.QtGui import QFont 
from PyQt5.QtGui import *    
from PyQt5.QtCore import *   
#from PyQt5 import QtCore, QtGui

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        #self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn_magazzino = QPushButton('Magazzino', self)
        btn_magazzino.setToolTip('Click qui per gestire il magazzino')
        btn_magazzino.resize(btn_magazzino.sizeHint())
        btn_magazzino.clicked.connect(self.btn_magazzino_clicked)
        btn_magazzino.move(50, 50)       
        
        btn_trasformati = QPushButton('Trasformati', self)
        btn_trasformati.setToolTip('This is a QPushButton widget')
        btn_trasformati.resize(btn_trasformati.sizeHint())
        btn_trasformati.clicked.connect(self.btn_trasformati_clicked)
        btn_trasformati.move(200, 50)       
        
        btn_venduti = QPushButton('Venduti', self)
        btn_venduti.setToolTip('This is a QPushButton widget')
        btn_venduti.resize(btn_venduti.sizeHint())
        btn_venduti.clicked.connect(self.btn_venduti_clicked)
        btn_venduti.move(350, 50)       
        
        btn_report_magazzino = QPushButton('Report\nMagazzino', self)
        btn_report_magazzino.setToolTip('This is a QPushButton widget')
        btn_report_magazzino.resize(btn_report_magazzino.sizeHint())
        btn_report_magazzino.clicked.connect(self.btn_report_magazzino_clicked)
        btn_report_magazzino.move(50, 100)       
        
        btn_report_venduti = QPushButton('Report\nVenduti', self)
        btn_report_venduti.setToolTip('This is a QPushButton widget')
        btn_report_venduti.resize(btn_report_venduti.sizeHint())
        btn_report_venduti.clicked.connect(self.btn_report_venduti_clicked)
        btn_report_venduti.move(350, 100)       
        
        self.setGeometry(30, 30, 500, 200)
        self.setWindowTitle('Tooltips')    
        self.show()
        
    def btn_magazzino_clicked(self):
        #print("cc")
        self.gui_mag = gui_magazzino.GM()
        self.gui_mag.show()
    def btn_trasformati_clicked(self):
        #print("cc")
        self.gui_trasf = gui_trasformati.GT()
        self.gui_trasf.show()
    def btn_venduti_clicked(self):
        #print("cc")
        self.gui_vend = gui_venduti.GV()
        self.gui_vend.show()
    def btn_report_magazzino_clicked(self):
        #print("cc")
        self.gui_rm = gui_report_magazzino.RM()
        self.gui_rm.show()
    def btn_report_venduti_clicked(self):
        #print("cc")
        self.gui_rv = gui_report_venduti.RV()
        self.gui_rv.show()
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

