#!/usr/bin/swift
//
// Project Euler.net Problem 2
//
// Find the sum of all the even-valued terms in the Fibonacci sequence
// which do not exceed four million.
//
// Each new term in the Fibonacci sequence is generated by adding the
// previous two terms. By starting with 1 and 2, the first 10 terms
// will be:
//
// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
//
// Find the sum of all the even-valued terms in the sequence which do
// not exceed four million.

var answer = 0
var f1 = 1, f0 = 1

while (f1 < 4000000) {
    (f1, f0) = ((f1+f0), f1)
    if ((f1 % 2) == 0) {
        answer += f1
    }
}
print("Answer is \(answer)")
