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
# Solved:
# ? problems solved
# Position #??? on level ?

import time
start_time = time.clock()

#import mini_network
#weights = mini_network.weights
import network
weights = network.weights


########################################
# Gather info on the starting point
nsize = len(weights)
print "Network size =", nsize
starting_vertices = 0
starting_weight = 0
for i in range(nsize):
    for j in range(i,nsize):
        if (weights[i][j] != 0):
            starting_vertices += 1
            starting_weight += weights[i][j]
print "There are {} vertices, weighing {}".format(starting_vertices, starting_weight)


########################################
# Build a useful data structure
links = []
for n in range(nsize):
    links_from_n = []
    for i in range(nsize):
        if (i == n):
            continue
        if (weights[i][n] != 0):
            links_from_n.append(i)
    links.append(links_from_n)


########################################
def print_network():
    # Analyze the matrix
    nvertices = 0
    nweight = 0
    for i in range(nsize):
        for j in range(i,nsize):
            if (weights[i][j] != 0):
                nvertices += 1
                nweight += weights[i][j]

    # Print the matrix
    print "The current connection matrix is..."

    print " {:2} ".format(' '),
    for i in range(nsize):
        print " {:2} ".format(i),
    print

    for i in range(nsize):
        print " {:2} ".format(i),
        for j in range(nsize):
            if (j == i):
                print "  . ",
            elif (weights[i][j] == 0):
                print "  - ",
            else:
                print "{:3} ".format(weights[i][j]),
        print
    print "There are {} vertices, which is {:.1f}% of the starting number of vertices of {}".format(nvertices, 100.0*nvertices/starting_vertices, starting_vertices)
    print "The weight is {}, which is {:.1f}% of the starting weight of {}".format(nweight, 100.0*nweight/starting_weight, starting_weight)

    print "links = "
    for ll in range(len(links)):
        print "   {} is linked to {}".format(ll, links[ll])
    print "----"


########################################
def find_loop():
    all_connections = []

    # Build initial list of connections - start nodes
    connections = []
    for i in range(nsize):
        if (len(links[i]) > 1):
            connections.append([i])
    all_connections.append(connections)

    # Build longer lists of connections by extending current connections
    for length in range(1, nsize):
        connections = []
        for con in all_connections[-1]:
            for next in links[con[-1]]:
                if ((next == con[0]) & (len(con) >= 3)):
                    # We've found a loop
                    return con
                elif next in con:
                    # This next loops back to earlier part of path
                    continue
                else:
                    # Create a longer path that adds next
                    connections.append(con + [next])
        all_connections.append(connections)

    return []


########################################
def disconnect_loop(loop):
    best_weight = 0
    best_start = 0
    best_end = 0
    for i in range(len(loop)):
        start = loop[i-1]
        end = loop[i]

        if (start > end):
            start, end = end, start

        weight = weights[start][end]
        assert (weight != 0), "{} is not a loop, vertex {}-{} has a weight of 0".format(loop, start, end)


        if (weight > best_weight):
            best_weight = weight
            best_start = start
            best_end = end
    print "Disconnecting {}-{} (weight = {})".format(best_start, best_end, best_weight)
    weights[best_start][best_end] = 0
    weights[best_end][best_start] = 0
    links[best_start].remove(best_end)
    links[best_end].remove(best_start)
    return


########################################
# Report some statistics on the network before we begin
print_network()


########################################
# Count the number of vertices
nvertices = 0
nweight = 0
for i in range(nsize):
    for j in range(i,nsize):
        if (weights[i][j] != 0):
            nvertices += 1
            nweight += weights[i][j]


########################################
# Main loop
progress = True
while(progress):
    progress = False
    loop = find_loop()
    if (len(loop) > 0):
        progress = True
        print "Found {}, a loop of length {}".format(loop, len(loop))
        disconnect_loop(loop)
        #print_network()

print_network()

print "No further progress can be made, this is the final network"
nweight = 0
for i in range(nsize):
    for j in range(i,nsize):
        if (weights[i][j] != 0):
            nweight += weights[i][j]
print "Answer = {}".format(starting_weight - nweight)
print "Time taken = {0} seconds".format(time.clock() - start_time)

## Code to test disconnect_loop using the example problem
#print "\ndisconnect_loop([0, 1, 3])"
#disconnect_loop([0, 1, 3])
#print_network()
#
#print "\ndisconnect_loop([1, 3, 4])"
#disconnect_loop([1, 3, 4])
#print_network()
#
#print "\ndisconnect_loop([2, 3, 5])"
#disconnect_loop([2, 3, 5])
#print_network()
#
#print "\ndisconnect_loop([3, 4, 6])"
#disconnect_loop([3, 4, 6])
#print_network()
#
#print "\ndisconnect_loop([0, 1, 3, 2])"
#disconnect_loop([0, 1, 3, 2])
#print_network()
#
#print "\ndisconnect_loop([3, 4, 6, 5])"
#disconnect_loop([3, 4, 6, 5])
#print_network()
