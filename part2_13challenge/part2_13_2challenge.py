# Squareクラスにchange_sizeメソッドを定義して、そこに渡した数値の分だけSquareオブジェクトの横幅を増やしたり、減らしたり（マイナスの場合）してみよう。

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_primeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size


a_square = Square(25)
print(a_square.calculate_primeter())
print(a_square.s1)

a_square.change_size(-29)
print(a_square.calculate_primeter())
print(a_square.s1)
