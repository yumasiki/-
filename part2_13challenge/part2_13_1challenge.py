# RectangleとSquareクラスを作ろう。両方のクラスに、その図形の外周の長さを計算して返すcalculate_perimeterメソッドを定義しよう。そして、RectangleとSquareのオブジェクトを作って、それぞれのcaculate_perimeterメソッドを呼ぼう。

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_primeter(self):
        return (self.width + self.length) * 2


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_primeter(self):
        return self.side * 4


a_rectangle = Rectangle(10, 20)
print(a_rectangle.calculate_primeter())

a_square = Square(25)
print(a_square.calculate_primeter())
