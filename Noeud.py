from typing import List, Tuple

import Etat

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Noeud:
    '''Noeud dans un arbre de recherche. Un noeud contient :
    L'Etat correspondant au noeud
    Un pointeur vers son parent
    L'action menant à cet état
    '''

    def __init__(self, Etat: Etat, parent=None, action=None):
        self.Etat = Etat
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1


    def get_Etat(self):
        return self.Etat

    def child_Noeud(self, problem: Bipartite_Subgraph, action: int) -> "Noeud":
        '''Retourne le noeud obtenu à partir d'un noeud et une action.'''
        return problem.succ(self.Etat, action)
    
    def get_Children(self):
        L_Children = List[Noeud]
        L_actions = Bipartite_Subgraph.actions(self.get_Etat())
        for i in L_actions:
            L_Children.append(Bipartite_Subgraph.succ(self,i))
    
    def expand(self, problem: Bipartite_Subgraph) -> List["Noeud"]:
        '''Retoune la liste des Noeuds atteignable en une etape à partir du noeud courant.'''
        L_Noeud = []
        Courant = self
        Etat_Intermediaire = problem.propagation(Courant.get_Etat())
        L_actions = problem.actions(Etat_Intermediaire)
        for i in L_actions:
            Etat_enfant = problem.succ(Etat_Intermediaire,i)
            Noeud_enfant = Noeud(Etat_enfant,Courant,i)
            L_Noeud.append(Noeud_enfant)
        return L_Noeud


##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
