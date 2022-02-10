# 数字を入力値として受け取り、その数字を2乗した戻り値を返す関数を書いてみよう。

def squared(x):
    """
    数字を入力値として受け取り、その数字を2乗した戻り値を返す(Takes an int and return it multipled by 2)
    :param x : int.
    :return: x multipled by 2.  
    """
    return x ** 2


a = int(input("数字を入力してください"))
print(squared(a))
