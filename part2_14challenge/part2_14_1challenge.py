# Squareクラスにsquare_list クラス変数を追加しよう。そして、新しくSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。
class Shape:
    def what_am_i(self):
        print("I am a shape")


class Square(Shape):
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(side)

    def calculate_primeter(self):
        return self.side * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square")


a_square = Square(25)
print(Square.square_list)

another_square = Square(55)
print(Square.square_list)
