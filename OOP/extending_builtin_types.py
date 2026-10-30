# Extending builtin-types
# self =  represents the current object.


# Extending str type
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())  # PythonPython


# Extending list type

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
list.append("1")
print(list)
