import string #cadena de plantilla
def listAlphabet(): #Almacenamiento de información
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]


print(listAlphabet())