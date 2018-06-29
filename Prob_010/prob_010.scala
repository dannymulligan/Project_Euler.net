// Project Euler.net Problem 10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

val limit_prime = 2000000
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

//for (i <- 0 until prime_table.length)
//    println("prime_table(" + i + ") = " + prime_table(i))


var answer: BigInt = 0
var n = 0
for (i <- 2 until limit_prime)
    if (prime_table(i) == 1) {
        answer += i
        n += 1
    }

println("The sum of the " + n + " primes below " + limit_prime + " is " + answer)
