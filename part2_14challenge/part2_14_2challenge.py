# Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。たとえば、Square(29)のようにオブジェクトを作ったら、print関数では29 by 29 by  29 by 29と出力しよう。

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

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)


a_square = Square(25)
print(a_square)
