"""
Bonjour nous allons créer un dictionnaire python qui
permettra de stocker les utilisateurs de notre programme
si un utilisteur n'est pas inscrit alors il n'aura pas
droit à la suite de notre programme.
"""

# Connexion au programme avec son identifiant et son mot de passe
identifiant = input('Veuillez saisir votre identifiant :')
print("Identifiant: "+identifiant)
password = input('Veuillez saisir votre mot de passe :')

# Création du dictionnaire
users = {}
print(users)
# Teste si l'identifiant et le mot de passe sont présent dans le dictionnaire
if (identifiant in users) and (password in users.values()):
    for k, v in users.items():
        if (k == identifiant and v == password):
            print ('vous aurez le programme')
        else:
            print ("vous n'aurez pas droit au programme ")

else:
    yesOrNo=input("Vous n'êtes pas encore inscrit, voulez-vous inscrire ? (tapez O pour continue ou N pour mettre fin) :")

    if (yesOrNo == 'o' or yesOrNo =='oui' or yesOrNo =='OUI' or yesOrNo =='Oui' or yesOrNo =='O'):

        users.update({identifiant:password})
        #users[identifiant]=password
    
    
