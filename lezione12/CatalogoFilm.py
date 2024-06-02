
# Catalogo Film 
# Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
# rimuovere e cercare film di un particolare regista. 
# Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

# Classe:
# - MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

#     Metodi:
#     - add_movie(director_name, movies): 
#Aggiunge uno o più film a un regista specifico nel catalogo. 
# Se il regista non esiste, viene creato un nuovo record. 
#Se il regista esiste, la sua lista di film viene aggiornata.

#     - remove_movie(director_name, movie_name): 
# Rimuove un film specifico dall'elenco dei film di un regista. 
# Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

#     - list_directors(): Elenca tutti i registi presenti nel catalogo.

#     - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

#     - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
# Restituisce un elenco dei registi e dei rispettivi film che contengono 
# la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo.

class MovieCatalog:
    def __init__(self):
        self.catalogo = {}

    def add_movie(self, director_name, movies):
        if director_name in self.catalogo:
            self.catalogo[director_name].add(movies)
        else:
            self.catalogo[director_name] = movies

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalogo:
            if movie_name in self.catalogo[director_name]:
                self.catalogo[director_name].remove(movie_name)
                print (f'{movie_name} rimosso da {director_name}')
                if not self.catalogo[director_name]:
                    del self.catalogo[director_name]
                    print (f'{director_name} è stato rimosso')
            else:
                print(f"Film '{movie_name}' non trovato per il regista '{director_name}'.")
        else:
            print(f"Regista '{director_name}' non trovato nel catalogo.")

    def list_directors(self):
        if self.catalogo:
            return list(self.catalogo.keys())
        else:
            return f'non ci sono registi '
    
    def get_movies_by_director(self, director_name):
        if director_name in self.catalogo:
            return self.catalogo[director_name]
        else:
            return f"Regista '{director_name}' non trovato nel catalogo."
        
    def search_movies_by_title(self, title):
        result = {}
        for director, movies in self.catalogo.items():
            matching_movies = []
            for movie in movies:
                if title.lower() in movie.lower():
                    matching_movies.append(movie)
            if matching_movies:
                result[director] = matching_movies

        if result:
            return result
        else:
            return f"Nessun film trovato contenente '{title}' nel titolo."
        



catalog = MovieCatalog()

# Elencare tutti i registi
print(catalog.list_directors())

# Aggiungere film
catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Django Unchained"])
catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk"])
catalog.add_movie("Steven Spielberg", ["Jurassic Park", "E.T.", "Schindler's List"])

# Elencare tutti i registi
print(catalog.list_directors())


# Rimuovere un film e potenzialmente il regista
catalog.remove_movie("Quentin Tarantino", "Kill Bill")
catalog.remove_movie("Quentin Tarantino", "Pulp Fiction")
catalog.remove_movie("Christopher Nolan", "Dunkirk")

# Elencare tutti i registi
print(catalog.list_directors())

# Ottenere tutti i film di un regista specifico
print(catalog.get_movies_by_director("Christopher Nolan"))

# Cercare film per titolo
print(catalog.search_movies_by_title("inception"))
print(catalog.search_movies_by_title("park"))


