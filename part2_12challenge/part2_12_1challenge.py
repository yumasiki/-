# リンゴと言われて思い浮かぶ、4つの属性を考えよう。その4つの属性をインスタンス変数に持つ、Appleクラスを定義しよう。

class Apple:
    def __init__(self, w, n, d, c):
        self.weight = w
        self.number = n
        self.day = d
        self.color = c
        print("Created!")


apple = Apple(100, 2, 10, "red")
print(apple)
