from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    
    @abstractmethod
    def createButton(self) -> Button:
        pass
    
    @abstractmethod
    def createChecklist(self) -> Checklist:
        pass
    
    
class WindowsFactory(AbstractFactory):
    
    def createButton(self) -> Button:
        return WindowsButton()
    def createChecklist(self) -> Checklist:
        return WindowsChecklist()
    
class AppleFactory(AbstractFactory):
    
    def createButton(self) -> Button:
        return AppleButton()
    def createChecklist(self) -> Checklist:
        return AppleChecklist()
    
#-------------------------------------------------------------------
#-------------------------------------------------------------------
class Button(ABC):
    
    @abstractmethod
    def onClick(self):
        pass
    
class WindowsButton(Button):
    
    def onClick(self):
        return "{Button in windows style}"
    
class AppleButton(Button):
    
    def onClick(self):
        return "{Button in apple style}"
    

class Checklist(ABC):
    
    @abstractmethod
    def onClick(self):
        pass
    
class WindowsChecklist(Checklist):
    
    def onClick(self):
        return "{Checklist in windows style}"
    
class AppleChecklist(Checklist):
    
    def onClick(self):
        return "{Checklist in apple style}"
    
    
def client_code(factory : AbstractFactory):
    print(factory.createButton().onClick())
    print(factory.createChecklist().onClick())
    
if __name__ == "__main__":
    print("Creating app in Windows")
    client_code(WindowsFactory())
    
    print("")
    
    print("Creating app in Windows")
    client_code(AppleFactory())