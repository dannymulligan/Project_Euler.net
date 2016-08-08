#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/

import Foundation

/* convenience function */
func pow2(power: Int) -> Int
{
  return Int(pow(2.0, Double(power)))
}
 

struct PowersOfTwoSequence4 : SequenceType
{
    let endPower : Int
    init(end: Int)
    {
        self.endPower = end
    }
    func generate() -> AnyGenerator<Int> {
        var power : Int = 0
        var nextClosure : () -> Int? = {
            (power < self.endPower) ? pow2(power++) : nil
        }
        return AnyGenerator<Int>(nextClosure)
        //return nextClosure
    }
}


for x in PowersOfTwoSequence4(end:10)
{
    print(x)
}