# Sample GUI Version : 1

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 97, 68, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.keithleyVolt = QtGui.QLineEdit(self.centralwidget)
        self.keithleyVolt.setGeometry(QtCore.QRect(110, 90, 91, 27))
        self.keithleyVolt.setObjectName(_fromUtf8("keithleyVolt"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 97, 68, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 97, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.timePeriod = QtGui.QLineEdit(self.centralwidget)
        self.timePeriod.setGeometry(QtCore.QRect(510, 90, 81, 27))
        self.timePeriod.setObjectName(_fromUtf8("timePeriod"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 90, 68, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 147, 68, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.arduinoVolt = QtGui.QLineEdit(self.centralwidget)
        self.arduinoVolt.setGeometry(QtCore.QRect(510, 140, 81, 27))
        self.arduinoVolt.setObjectName(_fromUtf8("arduinoVolt"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(600, 146, 68, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(277, 210, 191, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.totalTime = QtGui.QLineEdit(self.centralwidget)
        self.totalTime.setGeometry(QtCore.QRect(310, 240, 91, 27))
        self.totalTime.setObjectName(_fromUtf8("totalTime"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 246, 68, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.readings = QtGui.QPushButton(self.centralwidget)
        self.readings.setGeometry(QtCore.QRect(158, 300, 121, 27))
        self.readings.setObjectName(_fromUtf8("readings"))
        self.graph = QtGui.QPushButton(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(500, 300, 99, 27))
        self.graph.setObjectName(_fromUtf8("graph"))
        self.readingsTable = QtGui.QTableWidget(self.centralwidget)
        self.readingsTable.setGeometry(QtCore.QRect(100, 360, 571, 192))
        self.readingsTable.setRowCount(10)
        self.readingsTable.setObjectName(_fromUtf8("readingsTable"))
        self.readingsTable.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.readingsTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.readingsTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.readingsTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.readingsTable.setHorizontalHeaderItem(3, item)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 50, 81, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(497, 50, 91, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lightConditions = QtGui.QRadioButton(self.centralwidget)
        self.lightConditions.setGeometry(QtCore.QRect(580, 20, 201, 22))
        self.lightConditions.setObjectName(_fromUtf8("lightConditions"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(330, 290, 99, 61))
        self.start.setObjectName(_fromUtf8("start"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "SOURCERER", None))
        self.label_2.setText(_translate("MainWindow", "Voltage", None))
        self.label_3.setText(_translate("MainWindow", "(Volt)", None))
        self.label_4.setText(_translate("MainWindow", "Time Period", None))
        self.label_5.setText(_translate("MainWindow", "(Seconds)", None))
        self.label_6.setText(_translate("MainWindow", "Voltage", None))
        self.label_7.setText(_translate("MainWindow", " (Volt)", None))
        self.label_8.setText(_translate("MainWindow", "Time Period of Experiment", None))
        self.label_9.setText(_translate("MainWindow", "(Seconds)", None))
        self.readings.setText(_translate("MainWindow", "Show Readings", None))
        self.graph.setText(_translate("MainWindow", "Plot Graph", None))
        item = self.readingsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.readingsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Current", None))
        item = self.readingsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Voltage", None))
        item = self.readingsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Voltage(Arduino)", None))
        self.label_10.setText(_translate("MainWindow", "Soucemeter", None))
        self.label_11.setText(_translate("MainWindow", "Light Source", None))
        self.lightConditions.setText(_translate("MainWindow", "Change Light Conditions", None))
        self.start.setText(_translate("MainWindow", "Start", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

