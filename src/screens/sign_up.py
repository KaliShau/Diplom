from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SignUp(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_SignUp, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1112, 763)
        self.setStyleSheet("background-color: #1a1a1a;\n"
"color: #e7e7e5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout = QtWidgets.QWidget(parent=self)
        self.layout.setMaximumSize(QtCore.QSize(1094, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.layout.setPalette(palette)
        self.layout.setStyleSheet("QWidget {\n"
"background-color: #202122;\n"
"}\n"
"\n"
"QTextEdit {\n"
"border: 1px solid #353738;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"border: 1px solid #dc5049;\n"
"}\n"
"\n"
"")
        self.layout.setObjectName("layout")
        self.title = QtWidgets.QLabel(parent=self.layout)
        self.title.setGeometry(QtCore.QRect(440, 10, 211, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.info = QtWidgets.QLabel(parent=self.layout)
        self.info.setGeometry(QtCore.QRect(430, 50, 231, 71))
        font = QtGui.QFont()
        font.setBold(False)
        self.info.setFont(font)
        self.info.setStyleSheet("color: #a5a7aa;")
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.loginLabel = QtWidgets.QLabel(parent=self.layout)
        self.loginLabel.setGeometry(QtCore.QRect(390, 150, 61, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: #a5a7aa;")
        self.loginLabel.setWordWrap(True)
        self.loginLabel.setObjectName("loginLabel")
        self.signInButton = QtWidgets.QCommandLinkButton(parent=self.layout)
        self.signInButton.setGeometry(QtCore.QRect(430, 350, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signInButton.setFont(font)
        self.signInButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.signInButton.setDescription("")
        self.signInButton.setObjectName("signInButton")
        self.loginEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.loginEdit.setGeometry(QtCore.QRect(390, 170, 301, 31))
        self.loginEdit.setStyleSheet("")
        self.loginEdit.setObjectName("loginEdit")
        self.confrimPasswodLabel = QtWidgets.QLabel(parent=self.layout)
        self.confrimPasswodLabel.setGeometry(QtCore.QRect(390, 280, 151, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.confrimPasswodLabel.setFont(font)
        self.confrimPasswodLabel.setStyleSheet("color: #a5a7aa;")
        self.confrimPasswodLabel.setWordWrap(True)
        self.confrimPasswodLabel.setObjectName("confrimPasswodLabel")
        self.confrimPasswordEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.confrimPasswordEdit.setGeometry(QtCore.QRect(390, 300, 301, 31))
        self.confrimPasswordEdit.setStyleSheet("")
        self.confrimPasswordEdit.setObjectName("confrimPasswordEdit")
        self.errorLabel = QtWidgets.QLabel(parent=self.layout)
        self.errorLabel.setGeometry(QtCore.QRect(390, 430, 301, 71))
        font = QtGui.QFont()
        font.setBold(False)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: #a5a7aa;")
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.passwodLabel = QtWidgets.QLabel(parent=self.layout)
        self.passwodLabel.setGeometry(QtCore.QRect(390, 220, 61, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.passwodLabel.setFont(font)
        self.passwodLabel.setStyleSheet("color: #a5a7aa;")
        self.passwodLabel.setWordWrap(True)
        self.passwodLabel.setObjectName("passwodLabel")
        self.passwordEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.passwordEdit.setGeometry(QtCore.QRect(390, 240, 301, 31))
        self.passwordEdit.setStyleSheet("")
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout.addWidget(self.layout)

        self.errorLabel.setVisible(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Регистрация</span></p><p><span style=\" font-size:24pt;\"><br/></span></p></body></html>"))
        self.info.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.info.setText(_translate("Form", "<html><head/><body><p>Пожалуйста введить данные</p></body></html>"))
        self.loginLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.loginLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Логин</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.signInButton.setText(_translate("Form", "Зарегистрироваться"))
        self.confrimPasswodLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.confrimPasswodLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Подтвердите пароль</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.errorLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.errorLabel.setText(_translate("Form", "<html><head/><body><p>Ошибка</p></body></html>"))
        self.passwodLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.passwodLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Пароль</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
