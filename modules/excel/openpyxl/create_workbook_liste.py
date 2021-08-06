"""
Ce script créé un fichier Excel avec le module openpyxl
et rempli la colonne A1 avec les élements de la liste donnée.
"""
from openpyxl import Workbook

# liste des fruits
fruits=['Banane','Mangue','Orange','Goyave']

# creation du classeur excel
wb=Workbook()

# creation de la feuille
sheet=wb.create_sheet("Fruit")

# compteur de ligne
row = 0

# parcours de la liste des fruits
for indexf in range(len(fruits)):
    row = row + 1 

    # ecriture dans les cellules
    sheet.cell(row,1,fruits[indexf])

# sauvegarde du fichier
wb.save('Fruits.xlsx')



