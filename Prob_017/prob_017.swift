#!/usr/bin/swift
//
// Project Euler.net Problem 17
//
// If the numbers 1 to 5 are written out in words: one, two, three, four, five,
// then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
//
// If all the numbers from 1 to 1000 (one thousand) inclusive were written out
// in words, how many letters would be used?
//
// NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
// forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
// 20 letters. The use of "and" when writing out numbers is in compliance with
// British usage.


let LIMIT = 1000

var total_len = 0;

for i in 1...LIMIT {
    var len = 0
    var n = i
    var temp: Int

    // Thousands
    if (n >= 1000) {
        print("one thousand ", terminator:"")
        len += 11
        n -= 1000
    }

    // Hundreds
    if (n >= 100) {
        temp = n / 100
        if (temp == 9) { print("nine hundred " , terminator:"");  len += 11;  n -= 900; }
        if (temp == 8) { print("eight hundred ", terminator:"");  len += 12;  n -= 800; }
        if (temp == 7) { print("seven hundred ", terminator:"");  len += 12;  n -= 700; }
        if (temp == 6) { print("six hundred "  , terminator:"");  len += 10;  n -= 600; }
        if (temp == 5) { print("five hundred " , terminator:"");  len += 11;  n -= 500; }
        if (temp == 4) { print("four hundred " , terminator:"");  len += 11;  n -= 400; }
        if (temp == 3) { print("three hundred ", terminator:"");  len += 12;  n -= 300; }
        if (temp == 2) { print("two hundred "  , terminator:"");  len += 10;  n -= 200; }
        if (temp == 1) { print("one hundred "  , terminator:"");  len += 10;  n -= 100; }
    }

    // And
    if ((i > 100) && (n > 0)) {
        print("and ", terminator:"")
        len += 3
    }

    // Tens
    if (n >= 20) {
        temp = n / 10
        if (temp == 9) { print("ninety " , terminator:"");  len += 6;  n -= 90; }
        if (temp == 8) { print("eighty " , terminator:"");  len += 6;  n -= 80; }
        if (temp == 7) { print("seventy ", terminator:"");  len += 7;  n -= 70; }
        if (temp == 6) { print("sixty "  , terminator:"");  len += 5;  n -= 60; }
        if (temp == 5) { print("fifty "  , terminator:"");  len += 5;  n -= 50; }
        if (temp == 4) { print("forty "  , terminator:"");  len += 5;  n -= 40; }
        if (temp == 3) { print("thirty " , terminator:"");  len += 6;  n -= 30; }
        if (temp == 2) { print("twenty " , terminator:"");  len += 6;  n -= 20; }
    }

    // Tens
    if (n > 0) {
        if (n == 19) { print("nineteen " , terminator:"");  len += 8; }
        if (n == 18) { print("eighteen " , terminator:"");  len += 8; }
        if (n == 17) { print("seventeen ", terminator:"");  len += 9; }
        if (n == 16) { print("sixteen "  , terminator:"");  len += 7; }
        if (n == 15) { print("fifteen "  , terminator:"");  len += 7; }
        if (n == 14) { print("fourteen " , terminator:"");  len += 8; }
        if (n == 13) { print("thirteen " , terminator:"");  len += 8; }
        if (n == 12) { print("twelve "   , terminator:"");  len += 6; }
        if (n == 11) { print("eleven "   , terminator:"");  len += 6; }
        if (n == 10) { print("ten "      , terminator:"");  len += 3; }
        if (n ==  9) { print("nine "     , terminator:"");  len += 4; }
        if (n ==  8) { print("eight "    , terminator:"");  len += 5; }
        if (n ==  7) { print("seven "    , terminator:"");  len += 5; }
        if (n ==  6) { print("six "      , terminator:"");  len += 3; }
        if (n ==  5) { print("five "     , terminator:"");  len += 4; }
        if (n ==  4) { print("four "     , terminator:"");  len += 4; }
        if (n ==  3) { print("three "    , terminator:"");  len += 5; }
        if (n ==  2) { print("two "      , terminator:"");  len += 3; }
        if (n ==  1) { print("one "      , terminator:"");  len += 3; }
    }

    print("(length = \(len))")
    total_len += len
}

// Print the answer
print("The answer is \(total_len)")
