#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################################################################################################################################################################################################################################
############################################# PRE-DEFINED CONSTANTS ############################################# ############################################ CONSTANTES PRÉ-DÉFINIES ############################################
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    In this section, you will find some pre-defined constants that are needed for the game                      #    Dans cette section, vous trouvez des constantes pré-définies nécessaires pour la partie                     #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    TEAM_NAME : string                                                                                          #    TEAM_NAME : string                                                                                          #
#    ------------------                                                                                          #    ------------------                                                                                          #
#                                                                                                                #                                                                                                                #
#        This constant represents your name as a team                                                            #        Cette constante représente le nom de votre équipe                                                       #
#        Please change the default value to a string of your choice                                              #        Veuillez en changer la valeur par une chaîne de caractères de votre choix                               #
#                                                                                                                #                                                                                                                #
#    MOVE_XXX : char                                                                                             #    MOVE_XXX : char                                                                                             #
#    ---------------                                                                                             #    ---------------                                                                                             #
#                                                                                                                #                                                                                                                #
#        The four MOVE_XXX constants represent the possible directions where to move                             #        Les quatre constantes MOVE_XXX représentent les directions possibles où se déplacer                     #
#        The "turn" function should always return one of these constants                                         #        La fonction "turn" doit toujours renvoyer l'une d'entre elles                                           #
#        Please do not edit them (any other value will be considered incorrect and thus ignored)                 #        Merci de ne pas les éditer (toute autre valeur sera considérée comme incorrecte et sera ignorée)        #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################

TEAM_NAME = "Your name here"

MOVE_DOWN = 'D'
MOVE_LEFT = 'L'
MOVE_RIGHT = 'R'
MOVE_UP = 'U'

###################################################################################################################################################################################################################################
########################################### SPACE FOR FREE EXPRESSION ########################################### ############################################ ZONE D'EXPRESSION LIBRE ############################################
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    In this file, you will two functions: "preprocessing" and "turn"                                            #    Dans ce fichier, vous trouverez deux fonctions : "preprocessing" et "turn"                                  #
#    You need to edit these functions to create your PyRat program                                               #    Vous devez éditer ces fonctions pour réaliser votre programme PyRat                                         #
#    However, you are not limited to them, and you can write any Python code in this file                        #    Toutefois, vous n'êtes pas limité(e), et vous pouvez écrire n'importe quel code Python dans ce fichier      #
#    Please use the following space to write your additional constants, variables, functions...                  #    Merci d'utiliser l'espace ci-dessous pour écrire vos constantes, variables, fonctions...                    #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################


#location: doublé représantant les coordonnées d'une case


def inverse(liste):#inverse l'ordre des elements d'une liste
    inverse=[]
    for i in liste:
        inverse.append(liste.pop())
    return inverse

def aboveof(location):                      #Renvoi les coordonnées de la case au dessus de celle en argument
    loc=(0,0)
    if location[0]!=0:
        loc=(location[0]-1,location[1])
        return loc
    else:
        return location

def belowof(location,mazeHeight):                      #Renvoi les coordonnées de la case au dessOus de celle en argument
    loc=(0,0)
    if location[0]!=mazeHeight-1:
        loc=(location[0]+1,location[1])
        return loc
    else:
        return location
        
def rightof(location,mazeWidth):                      #Renvoi les coordonnées de la case à droite de celle en argument
    loc=(0,0)
    if location[1]!=mazeWidth-1:
        loc=(location[0],location[1]+1)
        return loc
    else:
        return location
        
def leftof(location):                       #Renvoi les coordonnées de la case à de celle en argument
    loc=(0,0)
    if location[1]!=0:
        loc=(location[0],location[1]-1)
        return loc
    else:
        return location
        
def canMove(mazeMap, fromLocation, toLocation): #Renvoi True si le passage est possible, False si le chemin est barré
    return toLocation in mazeMap [fromLocation]

def getMove (mazeMap, fromLocation, toLocation,mazeHeight,mazeWidth):   #bouge à la case voisine (toLocation) si le mouvement est possible
    currentLocation=fromLocation
    if canMove(mazeMap, fromLocation, toLocation):
        if toLocation==aboveof(fromLocation):
            return MOVE_UP
        elif toLocation==belowof(fromLocation,mazeHeight):
            return MOVE_DOWN
        elif toLocation==rightof(fromLocation,mazeWidth):
            return MOVE_RIGHT
        else :
            return MOVE_LEFT
    else:
        return None
        
