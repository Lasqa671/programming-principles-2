"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5

Write a function that returns a sublist of movies with an IMDB score above 5.5.

Write a function that takes a category name and returns just those movies under that category.

Write a function that takes a list of movies and computes the average IMDB score.

Write a function that takes a category and computes the average IMDB score.
"""
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

""" Functions below"""
#function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high_score(movie):
    return movie["imdb"] > 5.5
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def get_high_score_movies(movie_list):
    return [movie for movie in movie_list if is_high_score(movie)]
#Write a function that takes a category name and returns just those movies under that category.
def get_movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]
#Write a function that takes a list of movies and computes the average IMDB score.
def average_score(movie_list):
    if not movie_list:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movie_list)
    return total_score / len(movie_list)
#Write a function that takes a category and computes the average IMDB score.
def average_score_by_category(movie_list, category):
    category_movies = get_movies_by_category(movie_list, category)
    return average_score(category_movies)

print("Is The help IMDB score above 5.5?", is_high_score(movies[3]))

print()

high_score_movies = get_high_score_movies(movies)
print("Movies with IMDB score above 5.5:")
for movie in high_score_movies:
    print(movie["name"])

print()

romance_movies = get_movies_by_category(movies, "Romance")
print("Romance movies:")
for movie in romance_movies:
    print(movie["name"])

print()

average_all_scores = average_score(movies)
print("Average IMDB score for all movies:", average_all_scores)

print()

average_romance_scores = average_score_by_category(movies, "Romance")
print("Average IMDB score for Romance movies:", average_romance_scores)