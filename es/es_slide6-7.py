import datetime

class CSVFile():
    def __init__ (self, file_name):
        
        if not isinstance(file_name,str):
            raise TypeError(f"Errore: Il nome del file non e una stringa.")
       
        self.file_name = file_name
        
    def get_data(self, inizio  = None , fine = None ):
        
        if inizio is None or inizio <1:
            inizio = 1
        else:
            inizio = int(inizio)
        if fine < 1 or fine < inizio:
            raise ValueError(f"Errore: Il valore di fine deve essere maggiore o uguale a inizio e maggiore di 0.")   
        elif fine is not None:
            fine = int(fine)
            
            
            
        data = []
        try:
         with open(self.file_name, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        except FileNotFoundError:
            raise FileNotFoundError(f"Errore: Il file '{self.file_name}' non e stato trovato.")
        return data
    
class NumericalCSVFile(CSVFile):
    def __init__(self, file_name):
        super().__init__(file_name)
        
    def get_data(self):
       data = super().get_data()
       numerical_data = []
       for row in data[1:]:
            numerical_row = []
            for item in row:
                try:
                    numerical_row.append(item[0])
                    numerical_row.append(float(item[1]))
                except:
                    raise ValueError(f"Errore: Il valore '{item[1]}' non e un numero valido.")
            numerical_data.append(numerical_row)
       return numerical_data
def calcola_eta():   
    giorno = input("Inserisci giorno di nascita: ")
    mese = input("Inserisci mese di nascita: ")
    anno = input("Inserisci anno di nascita: ")
    try:
        giorno = int(giorno)
        mese = int(mese)
        anno = int(anno)
        if giorno < 1 or giorno > 31:
            raise ValueError("Errore: Il giorno deve essere compreso tra 1 e 31.")  
        if mese < 1 or mese > 12:
            raise ValueError("Errore: Il mese deve essere compreso tra 1 e 12.")    
        if anno < 1900 or anno > 2026:
            raise ValueError("Errore: L'anno deve essere compreso tra 1900 e 2026.")
        print(f"Data di nascita: {giorno}/{mese}/{anno}")
        
        
    except ValueError as e:
        print(e)    
    
    
    eta = datetime.datetime.now().year - anno
    print(f"Età: {eta} anni")
    compleanno = datetime.date(anno,mese,giorno)
    oggi = datetime.datetime.now().date()
    if compleanno < oggi:
        compleanno = datetime.date(oggi.year + 1, mese, giorno)
    tempo_alla_prossima_festa = compleanno - oggi
    
    
    print(f"Tempo alla prossima festa: {tempo_alla_prossima_festa.days} giorni")            

def scelte():
    flag = True
    while flag:
        valore = input("Scegli un'opzione (1-3): ")
        try:
            valore = int(valore)
            if valore < 1 or valore > 3:
                raise ValueError("Errore: L'opzione deve essere compresa tra 1 e 3.")
            print(f"Hai scelto l'opzione {valore}.")
        except ValueError as e:
            print(e)
        match valore:
            case 1:
                add1 = input("Inserisci il primo numero: ")
                add2 = input("Inserisci il secondo numero: ")
                somma = float(add1) + float(add2)
                print(f"La somma è: {somma}")
            case 2:
                sott1 = input("Inserisci il primo numero: ")
                sott2 = input("Inserisci il secondo numero: ")
                differenza = float(sott1) - float(sott2)
                print(f"La differenza è: {differenza}")
            case 3:
                print("stop")
                flag = False
            
    
if __name__ == "__main__":
    # csv_file = CSVFile('shampoo.csv')
    # print("Dati CSV:", csv_file.get_data())
    
    # numerical_csv_file = NumericalCSVFile('shampoo.csv')
    # print("Dati Numerici CSV:", numerical_csv_file.get_data())  
    
    # csv_file = CSVFile(1234)
    # calcola_eta()
    scelte()