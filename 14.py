# Donat un caracter que ens retorni true si es una vocal i fals si no ho es.
def vocal(a):
    if a=="a" or a=="A" or a=="e" or a=="E" or a=="i" or a=="I" or a=="o" or a=="O" or a=="u" or a=="U":
        return True
    else:
        return False

# Programa principal

a = input("escriu un caracter: ")
print("la funcio ens indica si es vocal o consonant",vocal(a))