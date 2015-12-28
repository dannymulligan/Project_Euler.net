#!/usr/bin/swift
//
// Project Euler.net Problem 6
//
// The sum of the squares of the first ten natural numbers is,
//
//     1^(2) + 2^(2) + ... + 10^(2) = 385
//
// The square of the sum of the first ten natural numbers is,
//
//     (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
//
// Hence the difference between the sum of the squares of the first
// ten natural numbers and the square of the sum is 3025 - 385 = 2640.
//
// Find the difference between the sum of the squares of the first one
// hundred natural numbers and the square of the sum.
//

let LIMIT = 100

var sum_sq = 0
var sum_n = 0
for n in 1...LIMIT {
    sum_sq += n * n
    sum_n += n
}

var sq_sum = sum_n * sum_n

let answer = sq_sum - sum_sq

print("Sum of squares of 1 to \(LIMIT) is \(sum_sq)")
print("Square of sum of 1 to \(LIMIT) is \(sq_sum)")

print("Difference is \(answer)")
