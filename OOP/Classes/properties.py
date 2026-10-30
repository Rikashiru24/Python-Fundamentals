# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # price = property(get_price, set_price) # Instead of this, we'll use @property decorator


# product = Product(-10)
# print(product.price)

# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or deleter attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = float(width)
        self._height = float(height)

    # ----------GETTER----------
    @property
    def width(self):
        if not hasattr(self, '_width'):
            return "No width defined"
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        if not hasattr(self, '_height'):
            return "No height defined"
        return f"{self._height:.1f}cm"

    # ----------SETTER----------
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print(f"Width cannot be {new_width}.")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print(f"Height cannot be {new_height}.")

    # ----------DELETER----------
    @width.deleter
    def width(self):
        del self._width
        print("Width attribute is deleted.")

    @height.deleter
    def height(self):
        del self._height
        print(f"Width attribute is deleted.")


rectangle = Rectangle(1, 2)
rectangle.width = 10
rectangle.height = 20
print(rectangle.width)
print(rectangle.height)
del rectangle.width
del rectangle.height
