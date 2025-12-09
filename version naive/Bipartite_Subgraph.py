from typing import List, Tuple
import copy
import random
from Etat import Etat
from Graph import Graph
from collections import deque

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Bipartite_Subgraph:

    def __init__(self, G: Graph):
        '''Le constructeur specifie le graph G=(V,E).'''
        self.G = G
        self.etat_initial = Etat(self.G,self.G.get_edges(),[])

    def is_bipartite(self, G: Graph):
        '''Retourne vrai si le graphe actuelle est biparti, faux sinon.'''
        color = {}

        for v in G.get_vertices():
            if v not in color:
                queue = deque([v])
                color[v] = 0
                while queue:
                    u = queue.popleft()
                    for n in G.get_neighbors(u):
                        if n not in color:
                            color[n] = 1 - color[u]
                            queue.append(n)
                        elif color[n] == color[u]:
                            return False
        return True


    def etat_initial(self) -> Etat:
        '''Retourne l'état initial'''
        return self.etat_initial   
    
    def succ(self, etat: Etat, action: Tuple[int,int]) -> Etat:
        '''Retourne l'etat obtenu après avoir executé une action sur un état.'''
        new_E_c = etat.get_E_c().copy()
        new_E_r = etat.get_E_r().copy()
        
        new_E_c.remove(action)
        new_E_r.append(action)

        new_etat = Etat(self.G,new_E_c,new_E_r)
        return new_etat
    
    def backtrack(self, assignment: Etat):
        global liste_solution
        G = Graph(assignment.get_V(), assignment.get_E_c())
        if self.is_bipartite(G):
            return assignment
        
        for edge in assignment.actions():
            new_assignment = self.succ(assignment, edge)
            result = self.backtrack(new_assignment)
            if result is not None:
                liste_solution.append(result)
                return result
        
        return None            

    def backtracking_search(self):
        result = self.backtrack(self.etat_initial)
        if result is not None:
            liste_solution.append(result)
        return result
    

import os

liste_solution = []
G = Graph([],[])
# Use absolute path to work from any directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "..", "Instances", "toy_model.txt")
G.txt_file_to_graph(file_path)

print(f"Graph loaded: {len(G.get_vertices())} vertices, {len(G.get_edges())} edges")
print(f"Initial graph is bipartite: {Bipartite_Subgraph(G).is_bipartite(G)}")

Problem = Bipartite_Subgraph(G)
result = Problem.backtracking_search()

print("debut de la résolution")
if result:
    print("Found solution:")
    print(result.__str__())
else:
    print("No solution found")

for s in liste_solution:
    print(s.__str__())
    print("nombre d'arete enlever: " + str(len(s.get_E_r())))
    print("\n")


print("Nombre de solution:" + str(len(liste_solution)))


##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
########################################################################################################toy_model_2##########################################################
