from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    def some_operation(self):
        product = self.factory_method()
        result = f"Create the {product.btnStyle()} and {product.onClick()}"
        return result
        
class WindowsCreator(Creator):
    
    def factory_method(self) -> Button:
        return WindowsButton()
    
class AppleCreator(Creator):
    
    def factory_method(self) -> Button:
        return AppleButton()
    

class Button(ABC):
    
    @abstractmethod
    def btnStyle(self) -> str:
        pass
    
    @abstractmethod
    def onClick(self) -> str:
        pass
    
    
class WindowsButton(Button):
    
    def btnStyle(self) -> str:
        return "{Button with the windows style}"

    
    def onClick(self) -> str:
        return "{Button with the windows click}"
    

class AppleButton(Button):
    
    def btnStyle(self) -> str:
        return "{Button with the apple style}"

    
    def onClick(self) -> str:
        return "{Button with the apple click}"
    
    
def client_code(creator : Creator):
    print(creator.some_operation())
    
if __name__ == "__main__":
    print("-----WINDOWS-----")
    client_code(WindowsCreator())
    
    print("")
    
    print("-----Apple-----")
    client_code(AppleCreator())
