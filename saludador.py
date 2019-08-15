nombre = input("¿Cuál es tu nombre?\n  " )
saludo = "Hola, "
print(saludo, nombre,"!")

monedas = int(input("¿Cuántas monedas tienes?\n  "))
siguiente = monedas + 1
print ("Yo tengo más. Tengo ", siguiente)

t = float(input("¿En cuantos segs corres 100m?\n  "))
dif = t%9.58
print("Eres", dif, "segundos más lento que Bolt  ")

mensaje = input("Ahora vamos, dime un pensamiento.\n  ")
print()
print("---------------------------------------------------------------")
print(nombre, "dice:", mensaje)
print("---------------------------------------------------------------")

llueve = True
temperatura = int(input("Mmm... Ingresa la temp\n "))

if temperatura >= 22:
	print("No cargues de más llevando paraguas y suéter")
elif llueve == True:
	print("Lleva paraguas y suéter")	
else: 
	print("Solo lleva un suéter")	
print("Te leo después. Adiós! ")


