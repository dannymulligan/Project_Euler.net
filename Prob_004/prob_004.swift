#!/usr/bin/swift
//
// Project Euler.net Problem 4
//
// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
// Find the largest palindrome made from the product of two 3-digit numbers.


func palindrome(candidate_int: Int) -> Bool {
    // Convert the candidate number to a string
    let candidate_str = String(candidate_int)
    let candidate_str_rev = String(candidate_str.characters.reverse())

    // Check if it is a palindrome
    return candidate_str == candidate_str_rev
}


var max_palindrome = 0
var max_i = 0, max_j = 0
var candidate: Int
for i in (100...999).reverse() {
    for j in (100...999).reverse() {
        candidate = i * j
        if ((candidate > max_palindrome) && palindrome(candidate)) {
            max_palindrome = candidate;
            (max_i, max_j) = (i, j)
            print("i = \(i), j = \(j), candidate = \(candidate)")
        }
    }
}


print("Largest palindrome is \(max_palindrome) from multiplying \(max_i) by \(max_j).")
