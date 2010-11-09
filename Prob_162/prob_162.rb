=begin
In the hexadecimal number system numbers are represented using 16 different digits:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist with all of the digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.

(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number as hexadecimal and without leading zeroes , e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)
=end
require 'matrix'

norm = Matrix[
  [0,13,0,1,1,0,0,0,0], #first
  [0,13,1,1,1,0,0,0,0], #nil
  [0,0,14,0,0,1,1,0,0], #0
  [0,0,0,14,0,1,0,1,0], #1
  [0,0,0,0,14,0,1,1,0], #a
  [0,0,0,0,0,15,0,0,1], #01
  [0,0,0,0,0,0,15,0,1], #0a
  [0,0,0,0,0,0,0,15,1], #1a
  [0,0,0,0,0,0,0,0,16] #01a
  ].transpose

=begin
first nil 0 1 a 01 0a 1a 01a
first 13 1 1
nil 13 1 1 1
0 14 1 1
1 14 1 1
a 14 1 1
01 15 1
0a 15 1
1a 15 1
01a 16
=end

three = Matrix[
  [0,0,0,1,1,0,0,0,0], #first
  [0,0,1,1,1,0,0,0,0], #nil
  [0,0,14,0,0,1,1,0,0], #0
  [0,0,0,14,0,1,0,1,0], #1
  [0,0,0,0,14,0,1,1,0], #a
  [0,0,0,0,0,15,0,0,1], #01
  [0,0,0,0,0,0,15,0,1], #0a
  [0,0,0,0,0,0,0,15,1], #1a
  [0,0,0,0,0,0,0,0,16] #01a
  ].transpose

=begin
3 left
first nil 0 1 a 01 0a 1a 01a
first 1 1
nil 1 1 1
0 14 1 1
1 14 1 1
a 14 1 1
01 15 1
0a 15 1
1a 15 1
01a 16
=end

two = Matrix[
  [0,0,0,0,0,0,0,0,0], #first
  [0,0,0,0,0,0,0,0,0], #nil
  [0,0,0,0,0,1,1,0,0], #0
  [0,0,0,0,0,1,0,1,0], #1
  [0,0,0,0,0,0,1,1,0], #a
  [0,0,0,0,0,15,0,0,1], #01
  [0,0,0,0,0,0,15,0,1], #0a
  [0,0,0,0,0,0,0,15,1], #1a
  [0,0,0,0,0,0,0,0,16] #01a
  ].transpose


=begin
2 left
first nil 0 1 a 01 0a 1a 01a
first
nil
0 1 1
1 1 1
a 1 1
01 15 1
0a 15 1
1a 15 1
01a 16
=end

one = Matrix[
  [0,0,0,0,0,0,0,0,0], #first
  [0,0,0,0,0,0,0,0,0], #nil
  [0,0,0,0,0,0,0,0,0], #0
  [0,0,0,0,0,0,0,0,0], #1
  [0,0,0,0,0,0,0,0,0], #a
  [0,0,0,0,0,0,0,0,1], #01
  [0,0,0,0,0,0,0,0,1], #0a
  [0,0,0,0,0,0,0,0,1], #1a
  [0,0,0,0,0,0,0,0,16] #01a
  ].transpose

=begin
1 left
first nil 0 1 a 01 0a 1a 01a
first
nil
0
1
a
01 1
0a 1
1a 1
01a 16

=end

v = Vector[1,0,0,0,0,0,0,0,0]
m = one*two*three
total = 0
(3..16).each do |size|
  if size == 3
    total += (m*v).to_a.reduce(:+)
  else
    total += (m*(norm**(size-3))*v).to_a.reduce(:+)
  end
end
p total, total.to_s(16).upcase

