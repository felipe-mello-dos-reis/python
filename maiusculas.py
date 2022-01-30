def maiusculas(frase):
    string = ''
    for char in frase:
        if char >= 'A' and char <= 'Z':
            string += char
    return string
