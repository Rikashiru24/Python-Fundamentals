# Duck Typing = It doesn't matter as long as each iterable or classes or objects has the same name method.
# "If it's walks like a duck and quacks like a duck, it is a duck."

class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):  # Only looks for the draw methods.
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