def create () :
    l=[]
    return l
 
# Tests if the queue is empty
def isEmpty (queue) :
    return len(queue)==0
 
# Appends an element to the queue
def push (element, queue) :
     queue.append(element)
     return queue
     
# Extracts an element from the queue
def pop (queue) :
    queue.pop(0)
    return queue
    
    
#Parcours en largeur
def parcours(mazeMap,playerLocation):
    structure_d_attente=[]
    structure_d_attente.append(playerLocation)
    routage={}                                              #dictionnaire pour faire une table de routage. Clef=sommets_marqués, renvoi sur predecesseur
    routage[playerLocation]=None                             #le sommet de depart n'a pas de prédecesseur
    while structure_d_attente!=[]:
        sommet_courant=structure_d_attente.pop(0)           #Pour enlever le Premier element (mode FIFO)
        for i in mazeMap[sommet_courant]:                   #on parcours les voisins de sommet_courant
            if i not in routage:                            #si i n'est PAS dans les sommets_marques:
                routage[i]=sommet_courant                   #on ajoute à la table l'élément et son prédecesseur
                structure_d_attente.append(i)               #on enleve l'élement i de la structure d'attente)
    return routage


#calcul le chemin le plus court de A à B    
def chemin_court(mazeMap,playerLocation,piecesOfCheese,num_cheese):
    global cases_a_parcourir
    routage=parcours(mazeMap,playerLocation)                     #On créé la table de routage
    cases_a_parcourir=[piecesOfCheese[num_cheese]]                   #liste de toutes les cases à parcourir (on part de l'arrivé et on cherche les prédeceseurs successif)
    predecesseur=piecesOfCheese[num_cheese]
    while predecesseur!=playerLocation:                  #tant qu'on est pas au point de depart
        cases_a_parcourir.append(routage[predecesseur]) #on ajoute le predecesseur
        predecesseur=routage[predecesseur]              #on cherche le predecesseur du predecesseur
    cases_a_parcourir.pop()                           #on enleve la pos de depart
    return cases_a_parcourir
    
#chemin pour tous les fromages        
def chemin_total(mazeMap,playerLocation,piecesOfCheese):
    global chemin
    chemin_intermediaire=[]
    chemin=chemin_court(mazeMap,playerLocation,piecesOfCheese,0)
    for i in range (1,len(piecesOfCheese)):
        chemin_intermediaire=chemin_court(mazeMap,piecesOfCheese[i-1],piecesOfCheese,i)
        chemin=chemin_intermediaire+chemin
    return chemin
    





