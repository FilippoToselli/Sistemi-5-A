import math
import random

print("Inserire grandezza matrice: ")
grandezzaMatrice = int(input())

graph = [grandezzaMatrice][grandezzaMatrice]

print("Inserire percentuale di zeri: ")
percZeri = int(grandezzaMatrice * int(input())) / 10

for r in range(grandezzaMatrice):
    for c in range(grandezzaMatrice):
        if(r == c):
            graph[r][c] = 0
        else:
            graph[r][c] = math.inf


unexploredNode = []   #nodi da esplorare
k = 0

for k in range(grandezzaMatrice):
    unexploredNode.insert(K)

for r in range(grandezzaMatrice):
    for c in range(grandezzaMatrice):
        if(random.randrange(0,101) < percZeri):
            graph[r][c] = 0
        else:
            graph[r][c] = random.randrange(1,10)


cntPasso=0

while len(unexploredNode)>0:
    print("Passo numero: %d"% cntPasso)
    print("Nodi inesplorati: ", unexploredNode)
    print("Lista delle label: ", labelList)
    print("-----------------------------------------------")
    #scelgo il nodo con label minore(k)
    infiniteList = [math.inf] * len(graph)
    
    for i in unexploredNode:
        infiniteList[i]=labelList[i]    #valore della labelList[i] 
    
    minimun = min(infiniteList)   #trovo il minimo

    if(minimun==math.inf):  #controllo per uscire dal ciclo
        break
    
    currentNode = infiniteList.index(minimun)  #prendo l'indice del valore minimo
    for node, weight in enumerate(graph[currentNode]):       #ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
        if(weight!=0):   #verifico che sia collegato e che non sia se stesso
            newLabel = labelList[currentNode] + weight
            if(newLabel<labelList[node]):
               labelList[node] = newLabel     #per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente
    
    cntPasso=cntPasso+1
    unexploredNode.remove(currentNode)    #rimuovo l'indice visitato  