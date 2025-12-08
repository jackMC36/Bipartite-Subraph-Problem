from typing import List, Tuple
import Graph

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Etat:
    '''
    un Graph G=(V,E). 
    X et Y deux ensembles de sommets.
    E l'ensemble des arretes.
    added_variables la liste des sommets assignés dans l'ordre.
    '''
    def __init__(self, G: Graph, X: set[int], Y: set[int],assigned_variables: list[int]):
        '''Le constructeur spécifie un ensemble de sommets X, un ensemble de sommets Y, une liste de arêtes E et une liste de sommet assigned_variables.'''
        self.G = G
        self.X = set(X)
        self.Y = set(Y)
        self.assigned_variables = assigned_variables

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

    def get_assigned_variables(self) -> list[int]:
        return self.assigned_variables

    def actions(self) -> set[int]:
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
            if not(self.is_X_assignable(v)):
                return False
            
        for v in self.Y:
            if not(self.is_Y_assignable(v)):
                return False
                
        return True

    def is_correctable(self,v) -> bool: 
        '''Retourne vrai si le sommet peut être réassigné, faux sinon.'''
        if v in self.get_X():
            return self.is_Y_assignable(v)
        if v in self.get_Y():
            return self.is_X_assignable(v)
        return False

    
    

    def is_X_assignable(self, value: int) -> bool:
        '''retourne vrai si v peut être ajouter à X, faux sinon.'''
        neighbors = set(self.G.get_neigbhors(value))
        for n in neighbors:
            if n in self.X:
                return False
        return True

    def is_Y_assignable(self, value: int) -> bool:
        '''retourne vrai si v peut être ajouter à X, faux sinon.'''
        neighbors = set(self.G.get_neigbhors(value))
        for n in neighbors:
            if n in self.Y:
                return False
        return True
                

    def is_terminal(self) -> bool:
        '''retourne vrai si l'état est terminal, faux sinon.'''
        return ((self.X.union(self.Y)) == self.G.V) and self.is_valid()


        

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