###################################################################################################################################################################################################################################
############################################# PREPROCESSING FUNCTION ############################################ ########################################### FONCTION DE PRÉ-TRAITEMENT ##########################################
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    This function is executed once at the very beginning of the game                                            #    Cette fonction est exécutée une unique fois au tout début de la partie                                      #
#    It allows you to make some computations before the players are allowed to move                              #    Vous pouvez y effectuer des calculs avant que les joueurs ne puissent commencer à bouger                    #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    mazeMap : dict(pair(int, int), dict(pair(int, int), int))                                                   #    mazeMap : dict(pair(int, int), dict(pair(int, int), int))                                                   #
#    ---------------------------------------------------------                                                   #    ---------------------------------------------------------                                                   #
#                                                                                                                #                                                                                                                #
#        Map of the maze as a data structure                                                                     #        Structure de données représentant la carte du labyrinthe                                                #
#        mazeMap[x] gives you the neighbors of cell x                                                            #        mazeMap[x] renvoie les voisins de la case x                                                             #
#        mazeMap[x][y] gives you the weight of the edge linking cells x and y                                    #        mazeMap[x][y] renvoie le poids de l'arête reliant les cases x et y                                      #
#        if mazeMap[x][y] is undefined, there is no edge between cells x and y                                   #        Si mazeMap[x][y] n'est pas défini, les cases x et y ne sont pas reliées par une arête                   #
#                                                                                                                #                                                                                                                #
#    mazeWidth : int                                                                                             #    mazeWidth : int                                                                                             #
#    ---------------                                                                                             #    ---------------                                                                                             #
#                                                                                                                #                                                                                                                #
#        Width of the maze, in number of cells                                                                   #        Largeur du labyrinthe, en nombre de cases                                                               #
#                                                                                                                #                                                                                                                #
#    mazeHeight : int                                                                                            #    mazeHeight : int                                                                                            #
#    ----------------                                                                                            #    ----------------                                                                                            #
#                                                                                                                #                                                                                                                #
#        Height of the maze, in number of cells                                                                  #        Hauteur du labyrinthe, en nombre de cases                                                               #
#                                                                                                                #                                                                                                                #
#    playerLocation : pair(int, int)                                                                             #    playerLocation : pair(int, int)                                                                             #
#    -------------------------------                                                                             #    -------------------------------                                                                             #
#                                                                                                                #                                                                                                                #
#        Initial location of your character in the maze                                                          #        Emplacement initial de votre personnage dans le labyrinthe                                              #
#        It is a pair (line, column), with (0, 0) being the top-left cell in the maze                            #        C'est une paire (ligne, colonne), (0, 0) étant la case en haut à gauche du labyrinthe                   #
#        playerLocation[0] gives you your current line                                                           #        playerLocation[0] renvoie votre ligne actuelle                                                          #
#        playerLocation[1] gives you your current column                                                         #        playerLocation[1] renvoie votre colonne actuelle                                                        #
#        mazeMap[playerLocation] gives you the cells you can access directly                                     #        mazeMap[playerLocation] renvoie les cases auxquelles vous pouvez accéder directement                    #
#                                                                                                                #                                                                                                                #
#    opponentLocation : pair(int, int)                                                                           #    opponentLocation : pair(int, int)                                                                           #
#    ---------------------------------                                                                           #    ---------------------------------                                                                           #
#                                                                                                                #                                                                                                                #
#        Initial location opponent's character in the maze                                                       #        Emplacement initial du personnage de votre adversaire dans le labyrinthe                                #
#        The opponent's location can be used just as playerLocation                                              #        La position de l'adversaire peut être utilisée comme pour playerLocation                                #
#        If you are playing in single-player mode, this variable is undefined                                    #        Si vous jouez en mode un joueur, cette variable n'est pas définie                                       #
#                                                                                                                #                                                                                                                #
#    piecesOfCheese : list(pair(int, int))                                                                       #    piecesOfCheese : list(pair(int, int))                                                                       #
#    -------------------------------------                                                                       #    -------------------------------------                                                                       #
#                                                                                                                #                                                                                                                #
#        Locations of all pieces of cheese in the maze                                                           #        Emplacements des morceaux de fromage dans le labyrinthe                                                 #
#        The locations are given in no particular order                                                          #        Les emplacements sont données dans un ordre quelconque                                                  #
#        As for the players locations, these locations are pairs (line, column)                                  #        Comme pour les positions des joueurs, ces emplacements sont des paires (ligne, colonne)                 #
#                                                                                                                #                                                                                                                #
#    timeAllowed : float                                                                                         #    timeAllowed : float                                                                                         #
#    -------------------                                                                                         #    -------------------                                                                                         #
#                                                                                                                #                                                                                                                #
#        Time that is allowed for preprocessing, in seconds                                                      #        Temps alloué pour le pré-traitement, en secondes                                                        #
#        After this time, players will have the right to move                                                    #        Après ce temps, les joueurs pourront commencer à bouger                                                 #
#        If your preprocessing is too long, you will still finish it                                             #        Si votre pré-traitement est trop long, vous terminerez quand même son exécution                         #
#        However, it will not prevent your opponent from moving                                                  #        Toutefois, cela n'empêchera pas votre adversaire de bouger                                              #
#        Make sure to finish your preprocessing within the allowed time                                          #        Assurez vous de terminer votre pré-traitement dans le temps imparti                                     #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    This function does not return anything                                                                      #    Cette fonction ne renvoie rien                                                                              #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################

def preprocessing (mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, piecesOfCheese, timeAllowed) :
    
    # Example prints that appear in the shell only at the beginning of the game
    print("<b>[mazeMap]</b> " + repr(mazeMap))
    print("<b>[mazeWidth]</b> " + repr(mazeWidth))
    print("<b>[mazeHeight]</b> " + repr(mazeHeight))
    print("<b>[playerLocation]</b> " + repr(playerLocation))
    print("<b>[opponentLocation]</b> " + repr(opponentLocation))
    print("<b>[piecesOfCheese]</b> " + repr(piecesOfCheese))
    print("<b>[timeAllowed]</b> " + repr(timeAllowed))
    print(str(aboveof(playerLocation)))
    print(str(belowof(playerLocation,mazeHeight)))
    print(str(rightof(playerLocation,mazeWidth)))
    print(str(leftof(playerLocation)))
    print(str(canMove(mazeMap,playerLocation,(0,1))))
    print(str(getMove (mazeMap, playerLocation, (0,1),mazeHeight,mazeWidth)))
    print("<b>[parcours]</b> " + str(parcours(mazeMap,playerLocation)))
    print("<b>[chemin le plus court]</b> " + str(chemin_total(mazeMap,playerLocation,piecesOfCheese)))

    

