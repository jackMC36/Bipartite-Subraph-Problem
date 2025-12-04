from typing import List, Tuple

import Graph.py

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Etat:
    '''
    un Graph G=(V,E). 
    X et Y deux ensembles de sommets.
    E l'ensemble des arretes.
    '''
    def __init__(self, G: Graph, X: set[int], Y: set[int]):
        '''Le constructeur spécifie une liste de sommets X, une liste de sommets Y,  et une liste de arêtes E.'''
        self.G = G
        self.X = set(X)
        self.Y = set(Y)

    def __str__(self):
        return "------------------------------\n"+"\n"+"Liste des sommets X: " + self.X.__str__() + "\n"+ "Liste de sommets Y" + self.Y.__str__() + "\n" +"------------------------------\n"

    def get_X(self) -> set[int]:
        '''Retourne la liste de sommets X.'''
        return self.X
    
    def get_Y(self) -> set[int]:
        '''Retourne la sequence de sommets Y.'''
        return self.Y

    def get_E(self):
        '''Retourne l'ensemble des arêtes.'''
        return self.G.get_edges()

    def actions(self) -> set(int):
        '''retourne l'ensemble des actions possibles.'''
        used_vertices = self.X.union(self.Y)
        total_vertices = set(self.G.get_vertices())
        return total_vertices.difference(used_vertices)

    def is_valid(self) -> bool:
        '''Retourne True si l'état est valide, faux sinon.'''
        G = self.G
        for v in G.get_vertices():
            neighbors = set(G.get_neigbhors(v))
            for n in neighbors:
                if (n in self.X) and (n in self.Y):
                    return False

        for v in self.X:
            if not(is_X_assignable(v)):
                return False
            
        for v in self.Y:
            if not(is_Y_assignable(v)):
                return False
                
        return True

    def is_X_assignable(self, value: int) -> bool:
        '''retourne vrai si v peut être ajouter à X, faux sinon.'''
        neighbors = set(G.get_neigbhors(value))
            for n in neighbors:
                if n in self.X:
                    return False
        return True

    def is_Y_assignable(self, value: int) -> bool:
        '''retourne vrai si v peut être ajouter à X, faux sinon.'''
        neighbors = set(G.get_neigbhors(value))
            for n in neighbors:
                if n in self.Y:
                    return False
        return True
                

    def is_terminal(self) -> bool:
        return ((self.X.union(self.Y)) == self.G.V) and self.is_valid()


        

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
