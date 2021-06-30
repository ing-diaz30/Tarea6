def division(a,b):
    return(a/b)

def area_cuadrado(lado):
    return lado*lado
def area_triangulo(base,altura):
    return (base*altura)/2

print("Elija un aopcion")

print("1.Division 2.Area del cuarado 3.Area del triangulo 4.Salir")

op=int(input("ingrese una opcion"))

if op==1:
    numero1=int(input("Ingrese numero uno: "))
    numero2=int(input("Ingrese numero dos: "))
    print("La division es:"+str(division(numero1,numero2)))

elif op==2:
    lad=int(input("Ingrese el lado del cuadrado: "))
    print("El area es"+str(area_cuadrado(lad)))

elif op==3:
    base=int(input("Ingrese la base: "))
    alt=int(input("Ingrese la altura: "))
    print("El area es"+str(area_triangulo(base,alt)))

else:
    print("El programa ha finalizado")def division(a,b):
    return(a/b)

def area_cuadrado(lado):
    return lado*lado
def area_triangulo(base,altura):
    return (base*altura)/2

print("Elija un aopcion")

print("1.Division 2.Area del cuarado 3.Area del triangulo 4.Salir")

op=int(input("ingrese una opcion"))

if op==1:
    numero1=int(input("Ingrese numero uno: "))
    numero2=int(input("Ingrese numero dos: "))
    print("La division es:"+str(division(numero1,numero2)))

elif op==2:
    lad=int(input("Ingrese el lado del cuadrado: "))
    print("El area es"+str(area_cuadrado(lad)))

elif op==3:
    base=int(input("Ingrese la base: "))
    alt=int(input("Ingrese la altura: "))
    print("El area es"+str(area_triangulo(base,alt)))

else:
    print("El programa ha finalizado")