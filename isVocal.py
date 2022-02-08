#Este programa recibe un caracter y devuelve si es vocal o no
input_char = input("Ingrese un caracter: ")

def isVocal(input_char):
    if 'aeiou'.find(input_char.lower())>-1:
        return True
    else:
        return False


print(isVocal(input_char))
