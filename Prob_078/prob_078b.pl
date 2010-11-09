($p[0], $n, $i, $m) = (1, 0, 1, 1e6);
 
for $i (1..250) {             #generate pentagonal numbers for generating function
  $p = $i*(3 * $i - 1)/2;
  push @k, $p, $p+$i;
}
 
while ($p[$n++]) {         #expand generating function to calculate p(n)
  my ($p, $i) = (0, 0);
  $p += ($i%4>1 ? -1 : 1 ) * $p[$n - $k[$i++]] while ($k[$i] <= $n); 
  $p[$n] = $p % $m; 
} 
print "Answer to PE78 = ",$n-1;
