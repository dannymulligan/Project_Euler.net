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

import math._

val limit = 100

var sum_sq : BigInt = 0
var sum : BigInt = 0
for (i <- 1 to limit) {
    sum_sq += i*i
    sum += i
}

val sq_sum: BigInt = sum * sum

println("Sum of squares of 1 to " + limit + " is " + sum_sq)
println("Square of sum of 1 to " + limit + " is " + sq_sum)

val answer = sq_sum - sum_sq

println("Difference is " + answer)
