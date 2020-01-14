import math

graph = [[0,3,0,4],
         [3,0,1,5],
         [0,1,0,2],
         [4,5,2,0]]

source = 0
nodeNumber = len(graph) #numero di elementi (qui il numero di parentesi)

labelList = [math.inf for i in range(nodeNumber)]
labelList[source] = 0   #labelList = [0,infinito, infinito, infinito]

unexploredNodes = [i for i in range(nodeNumber)]

#dobbiamo trovare il nodo con label minore perchè al primo giro è il nodo sorgente
while len(unexploredNodes) > 0:

    print(unexploredNodes)

    minLabel = min([labelList[node] for node in unexploredNodes])   #minLabel = 0 al primo turno

    for i in unexploredNodes:
        if labelList[i] == minLabel:
            currentNode = i
        else:
            break
    
    print(currentNode)
    unexploredNodes.remove(currentNode) #togliamo ogni volta così che prima o poi si esce dal while

    for neighbourNode, weight in enumerate(graph[currentNode]):   #facciamo un for per controllare la i vicini di ogni nodo
        if(weight > 0): #per vedere quali nodi sono vicini quindi quali pesi sono > 0
            distance = labelList[currentNode] + weight
            if(distance < labelList[neighbourNode]):
                labelList[neighbourNode] = distance
        

print("Pesi di ogni nodo: ")
print(labelList)