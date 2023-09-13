# Définition de la fonction affiche
def affiche(chaine):
    print("texte à afficher:", chaine)

# Définition de la classe Vélo
class Velo:
    def __init__(self, marque, taille_pneu, couleur, nombre_vitesses):
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nombre_vitesses = nombre_vitesses
        self.vitesse_courante = 1

    def gear_up(self):
        if self.vitesse_courante < self.nombre_vitesses:
            self.vitesse_courante += 1
        return self.vitesse_courante

    def gear_down(self):
        if self.vitesse_courante > 1:
            self.vitesse_courante -= 1
        return self.vitesse_courante

# Fonction principale
def main():
    # (1) Définir une chaîne de caractères str1
    str1 = "Ceci est un exemple de chaîne."

    # (2) Faire appel à la fonction affiche en lui passant la chaîne str1
    affiche(str1)

    # (3) Créer une instance de Vélo nommée v1
    v1 = Velo("Giant", "26 pouces", "Bleu", 7)

    # (4) Faire appel aux méthodes gear_up et gear_down
    print("Vitesse courante de v1:", v1.vitesse_courante)
    v1.gear_up()
    print("Après avoir augmenté la vitesse de v1:", v1.vitesse_courante)
    v1.gear_down()
    print("Après avoir diminué la vitesse de v1:", v1.vitesse_courante)

# Appeler la fonction principale pour exécuter le programme
if __name__ == "__main__":
    main()