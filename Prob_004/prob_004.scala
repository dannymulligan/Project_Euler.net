// Project Euler.net Problem 4
//
// A palindromic number reads the same both ways.
//
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
// Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome (candidate_int: Int): Boolean = {
    val candidate_str = candidate_int.toString
    val length = candidate_str.length
    for (i <- 0 until length) {
        if (candidate_str(i) != candidate_str(length-1-i))
            return false
    }
    true
}

var max_palindrome = 0
var max_i, max_j = 0

for (i <- 100 to 999; j <- i to 999) {
    val candidate = i * j
    if ((candidate > max_palindrome) && palindrome(candidate)) {
        max_palindrome = candidate
        max_i = i
        max_j = j
    }
}
println("Largest palindrome is " + max_palindrome + " from multiplying " + max_i + " by " + max_j + ".")
