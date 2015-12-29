#!/usr/bin/swift
//
// Project Euler.net Problem 14
//
// The following iterative sequence is defined for the set of positive
// integers:
//
//     n -> n/2 (n is even)
//     n -> 3n + 1 (n is odd)
//
// Using the rule above and starting with 13, we generate the following
// sequence:
//
//     13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
//
// It can be seen that this sequence (starting at 13 and finishing at
// 1) contains 10 terms.  Although it has not been proved yet (Collatz
// Problem), it is thought that all starting numbers finish at 1.
//
// Which starting number, under one million, produces the longest chain?
//
// NOTE: Once the chain starts the terms are allowed to go above one million.

let LIMIT = 1000000
//let LIMIT = 100

func seq_len(n: Int) -> Int {
    var len = 0
    var nn = n
    while (nn != 1) {
        if ((nn % 2) == 0) {
            nn = nn / 2
        } else {
            nn = 3*nn + 1
        }
        len += 1
    }
    return len
}

var max_len = 0
var max_n = 0
var len: Int
for n in 1..<LIMIT {
    len = seq_len(n)
    if (len > max_len) {
        max_len = len
        max_n   = n
        print("seq(\(n)) had length \(len)")
    }
}

print("Answer = \(max_n)")
