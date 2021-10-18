# Somme des Multiples de 3 et 5, jusqu'à 11
resultat = 0
for i in range(1, 11):
    if i%3 == 0 or i%5 == 0:
        resultat += i
print(resultat)

# Somme des Multiples de 3 et 5, jusqu'à 1000
resultat = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        resultat += i
print(resultat)