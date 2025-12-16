from typing import List, Tuple
import networkx as nx
import matplotlib.pyplot as plt

##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
cpt = 0

class Graph:
    '''Un graph G=(V,E)
    V est l'ensemble des sommets
    E est l'ensemble des arêtes
    '''


    def __init__(self,V: List[int],E: List[Tuple[int,int]]):
        '''Le constructeur spécifie une liste de sommet V, et une liste d'aretes E.'''
        self.V = V
        self.E = E

    def get_vertices(self) -> List[int]:
        return self.V
    
    def get_edges(self) -> list[Tuple[int,int]]:
        return self.E
    
    def get_neighbors(self,s:int) -> List[int]:
        l = []
        for e in self.E:
            if s == e[0]:
                l.append(e[1])
            if s == e[1]:
                l.append(e[0])
        return l
    
    
    def txt_file_to_graph(self, fd: str) -> None:
        '''Lit un fichier texte et remplit les sommets et arêtes du graphe.'''
        V = set()
        E = set()
        file = open(fd, "r")
        lines = file.readlines()
        n = int(lines[0].strip()) 
        for i in range(1,len(lines)):
            line = lines[i]
            node = i
            neighbors = [int(x) for x in line.strip().split()]
            V.add(node)
            for neighbor in neighbors:
                V.add(neighbor)
                if node < neighbor:
                    E.add((node, neighbor))
                else:
                    E.add((neighbor, node))
        self.V = list(sorted(V))
        self.E = list(E)

    def __str__(self):
        return "Vertices: \n" + self.V.__str__() + "\n" + "Edges: \n" + self.E.__str__() + "\n"
    
    def show(self):
        '''Affiche le graphe avec networkx et matplotlib.'''
        G = nx.Graph()
        G.add_nodes_from(self.V)
        G.add_edges_from(self.E)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='orange', edge_color='gray')
        plt.show()

    def is_sticking_out_edge(self,uv: Tuple[int,int]) -> bool:
        '''Retourne vrai si l'arête uv est sortante (ie. deg(u) == 1 ou deg (v) ==1), faux sinon.'''
        for s in uv:
            if len(self.get_neighbors(s)) == 1:
                return True
        return False
    
    def get_sticking_out_edges(self) -> List[Tuple[int,int]]:
        "Retourne le sous-ensemble des arêtes sortantes appartenant à E."
        l = []
        for e in self.get_edges():
            if self.is_sticking_out_edge(e):
                l.append(e)
        return l




##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
