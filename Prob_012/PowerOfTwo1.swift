#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/

import Foundation

/* convenience function */
func pow2(power: Int) -> Int
{
  return Int(pow(2.0, Double(power)))
}
 
struct PowersOfTwoGenerator1 : GeneratorType {
  typealias Element = Int
  var power : Int = 0
  mutating func next() -> Element?
  {
    return pow2(power++)
  }
}


var n=10 
var g = PowersOfTwoGenerator1()
while n-- > 0 {
  print(g.next()!)
}