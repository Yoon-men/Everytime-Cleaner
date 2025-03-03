"""
Driver-Manager

ver 1.2.2

~ 23:51 on Sat, Feb 15, 2025 ~
"""

# * ------------------------------------------------------------ *#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.options import Options as SafariOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.common.exceptions import WebDriverException

from typing import Optional

# * ------------------------------------------------------------ *#


class DriverManager:
    def __init__(self) -> None:
        self.driver: Optional[webdriver.Chrome | webdriver.Edge | webdriver.Firefox | webdriver.Safari] = None
        self.make_driver()
        return


    def make_driver(self) -> None:
        for make_driver in [
            self._make_chrome_driver,
            self._make_edge_driver,
            self._make_firefox_driver
            # self._make_safari_driver
        ]:
            try: 
                self.driver = make_driver()
                return
            except: 
                continue
        
        raise WebDriverException("Chrome, Edge, Firefox 브라우저를 모두 찾을 수 없어 WebDriver를 생성할 수 없습니다.")



    def terminate_driver(self) -> None:
        try:
            self.driver.quit()
        except:
            pass
        return



    def _make_chrome_driver(self) -> webdriver.Chrome:
        options = ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option(
            "excludeSwitches", ["enable-logging", "enable-automation"]
        )
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--mute-audio")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(2)

        return driver



    def _make_edge_driver(self) -> webdriver.Edge:
        options = EdgeOptions()
        options.add_argument("start-maximized")
        options.detach = True
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--mute-audio")
        
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(2)

        return driver



    def _make_firefox_driver(self) -> webdriver.Firefox:
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--mute-audio")
        
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(2)
        
        return driver



    def _make_safari_driver(self) -> webdriver.Safari:
        options = SafariOptions()

        driver = webdriver.Safari(options=options)
        driver.implicitly_wait(2)

        return driver