"""
Method without any definition called abstract method
Class holding that method called abstract class
"""
from abc import ABC, abstractmethod


class Webdriver(ABC):

    @abstractmethod
    def click(self):
        pass


class ChromeDriver(Webdriver):
    def click(self,dingdong):
        print(f"clicking in firefox {dingdong}")

    def click(self,dola, abnhygt):
        print(f"clicking in chrome {dola}")

    def capturing_screen_shot(self):
        print("capturing screenshots in chrome")


obj = ChromeDriver()
obj.click("dhimala","weeee")
obj.click("doola","gggg")
