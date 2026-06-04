
# Exercice

class pharmacie :
  def __init__(self, medicament, stock):
    self.medicament = medicament
    self.stock = stock

#Question 1

medicaments = [ "Paracétamol" , "Ibuprofène" , "Amorxicilline" , "Doliprane" , "Aspegic" ]

stock = [ 30 , 12 ,  4 , 18 , 7 ]

#Question 2

def afficher_stock () :
    for (i, j) in zip (medicaments, stock):
        print (f"{i} : {j} en stock " )
        
#Question 3

def verifier_alerte(nom, quantite):
   if quantite < 5:
     print(f"ALERTE : Stock de {name} insuffisant ({stock} unités restantes)")
     
for (i, j) in zip (medicaments, stock):
  verifier_alerte(medicaments, stock)
  
 #Question 4

def vendre(nom_medicament, quantite_vendue):
    index = medicaments.index(nom_medicament)
    if index >= 0:
        if quantite_vendue <= quantite[index]:
            quantite[index] -= quantite_vendue
            print(f"{quantite_vendu} unités de {nom_medicament} vendu avec succes")
        else:
            print(f"Stock insuffisant à la vente ({nom_medicament})")

#Question 5

def main():
    vendre('Paracétamol', 5)
    vendre('Doliprane', 10)
    vendre("Ibuprofène", 3)
    vendre("Amoxicilline", 6)

    verifier_alerte('Paracétamol', 5)
    verifier_alerte('Doliprane', 10)
    verifier_alerte("Ibuprofène", 3)
    verifier_alerte("Amoxicilline", 6)

#Question 6

    minimum = min(stock)

    for j in stock:
        if j < min(stock):
            min(stock) == j
        
    print(f"Le médicament ayant la plus faible quantité restante en stock est :{medicaments.index[nom_medicament]} avec {minimum} en stock")


main()