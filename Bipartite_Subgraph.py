from typing import List, Tuple
import copy

import Etat from Etat.py
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Bipartite_Graph:

    def __init__(self, G: Graph):
        '''Le constructeur specifie le graph G=(V,E).'''
        self.G = G
        self.Etat = Etat(self.G.get_vertices(),[],self.G.get_edges(),0,[],[])

    def etat_initial(self) -> Etat:
        '''Retourne l'état initial'''
        return Etat(self.G.get_vertices(),[],self.G.get_edges(),0,[],[])
    
    def actions(self, etat: Etat) -> set[int]:
        '''Retourne les actions qui peuvent etre prise à partir d'un état donner.'''
        if len(etat.get_X) >= len(etat.get_Y):
            return set()
        else:
            return etat.get_Y()
    
    def succ(self, etat: Etat, action: int) -> Etat:
        '''Retourne l'etat obtenu après avoir executé une action sur un état.'''


        new_X = etat.get_X().copy()
        new_Y = etat.get_Y().copy()
        new_n = etat.get_n()+1
        new_E = etat.get_E()
        
        if(action in etat.get_X()):
            raise ValueError
        
        new_X.add(action)
        new_Y.discard(action)
        new_etat = Etat(new_NB,new_B,self.G.get_edges(),new_n, new_B_v,new_C)
        return new_etat
        
    def goal_test(self, etat: Etat) -> bool:
        '''Verifie si l'etat est un etat but. '''
        return len(etat.get_X()) == len(etat.get_Y())
 
    def backtracking_search(self):
        etat_initial = Etat

    



##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
########################################################################################################toy_model_2##########################################################
