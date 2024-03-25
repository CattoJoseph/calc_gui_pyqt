from PyQt5 import QtCore, QtGui, QtWidgets,uic
import sys

class CalcUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''constructor method'''
        super(CalcUi, self).__init__()
        uic.loadUi("calc_window.ui", self)
        self.calcScreen.setAlignment(QtCore.Qt.AlignRight)
        self.show()
        self.current=""
        self.display =""
        self.addition.clicked.connect(lambda: self.opButton("+"))
        self.subtract.clicked.connect(lambda: self.opButton("-"))
        self.multiply.clicked.connect(lambda: self.opButton("*"))
        self.divide.clicked.connect(lambda: self.opButton("/"))
        self.decimal.clicked.connect(lambda: self.opButton("."))
        self.equals.clicked.connect(self.equalsMethod)
        
        self.clear.clicked.connect(lambda: self.clearMethod())

        self.zero.clicked.connect(lambda: self.numButton("0"))
        self.one.clicked.connect(lambda: self.numButton("1"))
        self.two.clicked.connect(lambda: self.numButton("2"))
        self.three.clicked.connect(lambda: self.numButton("3"))
        self.four.clicked.connect(lambda: self.numButton("4"))
        self.five.clicked.connect(lambda: self.numButton("5"))
        self.six.clicked.connect(lambda: self.numButton("6"))
        self.seven.clicked.connect(lambda: self.numButton("7"))
        self.eight.clicked.connect(lambda: self.numButton("8"))
        self.nine.clicked.connect(lambda: self.numButton("9"))
        

        #add button event listeners here


    def numButton(self, param):
        '''Handles number buttons'''
        self.current = self.current+str(param)
        self.calcScreen.setText(self.current)
        self.display = self.display + str(param)
        self.currentCalc.setText(self.display)
    
    def clearMethod(self):
        """resets the display"""
        self.current =""
        self.calcScreen.setText("0")
        self.display =""
        self.currentCalc.setText(self.display)

    def equalsMethod(self):
        '''handles the equals operation'''
        self.current = str(eval(self.display))
        self.calcScreen.setText(self.current)


    def opButton(self, op):
        """Handles operator buttons"""
        self.display = self.display+str(op) #this should only happen conditionally, 
        #only if anothe roperator hasn't been inputted already
        self.currentCalc.setText(self.display)
        self.current = ""



def mainApplication():
    app = QtWidgets.QApplication(sys.argv)
    window = CalcUi()
    app.exec_()
    app.quit() # quit when all windows are closed
    sys.exit(app.exec()) # execute the application event loop

mainApplication()