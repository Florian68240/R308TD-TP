class Personnage:
    def __init__(self, pseudo, niveau=1):
        self.pseudo = pseudo
        self.niveau = niveau
        self.points_de_vie = niveau
        self.initiative = niveau

    def attaque(self, autre_personnage):
        if self.initiative > autre_personnage.initiative:
            autre_personnage.points_de_vie -= self.niveau
            if autre_personnage.points_de_vie > 0:
                self.points_de_vie -= autre_personnage.niveau
        elif self.initiative < autre_personnage.initiative:
            self.points_de_vie -= autre_personnage.niveau
            if self.points_de_vie > 0:
                autre_personnage.points_de_vie -= self.niveau
        else:
            autre_personnage.points_de_vie -= self.niveau
            self.points_de_vie -= autre_personnage.niveau

    def combat(self, autre_personnage):
        while self.points_de_vie > 0 and autre_personnage.points_de_vie > 0:
            self.attaque(autre_personnage)
            if autre_personnage.points_de_vie <= 0:
                print(f"{autre_personnage.pseudo} a été vaincu par {self.pseudo}!")
            elif self.points_de_vie <= 0:
                print(f"{self.pseudo} a été vaincu par {autre_personnage.pseudo}!")

    def soigner(self):
        self.points_de_vie = self.niveau

# Test de la classe
if __name__ == "__main__":
    joueur1 = Personnage("Joueur1", 3)
    joueur2 = Personnage("Joueur2", 2)

    print(f"{joueur1.pseudo} (Niveau {joueur1.niveau}) vs {joueur2.pseudo} (Niveau {joueur2.niveau})")

    joueur1.combat(joueur2)

    # Soigner le joueur1 après le combat
    joueur1.soigner()
    print(f"{joueur1.pseudo} a été soigné et a maintenant {joueur1.points_de_vie} points de vie.")