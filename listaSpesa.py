lista=[]
y=7
print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
while y!=0:
    y=int(input("fai la tua scelta"))
    if y==1:
        
        lista.agg_elemento()
    if y==2:
        lista.visua_elemento()
        if lista==[]:
            print("la lista è vuota")
    if y==3:
        
        for lista in i:
            if x==lista[i]:
                lista.rim_elemento()
    if y==4:
        lista.cont_elemento

    if y==5:
        input("scrivi il nome dell'elemento che vuoi togliere")
        lista.rim_elemento()





def agg_elemento():
    x=input("aggiungi un elemento")
    lista.append(x) #l'input lo facciamo nel main

def visua_elemento():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")

def rim_elemento():
    x=int(input("scegli l'elemento da togliere"))
    lista.pop(x)

def cont_elemento():
    x=len(lista)
    print(f"la tua lista è lunga {x} elementi")