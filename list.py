
# #Exemple

# livres = ["Les trois mousquetaires", "Roméo & Juliette", \
#           "l'Avare","La chanson de Roland", "Les fleurs du mal"]
# print(livres)
# print(livres[4])

# #Exercices 1

# couleurs = ["bleu", "rouge", "vert", "jaune", "vert"] #Liste de couleurs
# print(couleurs)

# print(couleurs[3]) #N'affiche que le 4e élément de la liste

# couleurs.append("rose") #Rajoute un mot dans la liste à la fin
# couleurs.remove("bleu") #Retire l'élement de la liste en fonction de son nom
# couleurs.pop(0) #Retire l'élément de la liste en fonction de sa position

# print(couleurs)

# lenght_liste = len(couleurs) #Donne la longueur de la liste
# print(lenght_liste)

# index = couleurs.index("jaune") #Donne la position de mon élément dans la liste
# print(index)

# count = couleurs.count("vert") #Compte le nombre de fois que le même élément est présent dans la liste
# print(count)

# #Exercice 2

# sentence_list = ["Tableau", "Chaise", "Stylo"]
# sentence_string = " ".join(sentence_list) #Transforme la liste en string en choisissant le séparateur
# print(sentence_list)
# print(sentence_string)

# new_list = sentence_string.split(" ") #"Split" le string en liste en précisant le séparateur
# print(new_list)

# sentence_to_split = "Aujourd'hui j'ai mangé une pomme"
# print(sentence_to_split.split(" "))

# #Exercice 3

les_copains = ["Zoé", "Nico", "Aaron", "Marie"]
# print(les_copains)

# sans_Aaron = les_copains.remove("Aaron")
# longueur_list = len(les_copains)
# print(longueur_list)
# print(les_copains)

# les_copains.append("Simon")
# print(les_copains)

# list_index = les_copains.index("Nico")
# print(list_index)

# les_copains.append("Simon")
# count_Simon = les_copains.count("Simon")
# print(les_copains)
# print(count_Simon)

# sentence_test = "J'aime beaucoup mes copains"
# sentence_split = sentence_test.split(" ")
# print(sentence_split)

# sentence_string_again = " ".join(sentence_split) 
# print(sentence_string_again)

# #Exercice 4

# for i in les_copains:
#     if i == "Nico":
#         print("Nico est là ihi!")
#     else :
#         continue

# #Dictionnaire

# dictionnary = {
#     "color" : "red",
#     "name" : "Jim",
#     "number" :1994
# }
# print(dictionnary)
# print(dictionnary["color"])

# dictionnary["color"]="blue" 
# print(dictionnary["color"])

# #Exercice 1

# identity_car = {
#     "Brand" : "Skoda",
#     "Model" : "Fabia",
#     "Fuel" : "Essence",
#     "Year" : 2017,
#     "Doors" : 5
# }

# identity_car["Model"]="Fabia Combi"
# print(identity_car["Model"])

#Exercice 2 

employees = {
    "boss":{"name":"Noe", "salary" : 3000},
    "accountant":{"name":"Zoe", "salary" : 2600},
    "intern":{"name":"Simon", "salary" : 2300} 
}

employees["accountant"]["salary"]=2800

print(employees["accountant"]["salary"])
