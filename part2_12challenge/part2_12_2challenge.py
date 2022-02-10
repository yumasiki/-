# 円を表すCircleクラスを定義しよう。そのクラスに、面積を計算して返すメソッドareaを持たせよう。面積の計算には、pythonの組み込みモジュールmathのpi定数が使えます。次に、Circleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう。

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi


a_circle = Circle(2)
print(a_circle.calculate_area())
