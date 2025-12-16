from typing import List, Tuple
from Graph import Graph
from collections import deque

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################

class Etat:
    '''
    un Graph G=(V,E) le graphe initial.
    E_c l'ensemble des arretes actuelles.
    E_r l'ensemble des arretes retirées.

    '''
    def __init__(self, G: Graph, E_c: List[Tuple[int,int]], E_r: List[Tuple[int,int]]):
        '''Le constructeur spécifie le graph G, une liste de arêtes E_c, et une liste d'aretes E_r.'''
        self.G = G
        self.E_c = E_c
        self.E_r = E_r

    def __str__(self):
        return "------------------------------\n"+"\n"+"Liste des sommets : " + self.G.get_vertices().__str__() + "\n"+ "Liste des aretes retenues: " + self.E_c.__str__() + "\n" + "Liste des aretes retirées: " + self.E_r.__str__() + "------------------------------\n"

    def get_V(self) -> List[int]:
        '''Retourne la liste des sommets.'''
        return self.G.get_vertices()

    def get_E_c(self) -> List[Tuple[int,int]]:
        '''Retourne la liste des aretes retenues.'''
        return self.E_c
    
    def get_E_r(self) -> List[Tuple[int,int]]:
        '''Retourne la sequence des aretes supprimés.'''
        return self.E_r

    def actions(self) -> List[Tuple[int,int]]:
        '''retourne l'ensemble des actions possibles.'''
        l = []
        sticking_out_edges = self.G.get_sticking_out_edges()
        for e in self.get_problematic_edges():
            if e not in sticking_out_edges:
                l.append(e)
        return l

    def tentative_deux_coloration(self):
        '''Retourne une tentative de deux coloration potentiellement partiellement fausse.'''
        color = {}
        G = Graph(self.get_V(),self.get_E_c())

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
        return color
    
        
    def get_problematic_edges(self):
        "retourne l'ensembles des arêtes de la tentative de 2-coloration qui ont deux sommets de même couleurs."
        l = []
        coloration = self.tentative_deux_coloration()
        for e in self.get_E_c():
            u,v = e
            if coloration[u] == coloration[v]:
                l.append(e)
        return l


        

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################