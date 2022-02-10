# 任意のキーを入力させるプログラムを書こう。入力されたキーを使って、1つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。
from multiprocessing.connection import answer_challenge


my_dic = {"身長": "169cm",
          "好きな色": "blue",
          "好きな著者": "uminotika"}

answer = input("「身長」、「好きな色」、「好きな著者」の三つのうちから気になるワードを打ち込んでください。")

if answer in my_dic:
    result = my_dic[answer]
    print(result)
