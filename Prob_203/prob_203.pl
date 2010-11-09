#!/usr/bin/perl
# From: http://blog.dreamshire.com/2009/04/20/project-euler-problem-204-solution/
@primes = (2, 3, 5, 7, 11, 13, 17, 19);
$rows = 51; #more rows means more primes
$s = 0;
 
#use a hash, b, to select the distinct binomial coefficients from Pascal's triangle
while((@_=(1,map$_[$_-1]+$_[$_],1..@_))<=$rows){ grep $b{$_}++, @_}
 
for $x (keys %b) {
  $s+=$x if sqf($x);
}
print "Answer to PE203 = $s\n";


sub sqf { return ! grep @_[0]%($_*$_)==0, @primes }
