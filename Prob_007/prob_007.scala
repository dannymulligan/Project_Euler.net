// Project Euler.net Problem 7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
// can see that the 6th prime is 13.
//
// What is the 10,001st prime number?

val size = 10001

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



var n, i = 0
while (n < size) {
    if (prime_table(i) == 1) {
        n += 1
    }
    i += 1
}

println("The " + n + "th prime is " + (i-1))
