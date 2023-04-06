from Rectangle import *

longueur = int(input("Entrez votre longueur"))
largeur = int(input("Entrez votre largeur"))

rectangle = Rectangle(longueur,largeur)
print(rectangle.surface())