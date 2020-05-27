# Problemes de Cerca
Autors Alex Moñux, Neil Torrero, Marc Aynés
Llenguatge usat: Python
Interpret de python: python 3.8
IDE Usat: PyCharm

Importació del projecte:
PyCharm barra superior d'eines -> File -> Open...
Seleccionar la Carpeta Problemes-de-Cerca

En PyCharm, a dalt a la dreta, hi han els botons per executar i debuggar, a l'esquerra d'aquests hi ha la configuració que s'executarà, si en aquest no surt la paraula "main" escrita fer:
clic en el desplegable -> Edit configuaration
En la pantalla que apareix, a la esquerra veurem un + (add configuration) sortirà un desplegable, seleccionem de tots ells: Python
Un cop seleccionat a la dreta ens apareixera a la dreta unes opcions a omplir, a dal de tot hi ha un quadre de text anomenta "Name" aquest hem de posar el nom que vulguem, podem posar-hi main si ens va bé.
el seguent quadre de text que apareix és: "script Path: " aquest hem de seleccionar el fitxer main.py del nostre projecte, així doncs ens ha de quedar una cosa semblant a <ruta-del-vostre-ordinador>\Problemes-de-Cerca\main.py
on la <ruta-del-vostre-ordinador> pot ser alguna cosa semblant a C:\Documents\SBC

A l'apartat de environment ens hem d'assegurar de seleccionar el "Python Interpreter" a Python 3.8
I el "Working directory" a la carpeta d'aquest projecte: Problemes-de-Cerca sent quelcom semblant a:  <ruta-del-vostre-ordinador>\Problemes-de-Cerca

No ha d'haver cap problema amb la importació de llibreries, ja que Python les importa automàticament, si hi ha cap problema amb cap llibreria, gràcies a PyCharm aquestes sortiran en vermell en el codi i si intentem executar ens dirà on està el problema
posant el cursor sobre aquest tros de codi i apretant les tecles alt+intro hauriem de poder ser capaços de veure quina llibreria falta per importar i seleccionar import library.

Per executar aquest programa ens hem de dirigir a la fletxa verda d'adalt a la dreta, també anomenada run <nom de la configuració seleccionada> amb aquesta acció executarem la configuració que previament hem configurat.
També és pot usar les tecles Mayus(Shift) + F10.

A la execució, ens demanarà una ciutat origen, una ciutat destí i un algoritme a usar, Aquestes ciutats han de ser introduïdes exactament com estan en el fitxer.
Els algoritmes a usar, s'hauran de introduïr com "1" per A* i "2" per CSP.

Els resultats es mostraran com:
Barcelona -> Hospitalet de llobregat -> Bilbao, per mostrar per les ciutats visitades.
Seguidament és mostrarà el cost del camí.

També és mostrarà el cost temporal d'aquest algoritme en segons, amb la màxima presició possible.

Seguidament, és demana per una nova ciutat inicial, per així fer més proves.


Si volem tancar el programa ens haurem de dirigir al botó quadrat vermell anomenat Stop <nom de la configuració seleccionada>, també és pot usar les tecles Ctrl + F2


Per qualsevol problema d'execució que no estigui esmentat aquí si us plau envieu un correu a marc.aynesi@students.salle.url.edu, neil.torrero@students.salle.url.edu i alex.monux@students.salle.url.edu

