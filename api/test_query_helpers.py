from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# movie = get_movie(db, movie_id=1)
# print(movie.title, movie.genres)

# movies = get_movies(db, limit=5)
#for m in movies:
#    print(m.movieId, m.title, m.genres)

# rating = get_rating(db, user_id=1, movie_id=1)
# print(rating.userId, rating.movieId, rating.rating)

#ratings = get_ratings(db, min_rating = 3.4, limit=5)
#for r in ratings:
#    print(r.movieId, r.rating)

n_movies = get_movie_count(db)
print(f"Nombre de films: {n_movies}")

db.close()