###################################################################################################################################################################################################################################
################################################# TURN FUNCTION ################################################# ############################################ FONCTION DE TOUR DE JEU ############################################
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    Once the preprocessing is over, the game starts and players can start moving                                #    Une fois le pré-traitement terminé, la partie démarre et les joueurs peuvent commencer à bouger             #
#    The "turn" function is called at regular times                                                              #    La fonction "turn" est appelée à intervalles réguliers                                                      #
#    You should determine here your next move, given a game configuration                                        #    Vous devez déterminer ici votre prochain mouvement, étant donnée une configuration du jeu                   #
#    This decision will then be applied, and your character will move in the maze                                #    Cette décision sera ensuite appliquée, et votre personnage se déplacera dans le labyrinthe                  #
#    Then, the "turn" function will be called again with the new game configuration                              #    Ensuite, la fonction "turn" sera appelée à nouveau, avec la nouvelle configuration du jeu                   #
#    This process is repeated until the game is over                                                             #    Ce processus est répété jusqu'à la fin de la partie                                                         #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    mazeMap : dict(pair(int, int), dict(pair(int, int), int))                                                   #    mazeMap : dict(pair(int, int), dict(pair(int, int), int))                                                   #
#    ---------------------------------------------------------                                                   #    ---------------------------------------------------------                                                   #
#                                                                                                                #                                                                                                                #
#        Same argument as for the "preprocessing" function                                                       #        Même paramètre que pour la fonction "preprocessing"                                                     #
#        The value of mazeMap does not change between two calls of function "turn"                               #        La valeur de mazeMap ne change pas d'un appel à l'autre de la fonction "turn"                           #
#                                                                                                                #                                                                                                                #
#    mazeWidth : int                                                                                             #    mazeWidth : int                                                                                             #
#    ---------------                                                                                             #    ---------------                                                                                             #
#                                                                                                                #                                                                                                                #
#        Same argument as for the "preprocessing" function                                                       #        Même paramètre que pour la fonction "preprocessing"                                                     #
#        The value of mazeWidth does not change between two calls of function "turn"                             #        La valeur de mazeWidth ne change pas d'un appel à l'autre de la fonction "turn"                         #
#                                                                                                                #                                                                                                                #
#    mazeHeight : int                                                                                            #    mazeHeight : int                                                                                            #
#    ----------------                                                                                            #    ----------------                                                                                            #
#                                                                                                                #                                                                                                                #
#        Same argument as for the "preprocessing" function                                                       #        Même paramètre que pour la fonction "preprocessing"                                                     #
#        The value of mazeHeight does not change between two calls of function "turn"                            #        La valeur de mazeHeight ne change pas d'un appel à l'autre de la fonction "turn"                        #
#                                                                                                                #                                                                                                                #
#    playerLocation : pair(int, int)                                                                             #    playerLocation : pair(int, int)                                                                             #
#    -------------------------------                                                                             #    -------------------------------                                                                             #
#                                                                                                                #                                                                                                                #
#        Current location of your character in the maze                                                          #        Emplacement actuel de votre personnage dans le labyrinthe                                               #
#        At the first call of function "turn", it will be your initial location                                  #        Au premier appel de la fonction "turn", ce sera votre emplacement initial                               #
#                                                                                                                #                                                                                                                #
#    opponentLocation : pair(int, int)                                                                           #    opponentLocation : pair(int, int)                                                                           #
#    ---------------------------------                                                                           #    ---------------------------------                                                                           #
#                                                                                                                #                                                                                                                #
#        Current location of your opponent's character in the maze                                               #        Emplacement actuel de votre personnage dans le labyrinthe                                               #
#        At the first call of function "turn", it will be your opponent's initial location                       #        Au premier appel de la fonction "turn", ce sera votre emplacement initial                               #
#        If you are playing in single-player mode, this variable is undefined                                    #        Si vous jouez en mode un joueur, cette variable n'est pas définie                                       #
#                                                                                                                #                                                                                                                #
#    playerScore : float                                                                                         #    playerScore: float                                                                                          #
#    -------------------                                                                                         #    ------------------                                                                                          #
#                                                                                                                #                                                                                                                #
#        Your current score when the turn begins                                                                 #        Votre score actuel au début du tour                                                                     #
#        It is initialized at 0, and increases by 1 when you eat a piece of cheese                               #        Il est initialisé à 0, et augmente de 1 pour chaque morceau de fromage mangé                            #
#        If you reach the same piece of cheese as your opponent at the same moment, it is worth 0.5 points       #        Si vous arrivez sur le même morceau de fromage que votre adversaire au même moment, il vaut 0.5 points  #
#        If you are playing in single-player mode, this variable is undefined                                    #        Si vous jouez en mode un joueur, cette variable n'est pas définie                                       #
#                                                                                                                #                                                                                                                #
#    opponentScore : float                                                                                       #    opponentScore: float                                                                                        #
#    ---------------------                                                                                       #    --------------------                                                                                        #
#                                                                                                                #                                                                                                                #
#        The score of your opponent when the turn begins                                                         #        Le score de votre adversaire au début du tour                                                           #
#                                                                                                                #                                                                                                                #
#    piecesOfCheese : list(pair(int, int))                                                                       #    piecesOfCheese : list(pair(int, int))                                                                       #
#    -------------------------------------                                                                       #    -------------------------------------                                                                       #
#                                                                                                                #                                                                                                                #
#        Locations of all remaining pieces of cheese in the maze                                                 #        Emplacements des morceaux de fromage restants dans le labyrinthe                                        #
#        The list is updated at every call of function "turn"                                                    #        La liste est mise à jour à chaque appel de la fonction "turn"                                           #
#                                                                                                                #                                                                                                                #
#    timeAllowed : float                                                                                         #    timeAllowed : float                                                                                         #
#    -------------------                                                                                         #    -------------------                                                                                         #
#                                                                                                                #                                                                                                                #
#        Time that is allowed for determining the next move to perform, in seconds                               #        Temps alloué pour le calcul du prochain mouvement, en secondes                                          #
#        After this time, the decided move will be applied                                                       #        Après ce temps, le mouvement choisi sera appliqué                                                       #
#        If you take too much time, you will still finish executing your code, but you will miss the deadline    #        Si vous prenez trop de temps, votre code finira quand-même son excution, mais vous raterez le timing    #
#        Your move will then be considered the next time PyRat checks for players decisions                      #        Votre mouvement sera alors considéré la prochaine fois que PyRat vérifiera les décisions des joueurs    #
#        However, it will not prevent your opponent from moving if he respected the deadline                     #        Toutefois, cela n'empêchera pas votre adversaire de bouger s'il a respecté le timing                    #
#        Make sure to finish your computations within the allowed time                                           #        Assurez vous de terminer vos calculs dans le temps imparti                                              #
#        Also, save some time to ensure that PyRat will receive your decision before the deadline                #        Aussi, gardez un peu de temps pour garantir que PyRat recevra votre decision avant la fin du temps      #
#        If you are playing in synchronous mode, this variable is undefined                                      #        Si vous jouez en mode synchrone, cette variable n'est pas définie                                       #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################
#                                                                                                                #                                                                                                                #
#    This function should return one of the following constants: MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_UP       #    Cette fonction renvoie l'une des constantes suivantes : MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, MOVE_UP           #
#    The returned constant represents the move you decide to perform: down, left, right, up                      #    La constante renvoyée représente le mouvement que vous décidez d'effectuer : bas, gauche, droite, haut      #
#    Any other value will be ignored and will lead to a turn spent without moving                                #    Toute autre valeur sera ignorée, et entraînera la perte du tour de jeu                                      #
#                                                                                                                #                                                                                                                #
###################################################################################################################################################################################################################################

def turn (mazeMap, mazeWidth, mazeHeight, playerLocation, opponentLocation, playerScore, opponentScore, piecesOfCheese, timeAllowed) :
    
    # Example print that appears in the shell at every turn
    #print("Move: [" + MOVE_UP + "]")
    
    return getMove (mazeMap, playerLocation, chemin.pop(),mazeHeight,mazeWidth)
    
   # return MOVE_RIGHT
  
###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################
