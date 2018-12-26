''' Escribir un programa Python que muestre en pantalla
el número mínimo de billetes y monedas
en que podrían descomponerse 7.532€.'''

dinero=float(input("dinero que quiere descomponer en el menor numero de billetes y monedas posibles"))

billetes_500=int(dinero/500)
resto500=dinero-billetes_500*500

billetes_200=int(resto500/200)
resto200=resto500-billetes_200*200

billetes_100=int(resto200/100)
resto100=resto200-billetes_100*100

billetes_50=int(resto100/50)
resto50=resto100-billetes_50*50

billetes_20=int(resto50/20)
resto20=resto50-billetes_20*20

billetes_10=int(resto20/10)
resto10=resto20-billetes_10*10

billetes_5=int(resto10/5)
resto5=resto10-billetes_5*5

monedas_2=int(resto5/2)
resto2=resto5-monedas_2*2

monedas_1=int(resto2/1)
resto1=resto2-monedas_1*1

monedas_05=int(resto1/0.5)
resto05=resto1-monedas_05*0.5

monedas_02=int(resto05/0.2)
resto02=resto05-monedas_02*0.2

monedas_01=int(resto02/0.1)
resto01=resto02-monedas_01*0.1

monedas_005=int(resto01/0.05)
resto005=resto01-monedas_005*0.05


n=""
if not billetes_500==0:
    n+=str(billetes_500)+" billetes de 500 "
if not billetes_200==0:
    n+=str(billetes_200)+" billetes de 200 "
if not billetes_100==0:
    n+=str(billetes_100)+" billetes de 100 "
if not billetes_50==0:
    n+=str(billetes_50)+" billetes de 50 "
if not billetes_20==0:
    n+=str(billetes_20)+" billetes de 20 "
if not billetes_100==0:
    n+=str(billetes_10)+" billetes de 10 "
if not billetes_5==0:
    n+=str(billetes_5)+" billetes de 5 "
if not monedas_2==0:
    n+=str(monedas_2)+" monedas de 2 "
if not monedas_1==0:
    n+=str(monedas_1)+" monedas de 1 "
if not monedas_05==0:
    n+=str(monedas_05)+" moneda de 0.5 "
if not monedas_02==0:
    n+=str(monedas_02)+" moneda de 0.2 "
if not monedas_01==0:
    n+=str(monedas_01)+" moneda de 0.1 "
if not monedas_005==0:
    n+=str(monedas_005)+" moneda de 0.05 "

print(n)



