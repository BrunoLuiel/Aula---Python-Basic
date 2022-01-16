conjunto = {1, 2, 3, 4, 4}# Automaticamente já se declara conjunto quando estiver entre "{}" 
conjunto.add(5)

print(conjunto) # em print de conjunto os número repetidos não apareceram duas vezes

conjunto.discard(5)
print(conjunto)

conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

conjunto_intersection = conjunto.intersection(conjunto2)
print(conjunto_intersection)

