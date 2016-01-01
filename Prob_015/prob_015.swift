#!/usr/bin/swift
//
// Project Euler.net Problem 015
//
// Lattice paths
//
// Starting in the top left corner of a 2×2 grid, and only being able
// to move to the right and down, there are exactly 6 routes to the
// bottom right corner.
//
// How many such routes are there through a 20×20 grid?


let SIZE = 20

// Create an empty array of node values
var nodes = Array<Array<Int>>()
for x in 0...SIZE {
    var sublist = [Int](count:SIZE+1, repeatedValue:0)
    nodes.append(sublist)
}

var value_above: Int
var value_left: Int
for x in 0...SIZE {
    for y in 0...SIZE {
        if (x-1) < 0 {
            value_above = 0
        } else {
            value_above = nodes[x-1][y]
        }

        if (y-1) < 0 {
            value_left = 0
        } else {
            value_left = nodes[x][y-1]
        }

        if (x == 0) && (y == 0) {
            nodes[x][y] = 1
        } else {
            nodes[x][y] = value_above + value_left
        }
    }
}

print("For x \(SIZE)x\(SIZE) grid...")
print("Answer is \(nodes[SIZE][SIZE])")