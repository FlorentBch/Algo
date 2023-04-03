"""
Romain :

Ecrir un script qui permet de saisir un entier 
entre 1 et 3999
(pourquoi cette limitation ?).


Le script doit permettre de l'afficher en 
chiffre romain.

En bonus : le convertisseur inverse
"""



while Nombre<1 or Nombre>3999:
    Nombre = int(input("Entrez un chiffre entre 1 et 3999"))
    
Chiffre = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

