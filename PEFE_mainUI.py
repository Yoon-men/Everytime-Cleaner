from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QFontDatabase, QCursor, QFont

from os import path as osPath, environ
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
    
    check_box = ("QCheckBox{\n"
                    "color : #a6a6a6;\n"
                "}\n"
                "QCheckBox::indicator::unchecked{\n"
                    "image : url(:/img/ckb_unchecked_normal.png);\n"
                    "width : 20px;\n"
                    "height : 20px;\n"
                "}\n"
                "QCheckBox::indicator::unchecked::hover{\n"
                    "image : url(:/img/ckb_unchecked_hover.png);\n"
                "}\n"
                "QCheckBox::indicator::checked{\n"
                    "image : url(:/img/ckb_checked_normal.png);\n"
                    "width : 20px;\n"
                    "height : 20px;\n"
                "}\n"
                "QCheckBox::indicator::checked::hover{\n"
                    "image : url(:/img/ckb_checked_hover.png);\n"
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
        self.login_bt = QPushButton(self)
        self.login_bt.setGeometry(123, 245, 412, 46)
        self.login_bt.setStyleSheet(StyleSheets.start_button.value)
        self.login_bt.setText("로그인 및 데이터 가져오기")
        self.login_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_bt.setFocusPolicy(Qt.NoFocus)

        self.startDelete_bt = QPushButton(self)
        self.startDelete_bt.setGeometry(123, 245, 412, 46)
        self.startDelete_bt.setStyleSheet(StyleSheets.start_button.value)
        self.startDelete_bt.setText("삭제 시작")
        self.startDelete_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.startDelete_bt.setFocusPolicy(Qt.NoFocus)
        self.startDelete_bt.hide()

        self.remember_ckb = QCheckBox(self)
        self.remember_ckb.setGeometry(137, 308, 107, 18)
        self.remember_ckb.setFont(QFont("나눔고딕OTF", 12))
        self.remember_ckb.setStyleSheet(StyleSheets.check_box.value)
        self.remember_ckb.setFocusPolicy(Qt.NoFocus)
        self.remember_ckb.setText("아이디 기억")

        appdata_path = osPath.join(environ["LOCALAPPDATA"], "PEFE")
        appdata_file = osPath.join(appdata_path, "data.dat")
        if osPath.isfile(appdata_file) : 
            self.remember_ckb.setChecked(True)
            with open(appdata_file, 'r') as file : 
                user_id = file.read()
                print(file.read())
            self.userId_le.setText(user_id)

        self.forgot_bt = QPushButton(self)
        self.forgot_bt.setGeometry(378, 307, 150, 20)
        self.forgot_bt.setStyleSheet(StyleSheets.action_button.value + 
                                     "QPushButton{\n"
                                            "font-size : 12pt;\n"
                                        "}")
        self.forgot_bt.setText("아이디/비밀번호 찾기")
        self.forgot_bt.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgot_bt.setFocusPolicy(Qt.NoFocus)

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
        self.checkPosting_bt.setFocusPolicy(Qt.NoFocus)


        # messageBox_part
        self.userAccountNull_msgBox = QMessageBox()
        self.userAccountNull_msgBox.setWindowTitle("Account Error")
        self.userAccountNull_msgBox.setText("아이디와 비밀번호를 모두 입력해 주세요.")
        self.userAccountNull_msgBox.setIcon(QMessageBox.Critical)
        if osPath.isfile(icon_path) : 
            self.userAccountNull_msgBox.setWindowIcon(QIcon(icon_path))

        self.notLogin_msgbox = QMessageBox()
        self.notLogin_msgbox.setWindowTitle("Data Error")
        self.notLogin_msgbox.setText("로그인 및 데이터 가져오기 후에 다시 시도해 주십시오.")
        self.notLogin_msgbox.setIcon(QMessageBox.Critical)
        if osPath.isfile(icon_path) : 
            self.notLogin_msgbox.setWindowIcon(QIcon(icon_path))
        
        self.solvePuzzle_msgBox = QMessageBox()
        self.solvePuzzle_msgBox.setWindowTitle("사용자 퀘스트 발행")
        self.solvePuzzle_msgBox.setText("캡차 퍼즐 해결 후 로그인 버튼 클릭까지 진행해 주십시오.")
        self.solvePuzzle_msgBox.setIcon(QMessageBox.Warning)
        if osPath.isfile(icon_path) : 
            self.solvePuzzle_msgBox.setWindowIcon(QIcon(icon_path))





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    mainUI = MainUI()
    mainUI.show()
    sys.exit(app.exec_())
