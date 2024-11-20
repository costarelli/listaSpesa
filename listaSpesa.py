lista=[]
def agg_elemento(x, lista):
    lista.append(x) #l'input lo facciamo nel main

def visua_elemento(lista):
    for i in range(len(lista)):
    print(f"{i + 1}. {lista[i]}")
