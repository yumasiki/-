# Shapeクラスを定義しよう。呼ばれたら、"I am a shape"を返すメソッド what_am_i を定義しよう。前のチャレンジで定義したRectangleとSquareクラスを変更して、このShapeクラスを継承させよう。そして、RectangleとSquareのオブジェクトを生成して、このチャレンジで追加したメソッド what_am_i を呼んでみよう。

class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_primeter(self):
        return (self.width + self.length) * 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_primeter(self):
        return self.side * 4


a_rectangle = Rectangle(10, 20)
print(a_rectangle.what_am_i())

a_square = Square(25)
print(a_square.what_am_i())
