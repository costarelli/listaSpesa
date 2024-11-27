lista=[]
y=7
print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento ")
def agg_elemento(lista):
    x=input("aggiungi un elemento")
    lista.append(x)

def visua_elemento(lista):
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def rim_elemento(lista):
    x=int(input("scegli l'elemento da togliere"))
    lista.pop(x)

def cont_elemento(lista):
    x=len(lista)
    print(f"la tua lista è lunga {x} elementi")

while y!=0:
    y=int(input("fai la tua scelta "))
    if y==1:
        
        
        agg_elemento(lista)
    if y==2:
        visua_elemento(lista)
        if lista==[]:
            print("la lista è vuota")
    if y==3:
        
        for lista in i:
            if x==lista[i]:
                rim_elemento(lista)
    if y==4:
        cont_elemento(lista)

    if y==5:
        input("scrivi il nome dell'elemento che vuoi togliere")
        rim_elemento(lista)