#Este programa reciholabe una frase y la devuelve al reves
input_phrase = input("Escriba una frase: ")
def reversePhrase(input_phrase):
    return input_phrase[::-1]
print(reversePhrase(input_phrase))