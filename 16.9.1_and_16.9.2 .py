class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"

    def get_area_Square(self):  # Метод для вычисления площади прямоугольника
        return self.width * self.height


parameters = Rectangle(5, 10, 50, 100)

print(f"Rectangle: {parameters}")

square_rectangle = Rectangle(5, 10, 50, 100)

print(square_rectangle.get_area_Square())  # Вывод результата площади прямоугольника
