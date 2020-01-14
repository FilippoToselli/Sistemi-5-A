import math

print("Inserire la grandezza della matrice: ")
grandezzaMatrice = int(input())

for k in range(grandezzaMatrice):
    for i in range(grandezzaMatrice):
        graph[k][i] = False

dizionarioAdiacenze = {0:[1], 1:[0,3], 2:[5], 3:[1,4,7], 4:[3], 5:[2,6], 6:[5,7], 7:[6]}

def creaMatrice(dizAd):
    

def dijkstra(matAdiacenza, nodoSorgente):
    labelList = [math.inf] * len(graph) #inizializzazione delle label (moltiplico il numero di nodi per le righe)
    labelList[0] = 0                    #distanza dal nodo sorgente = 0

    unexploredNode = len(matAdiacenza[0])   #nodi da esplorare

    cntPasso=0

    while unexploredNode>0:
        print("Passo numero: %d"% cntPasso)
        print("Nodi inesplorati: ", unexploredNode)
        print("Lista delle label: ", labelList)
        print("-----------------------------------------------")
        #scelgo il nodo con label minore(k)
        infiniteList = [math.inf] * len(matAdiacenza)
        
        for i in unexploredNode:
            infiniteList[i]=labelList[i]    #valore della labelList[i] 

        if(nodoSorgente==math.inf):  #controllo per uscire dal ciclo
            break
        
        currentNode = infiniteList.index(nodoSorgente)  #prendo l'indice del valore minimo
        for node, weight in enumerate(matAdiacenza[currentNode]):       #ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
            if(weight!=0):   #verifico che sia collegato e che non sia se stesso
                newLabel = labelList[currentNode] + weight
                if(newLabel<labelList[node]):
                labelList[node] = newLabel     #per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente
        
        cntPasso=cntPasso+1
        unexploredNode = unexploredNode - 1    


#-------------------------------------------------------------------

creaMatrice(dizionarioAdiacenze)

dijkstra()