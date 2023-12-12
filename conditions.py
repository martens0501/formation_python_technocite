# meteo = input("Quel est la météo ? \n")
# if meteo == "pluie":
#     print("Sortez les parapluies !")
# else:
#     print("Ouf ! Il ne pleuvera pas")

# meteo = input("Quel est la météo ? \n")

# if meteo == "pluie":
#     print("Sortez les parapluies !")
# elif meteo == "soleil":
#     print("N'oublie pas ta casquette !")
# else:
#     print("Pas d'info sur la météo")

# Exercice 1 : Videur de boite de nuit

# old = input("Quel est ton âge ? \n")
# ans = str(old)
# if int(ans) >= 18 :
#     print("Bienvenue !")
# else :
#     print("Désolé, vous ne pouvez pas rentrer !")

# Exercice 2

# number1 = input ("Donne moi un nombre \n")

# number2 = input ("Donne moi un deuxième nombre \n")

# if int(number1) == int(number2):
#     print ("Egalité !")
# elif int(number1) > int(number2):
#     print (int(number1))
# else:
#     print (int(number2))

# Exercice 3

# number1 = input("Donne moi un nombre \n")

# number2 = input("Donne moi un deuxième nombre \n")

# number3 = input("Donne moi un troisième nombre \n")


# if int(number1) == int(number2) == int(number3):
#     print("Egalité !")
# elif int(number1) > int(number2):
#     if int(number1) > int(number3):
#         print(int(number1))
#     elif int(number1) < int(number3):  # else également suffisant
#         print(int(number3))

# elif int(number2) > int(number3):
#     if int(number2) > int(number1):
#         print(int(number2))
#     elif int(number2) < int(number1):  # else également suffisant
#         print(int(number1))
# else:
#     print(number3)

# Solution plus simple ...

# number1 = int(input ("Donne moi un nombre \n"))

# number2 = int(input ("Donne moi un deuxième nombre \n"))

# number3 = int(input ("Donne moi un troisième nombre \n"))

# if number1 == number2 == number3:
#     print ("Egalité !")

# elif number1 > number2 and number1 > number3:
#     print("Le plus grand est " + str(number1))

# elif number2 > number3 and number2 > number1:
#     print ("Le plus grand est " + str(number2))

# else:
#     print("Le plus grand est " + str(number3))

# Exercice 4

# number1 = int(input ("Donne moi un nombre \n"))

# number2 = int(input ("Donne moi un deuxième nombre \n"))

# if number1 > 0 or number2 > 0 :
#     print("Bravo!")
# else :
#     print("Dommage")

# Exercice 5

number1 = int(input("Donne moi un nombre \n"))

number2 = int(input("Donne moi un deuxième nombre \n"))

if (number1 > 0 and number2 < 0) or (number1 < 0 and number2 > 0):
    print("Bravo!")
else:
    print("Dommage")
