# HorseクラスとRiderクラスを定義しよう。コンポジションを使って、馬（Horse）に騎手（Rider）を持たせよう。

class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, weight, rider):
        self.name = name
        self.weight = weight
        self.rider = rider


rider_father = Rider("シンボリルドルフ")
a_horse = Horse("トウカイテイオー", 460, rider_father)

print("The name of Horse is {}".format(a_horse.name))
print("The name of Rider is {}".format(a_horse.rider.name))


print(a_horse.rider.name)
