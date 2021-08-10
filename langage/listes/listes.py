"""
Etude des listes en python
Nous montrerons comment utiliser les listes en python
- Création
- Parcours
"""

# Création d'une liste d'une liste vide avec []
fruits = []

# Affichage de la liste
print(fruits)

# Création d'une liste de 5 produits
produits = ['Gel douche','Savon curcuma', 'HE de menthes','HE de pomme','Crème rondeur']

# Affichage de la liste
print(produits)

# Les méthodes appliquées aux listes

# Ajoute un élement à la fin de la liste
#produits.append('Savon de bébé')
# Equivaut à
produits[len(produits):] = ['Savon de bébé'] 

# Affichage de la liste
print(produits)


