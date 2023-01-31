
import requests
from bs4 import BeautifulSoup
import studente
import mioTelegram
from ischedule import schedule, run_loop


URLS = ["https://docs.google.com/spreadsheets/d/e/2PACX-1vSxa-l5fqDBv5hOuNQ5q0kW19YOpPHAMe-kITWnBR567PIBhYkklOzpbjz-td77hY-jBw5_KGyz1fX7/pubhtml?gid=6878166&&range=A1:H&widget=false&chrome=false&headers=false&",
        "https://docs.google.com/spreadsheets/d/e/2PACX-1vSxa-l5fqDBv5hOuNQ5q0kW19YOpPHAMe-kITWnBR567PIBhYkklOzpbjz-td77hY-jBw5_KGyz1fX7/pubhtml?gid=695965261&range=A1:H&widget=false&chrome=false&headers=false&"]

IDS = ["6878166",
       "695965261"]

codici = []

emoji = ["💻", "📚"]

#ogni volta devo svuotarla immagino
def riempiLista(s):
    index = 0
    limit = 30
    studenti=[]
    for riga in s:

        
        materia = riga.contents[1].string   #mhhhh, può creare problemi?
        if materia!=None and index!=0:  #questo index!= l'ho messo perchè l'albero html mi costringeva, non ricordo il motivo preciso
            materia = str(materia)
            #genere = riga.contents[2].string
            #eta = riga.contents[3].string
            anno = riga.contents[4].string
            lezioni = str(riga.contents[5].string)
            
            #go = riga.contents[6].string
            
            info = riga.contents[7].get_text()
            ####
            numero = riga.contents[8].string.split()[1]
            walink = riga.contents[8].contents[0]['href']
            #print(walink)
            ####
            codici.append(numero)
            studenti.append(studente.student(materia, anno, lezioni, info, numero, walink))
            
            """ print(type(materia))
            print(type(lezioni))
            print(type(info))
            print(type(numero))
            print(type(walink)) 
            print("-----------") """
            


        
        index +=1
        if index >= limit:
            return studenti
    return studenti #nel caso, non si sa mai che la tabella sia più corta di 30 righe

def leggiVecchiCodici(i):
    with open(f'codici{i}.txt', 'r', encoding="utf-8") as f:
        return f.read()

def scriviCodici(i):
    with open(f'codici{i}.txt', 'w', encoding="utf-8") as f:
        for c in codici:
            f.write(f"{c} ")

def mergeCodici(vecchi, studenti, i):
    for s in studenti:
        if s.numero not in vecchi:
            mioTelegram.inviaMessaggio(s, emoji[i])

def main():
    #print("eccoci")

    for i in range(2):
        r = requests.get(URLS[i])
        s = BeautifulSoup(r.content, 'html.parser')
        #print("dimensione studenti ",sys.getsizeof(soup))
        #print("prima riga")
        mioTelegram.invio("prova nuovo repo")
        #print("prima riga")
        s = s.find("div", {"id":IDS[i]}) #file di informatica, potrebbe cambiare nel tempo?
        s = s.contents[0].contents[0].contents[1]  #questo è il tbody

        vecchiCodici = leggiVecchiCodici(i)
        studenti = riempiLista(s)
        s.decompose()
        #print(studenti[0])
        mergeCodici(vecchiCodici, studenti, i)
        scriviCodici(i)


if __name__ == "__main__":
    main()
    schedule(main, interval=1*60)
    run_loop()
