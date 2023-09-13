 # Attribut de classe
    matiere = "céramique"

    # Méthode d'initialisation
    def init(self, couleur, contenance_ml, marque):
        self.couleur = couleur
        self.contenance_ml = contenance_ml
        self.marque = marque
        self.contenu = None

    # Méthode pour définir le contenu de la tasse
    def remplir(self, boisson):
        self.contenu = boisson

    # Méthode pour boire la boisson dans la tasse
    def boire(self):
        if self.contenu is not None:
            boisson = self.contenu
            self.contenu = None
            print(f"La boisson ({boisson}) a été bue.")
        else:
            print("La tasse est vide.")

    # Méthode spéciale pour afficher la description de la tasse
    def str(self):
        description = f"La tasse de matière {Tasse.matiere}, de couleur {self.couleur} et de marque {self.marque} "
        if self.contenu is not None:
            description += f"a une contenance de {self.contenance_ml} ml et contient {self.contenu}."
        else:
            description += f"a une contenance de {self.contenance_ml} ml et est vide."
            return description


# Exemple d'utilisation de la classe Tasse
ma_tasse = Tasse("bleu", 50, "Duralex")
print(ma_tasse)  # Affiche la description initiale de la tasse

ma_tasse.remplir("café")
print(ma_tasse)  # Affiche la description de la tasse avec le contenu

ma_tasse.boire()
print(ma_tasse)  # Affiche la description de la tasse après avoir bu la boisson