#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/

import Foundation

/* convenience function */
func pow2(power: Int) -> Int
{
  return Int(pow(2.0, Double(power)))
}
 

struct PowersOfTwoSequence3 : SequenceType
{
    let endPower : Int
    struct Generator : GeneratorType {
        typealias Element = Int
        var power : Int = 0
        var endPower : Int
        init(end : Int)
        {
            endPower = end
        }
        mutating func next() -> Element?
        {
            return (power < endPower) ? pow2(power++) : nil
        }
    }
    init(end: Int)
    {
        self.endPower = end
    }
    func generate() -> Generator {
        return Generator(end: self.endPower)
    }
}


for x in PowersOfTwoSequence3(end:10)
{
    print(x)
}