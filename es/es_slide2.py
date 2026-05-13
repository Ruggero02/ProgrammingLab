#es1
def calcola_ore(minuti):
    ore = minuti// 60 
    minuti_rimanenti = minuti % 60
    print( f" {minuti} minuti corrispondono a {ore}h:{minuti_rimanenti}min")

minuti = 538
calcola_ore(minuti)

#es2
def quadrato_cubo():
    n = int(input("inserisci un numero:"))
    quadrato = n**2
    cubo = n**3
    print(f"il quadrato di {n} è: {quadrato} e il cubo è: {cubo}")
    
quadrato_cubo()    

#es3
def pari_dispari():
    n = int (input("inserisci un numero:"))
    if n % 2 == 0:
        print(f" Il numero {n} è pari.")
    else: 
        print(f"Il numero {n} è dispari.")
        
pari_dispari()        

#es4
def conta_lettera(parola,lettera):
    conta = 0
    for l in parola:
        if l == lettera:
            conta +=1
    print(f"La lettera '{lettera}' compare {conta} volte nella parola '{parola}'")
    
parola = input("inserisci una parola:")
lettera = input("inserisci una lettera:")
conta_lettera(parola,lettera)

#es5
def is_primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

n = int(input("inserisci un numero:"))
print(f"Il numero {n} è primo? {is_primo(n)}")

#es6
def calcola_somma():
    somma = 0 
    while True:
        n = int(input("inserisci un numero (o '0' per terminare):"))
        if n == 0:
            break
        somma +=n
        print(f"Somma parziale: {somma}")
    print(f"La somma totale è: {somma}")

calcola_somma()

#es7
def fattoriale(n):
    if n == 0: 
        return 1
    else:
        for i in range(1,n):
            n *= i
        return n
    
n = int(input("Inserisci un numero: "))
print(f"Il fattoriale di {n} è: {fattoriale(n)}")

#es8
def triangolo(n1,n2,n3):
    if n1 <=0 or n2 <=0 or n3 <=0:
        print("I lati del triangolo devono essere numeri positivi.")
    elif n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        if n1 == n2 == n3:
            print("Il triangolo è equilatero.")
        elif n1 == n2 or n1 == n3 or n2 == n3:
            print("Il triangolo è isoscele.")
        else:
            print("Il triangolo è scaleno.")
    
    else:
        print("I lati inseriti non possono formare un triangolo.")
        
n1 = int(input("Inserisci il primo lato del triangolo: "))
n2 = int(input("Inserisci il secondo lato del triangolo: "))    
n3 = int(input("Inserisci il terzo lato del triangolo: "))
triangolo(n1,n2,n3)

#es9 
def conta_vocali(parola):
    vocali = 'aeiouAEIOU'
    conta = 0 
    for c in parola:
        if c in vocali:
            conta +=1
    print(f"La parola '{parola}' contiene {conta} vocali.")
parola = input("Inserisci una parola: ")
conta_vocali(parola)
