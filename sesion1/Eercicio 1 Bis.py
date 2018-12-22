'''
Escribir un programa Python que muestre en pantalla la hora actual en el formato hh:mm:ss
sabiendo que han transcurrido 75936 segundos desde las doce de la noche.
'''

dimelahora=int(input("dime los segundos que han pasado desde las 12 de la noche "))

horas=int(dimelahora/3600)

minutosa=dimelahora%3600

minutos=int(minutosa/60)

segundos=minutosa%60

n=""
if not horas==0:
    n+=(str(horas) + " horas ")
if not minutos==0:
    n+=(str(minutos) + " minutos ")
if not segundos==0:
    n+=(str(segundos) + " segundos ")

print(n)



