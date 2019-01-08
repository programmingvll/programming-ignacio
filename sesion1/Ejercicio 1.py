#dhdb

'''
Escribir un programa Python que muestre en pantalla la hora actual en el formato hh:mm:ss
sabiendo que han transcurrido 75936 segundos desde las doce de la noche.
'''


segundos=int(input("dime los segundos que han pasado desde las 12 de la noche "))

horas=segundos%3600

print(horas)

minutos=horas%60

print(minutos)

horasreloj=int(segundos/3600)

minutosreloj=int(horas/60)

segundosreloj=minutos

print(horasreloj,minutosreloj,segundosreloj)

