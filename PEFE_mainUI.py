from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QFontDatabase, QCursor

from os import path as osPath
from enum import Enum


class StyleSheets(Enum) : 
    main_window = ("QMainWindow{\n"
                        "background-color : #ffffff;\n"
                    "}")
    
    line_edit = ("QLineEdit{\n"
                    "border : 1px solid #d6d6d6;\n"
                    "selection-background-color : #d6d6d6;\n"
                    "selection-color : #000000;\n"
                    "font-family : 나눔고딕OTF;\n"
                    "font-size : 15pt;\n"
                "}")
    
    start_button = ("QPushButton{\n"
                        "background-color : #c62917;\n"
                        "color : #ffffff;\n"
                        "font-family : 나눔고딕OTF;\n"
                        "font-size : 15pt;\n"
                        "font-weight : bold;\n"
                    "}")
    
    action_button = ("QPushButton{\n"
                        "background-color : transparent;\n"
                        "font-family : 나눔고딕OTF;\n"
                    "}")
    
    label = ("QLabel{\n"
                "color : #b6b6b6;\n"
                "font-family : 나눔고딕OTF;\n"
                "font-size : 13.5pt;\n"
                "font-weight : bold;\n"
            "}")


class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()

        self.signal()

    def mainUI(self) : 
        # basic_part
        self.setFixedSize(658, 428)
        self.setWindowTitle("Posting Eraser For Everytime")
        self.setStyleSheet(StyleSheets.main_window.value)
        icon_path = osPath.join(osPath.dirname(__file__), "Posting-Eraser-For-Everytime.ico")
        if osPath.isfile(icon_path) : 
            self.setWindowIcon(QIcon(icon_path))
        font_path = osPath.join(osPath.dirname(__file__), "NanumGothicBold.otf")
        if osPath.isfile(font_path) : 
            QFontDatabase.addApplicationFont(font_path)
        

        # title_part
        self.icon_lb = QLabel(self)
        self.icon_lb.setGeometry(107, 39, 100, 100)
        self.icon_lb.setStyleSheet("image : url(:/img/icon.png);")

        self.title_lb = QLabel(self)
        self.title_lb.setGeometry(277, 99, 260, 30)
        self.title_lb.setStyleSheet("image : url(:/img/title_label.png);")


        # enter_part
        self.userId_le = QLineEdit(self)
        self.userId_le.setGeometry(123, 141, 412, 46)
        self.userId_le.setStyleSheet(StyleSheets.line_edit.value)
        self.userId_le.setPlaceholderText("아이디")
        
        self.userPw_le = QLineEdit(self)
        self.userPw_le.setGeometry(123, 193, 412, 46)
        self.userPw_le.setStyleSheet(StyleSheets.line_edit.value)
        self.userPw_le.setPlaceholderText("비밀번호")
        self.userPw_le.setEchoMode(QLineEdit.Password)


        # action_part
        self.start_bt = QPushButton(self)
        self.start_bt.setGeometry(123, 245, 412, 46)
        self.start_bt.setStyleSheet(StyleSheets.start_button.value)
        self.start_bt.setText("삭제 시작")
        self.start_bt.setCursor(QCursor(Qt.PointingHandCursor))

        self.forgot_bt = QPushButton(self)
        self.forgot_bt.setGeometry(378, 307, 150, 20)
        self.forgot_bt.setStyleSheet(StyleSheets.action_button.value + 
                                     "QPushButton{\n"
                                            "font-size : 12pt;\n"
                                        "}")
        self.forgot_bt.setText("아이디/비밀번호 찾기")
        self.forgot_bt.setCursor(QCursor(Qt.PointingHandCursor))

        self.checkPosting_lb = QLabel(self)
        self.checkPosting_lb.setGeometry(178, 357, 264, 18)
        self.checkPosting_lb.setStyleSheet(StyleSheets.label.value)
        self.checkPosting_lb.setText("썼던 글들을 확인하고 싶으신가요?")
        
        self.checkPosting_bt = QPushButton(self)
        self.checkPosting_bt.setGeometry(450, 356, 36, 20)
        self.checkPosting_bt.setStyleSheet(StyleSheets.action_button.value + 
                                           "QPushButton{\n"
                                                "color : #c62917;\n"
                                                "font-size : 13.5pt;\n"
                                                "font-weight : bold;\n"
                                            "}")
        self.checkPosting_bt.setText("확인")
        self.checkPosting_bt.setCursor(QCursor(Qt.PointingHandCursor))



    def signal(self) : 
        pass                # Test code / please delete the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    sys.exit(app.exec_())