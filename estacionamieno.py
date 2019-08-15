
pesos_por_hora = 45;
llegada = int(input("Hora de llegada  "))%24
salida = int(input("Hora de salida  "))%24;

if salida > llegada: 
	precio = (llegada - salida)%24 * pesos_por_hora	
else: 
	precio = (salida -llegada)%24 * pesos_por_hora
       
print(precio)       
print("Buen viaje")
    
