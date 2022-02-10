# 文字列をfloat型に変換して戻り値とする関数を書いてみよう。起こり得る例外をキャッチする例外処理を書こう。

def convert(string):
    """Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("couldn't convert the string to a float")


c = convert("55.0")
print(c)
