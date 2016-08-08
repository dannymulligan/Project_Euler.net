#!/usr/bin/swift
let LIMIT_PRIME = 1000
var prime_table = [Int](count: LIMIT_PRIME, repeatedValue: 1)   // table of largest factor

func calculate_primes() {
    print("Calculating primes up to \(LIMIT_PRIME)")
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
    print("Done calculating primes")
}
