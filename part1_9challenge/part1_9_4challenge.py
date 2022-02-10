import csv
from encodings import utf_8

movies = [["トップガン", "リスキービジネス", "マイノリティーレポート"], [
    "タイタニック", "ザレバナント", "インセプション"], ["トレーニングデイ", "マンオンファイア", "フライト"]]
with open("movies2.csv", "w", encoding="utf-8", errors="ignore") as f:
    spamwriter = csv.writer(f, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
