from re import A


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)


class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        """被演算子として、認識されていない演算子にも__add__の特殊メソッドをいれることで、被演算子として認識させ、足し算の演算子で計算させることができる。"""
        return abs(self.n + other.n)


x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)
