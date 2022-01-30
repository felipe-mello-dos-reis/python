def conta_letras(frase,contar="vogais"):
    vogais = consoantes = 0
    for char in frase:
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U" or char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vogais+=1
        elif (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
            consoantes+=1 
    if contar == "vogais":
        return vogais
    else:
        return consoantes