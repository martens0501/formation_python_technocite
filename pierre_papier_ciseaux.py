import random

Name1 = input("Nom du joueur 1 ? \n")
Name2 = "Ordinateur"

PtsJ1 = 0
PtsJ2 = 0

max = 2  # nombre de manches gagnantes

while PtsJ1 < max and PtsJ2 < max:  # condition de continuation
    # "Tant que c'est vrai on continue."

    AnswerJ1 = input(Name1 + ", donne ta réponse \n")

    if AnswerJ1 != "pierre" and AnswerJ1 != "papier" and AnswerJ1 != "ciseaux":
        print("Revois ton orthographe " + Name1 + " !")

    else:
        AnswerJ2 = random.randint(1, 3)
        if AnswerJ2 == 1:
            print("L'ordinateur a joué 'Pierre'")
        elif AnswerJ2 == 2:
            print("L'ordinateur a joué 'Papier'")
        else:
            print("L'ordinateur a joué 'Ciseaux'")

        if (AnswerJ1 == "pierre" and AnswerJ2 == 1) \
            or (AnswerJ1 == "papier" and AnswerJ2 == 2) \
                or (AnswerJ1 == "ciseaux" and AnswerJ2 == 3):
            print("Egalité!")

        elif (AnswerJ1 == "ciseaux" and AnswerJ2 == 1) \
            or (AnswerJ1 == "pierre" and AnswerJ2 == 2) \
                or (AnswerJ1 == "papier" and AnswerJ2 == 3):
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
