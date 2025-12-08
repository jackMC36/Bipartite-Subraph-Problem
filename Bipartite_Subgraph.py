from typing import List, Tuple
import copy
import random
from Etat import Etat
from Graph import Graph


##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Bipartite_Graph:

    def __init__(self, G: Graph):
        '''Le constructeur specifie le graph G=(V,E).'''
        self.G = G
        self.etat_initial = Etat(self.G,[],[],[])

    def etat_initial(self) -> Etat:
        '''Retourne l'état initial'''
        return self.etat_initial   
    
    def succ(self, etat: Etat, action: int, chosen_set: str) -> Etat:
        '''Retourne l'etat obtenu après avoir executé une action sur un état.'''

        new_X = etat.get_X().copy()
        new_Y = etat.get_Y().copy()

        if(chosen_set == 'X'):
            if(action in etat.get_X()):
                raise ValueError
            new_X.add(action)
        
        if(chosen_set == 'Y'):
            if(action in etat.get_Y()):
                raise ValueError
            new_Y.add(action)
        
        
        new_etat = Etat(self.G,new_X,new_Y)
        return new_etat
    
    def assignement_correction(self,assignement: Etat, v: int, Ensemble: str):
        if assignement.is_correctable(v):
            corrected_X = assignement.get_X().copy()
            corrected_Y = assignement.get_Y().copy()
            if Ensemble == "X":
                corrected_X.add(v)
                corrected_Y.remove(v)
            if Ensemble == "Y":
                corrected_Y.add(v)
                corrected_X.remove(v)
        return Etat(self.G,corrected_X,corrected_Y,assignement.get_assigned_variables())

    
    def backtrack(self,assignement: Etat):

        if assignement.is_terminal():
            print("L'etat est terminal\n")
            return assignement

        var = random.choice(assignement.actions())

        possible_sets = {"X","Y"}
        for s in possible_sets:
            if s == "X":
                if assignement.is_X_assignable(var):
                    return self.backtrack(self.succ(assignement,var,s))
            if s == "Y":
                if assignement.is_Y_assignable(var):
                    return self.backtrack(self.succ(assignement,var,s))
        
        corrected_X = assignement.get_X().copy()
        corrected_Y = assignement.get_Y().copy()

        neighbors = self.G.get_edges(var)
        for n in neighbors:
            if assignement.is_correctable(n):
                if n in assignement.get_X():
                    assignement = self.assignement_correction(assignement,n,"Y")
                if n in assignement.get_Y():
                    assignement = self.assignement_correction(assignement,n,"X")
        return self.backtrack(self.succ(assignement,var,"X"))

            
                

            



    def backtracking_search(self):
        return self.backtrack(self, self.etat_initial)

        

    



##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
########################################################################################################toy_model_2##########################################################
