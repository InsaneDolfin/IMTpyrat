# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 00:14:46 2016

@author: Justin Guirautane
"""

  # Creates an empty priority queue
def create () :
    return []

# Tests if the priority queue is empty
def isEmpty (priorityQueue) :
    return priorityQueue == []

# Appends an element to the priority queue
# If the element exists, it is replaced by the new one
def push (element, score, priorityQueue) :
    for i in priorityQueue :
        (a,b)=i
        if a==element:
            b=score
            return priorityQueue
    priorityQueue.append((element, score))
    return priorityQueue

# Extracts an element from the priority queue
def pop (priorityQueue) :
    i,j=priorityQueue[0]
    index=0
    for i in range (len(priorityQueue)) :
        a,b=priorityQueue[i]
        if b<j:
            j=b
            index=i
    return priorityQueue.pop(index)  

###############################################################################

    
#algorithme de Dijkstra
def dijkstra(mazeMap, playerLocation):
    
    """
    In:
    mazeMap: liste de tuples, donné par PyRat
    playerLocation: tuple donnant la position initiale
    
    Out:
    routage: dictionnaire associant chaque position à son predecesseur
    distances: dictionnaire associant chaque position avec son poid (combien pour y aller depuis le debut)
    """
    
    # initialisation
    tas_min = []
    push(playerLocation, 0, tas_min)
    distances = {node : float("inf") for node in mazeMap}
    distances[playerLocation] = 0
    routage =  {}
    routage[playerLocation]=None #NECESSAIRE OU PAS?
    # boucle de l’algorithme
    while isEmpty (tas_min)==False :
        current_Location, distance = pop (tas_min)
        for voisin in mazeMap[current_Location]:
            dist_par_courant = distance + mazeMap[current_Location][voisin]
            if distances[voisin] > dist_par_courant:
                distances[voisin] = dist_par_courant
                push(voisin, dist_par_courant, tas_min)
                routage[voisin] = current_Location
    return distances,routage
    
    
def cheeseInOrder(mazeMap,playerLocation,piecesOfCheese):
    cheeseInOrder=[]  #liste des positions des fromages ordonnées  
    distance_fromage={} #contient les pos des fromages et la distances à laquelle ils sont de playerLoc
    distances,routage=dijkstra(mazeMap,playerLocation)
    for cheese in piecesOfCheese:
        distance_fromage[cheese]=distances[cheese]
    cheeseInOrder=sorted(distance_fromage, key=distance_fromage.get) #tri par rapport aux values (distances ici)   
    return cheeseInOrder
    
    
def cheeseInOrderAll(mazeMap,playerLocation,piecesOfCheese):
    cheeseInOrderAll=[]
    liste_fromage=piecesOfCheese
    #1er
    cheeseOrder=cheeseInOrder(mazeMap,playerLocation,liste_fromage)
    cheeseInOrderAll.append(cheeseOrder[0])
    liste_fromage.remove(cheeseOrder[0])
    #les autres
    for i in range (0,len(liste_fromage)):
        cheeseOrder=cheeseInOrder(mazeMap,cheeseInOrderAll[-1],liste_fromage)
        cheeseInOrderAll.append(cheeseOrder[0])
        liste_fromage.remove(cheeseOrder[0])
    return cheeseInOrderAll
    

    
    


mazeMap={(7, 3): {(6, 3): 1, (7, 2): 1}, (6, 9): {(6, 8): 1}, (1, 3): {(1, 2): 1, (0, 3): 4, (1, 4): 1}, (4, 8): {(4, 7): 1, (4, 9): 4}, (3, 0): {(2, 0): 1, (3, 1): 1}, (2, 8): {(2, 7): 1, (3, 8): 2, (2, 9): 6}, (9, 8): {(9, 9): 10, (9, 7): 5}, (8, 0): {(8, 1): 5, (9, 0): 5, (7, 0): 1}, (0, 7): {(0, 6): 9, (0, 8): 1, (1, 7): 5}, (6, 2): {(6, 1): 5, (5, 2): 1}, (1, 6): {(1, 5): 3, (2, 6): 1}, (3, 7): {(3, 8): 2, (4, 7): 7, (3, 6): 7}, (2, 5): {(2, 4): 1, (3, 5): 8}, (8, 5): {(8, 6): 1, (7, 5): 7}, (5, 8): {(5, 9): 1, (5, 7): 1, (6, 8): 10}, (4, 0): {(5, 0): 6}, (9, 0): {(8, 0): 5, (9, 1): 1}, (6, 7): {(5, 7): 1, (6, 6): 2, (7, 7): 2, (6, 8): 1}, (5, 5): {(5, 6): 8, (5, 4): 10, (6, 5): 6}, (7, 6): {(7, 5): 1, (7, 7): 9}, (5, 0): {(5, 1): 9, (6, 0): 1, (4, 0): 6}, (0, 4): {(0, 3): 1, (1, 4): 9}, (3, 5): {(4, 5): 9, (2, 5): 8, (3, 6): 1}, (1, 1): {(1, 2): 7, (0, 1): 1, (2, 1): 1}, (3, 2): {(3, 3): 1, (2, 2): 1}, (2, 6): {(1, 6): 1, (3, 6): 1}, (8, 2): {(8, 3): 1}, (4, 5): {(4, 6): 1, (3, 5): 9}, (9, 3): {(9, 2): 1, (8, 3): 1, (9, 4): 5}, (6, 0): {(6, 1): 3, (7, 0): 1, (5, 0): 1}, (1, 4): {(1, 5): 1, (1, 3): 1, (2, 4): 8, (0, 4): 9}, (7, 5): {(7, 6): 1, (8, 5): 7, (6, 5): 1}, (2, 3): {(2, 4): 1, (3, 3): 9, (2, 2): 9}, (1, 9): {(0, 9): 1, (1, 8): 8, (2, 9): 1}, (8, 7): {(8, 6): 7, (8, 8): 1, (7, 7): 1}, (4, 2): {(5, 2): 1, (4, 1): 1, (4, 3): 1}, (9, 6): {(9, 5): 10, (9, 7): 6}, (6, 5): {(6, 4): 1, (7, 5): 1, (5, 5): 6, (6, 6): 1}, (5, 3): {(6, 3): 1, (5, 4): 1}, (0, 1): {(0, 0): 5, (1, 1): 1, (0, 2): 3}, (7, 0): {(8, 0): 1, (6, 0): 1}, (6, 8): {(7, 8): 1, (6, 9): 1, (6, 7): 1, (5, 8): 10}, (3, 1): {(3, 0): 1, (2, 1): 6}, (9, 9): {(8, 9): 1, (9, 8): 10}, (0, 6): {(0, 5): 1, (0, 7): 9}, (1, 7): {(2, 7): 1, (1, 8): 2, (0, 7): 5}, (0, 9): {(1, 9): 1}, (7, 8): {(6, 8): 1, (7, 7): 1}, (2, 4): {(3, 4): 3, (2, 5): 1, (2, 3): 1, (1, 4): 8}, (8, 4): {(9, 4): 4}, (5, 9): {(4, 9): 5, (5, 8): 1}, (4, 7): {(3, 7): 7, (5, 7): 1, (4, 6): 1, (4, 8): 1}, (9, 1): {(9, 2): 1, (9, 0): 1}, (6, 6): {(5, 6): 3, (6, 7): 2, (6, 5): 1}, (5, 6): {(5, 7): 8, (6, 6): 3, (5, 5): 8, (4, 6): 1}, (7, 7): {(6, 7): 2, (7, 6): 9, (7, 8): 1, (8, 7): 1}, (2, 1): {(2, 0): 10, (3, 1): 6, (1, 1): 1}, (8, 9): {(8, 8): 2, (9, 9): 1, (7, 9): 3}, (9, 4): {(9, 5): 1, (9, 3): 5, (8, 4): 4}, (5, 1): {(4, 1): 1, (5, 0): 9}, (0, 3): {(1, 3): 4, (0, 2): 9, (0, 4): 1}, (7, 2): {(7, 3): 1, (7, 1): 1}, (1, 2): {(1, 3): 1, (1, 1): 7, (2, 2): 4}, (3, 8): {(3, 7): 2, (2, 8): 2}, (4, 9): {(5, 9): 5, (3, 9): 10, (4, 8): 4}, (3, 3): {(3, 2): 1, (2, 3): 9}, (2, 9): {(2, 8): 6, (3, 9): 9, (1, 9): 1}, (8, 1): {(8, 0): 5, (7, 1): 1}, (4, 4): {(5, 4): 1, (3, 4): 1}, (6, 3): {(6, 4): 1, (5, 3): 1, (7, 3): 1}, (1, 5): {(1, 6): 3, (0, 5): 1, (1, 4): 1}, (8, 8): {(8, 9): 2, (8, 7): 1}, (3, 6): {(3, 7): 7, (2, 6): 1, (3, 5): 1}, (2, 2): {(1, 2): 4, (3, 2): 1, (2, 3): 9}, (8, 6): {(8, 5): 1, (8, 7): 7}, (4, 1): {(5, 1): 1, (4, 2): 1}, (9, 7): {(9, 8): 5, (9, 6): 6}, (6, 4): {(7, 4): 1, (6, 3): 1, (6, 5): 1}, (5, 4): {(4, 4): 1, (5, 5): 10, (5, 3): 1}, (0, 0): {(0, 1): 5, (1, 0): 2}, (7, 1): {(8, 1): 1, (6, 1): 1, (7, 2): 1}, (0, 5): {(0, 6): 1, (1, 5): 1}, (1, 0): {(2, 0): 6, (0, 0): 2}, (0, 8): {(1, 8): 3, (0, 7): 1}, (7, 9): {(8, 9): 3}, (2, 7): {(2, 8): 1, (1, 7): 1}, (8, 3): {(9, 3): 1, (8, 2): 1}, (4, 6): {(4, 5): 1, (5, 6): 1, (4, 7): 1}, (9, 2): {(9, 3): 1, (9, 1): 1}, (3, 4): {(4, 4): 1, (2, 4): 3}, (6, 1): {(6, 2): 5, (6, 0): 3, (7, 1): 1}, (5, 7): {(5, 6): 8, (4, 7): 1, (6, 7): 1, (5, 8): 1}, (7, 4): {(6, 4): 1}, (2, 0): {(3, 0): 1, (1, 0): 6, (2, 1): 10}, (1, 8): {(0, 8): 3, (1, 9): 8, (1, 7): 2}, (3, 9): {(4, 9): 10, (2, 9): 9}, (4, 3): {(4, 2): 1}, (9, 5): {(9, 6): 10, (9, 4): 1}, (5, 2): {(4, 2): 1, (6, 2): 1}, (0, 2): {(0, 1): 3, (0, 3): 9}}
mazeMap2={(0,0):{(0,1):1,(1,0):1},(0,1):{(0,0):1,(0,2):1,(1,1):1},(0,2):{(0,1):1,(0,3):1,(1,2):1},(0,3):{(0,2):1,(0,4):1,(1,3):1},(0,4):{(0,3):1,(1,4):1},(1,0):{(1,1):1,(2,0):1,(0,0):1},(1,1):{(1,0):1,(1,2):1,(2,1):1,(0,1):1},(1,2):{(1,1):1,(1,3):1,(2,2):1,(0,2):1},(1,3):{(1,2):1,(1,4):1,(0,3):1,(2,3):1},(1,4):{(1,3):1,(2,4):1,(0,4):1},(2,0):{(2,1):1,(3,0):1,(1,0):1},(2,1):{(2,0):1,(2,2):1,(3,1):1,(1,1):1},(2,2):{(2,1):1,(2,3):1,(3,2):1,(1,2):1},(2,3):{(2,2):1,(2,4):1,(1,3):1,(3,3):1},(2,4):{(2,3):1,(3,4):1,(1,4):1},(3,0):{(3,1):1,(4,0):1,(2,0):1},(3,1):{(3,0):1,(3,2):1,(4,1):1,(2,1):1},(3,2):{(3,1):1,(3,3):1,(4,2):1,(2,2):1},(3,3):{(3,2):1,(3,4):1,(2,3):1,(4,3):1},(3,4):{(3,3):1,(4,4):1,(2,4):1},(4,0):{(4,1):1,(3,0):1},(4,1):{(4,0):1,(4,2):1,(3,1):1},(4,2):{(4,1):1,(4,3):1,(3,2):1},(4,3):{(4,2):1,(4,4):1,(3,3):1},(4,4):{(4,3):1,(3,4):1}}
playerLocation=(0,0)
piecesOfCheese=[(1,9),(4,9),(0,4),(4,3),(4,0),(2,0),(5,1),(9,9),(0,7),(2,4)]
piecesOfCheese2=[(4,0),(0,4),(2,0)]


l=cheeseInOrder(mazeMap2,playerLocation,piecesOfCheese2)
a=cheeseInOrderAll(mazeMap2,playerLocation,piecesOfCheese2)
print(l)
print('\n\n')
print(a)
print('\n\n\n\n')

