class CSVFile():
    def __init__ (self, file_name):
        self.file_name = file_name
    
    def get_data(self):
        data = []
        with open(self.file_name, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        return data
    
    
class Canguro():
    def __init__(self, nome,tasca= None):
        self.nome = nome
        if tasca is None:
            tasca = []
        else:    
         self.tasca = tasca
        
    def intasca(self, oggetto):
        self.tasca.append(oggetto)
        
    def __str__(self):
        return f"{self.nome} ha in tasca: {self.tasca}"
    
class Veicolo ():
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.speed = 0 

    def __str__(self):
        return f"{self.anno} {self.marca} {self.modello}"
    
    def accellera(self):
        self.speed +=5
        
    def frena(self):
        if self.speed <0:
            self.speed = 0
        self.speed -=5
        
    def get_speed(self):
        return self.speed       
    
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, porte):
        super().__init__(marca, modello, anno)
        self.porte = porte
        
    def __str__(self):
        return f" {super().__str__()} e porte: {self.porte}"   
    
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
        
    def __str__(self):
        return f" {super().__str__()} e tipo: {self.tipo}"    



class Persona():
    def __init__(self,ruolo, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.ruolo = ruolo
        
    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome} e sono un {self.ruolo}")
    
class Studente(Persona):
    def __init__(self, nome, cognome,corsi=None):
        super().__init__("Studente UNITS",nome, cognome)
        
        if corsi is None:
            corsi = []
        else:
            self.corsi = corsi
     
    def eiste_docente(self, docenti):
     for docente in docenti:
         for corsi in self.corsi:
            if corsi in docente.corsi:
                print(f" {docente.nome} {docente.cognome} insegna il corso di {corsi}")
            else:   
                print(f" {docente.nome} {docente.cognome} insegna il corso di {corsi}")
        
        
        
        
    def saluta(self):
       Persona.saluta(self)
       print(">Frequento i corsi di: ", self.corsi)
       
    
       
class Docente(Persona):
    def __init__(self, nome, cognome, corsi=None):
        super().__init__("Docente UNITS",nome, cognome)
        if corsi is None:
            corsi = []
        else:
            self.corsi = corsi
            
    def insegna(self, studente):
        if (set(self.corsi) == set(studente.corsi)):
            print(f"{self.nome} {self.cognome} insegna a {studente.nome} {studente.cognome} tutti i corsi")
        else:
            print(f"{self.nome} {self.cognome} insegna a {studente.nome} {studente.cognome} solo alcuni corsi")
                
        
    def saluta(self):
        Persona.saluta(self)
        print(">Docente del corso di: ", self.corsi)      
        


class Poligono():
    def __init__(self,numero_lati):
        self.numero_lati = numero_lati
    
    def __str__(self):
        return f"Il poligono ha {self.numero_lati} lati"
    
class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
        
    def __str__(self):
        return f"{super().__str__()} è quadrilatero"        

class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)    
        
    def area(self):
        return self.base * self.altezza 
       
    def __str__(self):
        return f"{super().__str__()} con base {self.base} e altezza {self.altezza} perimetro: {self.perimetro()} area: {self.area()}"
    
    
class Triangolo(Poligono):
    def __init__(self,lato1,lato2,lato3):
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3
        
    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3
    
    def is_equilatero(self):
        return self.lato1 == self.lato2 == self.lato3
    
    def __str__(self):
        return f"{super().__str__()} con lati {self.lato1}, {self.lato2}, {self.lato3} perimetro: {self.perimetro()} è equilatero: {self.is_equilatero()}"

if __name__ == "__main__":
    
    can = Canguro('Can')
    can.intasca('palla')

    guro = Canguro('Guro')
    guro.intasca('bambola') 
    print(can)
    print(guro)    

    auto1 = Auto('Fiat', 'Panda', 2020, 5)
    print(auto1)

    moto1 = Moto('Yamaha', 'R1', 2021, 'Sportiva')
    print(moto1)
    
    
    corsi = ['Informatica', 'Matematica', 'Fisica', 'Chimica','Biologia']
    obj_Irene = Studente('Irene', 'Rossi', corsi)
    obj_Irene.saluta()
    obj_Martino = Docente('Martino', 'Bianchi', ['Informatica', 'Matematica'])
    obj_Martino.saluta()
    obj_Martino.insegna(obj_Irene)
    obj_Luca = Docente('Luca', 'Verdi', ['Informatica', 'Matematica', 'Fisica', 'Chimica','Biologia'])
    obj_Francesco = Docente('Francesco', 'Neri', ['Informatica', 'Matematica', 'Fisica'])
    doc_list = [obj_Martino, obj_Luca, obj_Francesco]
    obj_Irene.eiste_docente(doc_list)
    
    pol = Poligono(5)
    print(pol)
    quad = Quadrilatero()
    print(quad)
    ret = Rettangolo(10, 5)
    print(ret)
    tri = Triangolo(3, 4, 5)
    print(tri)