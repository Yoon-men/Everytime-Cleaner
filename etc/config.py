"""
Config

ver 1.4.1

~ 23:44 on Mon, Mar 3, 2025 ~
"""

# * ------------------------------------------------------------ *#

import os
import sys
import pickle
from typing import Dict, Optional
import traceback

import certifi
import platform

# * ------------------------------------------------------------ *#

from etc.logger import *

# * ------------------------------------------------------------ *#


class Config:
    # 기본값 설정 (하위 클래스에서 반드시 재정의할 것)
    VERSION: str = "UNKNOWN_VERSION"
    LAST_UPDATED: str = "UNKNOWN_DATE"
    PROJECT_NAME: str = "UNNAMED_PROJECT"

    # 내부 변수
    _logger: Optional[logging.Logger] = None
    _initialized: bool = False


    @classmethod
    def initialize(cls) -> None:
        """
        하위 클래스에서 반드시 호출할 것
        """
        cls._init_logger()
        cls._load_data()

        cls._initialized = True
        return


    @classmethod
    def _init_logger(cls) -> None:
        if not cls._initialized:
            # 누락된 필드 검출
            required_fields = []
            if cls.PROJECT_NAME == "UNNAMED_PROJECT":
                required_fields.append("PROJECT_NAME")
            if cls.VERSION == "UNKNOWN_VERSION":
                required_fields.append("VERSION")

            # 오류 발생 조건 확인
            if required_fields:
                raise RuntimeError(
                    f"These fields must be overridden in the child class: {', '.join(required_fields)}"
                )

            # Logger 초기화
            cls._logger = init_logger(
                name=cls.PROJECT_NAME,
                version=cls.VERSION,
                c_level=DEBUG,
                f_level=INFO,
                f_path="./log",
            )
            cls._initialized = True
        return
    

    @classmethod
    def logger(cls) -> logging.Logger:
        if not cls._initialized:
            raise RuntimeError("Config.initialize() must be called first")
        
        return cls._logger



    def get_base_path() -> str:
        if getattr(sys, "frozen", False):
            # PyInstaller
            if hasattr(sys, "_MEIPASS"):
                return sys._MEIPASS
            # py2app
            else:
                return os.path.join(os.path.dirname(sys.executable), "..", "Resources")
        else:
            return os.getcwd()


    FONT_PATH: str = os.path.join(get_base_path(), "res", "NanumGothicBold.otf")
    ICON_PATH: str = os.path.join(
        get_base_path(),
        "res",
        # f"icon.{'ico' if platform.system() == 'Windows' else 'icns'}"
        "icon.png"
    )
    SVG_PATH: str = os.path.join(get_base_path(), "res", "img", "loading.svg")
    ENV_PATH: str = os.path.join(get_base_path(), ".env")

    PLATFORMS_PATH: str = os.path.join(get_base_path(), "platforms")


    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1.0"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1.0"
    os.environ["QT_SCALE_FACTOR"] = "1.0"

    os.environ["SSL_CERT_FILE"] = certifi.where()

    DATA_PATH: str = "data.dat"
    DATA: Dict = {}

    @classmethod
    def save_data(cls) -> None:
        with open(cls.DATA_PATH, "wb") as f:
            pickle.dump(cls.DATA, f)
        return

    @classmethod
    def _load_data(cls) -> bool:
        if not os.path.isfile(cls.DATA_PATH):
            return False

        try: 
            with open(cls.DATA_PATH, "rb") as f:
                cls.DATA: Dict = pickle.load(f)
        except: 
            exc_type, exc_value, exc_traceback = sys.exc_info()
            formatted_traceback = traceback.format_exception(
                exc_type, exc_value, exc_traceback
            )
            exc_msg = "".join(formatted_traceback)

            cls.logger().error(f"An error occured while loading the data.\n{exc_msg}")
            return False
        
        return True