def encontra_impares(lista, impares = None):
    if impares == None:
        impares = []
    if lista[0]%2 == 1:
        impares.append(lista[0])
    if len(lista)>1:
        encontra_impares(lista[1:], impares)
    return impares

print(encontra_impares([1,2,3,4,5,6,7]))
