''' Dado el número entero 753,
 escribir un programa Python que escriba en pantalla sus cifras en orden inverso.'''

numero=int(input(" escriba un número de tres cifras"))

#Luego invertimos el numero. Se puede hacer mediante manejo de strings, pero aca lo haremos de modo matematico.
#Obtenemos el primer digito
digito_1 = int(numero/100)

#Luego, obtenemos el segundo digito
numero = numero%100
digito_2 = int(numero/10)

#Y finalmente, obtenemos el tercer digito
digito_3 = numero%10

#Ahora, hace falta invertir el numero y mostrarlo en pantalla
numero_inv=digito_3,digito_2,digito_1

input(numero_inv)

