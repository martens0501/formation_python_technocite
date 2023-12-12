case1 = " "
case2 = " "
case3 = " "
case4 = " "
case5 = " "
case6 = " "
case7 = " "
case8 = " "
case9 = " "


Joueur1 = input("Qui est le premier combattant ? \n")
Joueur2 = input("Qui est le second combattant ? \n")


CombiJ1 = 0
CombiJ2 = 0

# boucle

while True :  # boucle qui permet de rejouer une partie 

    while CombiJ1 != 1 and CombiJ2 != 1 :  # boucle de jeu : tant que personne ne gagne, la boucle continue

        AnswerJ1 = input(Joueur1 + " où positionnes-tu ta lettre ?\n")

        if AnswerJ1 == "1" :        # on attribue un X à la case choisie car la case est "vide" de base
            case1 = "X"
        elif AnswerJ1 == "2" :
            case2 = "X"
        elif AnswerJ1 == "3" :
            case3 = "X"
        elif AnswerJ1 == "4" :
            case4 = "X"
        elif AnswerJ1 == "5" :
            case5 = "X"
        elif AnswerJ1 == "6" :
            case6 = "X"
        elif AnswerJ1 == "7" :
            case7 = "X"
        elif AnswerJ1 == "8" :
            case8 = "X"
        elif AnswerJ1 == "9" :
            case9 = "X"



        if case1 == case2 == case3 == "X"\
                or case4 == case5 == case6 == "X"\
                or case7 == case8 == case9 == "X"\
                or case1 == case4 == case7 == "X"\
                or case2 == case5 == case8 == "X"\
                or case3 == case6 == case9 == "X"\
                or case1 == case5 == case9 == "X"\
                or case3 == case5 == case7 == "X" :
                
                CombiJ1 = 1
                continue
        
        if (case1 == "X" or case1 == "O") and \
         (case2 == "X" or case2 == "O") and \
            (case3 == "X" or case3 == "O") and \
                (case4 == "X" or case4 == "O") and \
                    (case5 == "X" or case5 == "O") and \
                        (case6 == "X" or case6 == "O") and \
                            (case7 == "X" or case7 == "O") and \
                                (case8 == "X" or case8 == "O") and \
                                    (case9 == "X" or case9 == "O") :
            CombiJ1 = 1
            CombiJ2 = 1
            print("Egalité !")
            continue
        
        AnswerJ2 = input(Joueur2 + " où positionnes-tu ta lettre ?\n")

        if AnswerJ2 == "1" :
            case1 = "O"
        elif AnswerJ2 == "2" :
            case2 = "O"
        elif AnswerJ2 == "3" :
            case3 = "O"
        elif AnswerJ2 == "4" :
            case4 = "O"
        elif AnswerJ2 == "5" :
            case5 = "O"
        elif AnswerJ2 == "6" :
            case6 = "O"
        elif AnswerJ2 == "7" :
            case7 = "O"
        elif AnswerJ2 == "8" :
            case8 = "O"
        elif AnswerJ2 == "9" :
            case9 = "O"
        
        

        if case1 == case2 == case3 == "O"\
            or case4 == case5 == case6 == "O"\
            or case7 == case8 == case9 == "O"\
            or case1 == case4 == case7 == "O"\
            or case2 == case5 == case8 == "O"\
            or case3 == case6 == case9 == "O"\
            or case1 == case5 == case9 == "O"\
            or case3 == case5 == case7 == "O" :
        
            CombiJ2 = 1

    if CombiJ1 == 1 and CombiJ2 == 0 :
        print(Joueur1 + " WINNER !")
        
    elif CombiJ2 == 1 and CombiJ1 == 0 :
        print(Joueur2 + " WINNER !")
        
    partie_suivante = input("Veux-tu rejouer ? \n")

    if partie_suivante == "oui" or partie_suivante == "yes" :
        CombiJ1 = 0 
        CombiJ2 = 0
        case1 = " "
        case2 = " "
        case3 = " "
        case4 = " "
        case5 = " "
        case6 = " "
        case7 = " "
        case8 = " "
        case9 = " "
        print("C'est reparti")

    else :
        print("A bientôt !")
        break


   
       