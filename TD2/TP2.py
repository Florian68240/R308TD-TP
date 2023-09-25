class Personnage:
    def __init__(self, pseudo, niveau=1):
        self.pseudo = pseudo
        self.niveau = niveau
        self.points_de_vie = niveau
        self.initiative = niveau

    def attaque(self, autre_personnage):
        degats = self.degats()
        autre_personnage.points_de_vie -= degats

        print(f"{self.pseudo} attaque et inflige {degats} dégâts à {autre_personnage.pseudo}")

    def combat(self, autre_personnage):
        while self.points_de_vie > 0 and autre_personnage.points_de_vie > 0:
            self.attaque(autre_personnage)
            print(f"{self.pseudo}: Points de vie restants = {self.points_de_vie}")
            print(f"{autre_personnage.pseudo}: Points de vie restants = {autre_personnage.points_de_vie}")

    def soigner(self):
        self.points_de_vie = self.niveau

    def degats(self):
        return self.niveau


class Guerrier(Personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau)
        self.points_de_vie = niveau * 8 + 4
        self.initiative = niveau * 4 + 6

    def degats(self):
        return self.niveau ** 2


class Mage(Personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau)
        self.points_de_vie = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.mana = niveau * 5

    def degats(self):
        if self.mana >= 4:
            self.mana -= 4
            return self.niveau + 3
        else:
            return self.niveau

    def attaque(self, autre_personnage):
        degats_mage = self.degats()
        degats_autre_personnage = autre_personnage.degats()

        autre_personnage.points_de_vie -= degats_mage
        self.points_de_vie -= degats_autre_personnage

        print(f"{self.pseudo} attaque et inflige {degats_mage} dégâts à {autre_personnage.pseudo}")
        print(f"{autre_personnage.pseudo} attaque et inflige {degats_autre_personnage} dégâts à {self.pseudo}")


class Joueur:
    def __init__(self, nom, nombre_max_personnages):
        self.nom = nom
        self.nombre_max_personnages = nombre_max_personnages
        self.personnages = []

    def ajouter_personnage(self, personnage):
        if len(self.personnages) < self.nombre_max_personnages:
            self.personnages.append(personnage)
            print(f"{personnage.pseudo} a été ajouté à la liste des personnages de {self.nom}.")
        else:
            print(f"Impossible d'ajouter {personnage.pseudo}. Le nombre maximum de personnages est atteint.")

    def get_personnage_par_numero(self, numero):
        if 1 <= numero <= len(self.personnages):
            return self.personnages[numero - 1]
        else:
            return None

    def get_personnage_par_pseudo(self, pseudo):
        for personnage in self.personnages:
            if personnage.pseudo == pseudo:
                return personnage
        return None

    def eliminer_personnage_par_numero(self, numero):
        personnage = self.get_personnage_par_numero(numero)
        if personnage:
            self.personnages.remove(personnage)
            print(f"{personnage.pseudo} a été éliminé de la liste des personnages de {self.nom}.")
        else:
            print(f"Aucun personnage trouvé avec le numéro {numero}.")

    def eliminer_personnage_par_pseudo(self, pseudo):
        personnage = self.get_personnage_par_pseudo(pseudo)
        if personnage:
            self.personnages.remove(personnage)
            print(f"{personnage.pseudo} a été éliminé de la liste des personnages de {self.nom}.")
        else:
            print(f"Aucun personnage trouvé avec le pseudo {pseudo}.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création de deux personnages
    joueur1 = Joueur("Joueur 1", nombre_max_personnages=3)

    personnage1 = Personnage("Guerrier", niveau=3)
    personnage2 = Guerrier("Guerrier 2", niveau=2)
    personnage3 = Mage("Mage 1", niveau=3)

    # Ajout des personnages au joueur
    joueur1.ajouter_personnage(personnage1)
    joueur1.ajouter_personnage(personnage2)
    joueur1.ajouter_personnage(personnage3)

    # Combat entre les personnages
    joueur1.get_personnage_par_numero(1).combat(joueur1.get_personnage_par_numero(2))

    # Soigner un personnage
    joueur1.get_personnage_par_pseudo("Guerrier").soigner()
    print(f"{joueur1.get_personnage_par_pseudo('Guerrier').pseudo} a été soigné.")

    # Élimination d'un personnage
    joueur1.eliminer_personnage_par_pseudo("Mage 1")
"""
-------------------------------------
|         Class Guerrier           |
-------------------------------------
| - pseudo: str                     |
| - niveau: int                     |
| - points_de_vie: int              |
| - initiative: int                 |
-------------------------------------
| + Guerrier(ps : String):|
| + Guerrier(ps : String, niveau: Int) :|
| + soin():                         |
| + degats(): Int                   |
-------------------------------------

-------------------------------------
|           Class Mage             |
-------------------------------------
| - pseudo: str                     |
| - niveau: int                     |
| - points_de_vie: int              |
| - initiative: int                 |
| - mana: int                       |
-------------------------------------
| + Mage(ps :String):               |
| + Mage(ps :String), niveau: Int) :|
| + soin():                         |
| + degats(): Int                   |
-------------------------------------


-------------------------------------
|         Class Joueur             |
-------------------------------------
| - nom: str                        |
| - liste_personnages: Personnage[] |
| - personnages: List[Personnage]   |
-------------------------------------
| + Joueur(nom: String):      |
| + Joueur(nom: String, maximum : Int):
| + Joueur(nom: String, liste_p : Personnage[]) |
| + Joueur(nom: String, liste_p : Personnage[], maximum : Int
| + ajouter_Personnage(p: Personnage ):     |
| + rechercher_Personnage(Id: Int): Personnage |
| + rechercher_Personnage(p:Personnage): Personnage 
| + rechercher_Personnage(nom : String): Personnage  |
| + effacer_Personnage(id: int)    |
| + effacer_Personnage(nom : String)      |
| + effacer_Personnage(p : Personnage):    |
-------------------------------------


-------------------------------------
|         Class Personnage         |
-------------------------------------
| - pseudo: str                     |
| - niveau: int                     |
| - points_de_vie: int              |
| - initiative: int                 |
-------------------------------------
| + Personnage(ps : string)          |
| + Personnage(ps : string), niveau : Int): |
| + attaque(opposant: Personnage)    |
| + combat(opposant: Personnage)     |
| + soigner()                        |
| + degats(): int                    |
-------------------------------------
"""