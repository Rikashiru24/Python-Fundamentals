from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"
      
class French(Greet):
  def say_hello(self):
   	return "Bonjour!"

g = French()
print(g.say_hello())