# Ceci est un client de test pour l'API FastAPI, utilisant httpx pour les requêtes HTTP.

# %%
import httpx

# %%
# La liste de 5 films
response = httpx.get("http://127.0.0.1:8000/movies", params={"limit": 5})

# %%
type(response)

# %%

response.json()
# %%

httpx.get("http://127.0.0.1:8000/movies/4").json()

# %%

httpx.get("http://127.0.0.1:8000/analytics").json()

# %%
