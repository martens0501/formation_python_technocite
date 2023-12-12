# Boucle "for"

# for i in range (1,10):
#     print("Bonjour")
#     print(i)

# Exercice 1

# for i in range(5):
#     print("Au revoir")
#     print(i)

# Boucle "While"

# max = 4
# i = 0

# while(i<max)
#     print("C'est bon!")
#     i = i + 1

# Exercice 2

# max = 7
# i = 0

# while (i < max):
#     print("Hello")
#     i = i + 1 #peut aussi s'écrire i+=1

# Boucle while and for

# for i in range(5):
#     if i == 3 :
#         continue
#     print(i)

# Exercice 3

# max = 7
# i = 0

# while (i<max):
#     if i == 3 or i == 5:
#         i+=1
#         continue
#     print("Hello")
#     print(i)
#     i+=1

# OU

# for i in range(7)
#     if i == 3 or i == 5 :
#         continue
#     print("Bonjour")
#     print(i)

# While et Break

# i = 0

# while True:
#     if not i == 1:
#         i+=1
#         print(i)
#     if i == 1:
#         print("I est 1")
#         i+=1
#     if i == 2:
#         i+=2
#         print(i)
#     if i == 4:
#         print("C'est bon")
#         break

# Exercice 4

# i = 0

# while True:
#     print(i)
#     if i == 7:
#         print("stop")
#         break
#     i += 1

# # JEU - Pierre, papier, ciseaux !

Name1 = input("Nom du joueur 1 ? \n")
Name2 = input("Nom du joueur 2 ? \n")

PtsJ1 = 0
PtsJ2 = 0

max = 3  # nombre de manches gagnantes

while PtsJ1 < max and PtsJ2 < max:  # condition de continuation
    # "Tant que c'est vrai on continue."

    AnswerJ1 = input(Name1 + ", donne ta réponse \n")

    if AnswerJ1 != "pierre" and AnswerJ1 != "papier" and AnswerJ1 != "ciseaux":
        print("Revois ton orthographe " + Name1 + " !")

    else:
        AnswerJ2 = input(Name2 + ", donne ta réponse \n")

        if AnswerJ2 != "pierre" and AnswerJ2 != "papier" and \
                AnswerJ2 != "ciseaux":
            print("Revois ton orthographe " + Name2 + " !")

        elif AnswerJ1 == AnswerJ2:
            print("Egalité!")

        elif (AnswerJ1 == "ciseaux" and AnswerJ2 == "pierre") \
            or (AnswerJ1 == "pierre" and AnswerJ2 == "papier") \
                or (AnswerJ1 == "papier" and AnswerJ2 == "ciseaux"):
            print(Name2 + " Win!")
            PtsJ2 = PtsJ2 + 1
            print(Name1 + " " + str(PtsJ1) + " " +
                  "-" + " " + Name2 + " " + (str(PtsJ2)))

        else:
            print(Name1 + " Win!")
            PtsJ1 = PtsJ1 + 1
            print(Name1 + " " + str(PtsJ1) + " " +
                  "-" + " " + Name2 + " " + (str(PtsJ2)))

if PtsJ1 == 2:
    print(Name1 + " Big Winner!")

elif PtsJ2 == 2:
    print(Name2 + " Big Winner!")
