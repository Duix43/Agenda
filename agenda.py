from fonctions import *

def main():
    termine=False
    while not termine:
        print("""
        1.Ajouter un contact
        2.Supprimer un contact
        3.Modifier un contact
        4.Trouver un contact
        5.Sortir du programme
        """)
        utilisateur=input("Entrer une commande: ")
        if utilisateur=="1":
            message=ajouter_contact()
            print(message)
        elif utilisateur=="2":
            nom_contact=input("Entrer le nom du contact: ")
            message=supprimer_contact(nom_input=nom_contact)
            print(message)
        elif utilisateur=="3":
            message=modifier_contact()
            print(message)
        elif utilisateur=="4":
            nom_contact=input("Entrer le nom du contact: ")
            message=trouver_contact(nom_input=nom_contact)
            print(message)
        elif utilisateur=="5":
            termine=True
        else:
            print("La commande est invalide")
            
main()