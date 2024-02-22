def ajouter_contact()->str:
    nom_input=input("Entrer un le nom du contact: ")
    lire_fichier=open("agenda.txt","r")
    liste_contact=lire_fichier.readlines()
    for contact in liste_contact:
        if contact!="":
            infos=contact.split(": ")
            nom, _=infos
            if nom==nom_input:
                lire_fichier.close()
                return "Ce contact existe déjà"
    lire_fichier.close()
    numero_input=input("Entrer le numero du contact: ")
    ajouter_fichier=open("agenda.txt","a")
    ajouter_fichier.write(f"{nom_input}: {numero_input}\n")    
    ajouter_fichier.close()
    return "Votre contact a été créer"

def supprimer_contact(nom_input:str)->str:
    lire_fichier=open("agenda.txt","r")
    contenu=lire_fichier.read()
    liste_contact=contenu.split("\n")
    for indice in range(len(liste_contact)-1):
        infos=liste_contact[indice].split(": ")
        nom, _=infos
        if nom==nom_input:
            liste_contact.pop(indice)
            lire_fichier.close()
            ecrire_fichier=open("agenda.txt","w")
            for contact in liste_contact:
                if contact != "":
                    ecrire_fichier.write(contact+"\n")
            ecrire_fichier.close()
            return "Le contact a été supprimé"
    lire_fichier.close()
    return "Le contact n'a pas été trouvé"        

def modifier_contact():
    nom_input=input("Entrer le contact que vous voulez modifier: ")
    lire_fichier=open("agenda.txt","r")
    liste_contact=lire_fichier.readlines()
    for indice in range(len(liste_contact)):
        infos=liste_contact[indice].split(": ")
        nom, _=infos
        if nom==nom_input:
            numero_input=input("Entrer le nouveau numéro de téléphone: ")
            liste_contact[indice]=f"{nom_input}: {numero_input}\n"
            lire_fichier.close()
            ecrire_fichier=open("agenda.txt","w")
            for contact in liste_contact:
                if contact!="":
                    ecrire_fichier.write(contact) 
            ecrire_fichier.close()
            return "Le contact a été modifier avec succés"
    lire_fichier.close()
    return "Le contact n'a pas été trouvé"


def trouver_contact(nom_input:str)->str:
    fichier=open("agenda.txt","r")
    liste_contact=fichier.readlines()
    fichier.close()
    for contact in liste_contact:
        nouveau_contact=contact.replace("\n","")
        infos=nouveau_contact.split(": ")
        nom,numero=infos
        if nom == nom_input:
            return numero
    return "Le contact n'a pas été trouvé"