"""
+-------------------+
| Point |
+-------------------+
| - x: float |
| - y: float |
+-------------------+
| + Point() |
| + Point(x: float, y: float) |
| + distance(x: float, y: float): float |
| + distance(p = Point): float |
+-------------------+
"""
import math
#Classe Point
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def __str__(self):
        distance1 = self.distance(1, 1)
        distance2 = self.distance_to(Point(3, 4))
        return f"Distance entre point1 et (1, 1) : {distance1}, Distance entre point1 et point2 : {distance2}"
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self, new_x):
        self.__x = new_x
    def set_y(self, new_y):
        self.__y = new_y
    def distance(self, a, b):
        delta_x = self.__x - a
        delta_y = self.__y - b
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def distance_to(self, other_point):
        delta_x = self.__x - other_point.get_x()
        delta_y = self.__y - other_point.get_y()
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

# Exemple d'utilisation de la classe Point
point1 = Point()  # Utilisation du constructeur par défaut (0, 0)
point2 = Point(3, 4)  # Utilisation du second constructeur (3, 4)

distance1 = point1.distance(1, 1)  # Calcule la distance entre point1 et (1, 1)
distance2 = point1.distance_to(point2)  # Calcule la distance entre point1 et point2

print("Distance entre point1 et (1, 1) :", distance1)
print("Distance entre point1 et point2 :", distance2)
print(point1)  # Affiche les distances à l'aide de la méthode __str__

print("------------------------------------")
"""
+-------------------+
| Cercle |
+-------------------+
| - centre: Point |
| - rayon: float |
+-------------------+
| + Cercle(rayon: float) |
| + Cercle(centre: Point, rayon: float) |
| + diametre(): float |
| + perimetre(): float |
| + surface(): float |
| + intersection_autre_cercle(autre_cercle: Cercle): bool |
| + point_dans_cercle(point: Point): bool |
+-------------------+
"""
#Classe cercle
class Cercle:
    def __init__(self, centre=None, rayon=0):
        if centre is None:
            centre = Point()
        self.__centre = centre
        self.__rayon = rayon

    # Getter pour le rayon
    def get_rayon(self):
        return self.__rayon

    # Setter pour le rayon
    def set_rayon(self, new_rayon):
        self.__rayon = new_rayon

    # Getter pour le centre
    def get_centre(self):
        return self.__centre

    # Setter pour le centre
    def set_centre(self, new_centre):
        self.__centre = new_centre

    def diametre(self):
        return 2 * self.get_rayon()

    def perimetre(self):
        return 2 * math.pi * self.get_rayon()

    def surface(self):
        return math.pi * self.get_rayon() ** 2

    def intersection_autre_cercle(self, autre_cercle):
        distance_centres = self.get_centre().distance_to(autre_cercle.get_centre())
        return distance_centres <= self.get_rayon() + autre_cercle.get_rayon()

    def point_dans_cercle(self, point):
        distance_centre_point = self.get_centre().distance_to(point)
        return distance_centre_point <= self.get_rayon()

# Exemple d'utilisation de la classe Cercle
point1 = Point(0, 0)
cercle1 = Cercle(point1, 5)
cercle2 = Cercle(Point(3, 4), 3)

print("Diamètre de cercle1 :", cercle1.diametre())
print("Périmètre de cercle1 :", cercle1.perimetre())
print("Surface de cercle1 :", cercle1.surface())

if cercle1.intersection_autre_cercle(cercle2):
    print("Les cercles sont en intersection.")
else:
    print("Les cercles ne sont pas en intersection.")

point_test = Point(2, 2)
if cercle1.point_dans_cercle(point_test):
    print("Le point_test est à l'intérieur de cercle1.")
else:
    print("Le point_test n'est pas à l'intérieur de cercle1.")

