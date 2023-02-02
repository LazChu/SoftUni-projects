import sys

movies_to_watch = int(input())

combine_rating = 0

max_rating = -sys.maxsize
min_rating = sys.maxsize
for movie in range(movies_to_watch):
    movie_name = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        movie_high = movie_name
    elif rating < min_rating:
        min_rating = rating
        movie_low = movie_name
    combine_rating += rating
    avg_rating = combine_rating / movies_to_watch
print(f"{movie_high} is with highest rating: {max_rating:.1f}")
print(f"{movie_low} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")
