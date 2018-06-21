#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:14:35 2018

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

cube = fits.getdata('ngc3627_co21_12m+7m+tp_mask.fits')

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
#H = G.subgraph(nodes)
#graphs = list(nx.connected_component_subgraphs(G))

#UG = G.to_undirected()

# extract subgraphs
sub_graphs = nx.connected_component_subgraphs(G)

for i, sg in enumerate(sub_graphs):
    print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    print("\tNodes:", sg.nodes())
    if i == 3:
        L = sg.nodes()
    print("\tEdges:", sg.edges())


#print(graphs)

#print(H.neighbors(64))
#print("GOOD")
H = G.subgraph(L)
nx.draw(H, with_labels=True)

#starting with 20 




#print(degrees0)

#
#out = np.where(coordinates0)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(out[0],out[1],out[2],'r,')
#

plt.show()