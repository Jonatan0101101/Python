def sumar_llista(a):
    sumatori=0
    for i in a:
        sumatori+= (i*i)
    return sumatori
def multiplicar_lista(lista):
    multiplicado=1
    for x in lista:
         multiplicado*= x
    return multiplicado

y=[1,3,4,5,7]
print("El sumatori es: ",sumar_llista(y))




