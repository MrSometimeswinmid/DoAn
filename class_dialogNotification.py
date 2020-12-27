from PyQt5.QtCore import Qt
from class_convertType import ConvertThisQObject
import team_config

from PyQt5.QtWidgets import *

from PyQt5 import uic


class NotificationWindow(QDialog):

    def __init__(self, title: str, content: str, parent):
        super(NotificationWindow, self).__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.content = content
        self.title = title
        uic.loadUi(team_config.UI_NOTIFICATION, self)
        self.label_title = ConvertThisQObject(self, QLabel, 'labelTitle').toQLabel()
        self.label_content = ConvertThisQObject(self, QLabel, 'labelContent').toQLabel()
        self.button_ok = ConvertThisQObject(self, QPushButton, 'pushButtonOK').toQPushButton()
        self.button_ok.clicked.connect(lambda: self.reject())
        self.setupUI()

    def setupUI(self):
        self.label_title.setText(self.title)
        self.label_content.setText(self.content)

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()

    def mouseMoveEvent(self,event):
        if self.moving:
            self.move(event.globalPos()-self.offset)

