lists = [1, 2, 4, 7, 9]

while True:
    answer = input("数字を入力してください。qで終了。")

    if answer == "q":
        break

    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、qで終了します。")
    if answer in lists:
        print("正解")
    else:
        print("不正解")
