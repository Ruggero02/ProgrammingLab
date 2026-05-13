import os 
import csv 

#es1 
def somma_lista(lista):
    somma = 0
    for n in lista:
        somma += n
    return somma
numeri = [1, 2, 3, 4, 5]
print(f"La somma dei numeri nella lista {numeri} è: {somma_lista(numeri)}")

#es2
def is_palindromo(parola):
    parola = parola.lower()
    return parola == parola[::-1]
parola = input("Inserisci una parola: ")
print(f"La parola '{parola}' è palindroma? {is_palindromo(parola)}")

#es3
def scambia_in_lista(lista, indice1, indice2):
    tmp = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = tmp
numeri = [1, 2, 3, 4, 5]
print(f"Lista prima dello scambio: {numeri}")
scambia_in_lista(numeri, 1, 3)
print(f"Lista dopo lo scambio: {numeri}")

#es4
def almeno_un_elemento(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True
    return False
lista1 = [1, 2, 3]
lista2 = [4, 5, 3]
print(f"Le liste {lista1} e {lista2} hanno almeno un elemento in comune? {almeno_un_elemento(lista1, lista2)}")

#es5
def convert_numero_in_stringa(lista):
    dict_numero_stringa = { 0: "zero", 1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque", 6: "sei", 7: "sette", 8: "otto", 9: "nove"}
    lista_stringa = []
    for numero in lista:
        if numero in dict_numero_stringa:
            lista_stringa.append(dict_numero_stringa[numero])
    return lista_stringa
numeri = [0,5,6,8,7,6,3,5,1,2]
print(f"Lista di numeri: {numeri}")
print(f"Lista di stringhe: {convert_numero_in_stringa(numeri)}")

#es1_2
def conta_parole(lista):
    conta = {}
    for parola in lista:
        conta[parola] = conta.get(parola, 0) + 1
    return conta
parole = ["ciao", "mondo", "ciao", "programmazione", "mondo", "ciao"]
print(f"Lista di parole: {parole}")
print(f"Conteggio delle parole: {conta_parole(parole)}")

#es2_2
def somma_colonna(file_path):
    somma = 0 
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  
        for row in reader:
            valore = float(row[1])
            somma += valore
            
    return round(somma,1)
file_path = 'ProgrammingLab\\shampoo.csv'
print(f"La somma della colonna sales è: {somma_colonna(file_path)}")

#es3_2
def conta_parola_in_file(file_path, parola):
    conta = 0 
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if parola in row:
                conta += 1
    return conta

parola = 'shampoo'
print(f"La parola {parola} appare {conta_parola_in_file(file_path, parola)} volte nel file.")

#es4_2
def dizionario_da_fle(file_path):
    dizionario = {}
    with open(file_path, 'r') as file:
        for row in file:
            parole = row.strip().split('\t')
            for parola in parole:
                if parola in dizionario:
                    dizionario[parola] += 1
                else:          
                    dizionario[parola] = 1
    return dizionario
print(f"Dizionario delle parole nel file: {dizionario_da_fle(file_path)}")

#es5_2
def rimuovi_duplicati(file_path):
    linee = set()
    with open(file_path, 'r') as file:
        for linea in file:
            linee.add(linea.strip())
            with open('unique.txt', 'w') as output:
                for linea in linee:
                    output.write(linea + '\n')
                    
rimuovi_duplicati(file_path)