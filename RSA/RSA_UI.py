# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RSA_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 849)
        MainWindow.setMinimumSize(QtCore.QSize(595, 849))
        MainWindow.setMaximumSize(QtCore.QSize(595, 849))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                        "    background-color: white;\n"
                                        "}\n"
                                        "\n"
                                        "#text_input {\n"
                                        "    border-top: 3px solid #1E90FF;\n"
                                        "    border-bottom: 3px solid #1E90FF;\n"
                                        "    background-color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton {\n"
                                        "    color: white;\n"
                                        "    background-color: #1E90FF;\n"
                                        "    border: 0\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:disabled {\n"
                                        "    color: white;\n"
                                        "    background-color: #00BFFF;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    color: white;\n"
                                        "    background-color: #00BFFF;\n"
                                        "}\n"
                                        "\n"
                                        "#label_encrypt {\n"
                                        "    border-top: 3px solid #1E90FF;\n"
                                        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_input = QtWidgets.QTextEdit(self.centralwidget)
        self.text_input.setEnabled(True)
        self.text_input.setMaximumSize(QtCore.QSize(1000, 301))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(12)
        self.text_input.setFont(font)
        self.text_input.setObjectName("text_input")
        self.verticalLayout.addWidget(self.text_input)
        self.button_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.button_encrypt.setMaximumSize(QtCore.QSize(5000, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_encrypt.setFont(font)
        self.button_encrypt.setObjectName("button_encrypt")
        self.verticalLayout.addWidget(self.button_encrypt)
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_key.setFont(font)
        self.label_key.setText("")
        self.label_key.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key.setObjectName("label_key")
        self.verticalLayout.addWidget(self.label_key)
        self.label_encrypt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_encrypt.setFont(font)
        self.label_encrypt.setText("")
        self.label_encrypt.setTextFormat(QtCore.Qt.RichText)
        self.label_encrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_encrypt.setObjectName("label_encrypt")
        self.label_encrypt.setWordWrap(True)
        self.verticalLayout.addWidget(self.label_encrypt)
        self.button_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.button_decrypt.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_decrypt.setFont(font)
        self.button_decrypt.setObjectName("button_decrypt")
        self.verticalLayout.addWidget(self.button_decrypt)
        self.label_decrypt = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_decrypt.setFont(font)
        self.label_decrypt.setText("")
        self.label_decrypt.setWordWrap(True)
        self.label_decrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_decrypt.setObjectName("label_decrypt")
        self.verticalLayout.addWidget(self.label_decrypt)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA_Vasilev"))
        self.button_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.button_decrypt.setText(_translate("MainWindow", "Decrypt"))
