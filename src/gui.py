# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vsfeedspeed.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_vsfeedspeedgui(object):
    def setupUi(self, vsfeedspeedgui):
        vsfeedspeedgui.setObjectName("vsfeedspeedgui")
        vsfeedspeedgui.resize(800, 800)
        vsfeedspeedgui.setMinimumSize(QtCore.QSize(600, 800))
        self.tabWidget = QtWidgets.QTabWidget(vsfeedspeedgui)
        self.tabWidget.setGeometry(QtCore.QRect(40, 20, 401, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 61, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 182, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 40, 167, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(110, 80, 167, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 373, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.material_combo_box = QtWidgets.QComboBox(self.layoutWidget)
        self.material_combo_box.setObjectName("material_combo_box")
        self.horizontalLayout_2.addWidget(self.material_combo_box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout.addWidget(self.lineEdit_12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 40, 256, 41))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(30, 20, 62, 17))
        self.label_14.setObjectName("label_14")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 100, 260, 128))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 356, 161))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_8.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_10.addWidget(self.lineEdit_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_11.addWidget(self.lineEdit_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.tab_3, "")
        self.frame = QtWidgets.QFrame(vsfeedspeedgui)
        self.frame.setGeometry(QtCore.QRect(460, 100, 321, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(10, 100, 101, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(10, 130, 101, 17))
        self.label_12.setObjectName("label_12")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 100, 191, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 130, 191, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_49 = QtWidgets.QLabel(self.frame)
        self.label_49.setGeometry(QtCore.QRect(120, 20, 62, 17))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame)
        self.label_50.setGeometry(QtCore.QRect(10, 170, 171, 17))
        self.label_50.setObjectName("label_50")

        self.retranslateUi(vsfeedspeedgui)
        self.tabWidget.setCurrentIndex(3)
        self.lineEdit_12.textChanged['QString'].connect(self.material_combo_box.clear)
        QtCore.QMetaObject.connectSlotsByName(vsfeedspeedgui)

    def retranslateUi(self, vsfeedspeedgui):
        _translate = QtCore.QCoreApplication.translate
        vsfeedspeedgui.setWindowTitle(_translate("vsfeedspeedgui", "vsfeedspeedgui"))
        self.label_15.setText(_translate("vsfeedspeedgui", "Motor HP"))
        self.label_16.setText(_translate("vsfeedspeedgui", "Efficiency"))
        self.lineEdit_14.setPlaceholderText(_translate("vsfeedspeedgui", "0.9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("vsfeedspeedgui", "Machine"))
        self.label.setText(_translate("vsfeedspeedgui", "Workpiece Material"))
        self.label_2.setText(_translate("vsfeedspeedgui", "Brinell Hardness"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("vsfeedspeedgui", "Workpiece"))
        self.label_14.setText(_translate("vsfeedspeedgui", "Tool Crib"))
        self.label_3.setText(_translate("vsfeedspeedgui", "Tool Material"))
        self.label_4.setText(_translate("vsfeedspeedgui", "Coating"))
        self.label_5.setText(_translate("vsfeedspeedgui", "Number of Teeth"))
        self.label_8.setText(_translate("vsfeedspeedgui", "Diameter (in)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("vsfeedspeedgui", "Tool"))
        self.label_6.setText(_translate("vsfeedspeedgui", "Chosen Work Material"))
        self.label_7.setText(_translate("vsfeedspeedgui", "Chosen Tool"))
        self.label_13.setText(_translate("vsfeedspeedgui", "Operation Type (Face, End, Slit)"))
        self.label_9.setText(_translate("vsfeedspeedgui", "Depth of Cut"))
        self.label_10.setText(_translate("vsfeedspeedgui", "Width of Cut"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("vsfeedspeedgui", "Operation"))
        self.label_11.setText(_translate("vsfeedspeedgui", "Feedrate (ipm)"))
        self.label_12.setText(_translate("vsfeedspeedgui", "Speed (RPM)"))
        self.label_49.setText(_translate("vsfeedspeedgui", "Results"))
        self.label_50.setText(_translate("vsfeedspeedgui", "Percent Power Required"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vsfeedspeedgui = QtWidgets.QWidget()
    ui = Ui_vsfeedspeedgui()
    ui.setupUi(vsfeedspeedgui)
    vsfeedspeedgui.show()
    sys.exit(app.exec_())