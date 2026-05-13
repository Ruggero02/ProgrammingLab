import random

class Coin():
    def __init__(self, faccia ='Testa'):
        self.faccia = faccia
    
    def lancia(self):
        self.faccia = random.choice(['Testa', 'Croce'])
    
    def get_faccia(self):
        return self.faccia

moneta = Coin()
moneta.lancia()
print(moneta.get_faccia())

class Veicolo():
    def __init__(self, modello, marca, anno, speed):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
    
    def __str__(self):
        return f"{self.marca}, {self.modello}, {self.anno}, Velocità: {self.speed} km/h"
    
    def accellerare(self):
        self.speed += 5
    
    def frenare(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
    def get_speed(self):
        return self.speed

auto = Veicolo('Model S', 'Tesla', 2020, 0)
print(auto)
auto.accellerare()
print(f"velocità attuale: {auto.get_speed()} km/h")
auto.accellerare()
print(f"velocità attuale: {auto.get_speed()} km/h")
auto.frenare()
print(f"velocità attuale: {auto.get_speed()} km/h")

class CSVFile():
    def __init__(self,file_name):
        self.name = file_name
        self.data = []
        
    def get_data(self):
        with open(self.name, 'r') as file:
            for line in file:
                self.data.append(line.strip().split('\t'))
        return self.data


csv = CSVFile('ProgrammingLab\\shampoo.csv')
data = csv.get_data()
print(data)
        
    
        
