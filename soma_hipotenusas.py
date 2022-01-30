def e_hipotenusa(n):
    a = 1
    while a < n:
        b = 1
        while b < n:
            if n**2 == a**2 + b**2:
                return True
            b+=1
        a+=1
    return False


def soma_hipotenusas(n):
    i = 1
    cont = 0
    while i <= n:
        if e_hipotenusa(i):
            cont+=i
        i+=1
    #return cont
    return cont