# ENCAPSULATION - bundling data (variables) and the methods that operate on that data into a single unit (a class) while restricting direct access to the object's internal components

class Bank:
    def __init__(self, current_bal: float, maintaining_bal: float):
        self.__current_bal = current_bal
        self.__maintaining_bal = maintaining_bal

    def get_current_bal(self):
        return self.__current_bal

    def set_current_bal(self, current_bal):
        if current_bal > 0:
            self.__current_bal += current_bal
        else:
            print("Added value cannot be zero-value.")

acc1 = Bank(5000, 2000)
print(acc1.get_current_bal())
acc1.set_current_bal(5000)
print(acc1.get_current_bal())
