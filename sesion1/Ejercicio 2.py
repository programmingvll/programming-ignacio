'''Escribir un programa Python que calcule la rentabilidad de un depósito anual de 234.000 € al 4.5%
y la muestre en pantalla.
'''

Depositoanual=int(input(" depósito anual "))

Interesanual=float(input(" interes anual "))

Interesesanuales= int(Depositoanual*Interesanual)

print( " Intereses en un año", Interesesanuales)

Capitalfinal=int(Interesesanuales+Depositoanual)

print("Capital acumulado al final del año con los intereses", Capitalfinal)

Rentabilidadanual=(Capitalfinal-Depositoanual)/Depositoanual

print("Rentabilidad anual TIR", Rentabilidadanual)


''' Me ha llevado tiempo meter el decimal como float, pero como se resolvia
el ejercicio ha sido fácil de plantear'''

