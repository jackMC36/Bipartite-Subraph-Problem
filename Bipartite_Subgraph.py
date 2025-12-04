from typing import List, Tuple
import copy
import random

import Etat from Etat.py
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Bipartite_Graph:

    def __init__(self, G: Graph):
        '''Le constructeur specifie le graph G=(V,E).'''
        self.G = G
        self.etat_initial = Etat(self.G,[],[])

    def etat_initial(self) -> Etat:
        '''Retourne l'état initial'''
        return etat_initial   
    
    def succ(self, etat: Etat, action: int, chosen_set: str) -> Etat:
        '''Retourne l'etat obtenu après avoir executé une action sur un état.'''

        new_X = etat.get_X().copy()
        new_Y = etat.get_Y().copy()

        if(chosen_set == 'X')
            if(action in etat.get_X()):
                raise ValueError
            new_X.add(action)
        
        if(chosen_set == 'Y')
            if(action in etat.get_Y()):
                raise ValueError
            new_Y.add(action)
        
        
        new_etat = Etat(self.G,new_X,new_Y)
        return new_etat
    
    def backtrack(self,assignement: Etat):
        if assignement.is_terminal():
            print("L'etat est terminal\n")
            return assignement

        var = random.choice(assignement.actions())
        possible_sets = {"X","Y"}
        for s in possible_sets:
            



    def backtracking_search(self):
        return backtrack(self, self.etat_initial)

        

    



##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
########################################################################################################toy_model_2##########################################################
