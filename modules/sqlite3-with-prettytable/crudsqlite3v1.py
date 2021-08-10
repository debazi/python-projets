import sqlite3
from prettytable import *



# creation et connection à la base de donnée
conn = sqlite3.Connection('./db/crudDB.db')
cursor = conn.cursor()

# supprime la table users si elle existe
#cursor.execute("""DROP TABLE IF EXISTS users""")

# creation de la table utilisateur
cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    fullname TEXT,
                    password TEXT
            )"""
)
conn.commit()

# creation du formulaire de saisie
nb = 'o'
while nb != 'f':
    print('=================================')
    username = input('Nom utilisateur: ')
    fullname = input('Nom complet: ')
    password = input('Mot de passe: ')

    # liste des données et insertion dans la base de donnée
    usersData = (username, fullname, password)
    cursor.execute(
    """INSERT INTO users(username, fullname, password) VALUES (?,?,?)""",
    usersData,
    )
    conn.commit()

    print('---------------------------------')
    nb = input('Continuez la saisie? [o/f] ')

# liste des utilisateurs
cursor.execute("""SELECT username, fullname,password FROM users""")
users = cursor.fetchall()

# affichage des utilisateurs
tableau = PrettyTable()
tableau.field_names = ["Identifiant", "Nom complet", "Mot de passe"]

# parcours du tableau et affichage dans le terminal
for user in users:
    tableau.add_row(list(user))

print(tableau)


print(' ')
print("Merci d'avoir utilisé notre programme v0.2 ")



















