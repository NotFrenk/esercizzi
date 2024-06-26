### CLASSI GENERE
# Si creino tre classi chiamate Azione, Commedia e Drama, tutte derivanti dalla classe Film. 
# Ognuna di queste classi ha un attributo privato di tipo string chiamato genere, 
# che equivale al genere di film (genere="Azione", nella classe Azione) 
# ed un attributo privato di tipo float chiamato penale.
# I film di azione hanno una penalità di 3 euro al giorno, le commedie hanno una penale di 2.50 euro al giorno, 
# i film drammatici hanno una penale di 2 euro al giorno.

# - Per ognuna di queste classi si implementi un metodo chiamato:
# getGenere(), che ritorna il genere di film

# getPenale(), che ritorna il valore della penale

# calcolaPenaleRitardo(), 
# che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.

from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.genere = 'Azione'
        self.penale:float = 3.0

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, giorni_di_ritardo:int):
        return giorni_di_ritardo * self.penale

    
class Commedia(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.genere = 'Commedia'
        self.penale:float = 2.50

    def getGenere(self):
        return self.genere
    
    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, giorni_di_ritardo:int):
        return giorni_di_ritardo * self.penale

class Drama(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.genere = 'Drama'
        self.penale:float = 2

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale

    def calcolaPenaleRitardo(self, giorni_di_ritardo:int):
        return giorni_di_ritardo * self.penale
