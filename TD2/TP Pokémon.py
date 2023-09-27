class Pokémon:
    def __init__(self, nom, poids, taille):
        self.nom = nom
        self.poids = poids
        self.taille = taille

    def __str__(self):
        return f"Je suis le Pokémon {self.nom} mon poids est de {self.poids} kg, ma taille est de {self.taille}m"


class PokémonSportif(Pokémon):
    def __init__(self, nom, poids, taille, nombre_pattes, taille_pattes, freq_cardiaque):
        super().__init__(nom, poids, taille)
        self.nombre_pattes = nombre_pattes
        self.vitesse = nombre_pattes * taille_pattes * 3
        self.freq_cardiaque = freq_cardiaque

    def __str__(self):
        return f"Je suis le Pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.vitesse} km/h j'ai {self.nombre_pattes} pattes, ma taille est de {self.taille}m ma fréquence cardiaque est de {self.freq_cardiaque} pulsations à la minute"


class PokémonCasanier(Pokémon):
    def __init__(self, nom, poids, taille, heures_tv):
        super().__init__(nom, poids, taille)
        self.heures_tv = heures_tv

    def __str__(self):
        return f"Je suis le Pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.heures_tv * 3} km/h j'ai 2 pattes, ma taille est de {self.taille}m je regarde la télé {self.heures_tv}h par jour"


class PokémonMer(Pokémon):
    def __init__(self, nom, poids, nombre_nageoires):
        super().__init__(nom, poids, 0)  # La taille des Pokémon de mer est mise à 0 car ils ne se déplacent que dans l'eau.
        self.nombre_nageoires = nombre_nageoires

    def __str__(self):
        return f"Je suis le Pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.poids / 25} km/h j'ai {self.nombre_nageoires} nageoires"


class PokémonCroisiere(PokémonMer):
    def __init__(self, nom, poids, nombre_nageoires):
        super().__init__(nom, poids, nombre_nageoires)

    def __str__(self):
        return f"Je suis le Pokémon {self.nom} mon poids est de {self.poids} kg, ma vitesse est de {self.poids / 25 * self.nombre_nageoires / 2} km/h j'ai {self.nombre_nageoires} nageoires"


# Création d'un tableau de Pokémon
pokemons = [
    PokémonSportif("Pikachu", 18, 0.85, 2, 0.3, 120),
    PokémonCasanier("Salameche", 12, 0.65, 8),
    PokémonMer("Rondoudou", 45, 2),
    PokémonCroisiere("Bulbizarre", 15, 3)
]

# Affichage des Pokémon à l'aide d'une boucle for
for pokemon in pokemons:
    print(pokemon)
