import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
                                                             "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as f:
    spamwriter = csv.writer(f, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
