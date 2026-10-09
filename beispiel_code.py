#!/usr/bin/env python3

# Bedingte Anweisungen in Pyhton 

# Variablen
x = 10
y = 5

# Einfache if-Bedingung
if x > y:
    print("A: x ist größer als y")

# if-else-Bedingung
if x <= y:
    print("B: x ist kleiner-gleich y")
else:
    print("B: x ist nicht kleiner-gleich y")

# if-elif-else-Bedingung
if x == y:
    print("C: x ist gleich y")
elif x > y: 
    print("C: x ist größer als y")
else:
    print("C: x ist kleiner als y")

# Aufgabe: 
# Legen Sie zwei Variablen mit verschiedenen float Zahlenwerte an.
# Schreiben Sie eine if-else-Bedingung, die prüft, ob die erste Zahl 
# größer gleich oder kleiner der zweiten Zahl ist, und geben Sie das
# entsprechende Ergebnis aus.

a = 2.5
b = 1002.5

if a >= b:
    print("Aufgabe: Die Zahl " + str(a) + " ist größer gleich der Zahl " + str(b))
else:
    print("Die Zahl " + str(a) + " ist kleiner als " + str(b))