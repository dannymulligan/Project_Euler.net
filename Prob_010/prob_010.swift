#!/usr/bin/swift
//
// Project Euler.net Problem 10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

let LIMIT_PRIME = 2000000
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
var n = 0
for i in 2..<LIMIT_PRIME {
    if (prime_table[i] == 1) {
        answer += i
        n += 1
    }
}

print("The sum of the \(n) primes below \(LIMIT_PRIME) is \(answer)")
