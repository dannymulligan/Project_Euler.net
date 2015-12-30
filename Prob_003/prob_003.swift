#!/usr/bin/swift
//
// Project Euler.net Problem 3
//
// Find the largest prime factor of a composite number.
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?
//

import Foundation

let TARGET = 600851475143
let SQRT_TARGET = 1 + Int(floor(sqrt(Float(TARGET))))

let LIMIT_PRIME = SQRT_TARGET
var prime_table = [Int](count: LIMIT_PRIME, repeatedValue: 1)  // table of largest factor

func calculate_primes() {
    var i = 2
    var j: Int
    while (i < (LIMIT_PRIME/2)) {
        if (prime_table[i] == 1) {
            j = i*2
            while (j < LIMIT_PRIME) {
                prime_table[j] = i
                j += i
            }
        }
        i += 1
    }
}

calculate_primes()

var answer = 0
var i = LIMIT_PRIME - 1
while (answer == 0){
    if (prime_table[i] == 1) {
        if ((TARGET % i) == 0) {
            answer = i
        }
    }
    i -= 1
}
i += 1

print("Answer is \(i)")
