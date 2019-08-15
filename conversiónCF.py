print("\n1.- Cálcula el área de un Cuadrado\n")
print("2.- Cálcula el área de un Círculo\n")
print("3.- Cálcula el área de un Triángulo\n")
print("4.- Convierte grados Celsius a Fahrenheit\n")
op = input ("Selecciona una opción: ")

op = int(op)

if (op == 1):
    arg = float(input("\nInserta el valor de alguno de los lados\n "))
    print("El área es: ", arg*4) 
    
if (op == 2):
    arg = float(input("\nInserta el valor del radio\n "))   
    print("El área es: ", arg*(3.1416**2) )
    
if (op == 3):   
    op1 = float(input("\nIngresa el valor de la base\n "))
    op2 = float(input("\nIngresa el valor de la altura\n "))
    print("El área es: ", (op1 * op2)/2)

if (op == 4):
	arg = int(input("¿Cual es la temperatura en grados Fahrenheit?\n "))
	print ("f°   c°")
	print (arg, " ", int((arg - 32)*5/9))

	

