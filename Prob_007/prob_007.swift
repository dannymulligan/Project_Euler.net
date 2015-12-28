#!/usr/bin/swift
//
// Project Euler.net Problem 7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10,001st prime number?


let LIMIT_PRIME = 125000
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

print("Done calculating primes")

var cnt = 0
var i = 1
while (cnt < 10001) {
    i += 1
    if (prime_table[i] == 1) {
        cnt += 1
    }
}
print("Answer is \(i)")
