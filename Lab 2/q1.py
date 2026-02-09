movies = []

n = int(input("Enter number of movies: "))
for i in range(n):
    name = input("Enter movie name: ")
    rating = float(input("Enter rating: "))
    movies.append((name, rating))

total = 0
highest_movie = movies[0]

for movie in movies:
    total += movie[1]
    if movie[1] > highest_movie[1]:
        highest_movie = movie

average = total / n

print("Average Rating:", average)
print("Highest Rated Movie:", highest_movie[0])

print("Movies above average rating:")
for movie in movies:
    if movie[1] > average:
        print(movie[0])
