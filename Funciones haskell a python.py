def factorial(n):
    if (n==0):
        return 1
    else:
        return n* factorial(n-1)
n=int(input("\nIngrese un número  "))
print("El facotiral del número es " + str(factorial(n))) 
        
def cuadrado(n):
    if (n==1):
        return 1
    else:
        return n * n
n = int(input("\nIngrese un número  "))
print ("El cuadrado del número es  " + str(cuadrado(n)))


def sumaLista(lista):
    if len(lista)== 1:
        return lista[0]
    else:
        return lista[0]+sumaLista(lista[1:])
print ("La suma de la lista [2,3,4] es  "+  str(sumaLista([2,3,4])))

def invertir(lista):
    if lista == " ":
        return lista
    else:
        return reverse(lista[1:])+lista[0]
def mayor(list):
    if len(list) == 1:
        return list[0]
    else:
        m = mayor(list[1:])
        return m if m > list[0] else list[0]
list = eval(input("Ingrese una lista de números: "))
print("El mayor elemento de la lista es: ", mayor(list))






    
