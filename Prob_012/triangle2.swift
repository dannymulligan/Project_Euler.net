#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/

func TriangleGenerator(end: Int) -> AnyGenerator<Int> {
    var i: Int = 1
    var t: Int = 0

    return anyGenerator {
        t += i
        i += 1
        return (i <= end+1) ? t : nil
    }
}


var i = 0
for x in TriangleGenerator(16) {
    i += 1
    print("Triangle number \(i) = \(x)")
}