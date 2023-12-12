# # JEU 1 - Pierre, papier, ciseaux !

Name1 = input("Nom du joueur 1 ? \n")
Name2 = input("Nom du joueur 2 ? \n")

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

    else:
        print(Name1 + " Win!")

# !!! 2eme version !!!


Name1 = input("Nom du joueur 1 ? \n")
Name2 = input("Nom du joueur 2 ? \n")

PtsJ1 = 0
PtsJ2 = 0

max = 3  # nombre de manches gagnantes

while PtsJ1 < max and PtsJ2 < max:  # condition de continuation
    # "Tant que c'est vrai on continue."

    AnswerJ1 = input(Name1 + ", donne ta réponse \n")

    if AnswerJ1 != "pierre" and AnswerJ1 != "papier" and \
          AnswerJ1 != "ciseaux":
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

# JEU 2 - Morpions


