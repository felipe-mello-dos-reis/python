largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
l = a = 1
while a <= altura:
    if a == 1 or a == altura:
        while l <= largura:
            print("#", end = "")
            l+=1
    else:
        print("#", end = "")
        l=3
        while l <= largura:
            print(" ", end = "")
            l+=1
        print("#", end = "")

    l=1
    a+=1
    print()