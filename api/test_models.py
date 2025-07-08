# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %%
# Tester la récupération de quelques films
movies = db.query(Movie).limit(12).all() # all permet de récupérer tous les résultats

for movie in movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
    if movie.link:
        print(f"IMDB ID: {movie.link.imdbId}, TMDB ID: {movie.link.tmdbId}")
    else:
        print("No link information available.")
    print("-" * 40)

# %%
# Récupérer les films du genre Action
action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(10).all()

for movie in action_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
    if movie.link:
        print(f"IMDB ID: {movie.link.imdbId}, TMDB ID: {movie.link.tmdbId}")
    else:
        print("No link information available.")
    print("-" * 40)
# %%
# Tester la récupération de quelques évaluations
Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(f"User ID: {rating.userId}, Movie ID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")
    movie = db.query(Movie).filter(Movie.movieId == rating.movieId).first()
    if movie:
        print(f"Movie Title: {movie.title}")
    else:
        print("No movie found for this rating.")
    print("-" * 40)

# %%
# Récuperer les films dont la note est supérieur à 4

hight_rated_movies = (
    db.query (Movie.title, Rating.rating)
    .join(Rating) # on peut preciser les cles ici mais c'est facultatif car on les a precise dans chaque classe
    .filter(Rating.rating >= 4)
    .limit(10)
    .all()
)

for title, rating in hight_rated_movies:
    print(f"Title: {title}, Rating: {rating}")
# %%
# Recuperation de tags associees aux films

tags = db.query(Tag).limit(10).all()

for tag in tags:
    print(f"User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}")
    movie = db.query(Movie).filter(Movie.movieId == tag.movieId).first()
    if movie:
        print(f"Movie Title: {movie.title}")
    else:
        print("No movie found for this tag.")
    print("-" * 40)

# %%
# Tester la classe Link

links = db.query(Link).limit(10).all()

for link in links:
    print(f"Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")
    movie = db.query(Movie).filter(Movie.movieId == link.movieId).first()
    if movie:
        print(f"Movie Title: {movie.title}")
    else:
        print("No movie found for this link.")
    print("-" * 40)
# %%

db.close()  # Fermer la session de base de données

# %%
