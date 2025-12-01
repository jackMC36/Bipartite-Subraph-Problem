from typing import List, Tuple

import Graph.py

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Etat:
    '''
    Un Etat decrit un Graph G=(V,E). 
    X et Y deux ensembles de sommets.
    E l'ensemble des arretes.
    '''
    def __init__(self, G: Graph, X: set[int], Y: set[int], E: List[Tuple[int, int]]):
        '''Le constructeur spécifie une liste de sommets X, une liste de sommets Y,  et une liste de arêtes E.'''
        self.G = G
        self.X = set(X)
        self.Y = set(Y)
        self.E = set(E)

    def __str__(self):
        return "------------------------------\n"+"\n"+"Liste des sommets X: " + self.X.__str__() + "\n"+ "Liste de sommets Y" + self.Y.__str__() + "\n" +"------------------------------\n"

    def get_X(self) -> set[int]:
        '''Retourne la liste de sommets X.'''
        return self.X
    
    def get_Y(self) -> set[int]:
        '''Retourne la sequence de sommets Y.'''
        return self.Y

    def get_E(self) -> set[int]:
        '''Retourne l'ensemble des arêtes.'''
        return self.E

    def is_valid(self) -> bool:
        '''Retourne True si l'état est valide, faux sinon.'''
        G = self.G
        for v in G.get_vertices():
            neighbors = set(G.get_neigbhors(v))
            in_both_sets = False
            for n in neighbors:
                in_both_sets = (n in self.X) and (n in self.Y)

    def is_terminal(self) -> bool:
        return len(self.X) 


        

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
