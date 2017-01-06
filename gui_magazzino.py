from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
    
class GM (QtWidgets.QMainWindow):
    def __init__(self):
        super(GM, self).__init__()
        
        self.resize(800,600)
        self.setWindowTitle("Magazzino")
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.setStyleSheet("NewLibrary {border-image: url(wood.jpg);}")
        #self.windowModality(QtWidgets.ApplicationModal)
        #self.windowModality=QtCore.Qt.ApplicationModal
        #self.setwindowModality(QtCore.Qt.ApplicationModal)
        #File Menu
        #main_menu = self.menuBar()
        #file_menu = main_menu.addMenu("File")
        self.initialize()

    def initialize(self):
        #centralwidget = QtWidgets.QWidget(self)
        #self.mainLayout = QtWidgets.QVBoxLayout(centralwidget)
        #self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        #some useful buttons in the future
        #self.setCentralWidget(centralwidget)
        
        btn_inserisci_acquisto = QPushButton('Inserisci\nAcquisto', self)
        btn_inserisci_acquisto.setToolTip('This is a QPushButton widget')
        btn_inserisci_acquisto.resize(300,200)
        btn_inserisci_acquisto.clicked.connect(self.btn_inserisci_acquisto_clicked)
        btn_inserisci_acquisto.move(50, 200)       
        
        btn_modifica_costo = QPushButton('Modifica\nCosto', self)
        btn_modifica_costo.setToolTip('This is a QPushButton widget')
        btn_modifica_costo.resize(300,200)
        btn_modifica_costo.clicked.connect(self.btn_modifica_costo_clicked)
        btn_modifica_costo.move(450, 200)       
        self.show()
    
    def btn_inserisci_acquisto_clicked(self):
        print("cc")
        #self.gui_mag = gui_magazzino.GM()
        #self.gui_mag.show()
    def btn_modifica_costo_clicked(self):
        print("cc")
        #self.gui_trasf = gui_trasformati.GT()
        #self.gui_trasf.show()
    
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit',
                                    "Close the application?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
