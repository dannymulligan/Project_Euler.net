#!/usr/bin/swift
//
// Project Euler.net Problem 9
//
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//     a^(2) + b^(2) = c^(2)
//
// For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.



// Since a + b + c are equal to 1000, and a < b < c, the minimum value
// for c must be 335. If c = 334, then at most b = 333, and at most a =
// 332, and a + b + c = 999 which is too small.
//
// The maximum value of c is 997, because if a = 1, and b = 2 and c =
// 998, then a + b + c = 1001 which is too big.
//
// So we're going to search for c values between 335 and 997.


func find_answer_version3(cmin: Int, cmax: Int, target: Int) {
    var a: Int
    for c in cmin..<cmax {
        for b in 2..<c {
            a = target - b - c
            if a > b || a < 1 {
                continue
            }
            if (a*a + b*b) == c*c {
                print("\(a)^2 + \(b)^2 = \(c)^2, a + b + c = \(a+b+c), abc = \(a*b*c)")
            }
        }
    }
}

find_answer_version3(335, cmax: 998, target: 1000)
