"""
+-------------------+
| Point |
+-------------------+
| - x: double |
| - y: double |
+-------------------+
| + Point() |
| + Point(a: double, b: double) |
| + distance(a: double, b: double): double |
| + distance(camarade: Point): double |
+-------------------+
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, a, b):
        delta_x = self.x - a
        delta_y = self.y - b
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def distance_to(self, other_point):
        delta_x = self.x - other_point.x
        delta_y = self.y - other_point.y
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

# Exemple d'utilisation de la classe Point
point1 = Point()  # Utilisation du constructeur par défaut (0, 0)
point2 = Point(3, 4)  # Utilisation du second constructeur (3, 4)

distance1 = point1.distance(1, 1)  # Calcule la distance entre point1 et (1, 1)
distance2 = point1.distance_to(point2)  # Calcule la distance entre point1 et point2
print("------------------------------------")
print("Distance entre point1 et (1, 1) :", distance1)
print("Distance entre point1 et point2 :", distance2)


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

import math

class Cercle:
    def __init__(self, rayon=0):
        self.centre = Point()
        self.rayon = rayon

    def __init__(self, centre, rayon):
        self.centre = centre
        self.rayon = rayon

    def diametre(self):
        return 2 * self.rayon

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def intersection_autre_cercle(self, autre_cercle):
        distance_centres = self.centre.distance_to(autre_cercle.centre)
        return distance_centres <= self.rayon + autre_cercle.rayon

    def point_dans_cercle(self, point):
        distance_centre_point = self.centre.distance_to(point)
        return distance_centre_point <= self.rayon

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

class Rectangle:
    def __init__(self, bas_gauche=Point(), longueur=1, hauteur=1):
        self.bas_gauche = bas_gauche
        self.longueur = longueur
        self.hauteur = hauteur

    def __init__(self, bas_gauche, haut_droit):
        self.bas_gauche = bas_gauche
        self.longueur = haut_droit.x - bas_gauche.x
        self.hauteur = haut_droit.y - bas_gauche.y

    def surface(self):
        return self.longueur * self.hauteur

    def perimetre(self):
        return 2 * (self.longueur + self.hauteur)

    def position_bas_gauche(self):
        return self.bas_gauche

    def position_bas_droit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y)

    def position_haut_gauche(self):
        return Point(self.bas_gauche.x, self.bas_gauche.y + self.hauteur)

    def position_haut_droit(self):
        return Point(self.bas_gauche.x + self.longueur, self.bas_gauche.y + self.hauteur)

    def point_dans_rectangle(self, point):
        return (self.bas_gauche.x <= point.x <= self.bas_gauche.x + self.longueur) and \
               (self.bas_gauche.y <= point.y <= self.bas_gauche.y + self.hauteur)

# Exemple d'utilisation de la classe Rectangle
point_bas_gauche = Point(0, 0)
point_haut_droit = Point(4, 3)

rectangle = Rectangle(point_bas_gauche, point_haut_droit)

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
import math

class TriangleRectangle:
    def __init__(self, cote1, cote2, angle_droit=Point()):
        self.cote1 = cote1
        self.cote2 = cote2
        self.angle_droit = angle_droit

    def hypothenuse(self):
        return math.sqrt(self.cote1 ** 2 + self.cote2 ** 2)

    def perimetre(self):
        return self.cote1 + self.cote2 + self.hypothenuse()

    def surface(self):
        return 0.5 * self.cote1 * self.cote2

    def est_isocèle(self):
        return self.cote1 == self.cote2

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