import sqlite3
from prettytable import *


# creation et connection à la base de donnée
conn = sqlite3.Connection('./db/crudDB.db')
cursor = conn.cursor()
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


# affichage des utilisateurs
with conn:
    cursor.execute("""SELECT username, fullname FROM users""")
    tab = from_db_cursor(cursor) 
print(tab)

print(' ')
print("Merci d'avoir utilisé notre programme ")



