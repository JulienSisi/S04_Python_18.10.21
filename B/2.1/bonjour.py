# Afficher bonjour
print("\n")
print("--> Manipulation de chaines de caracteres <--\n")
bonjour = "Hello World!"
print(bonjour)

# Afficher premiere lettre bonjour
first_char = bonjour[0]
print('Premier caractere : ', first_char)
print("\n")

# Compter longueur chaine de caracteres
print(len(bonjour))

# Afficher derniere lettre bonjour
last_char = bonjour[-1]
print('Dernier caractere : ', last_char)
print("\n")

# Afficher les caracteres de la lettre 1 à la lettre 3
first_sample_char = bonjour[0:3]
print('Premier caractere : ', first_sample_char)
print("\n")

# Afficher les caracteres de la lettre 3 à la fin
sec_sample_char = bonjour[6:-1]
print('Premier caractere : ', sec_sample_char)
print("\n")

# Vérification chaine de caracteres du debut
if first_sample_char == "Hel" :
  print("Vérification OK, bonjour commence bien par Hel")
else :
  print("Vérification NOK, bonjour ne commence pas par Hel")

# Vérification chaine de caracteres de fin
if sec_sample_char == "World" :
  print("Vérification OK, bonjour fini bien par World !")
else :
  print("Vérification NOK, bonjour ne fini pas par World !")