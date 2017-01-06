from PyQt5 import QtCore, QtGui,QtWidgets

class RV (QtWidgets.QMainWindow):
    def __init__(self):
        super(RV, self).__init__()
        
        self.resize(800,600)
        self.setWindowTitle("Report Venduti")
        #self.setStyleSheet("NewLibrary {border-image: url(wood.jpg);}")
        
        #File Menu
        #main_menu = self.menuBar()
        #file_menu = main_menu.addMenu("File")
        self.initialize()

    def initialize(self):
        centralwidget = QtWidgets.QWidget(self)
        self.mainLayout = QtWidgets.QVBoxLayout(centralwidget)
        self.mainLayout.setAlignment(QtCore.Qt.AlignCenter)
        
        #some useful buttons in the future
        self.setCentralWidget(centralwidget)
        self.show()
    
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Exit',
                                    "Close the application?",
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
