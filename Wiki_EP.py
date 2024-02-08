# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


"""
Ermittelt die aktuellen Seitenlängen in Bytes einer Liste von Abgeordneten

"""

import urllib
import bs4
import os
import csv


####################################################################
###### TEIL 1 - KREIERE ITERATOR MIT ALLEN LINKS ###################
####################################################################



os.chdir("S:\mitarbeiter\Anna\Python")


L1 = open("EP_Links2.txt").readlines()
L2 = [i.rstrip() for i in L1]
L3 = [i[30:] for i in L2] 

Links = ["https://de.wikipedia.org/w/index.php?title="+i+"&action=info" for i in L3]
 # Fertige Liste mit Links
     
        
        
####################################################################
###### TEIL 2 - SCHLEIFE UEBER LINKS ###############################
####################################################################    

Liste_Bytes = []                            # In der Liste wird das Endergebnis pro Link gespeichert.

for link in Links:                          # Die ersten vier Zeilen lesen den HTML-Code für die entsprechende Zeile in der Tabelle aus
    
    seiteninfo = urllib.urlopen(link)                    
    bs = bs4.BeautifulSoup(seiteninfo.read()) 
    bs1 = bs.find_all("tr", {"id":"mw-pageinfo-length"}, {"style":"vertical-align: top;"})
   
    
    for x in bs1:                           # Extrahiere Inhalt der Zeile: "Seitenlänge (in Bytes)xxx"
        length = x.get_text()                   
        
                                            # Das Problem ist, dass man den Slicing-Operator auf dem Object Length nicht anwenden kann. Das liegt an der Formatierung (Unicode).
                                            # Wegen dem "ä" in Seitenlänge kann man length auch nicht direkt in String formatieren. 
                                            # Daher werden im nächsten Schritt die Zahlen einzeln ausgelesen und anschließend transformiert. 
                                            # Die längeste Bio (Merkel) hat ca. 160000 Bytes, d.h. mit den 7 letzten Stellen aus Length kommt man auf jeden Fall hin               


    one = length[-1]
    two = length[-2]
    three = length[-3]

    # hier den Punkt weglassen

    five = length[-5]
    six = length[-6]
    seven = length[-7]

# Nun muss man das Ganze zu einem Integer zusammensetzen. In den meisten Fällen wird die Länge der Bios < 7 Zeichen sein.
# Also müssen die Zeichen, die man nicht zu Integern umformen kann, rausgeschmissen werden.

# Schritt 1

    Liste = [seven, six, five, three, two, one] 
    Liste_2 = []

    for l in Liste:
        try:
            l = int(l)
            Liste_2.append(l)
        except ValueError:
                pass


# Schritt 2
# Aus Liste_2 muss man jetzt noch eine einzige Zahl zusammensetzen.
    
    


    if len(Liste_2) == 1:
        Bytes = Liste_2[0]
        Liste_Bytes.append(Bytes)
    elif len(Liste_2) == 2:
        Bytes = Liste_2[0]*10 + Liste_2[1]
        Liste_Bytes.append(Bytes)
    elif len(Liste_2) == 3:
        Bytes = Liste_2[0]*100 + Liste_2[1]*10 + Liste_2[2]
        Liste_Bytes.append(Bytes)
    elif len(Liste_2) == 4:
        Bytes = Liste_2[0]*1000 + Liste_2[1]*100 + Liste_2[2]*10 + Liste_2[3]
        Liste_Bytes.append(Bytes)
    elif len(Liste_2) == 5:
        Bytes = Liste_2[0]*10000 + Liste_2[1]*1000 +Liste_2[2]*100 + Liste_2[3]*10 + Liste_2[4]
        Liste_Bytes.append(Bytes)
    else:
        Bytes = Liste_2[0]*100000 + Liste_2[1]*10000 +Liste_2[2]*1000 + Liste_2[3]*100 + Liste_2[4] * 10 + Liste_2[5]
        Liste_Bytes.append(Bytes)
       

with open('BytesEP.csv', 'wb') as myfile:
    wr = csv.writer(myfile, delimiter = "\n")
    wr.writerow(Liste_Bytes)

# Schließlich muss das Ergebnis abgespeichert werden.    
    