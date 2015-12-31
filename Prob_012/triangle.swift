#!/usr/bin/swift

// Based on code from:
//     http://iosdeveloperzone.com/2014/10/13/swift-standard-library-generators-sequences-and-collections/


struct TriangleSequence: SequenceType {
    let n: Int
    
    struct Generator: GeneratorType {
        typealias Element = Int
        var i: Int = 1
        var t: Int = 0
        var n: Int
        
        init(end: Int) {
            n = end
        }
        
        mutating func next() -> Element? {
            t += i
            i += 1
            return (i <= n+1) ? t : nil
        }
    }
    
    init(end: Int) {
        self.n = end
    }
    
    func generate() -> Generator {
        return Generator(end: self.n)
    }
}


var i = 0
for x in TriangleSequence(end:16) {
    i += 1
    print("Triangle number \(i) = \(x)")
}