# Poly meaning 'Many', Morph meaning 'Forms'
# To achieved Polymorphism, start by defining a base class, define a common behavior or method needed in its derivatives or children
# and achieved polymorphic behavior
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# Determine at runtime, it doesn't know which class or control it controls.
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
