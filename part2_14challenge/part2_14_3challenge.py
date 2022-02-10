# 2つのパラメーターを受け取る関数を書こう。この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseを返そう。

def compare(obj1, obj2):
    return obj1 is obj2


a = input("print one word.")
b = input("print one word.")

print(compare(a, b))