print("------------------------------------")
"""
  +-----------------------+
  |       Rectangle      |
  +-----------------------+
  | - bas_gauche: Point  |
  | - longueur: float    |
  | - hauteur: float     |
  +-----------------------+
  | + Rectangle()                      |
  | + Rectangle(longueur: float, hauteur: float) |
  | + Rectangle(bas_gauche: Point, haut_droit: Point) |
  | + surface(): float |
  | + perimetre(): float |
  | + position_bas_gauche(): Point |
  | + position_bas_droit(): Point |
  | + position_haut_gauche(): Point |
  | + position_haut_droit(): Point |
  | + point_dans_rectangle(point: Point): bool |
  +-----------------------+
"""
#Classe Rectangle
class Rectangle:
    def __init__(self, bas_gauche=Point(), longueur=1, hauteur=1):
        self.__bas_gauche = bas_gauche
        self.__longueur = longueur
        self.__hauteur = hauteur

    def surface(self):
        return self.__longueur * self.__hauteur

    def perimetre(self):
        return 2 * (self.__longueur + self.__hauteur)

    # Getters pour la position du bas gauche
    def get_position_bas_gauche(self):
        return self.__bas_gauche

    # Getter pour la position du bas droit
    def get_position_bas_droit(self):
        return Point(self.__bas_gauche.get_x() + self.__longueur, self.__bas_gauche.get_y())

    # Getter pour la position du haut gauche
    def get_position_haut_gauche(self):
        return Point(self.__bas_gauche.get_x(), self.__bas_gauche.get_y() + self.__hauteur)

    # Getter pour la position du haut droit
    def get_position_haut_droit(self):
        return Point(self.__bas_gauche.get_x() + self.__longueur, self.__bas_gauche.get_y() + self.__hauteur)

    def point_dans_rectangle(self, point):
        return (self.__bas_gauche.get_x() <= point.get_x() <= self.__bas_gauche.get_x() + self.__longueur) and \
               (self.__bas_gauche.get_y() <= point.get_y() <= self.__bas_gauche.get_y() + self.__hauteur)

# Exemple d'utilisation de la classe Rectangle
point_bas_gauche = Point(0, 0)
point_haut_droit = Point(4, 3)

rectangle = Rectangle(point_bas_gauche, 4, 3)

print("Surface du rectangle :", rectangle.surface())
print("Périmètre du rectangle :", rectangle.perimetre())

point_test = Point(2, 2)
if rectangle.point_dans_rectangle(point_test):
    print("Le point_test est situé dans le rectangle.")
else:
    print("Le point_test n'est pas situé dans le rectangle.")

print("------------------------------------")

"""
  +-----------------------+
  |   TriangleRectangle  |
  +-----------------------+
  | - cote1: float       |
  | - cote2: float       |
  | - angle_droit: Point|
  +-----------------------+
  | + TriangleRectangle(cote1: float, cote2: float) |
  | + TriangleRectangle(cote1: float, cote2: float, angle_droit: Point) |
  | + hypothenuse(): float |
  | + perimetre(): float |
  | + surface(): float |
  | + est_isocèle(): bool |
  +-----------------------+

"""
# Classe TriangleRectangle
class TriangleRectangle:
    def __init__(self, cote1, cote2, angle_droit=Point()):
        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__angle_droit = angle_droit

    def hypothenuse(self):
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    def perimetre(self):
        return self.__cote1 + self.__cote2 + self.hypothenuse()

    def surface(self):
        return 0.5 * self.__cote1 * self.__cote2

    def est_isocèle(self):
        return self.__cote1 == self.__cote2

    # Getters pour les côtés et l'angle droit
    def get_cote1(self):
        return self.__cote1

    def get_cote2(self):
        return self.__cote2

    def get_angle_droit(self):
        return self.__angle_droit

# Exemple d'utilisation de la classe TriangleRectangle
point_angle_droit = Point(0, 0)
triangle1 = TriangleRectangle(3, 4)  # Utilisation du premier constructeur
triangle2 = TriangleRectangle(5, 12, point_angle_droit)  # Utilisation du second constructeur

print("Longueur de l'hypothénuse de triangle1 :", triangle1.hypothenuse())
print("Périmètre de triangle2 :", triangle2.perimetre())
print("Surface de triangle1 :", triangle1.surface())

if triangle1.est_isocèle():
    print("triangle1 est isocèle.")
else:
    print("triangle1 n'est pas isocèle.")

# Accéder aux attributs privés
print("Côté 1 de triangle1 :", triangle1.get_cote1())
print("Côté 2 de triangle1 :", triangle1.get_cote2())
print("Angle droit de triangle2 :", triangle2.get_angle_droit().get_x(), triangle2.get_angle_droit().get_y())