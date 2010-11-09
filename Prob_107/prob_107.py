#!/usr/bin/python
#
# Project Euler.net Problem 107
# 
# Determining the most efficient way to connect the network.
#
# The following undirected network consists of seven vertices and
# twelve edges with a total weight of 243.
# 
#               20
#          B --------- E
#        /   \       /   \  
#     16/   17\     /18   \11 
#      /       \   /       \
#     A -------- D -------- G
#      \  21   /   \   23  /
#     12\     /28   \19   /27
#        \   /       \   /
#          C --------- F
#               31
#
# The same network can be represented by the matrix below.
#             A       B       C       D       E       F       G
#     A       -       16      12      21      -       -       -
#     B       16      -       -       17      20      -       -
#     C       12      -       -       28      -       31      -
#     D       21      17      28      -       18      19      23
#     E       -       20      -       18      -       -       11
#     F       -       -       31      19      -       -       27
#     G       -       -       -       23      11      27      -
# 
# However, it is possible to optimise the network by removing some
# edges and still ensure that all points on the network remain
# connected. The network which achieves the maximum saving is shown
# below. It has a weight of 93, representing a saving of 243 - 93 =
# 150 from the original network.
# 
#
#          B           E
#        /   \       /   \  
#     16/   17\     /18   \11 
#      /       \   /       \
#     A          D          G
#      \           \
#     12\           \19
#        \           \
#          C           F
#
# Using network.txt (right click and 'Save Link/Target As...'), a 6K
# text file containing a network with forty vertices, and given in
# matrix form, find the maximum saving which can be achieved by
# removing redundant edges whilst ensuring that the network remains
# connected.
#
# Answer:
# Solved:
# ? problems solved
# Position #??? on level ?

import mini_network
net = mini_network.net
#import network
#net = network.net

nvert = len(net)

# Zero out the bottom half of the matrix
for i in range(nvert):
    for j in range(nvert):
        if (j <= i):
            net[i][j] = 0

# Print the matrix
#for i in net:
#    print i

# Calculate the Network Weight & count the Network Vertices
nweight = 0
nedges = 0
for i in net:
    for j in i:
        nweight += j
        if (j != 0):
            nedges += 1
print "Network Weight =", nweight

# Count the Network Vertices
print "Network Vertices =", nvert

# Count the Network Edges
print "Network Edges =", nedges

# Count the connections
conns = [0]*nvert
print conns
for i in range(nvert):
    for j in range(nvert):
        if (net[j][i] != 0):
            conns[i] += 1
            conns[j] += 1
print conns

