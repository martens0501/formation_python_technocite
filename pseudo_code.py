# Pseudo_code et algorigramme

# demander un numero entre 1 et 10 jusquà ce que la réponse convienne => boucle
# n = 0

# si reponse >20 alors écrire "plus petit"
# si réponse <10 alors écrire "plus grand"

# => Code

# n = 0

# while n < 10 or n > 20:

#     n = int(input("Donne moi un nombre entre 10 et 20 \n"))

#     if n < 10:
#         print("Plus grand!")

#     if n > 20:
#         print("Plus petit!")

# print("Bien joué!")


# Library online

# from math import factorial, pi

# print("Factorial is", factorial(5))
# print("Perimeter is", 2*pi*10)

# def calculate_factorial(n):
#     factorial(n)
#     print("Factorial is", factorial(n))

# calculate_factorial(5)

# def calculate_factorial(n):
#     x = factorial(n)
#     return x

# var = calculate_factorial(5)
# print("Factorial is", var)


# def calculate_perimeter_circle(r):
#     perimeter_circle = 2*pi*r
#     print("The perimeter of the circle is", perimeter_circle)

# calculate_perimeter_circle(10)

# def calculate_perimeter_circle(r):
#     perimeter_circle = 2*pi*r
#     return perimeter_circle

# var=calculate_perimeter_circle(10)
# print("The perimeter of the circle is", var)


# Date et Heure

# from datetime import datetime, timedelta, timezone

# Exercice 1

# # Obtenir la date et l'heure actuelles
# maintenant = datetime.now()
# Dans_7_jours = maintenant + timedelta(days=7)

# # Afficher la date du jour et dans 7 jours
# date_du_jour = maintenant.date()
# date_dans_7_jours = Dans_7_jours.date()
# print("Date du jour :", date_du_jour)
# print("Date dans 7 jours :", date_dans_7_jours)

# Exercice 1 bis

# # Obtenir la date et l'heure actuelles
# maintenant = datetime.now()
# Dans_7_jours = maintenant + timedelta(days=7)

# # Afficher la date du jour et dans 7 jours
# date_du_jour = maintenant.date()
# date_dans_7_jours = Dans_7_jours.date()

# format = "%d/%m/%Y"

# date_du_jour_bon_format = date_du_jour.strftime(format)
# date_dans_7_jours_bon_format = date_dans_7_jours.strftime(format)

# print("Date du jour :", date_du_jour_bon_format)
# print("Date dans 7 jours :", date_dans_7_jours_bon_format)


# Exercice 2

# # Obtenir la date et l'heure actuelles
# maintenant = datetime.now()

# # Ajouter 3 heures à la date et l'heure actuelles
# Dans_3h = maintenant + timedelta(hours=3)

# # Afficher les résultats
# print("Date et heure actuelles :", maintenant)
# print("Date et heure dans 3 heures :", date_dans_3h)

# Exercice 3

# heure_actuelle = datetime.now()
# dans_3h = heure_actuelle + timedelta(hours=3)

# format = "%H:%M"

# dans_3h_bon_format = dans_3h.strftime(format)
# print(dans_3h_bon_format)

# Bonus NY

# #  Méthode 1

# offset = int(input("Décalage par rappot à UTC ? \n"))
# tz= timezone(timedelta(hours=offset))
# today_in_ny = datetime.now(tz)
# print(today_in_ny.strftime("%H:%M"))

# #  Méthode 5

# tz= timezone(timedelta(hours=-5))
# today = datetime.now()
# today_in_ny = today.astimezone(tz)
# print(today_in_ny.strftime("%H:%M"))
