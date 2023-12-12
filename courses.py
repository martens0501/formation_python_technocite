# Créer une liste vide

list = []

def add_something (ajout):
    new_add=list.append(ajout)
    return new_add

def delete_something(retire):
    new_delete=list.remove(retire)
    return new_delete

while True :
    Answer = int(input("\n Que veux-tu faire ? \n \n \
    1. Ajouter un article dans la liste. \n \
    2. Retirer un article dans la liste. \n \
    3. Afficher la liste de courses. \n \
    4. Réinitialiser la liste. \n \
    5. Cloturer et afficher la liste de course. \n \n"))

    if Answer == 1 :

        add = input("\n Que veux-tu rajouter à ta liste de courses ? \n")     
        add_something(add)
        print(f"{add} a été ajouté à ta liste de courses")

    elif Answer == 2 :

        delete = input("\n Que veux-tu retirer à ta liste de courses? \n")
        delete_something(delete)
        print(f"{delete} a été supprimé de ta liste de courses")

    elif Answer == 3 :
        item_list= "\n".join(list)
        print("####################  Liste temporaire  ####################")
        print(item_list)

    elif Answer == 4 :
        double_check = input("\n Es-tu sûr de vouloir vider la liste ? \n \
    Si oui appuie sur 1. \n \
    Si non appuie sur 2. \n")

        if double_check == 1 :
            list.clear()
            print("Ta liste de courses est vide")

        elif double_check == 2:
            continue
        

    elif Answer == 5 :
        item_list= "\n".join(list)
        print("####################  Ta liste est prête!  ####################")
        print(item_list)
        break

    else:
        print("Je ne comprends pas...")
        continue
