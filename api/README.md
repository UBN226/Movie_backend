
# MovieLens API

Bienvenue dans **MovieLens API**, un projet éducatif développé avec **FastAPI** dans le cadre d'une formation complète sur la Data Science et le développement d’API. Cette API RESTful permet d’explorer dynamiquement les données du célèbre dataset **MovieLens**.

> Ce projet fait partie de ma progression dans la formation "Data Science avec Python, SQL, FastAPI, Streamlit & Docker" sur Udemy.

---

## Fonctionnalités clés

- Rechercher des films par titre, genre ou ID
- Accéder aux évaluations faites par les utilisateurs
- Visualiser et gérer les tags associés aux films
- Récupérer les identifiants IMDB et TMDB
- Obtenir des statistiques globales sur les données

---

## Prérequis

- Python ≥ 3.13
- Un client HTTP comme `httpx` ou `requests`

Installation rapide :

```bash
pip install httpx
```

---

## Lancer l’API localement

Exécuter le serveur FastAPI :

```bash
uvicorn app.main:app --reload
```

Accès :

- API : http://localhost:8000
- Swagger : http://localhost:8000/docs
- Redoc : http://localhost:8000/redoc

---

## Endpoints disponibles

| Méthode | Endpoint                            | Description |
|---------|-------------------------------------|-------------|
| GET     | `/`                                 | Vérifie que l'API fonctionne |
| GET     | `/movies`                           | Liste paginée des films (filtres par genre, titre, etc.) |
| GET     | `/movies/{movie_id}`                | Détails d’un film |
| GET     | `/ratings`                          | Liste paginée des évaluations |
| GET     | `/ratings/{user_id}/{movie_id}`     | Évaluation d’un film par un utilisateur |
| GET     | `/tags`                             | Liste des tags |
| GET     | `/tags/{user_id}/{movie_id}/{tag}`  | Détail d’un tag spécifique |
| GET     | `/links`                            | Liste des identifiants IMDB / TMDB |
| GET     | `/links/{movie_id}`                 | Identifiants d’un film donné |
| GET     | `/analytics`                        | Statistiques globales sur la base |

---

## Exemples d’utilisation (httpx)

Lister les films :

```python
import httpx
response = httpx.get("http://localhost:8000/movies", params={"limit": 5})
print(response.json())
```

Obtenir un film spécifique :

```python
movie_id = 1
response = httpx.get(f"http://localhost:8000/movies/{movie_id}")
print(response.json())
```

Rechercher les évaluations d’un film :

```python
response = httpx.get("http://localhost:8000/ratings", params={"movie_id": 1})
print(response.json())
```

Récupérer un tag :

```python
response = httpx.get("http://localhost:8000/tags/5/1/superbe")
print(response.json())
```

Statistiques globales :

```python
response = httpx.get("http://localhost:8000/analytics")
print(response.json())
```

---

## Objectifs pédagogiques

Ce projet m’a permis de :

- Créer une API REST avec FastAPI
- Interagir avec une base SQL (SQLite/PostgreSQL)
- Utiliser SQLAlchemy pour les modèles ORM
- Documenter l’API avec Swagger et Redoc
- Préparer le projet pour un déploiement avec Docker

---

## Cas d’usage

- Intégration dans un dashboard Streamlit
- Formation à l’utilisation d’API dans un notebook Jupyter
- Création de microservices de Data Science
- Démonstration dans un portfolio ou entretien technique

---

## Contribuer

Les contributions sont bienvenues :

- Nouveaux endpoints (recommandation, filtrage par date, etc.)
- Tests automatisés
- Optimisation des requêtes
- Déploiement Dockerisé sur le cloud

---

## Ressources utiles

- MovieLens dataset : https://grouplens.org/datasets/movielens/
- Swagger UI : http://localhost:8000/docs
- Redoc : http://localhost:8000/redoc

---

## Déploiement et SDK

- Hébergement Cloud : [*Sur Render*](https://film-api-3i06.onrender.com)
- SDK Python : *à venir*

---

## Auteur

Développé par **Ulrich Boris NIADA**  
[LinkedIn](https://www.linkedin.com/in/ulrich-boris-niada-825a25226)  
Étudiant en Data Science, Big Data et Intelligence Artificielle

---

## Licence

Ce projet est libre d'utilisation à des fins pédagogiques. Aucun droit exclusif n'est revendiqué.
