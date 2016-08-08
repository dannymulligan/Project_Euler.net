#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/

import Foundation

/* convenience function */
func pow2(power: Int) -> Int
{
  return Int(pow(2.0, Double(power)))
}
 

struct PowersOfTwoGenerator2 : GeneratorType {
    typealias Element = Int
    var power : Int = 0
    let endPower : Int
    init(end : Int)
    {
        endPower = end
    }
    mutating func next() -> Element?
    {
        return (power < endPower) ? pow2(power++) : nil
    }
}


var g2 = PowersOfTwoGenerator2(end:10)
while let x = g2.next() {
    print(x)
}