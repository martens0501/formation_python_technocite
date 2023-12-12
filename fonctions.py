# Exercice 1

# def moyenne(n1,n2):
#     x = ((n1 + n2)/2)
#     return x

# f=moyenne(2,6)
# print(f)

# Exercice 2

# age = int(input("Quel est ton âge ? \n"))
# x = 5

# def ajouter_x(age):
#     age = age + x
#     return age

# f=ajouter_x(age)
# print("Dans " + str(x) + " années tu auras " + str(f) + " ans")

# Exercice 3

# def identity(name, naissance):
#     age = 2050 - naissance
#     print(name + ", en 2050 tu auras " + str(age) + " ans.")


# identity("Zoé", 1997)

# Exercice 4

# def TVA(PrixAchat1,PrixAchat2):
#     TVA1 = PrixAchat1*0.21
#     print(TVA1)
#     TVA2 = PrixAchat2*0.21
#     print(TVA2)
#     TVAtot = TVA1 + TVA2
#     print(TVAtot)

# TVA(5,3)

#   => Correction

# achat1 = 500
# achat2 = 1426


# def calcul_tva(full_price):
#     tva = full_price*0.21
#     return tva


# tva_achat1 = calcul_tva(achat1)
# tva_achat2 = calcul_tva(achat2)

# sum_TVA = tva_achat1 + tva_achat2

# print(f"la première TVA est de {tva_achat1} €")
# print(f"la seconde TVA est de {tva_achat2} €")
# print(f"la somme des deux TVA est de {sum_TVA} €")

# #Exercice supplémentaire 1

# word = "ordinateur"

# def inverse_word(string):
#     reverse ="".join(reversed(string))
#     return reverse

# reverse_ordi = inverse_word(word)
# print(reverse_ordi)

# #Exercice supplémentaire 2 (Enlever les "e" du mot "exercice")

# mot = "exercice"
# mot_sans_e = mot.replace("e", "")
# print(mot_sans_e)

# OR

# def remove_one_character(word,char):
#     return word.replace(char,"")

# print(remove_one_character("exercice", "e"))

# #Solution Noémie

# def remove_one_character(word, char):
#     list_word = list(word)
#     for i in list_word:
#         if i == char:
#             list_word.remove(i)
#     return "".join(list_word)

# print(remove_one_character("exercice", "e"))

#Exercice supplémentaire 3

# #Solution Noémie

# alphabet =["a","b","c","d","d","e","f","g","h","j","k","l", \
#            "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# def check_alphabet(word):
#     for letter in alphabet:
#         if letter not in word: 
#             return False
#     return True
        
# word_test =  "chaise"
# is_in_alphabet=check_alphabet(word_test)

# if is_in_alphabet:
#     print("Le mot contient toutes les lettres de l'alphabet")
# else:
#     print("Le mot ne contient pas toutes les lettres de l'alphabet")

# #Solution Chat GPT

# import string

# def contient_toutes_lettres_alphabet(chaine):
#     alphabet = set(string.ascii_lowercase)
#     return set(chaine.lower()) >= alphabet

# string_test = "Anticonstitutionnellement"
# resultat = contient_toutes_lettres_alphabet(string_test)

# if resultat:
#     print("La chaîne contient toutes les lettres de l'alphabet.")
# else:
#     print("La chaîne ne contient pas toutes les lettres de l'alphabet.")
 