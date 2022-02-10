# 三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height / 2


triangle = Triangle(3, 4)
print(triangle.calculate_area())
