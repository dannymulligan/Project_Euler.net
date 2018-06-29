// Project Euler.net Problem 3
//
// Find the largest prime factor of a composite number.
//
// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

import math._

val target = BigInt(600851475143L)
val sqrt_target = (sqrt(target.toFloat) + 1.0).toInt

println("sqrt_target = " + sqrt_target)

val limit_prime = sqrt_target.toInt
var prime_table = new Array[Int](limit_prime)  // table of largest factor
for (i <- 0 until limit_prime)
    prime_table(i) = 1


def calculate_primes (): Unit = {
    var i = 2
    while (i < (limit_prime/2)) {
        if (prime_table(i) == 1) {
            var j = i*2
            while (j < limit_prime) {
                prime_table(j) = i
                j += i
            }
        }
        i += 1
    }
}

calculate_primes()

var answer = 0
var i = limit_prime - 1
while (answer == 0) {
    if (prime_table(i) == 1) {
        if ((target % i) == 0) {
            answer = i
        }
    }
    i -= 1
}
i += 1

println("Answer is " + answer)
