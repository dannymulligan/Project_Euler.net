#!/usr/bin/env python3
# coding=utf-8
#
# Project Euler.net Problem 449
#
# Chocolate covered candy
#
# Phil the confectioner is making a new batch of chocolate covered
# candy. Each candy centre is shaped like an ellipsoid of revolution
# defined by the equation: b^2x^2 + b^2y^2 + a^2z^2 = a^2b^2.
#
# Phil wants to know how much chocolate is needed to cover one candy
# centre with a uniform coat of chocolate one millimeter thick.
#
# If a=1 mm and b=1 mm, the amount of chocolate required is 28 pi / 3 mm^3
#
# If a=2 mm and b=1 mm, the amount of chocolate required is
# approximately 60.35475635 mm^3.
#
# Find the amount of chocolate in mm3 required if a=3 mm and b=1
# mm. Give your answer as the number rounded to 8 decimal places
# behind the decimal point.

import sys
import time
start_time = time.clock()

########################################


print("Time taken = {:.2f} seconds".format(time.clock() - start_time))
