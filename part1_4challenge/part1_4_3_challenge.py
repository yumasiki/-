# 3つの必須引数と2つのオプション引数がある関数を書いてみよう。
def Test(x, y, z, a=1, b=2):
    print(x, y, z, a, b)


Test(4, 5, 6)


def add_mult(a, b, c, x=100, z=1000):
    """
    Returns the result of two optional params
      multiplied by the addition of 3 required
      params.
      :param a: int.
      :param b: int.
      :param c: int.
      :param x: int.
      :param z: int.
      :return: int.
    """
    return (a + b + c) * x * z


result = add_mult(10, 15, 25)
print(result)
