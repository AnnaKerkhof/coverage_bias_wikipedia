# -*- coding: utf-8 -*-
"""
Ermittelt die aktuellen Seitenlängen in Bytes einer Liste von Abgeordneten

"""

import urllib
import bs4
import os



####################################################################
###### TEIL 1 - KREIERE ITERATOR MIT ALLEN LINKS ###################
####################################################################



os.chdir("S:\mitarbeiter\Anna\Python")

Liste_plain = open("Names_Plain.txt").readlines()       # Lade Liste mit allen Abgeordneten
Plain = [i.rstrip() for i in Liste_plain]

Unterstrich = [i.replace(" ", "_") for i in Plain]       # Jetzt ist der Unterstrich drin, den man in den Links braucht


Links = ["https://de.wikipedia.org/w/index.php?title="+i+"&action=info" for i in Unterstrich] # Fertige Liste mit Links
     
        
        
####################################################################
###### TEIL 2 - SCHLEIFE UEBER LINKS ###############################
####################################################################    



# Die ersten vier Zeilen lesen den HTML-Code für die entsprechende Zeile in der Tabelle aus
 
seiteninfo = urllib.urlopen("https://de.wikipedia.org/w/index.php?title=Alexander_Funk_(Politiker)&action=info")
bs = bs4.BeautifulSoup(seiteninfo.read()) 
print bs
bs1 = bs.find_all("tr", {"id":"mw-pageinfo-length"}, {"style":"vertical-align: top;"})
print bs1

# Dieser Loop extrahiert den Inhalt der Zeile: "Seitenlänge (in Bytes)xxx"

for x in bs1:
    length = x.get_text()
    print length



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

print Liste_2

# Schritt 2
# Aus Liste_2 muss man jetzt noch eine einzige Zahl zusammensetzen.

if len(Liste_2) == 4:
    Bytes = Liste_2[0]*1000 + Liste_2[1]*100 + Liste_2[2]*10 + Liste_2[3]
    print Bytes
elif len(Liste_2) == 5:
    Bytes = Liste_2[0]*10000 + Liste_2[1]*1000 +Liste_2[2]*100 + Liste_2[3]*10 + Liste_2[4]
    print Bytes
else:
    Bytes = Liste_2[0]*100000 + Liste_2[1]*10000 +Liste_2[2]*1000 + Liste_2[3]*100 + Liste_2[4] * 10 + Liste_2[5]
    print Bytes

# Schließlich muss das Ergebnis abgespeichert werden.    
    