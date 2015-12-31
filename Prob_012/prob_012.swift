#!/usr/bin/swift
//
// Project Euler.net Problem 12
//
// The sequence of triangle numbers is generated by adding the natural
// numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 +
// 7 = 28. The first ten terms would be:
//
//     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
//
// Let us list the factors of the first seven triangle numbers:
//
//      1: 1
//      3: 1,3
//      6: 1,2,3,6
//     10: 1,2,5,10
//     15: 1,3,5,15
//     21: 1,3,7,21
//     28: 1,2,4,7,14,28
//
// We can see that 28 is the first triangle number to have over five
// divisors.
//
// What is the value of the first triangle number to have over five
// hundred divisors?


//let MAX = 100
let MAX = 12376  // t(12375) = 76576500 with 576 divisors
let GOAL = 500

let LIMIT_PRIME = (MAX*(MAX+1)/2 + 1)
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

calculate_primes()


func prime_factors(n: Int) -> [Int] {
    var factors: [Int] = []
    var nn = n
    while (nn != 1) {
        if (prime_table[nn] == 1) {
            // nn is a prime
            factors.append(nn)
            nn = 1
        } else {
            // nn is a composite number
            factors.append(prime_table[nn])
            nn /= prime_table[nn]
        }
    }
    factors = factors.reverse()
    return factors
}


func triangle(end: Int) -> AnyGenerator<Int> {
    var i: Int = 1
    var t: Int = 0

    return anyGenerator {
        t += i
        i += 1
        return (i <= end+1) ? t : nil
    }
}


func divisors(n: Int) -> Int {
    let d = prime_factors(n)
    
    var divs = 1
    var mult = 2
    var prev_factor = 0
    for factor in d {
        if (factor == prev_factor) {
            divs /= mult
            mult += 1
        } else {
            mult = 2
        }
        divs *= mult
        prev_factor = factor
    }
    return divs
}


var max_divs = 0
var i = 0
for t in triangle(MAX) {
    i += 1

    let divs = divisors(t)

    if (divs > max_divs) {
        max_divs = divs
        print("\(i): Triangle number \(t) has \(divs) divisors")
    }

    if ((i % 1000) == 0) {
        print("    \(i): Triangle number \(t) has \(divs) divisors")
    }

    if (divs > GOAL) {
        print("t = \(t), divs = \(divs)")
        print("Answer =", t)
        //exit()
    }
}
