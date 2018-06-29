// Project Euler.net Problem 9
//
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//     a^(2) + b^(2) = c^(2)
//
// For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.


def find_answer_version3 (cmin: Int, cmax: Int, target: Int): Unit = {
    for (c <- cmin until cmax)
        for (b <- 2 until c) {
            val a = target - b - c
            if (((a*a + b*b) == c*c) && (a > 1) && (b > a))
                printf("%d^2 + %d^2 = %d^2, a + b + c = %d, abc = %d\n", a, b, c, a+b+c, a*b*c)
                //return a*b*c
        }
}

val answer = find_answer_version3(335, 998, 1000)
