#ejemplo de uso de listas
misnovias=["melany","robertote","kevin","ARK"]
misNumeros=[777,2210,666,64]
#Mostrando mis novias
print(misnovias)
#Mostrando mis numeros
print(misNumeros)
print("---accediendo a los elementos de la lista---")
print(misnovias[-2],"\n")
if "yo" in misnovias:
    print("si, 'melany' esta en la lista de mis novias")
else:
    print("chale, no eres mi chava")
print("Numero de novias")
Nnovias=len(misnovias)
print(f"Numero de novias: {Nnovias}")
print("\nciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1