def plus_grand_nombre():
    nombre1 = float(input('Entrez le premier nombre : '))
    nombre2 = float(input('Entrez le deuxième nombre : '))

    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "égaux"


resultat = plus_grand_nombre()
print("Le nombre le plus grand est :", resultat)

