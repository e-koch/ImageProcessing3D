#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:36:16 2018

@author: haswani
"""


from skan import csr
import numpy as np
from skimage.morphology import skeletonize,skeletonize_3d
from astropy.io import fits
from skimage.morphology import binary_opening,binary_dilation,binary_erosion,closing,dilation,opening,ball,remove_small_holes
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio as iio
from skan import draw

cube = fits.getdata('ngc3627_co21_12m+7m+tp_pbcorr_round_k_correct_mask.fits')

#cube = fits.getdata('ngc3627_co21_12m+7m+tp_mask.fits')

#Parameter :
parameter = 5
cutnodes = []



selem = ball(3)

ddilate = dilation(cube, selem)
dclose = closing(ddilate)
dskel2 = skeletonize_3d(dclose)

#subcube = remove_holes[15:, 15:45, 15:45]

pixel_graph0, coordinates0, degrees0 = csr.skeleton_to_csgraph(dskel2)

subcube = dskel2[125:175,300:500, 50:200]

#Graph


import networkx as nx

pixel_graph1, coordinates1, degrees1 = csr.skeleton_to_csgraph(subcube)

#print(pixel_graph1.paths_list())

nodes = range(15,75)
G = nx.from_scipy_sparse_matrix(pixel_graph1) 

for node in G.node:
    G.node[node]['pos'] = coordinates1[node]

print("Number of nodes before Pruning:")
print(nx.number_of_nodes(G))

#H = G.subgraph(nodes)
#graphs = list(nx.connected_component_subgraphs(G))

#UG = G.to_undirected()

# extract subgraphs
sub_graphs = nx.connected_component_subgraphs(G)

subgraphlist = []

for i, sg in enumerate(sub_graphs):
    #print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    #print("\tNodes:", sg.nodes())
    subgraphlist.append(sg.nodes())
    if i == 3: # change this value to check with different subgraphs
        L = sg.nodes()
    #print("\tEdges:", sg.edges())

#end points
#import itertools


#print(graphs)

#print(H.neighbors(64))
#print("GOOD")
#H = G.subgraph(L)

#H = nx.Graph(G.subgraph(L))  - this is working

nodesToBeRemoved = []

for j in subgraphlist:
    H = nx.Graph(G.subgraph(j)) # for all the subgraphs
#print(list(itertools.chain(H.nx.Graph.edges_iter())))
    
    #Removing subgraphs with less then parameter length (5)
#    if nx.number_of_nodes(H) <= parameter:
#       print("cleared")
#        H.clear()
    #above will remove nodes just from the view of subgraph and not the original one
#    if nx.number_of_nodes(H) <= parameter:
#        print("Hey")
#        print(H.nodes())
#        G.remove_nodes_from(H.nodes())
#    
    
    
    
#for n in H.nodes:
#    print(G.degree(n))
    endPoints = []

    for n in H.nodes:
        if H.degree(n)==1:
            endPoints.append(n)
    #print(endPoints) #all the endpoints

    junction = []

    for n in H.nodes:
        if H.degree(n)>2:
            junction.append(n) # all the junction points


    for k in junction: #for all the junction nodes removing the branches
#            p = nx.shortest_path(H,source=k,target=endPoints[0])
#            print("Path :")
#            print(len(p))
#            
          #  minimum = 30 #just a large number 
            for i in endPoints:
                if nx.has_path(H,k,i) and H.degree(k) > 2:
                    
                    p = nx.shortest_path(H,source=k,target=i)
          #          print("Path :")
           #         print(i)
           #         print(len(p))
                    length = len(p)
                    if length < parameter:
                        #minimum = length
                        cutnode = p[1]
            #            print("TO cut: ")
             #           print(cutnode)
            
            
                        if H.has_edge(k, cutnode):
                            H.remove_edge(k,cutnode)
              #              print("SubGraph Number")
               #             print(j)
                #            print("Cutting edges ")
                 #           print(k, cutnode)
                            cutnodes.append(cutnode)
     #REmoving Subgraph less then parameter length(here 5nodes)
        
        
            for n in cutnodes:
                if G.has_edge(k,n):
                    G.remove_edge(k,n)
                    print("removed")
            #print(cutnodes) 



#Removing nodes                 
    if nx.number_of_nodes(H) <= parameter:
        print("removing nodes")
        print(H.nodes())
        G.remove_nodes_from(H.nodes())

print("Number of nodes After removing Subgraphs < parameter length:")
print(nx.number_of_nodes(G))
                            
#removing Subgraphs afer removing edges

sub_graphs2 = nx.connected_component_subgraphs(G)

subgraphlist2 = []

for i, sg in enumerate(sub_graphs2):
    #print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    #print("\tNodes:", sg.nodes())
    subgraphlist2.append(sg.nodes())

for j in subgraphlist2:
    H2 = nx.Graph(G.subgraph(j)) 
    if nx.number_of_nodes(H2) <= parameter:
        print("removing nodes 2")
        print(H.nodes())
        G.remove_nodes_from(H2.nodes())    
    


      
##        

                
                    
K = nx.Graph(G.subgraph(L))



new_posns = {}
for node in K.node:
    new_posns[node] = K.node[node]['pos']


print("Number of nodes After Pruning:")
print(nx.number_of_nodes(G))

#Graph Plotting

def network_plot_3D(G, angle, save=False):

    # Get node positions
    pos = nx.get_node_attributes(G, 'pos')
    
    # Get number of nodes
 #   n = G.number_of_nodes()

    # Get the maximum number of edges adjacent to a single node
    edge_max = max([G.degree(i) for i in G.nodes])

    # Define color range proportional to number of edges adjacent to a single node
    colors = [plt.cm.plasma(G.degree(i)/edge_max) for i in G.nodes] 

    # 3D network plot
    with plt.style.context(('ggplot')):
        
        fig = plt.figure(figsize=(10,7))
        ax = Axes3D(fig)
        
        # Loop on the pos dictionary to extract the x,y,z coordinates of each node
        for i, (key, value) in enumerate(pos.items()):
            xi = value[0]
            yi = value[1]
            zi = value[2]
            
            # Scatter plot
            ax.scatter(xi, yi, zi, c=colors[i], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
        
        # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
        # Those two points are the extrema of the line to be plotted
        for i,j in enumerate(G.edges()):

            x = np.array((pos[j[0]][0], pos[j[1]][0]))
            y = np.array((pos[j[0]][1], pos[j[1]][1]))
            z = np.array((pos[j[0]][2], pos[j[1]][2]))
        
        # Plot the connecting lines
            ax.plot(x, y, z, c='black', alpha=0.5)
    
    # Set the initial view
    ax.view_init(30, angle)

    # Hide the axes
    #ax.set_axis_off()

    if save is not False:
        plt.savefig(str(angle).zfill(3)+".png")
        plt.close('all')
    else:
        plt.show()
    
    return

#def generate_random_3Dgraph(n_nodes, radius, seed=None):
# 
#    if seed is not None:
#        random.seed(seed)
#    
#    # Generate a dict of positions
#    pos = {i: (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)) for i in range(n_nodes)}
#    
#    # Create random 3D network
#    G = nx.random_geometric_graph(n_nodes, radius, pos=pos)
# 
#    return G
#
#n=200
#G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
#network_plot_3D(G,0, save=False)

##FINDING VELOCITY AND SPATIAL LENGTH
node_number = []
cordinates = []
spatial_length = [] 
veloctiy_length = [] 
#will zip them all together in end

sub_graphs3 = nx.connected_component_subgraphs(G)
#extracting all subgraphs to work on each subgraphs individually

subgraphlist3 = []

for i, sg in enumerate(sub_graphs3):
    #print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    #print("\tNodes:", sg.nodes())
    subgraphlist3.append(sg.nodes())
    if i == 3: # change this value to check with different subgraphs
        L = sg.nodes()

#subgraphlist3 is the required list of all subgraphs

#test = [[0,0,0]]
test = []
#test is used to test functionalities of python

for j in subgraphlist3:
    H3 = nx.Graph(G.subgraph(j)) 
    endPoints = [] #endpoints of each subgraph
    junction = []   #junction of each subgraph
    for n in H3.nodes:
        if H3.degree(n)==1:
            endPoints.append(n)
        elif H3.degree(n)>2:
            junction.append(n)
        #else:
            #print("others")
            
    count = 0     
    for node in H3.node:
        if node in endPoints: #check if selected node is in the list of endpoitns
            print("Start")
            neighbor_node = H3.neighbors(node)
            #print(neighbor_node)
            
            if neighbor_node not in endPoints and neighbor_node not in junction:
                pointer_node = H3.node[node]['pos']
                print("Neighbour test")
                #next_node = H3.node[neighbor_node]['pos']
                #print(H3.node[neighbor_node]['pos'])
                spatialDistanceBetweenNodes = 0
                #velocityLengthBetweenNodes = abs(next_node - pointer_node)
            
        test.append(H3.node[node]['pos'])
        #print(test[0][0][0])
        print(node)
        print(test[count])
        test_list = test[count]
        count = count + 1
        print(test_list[0])


        
#print(endPoints)


#nx.draw(K, with_labels=True)

#starting with 20 




#print(degrees0)

#
#out = np.where(coordinates0)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')
#

#plt.show()