import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math as mt
import glob
import pandas as pd
from matplotlib.pyplot import figure
import random
from networkx.algorithms.distance_measures import center
from networkx.algorithms import community
# if you get error "No module found" just write command in terminal : pip3 install modulename, and hit enter.
#for example we wanted to install networkx library type command : 'pip3 install networkx' then hit enter key on keyboard. 
def genrate_cactusgraph(minimum_nodes, maximum_nodes, gap_in_size):
    for v_size in range(minimum_nodes,maximum_nodes,gap_in_size):
        #g = nx.read_adjlist(file, nodetype=int)
        g = nx.generators.random_tree(v_size,seed=5)
        node_label = max(list(g.nodes()))+1
        #print(file,len(g.nodes()))
        number_of_circles  = mt.ceil(len(g.nodes())/4)
        vertices_replace   = random.sample(list(g.nodes()),number_of_circles) 
        circle_lengths     = random.choices([x for x in range(2,mt.ceil(mt.sqrt(len(g.nodes()))+5))],k=number_of_circles)
        #print(vertices_replace, circle_lengths)
        for (n,u) in zip(circle_lengths,vertices_replace):
            G = nx.cycle_graph(n)
            H = nx.relabel_nodes(G, lambda x: x + node_label)
            node_label = node_label + n
            for edges in H.edges():
                g.add_edge(edges[0],edges[1])
            #print(list(g.neighbors(u)))
            rings_joint = random.choices(list(H),k=len(list(g.neighbors(u))))
            #print("rings joint! ", rings_joint)
            for (v,w) in zip(g.neighbors(u),rings_joint):
                #print("edge: ",v,w)
                g.add_edge(v,w)
            g.remove_node(u)
            #print("removed : ", u)
        #figure(figsize=(15, 8), dpi=80)
        #nx.draw_networkx(g)
        #plt.show()
        with open(f'../DATA/CACTUS_GRAPH/cactus_{v_size}.txt', 'w') as f:
            for edge in g.edges():
                f.write(f'{edge[0]} {edge[1]}\n')
            f.close()
        #print(g.nodes())
        print(f'../DATA/CACTUS_GRAPH/cactus_{v_size}.txt')
        #brea
genrate_cactusgraph(100,5000,200)
# cactus graph genrated of sizes 100, 200,400,600 upto 5000.
