# Funcion que calcula si un año es bisiesto

def bisiesto():
    year = int(input("Introduce un año: "))
    if year%4 == 0:
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")



bisiesto()
