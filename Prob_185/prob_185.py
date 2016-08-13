#!/usr/bin/env python
# coding=utf-8
#
# Project Euler.net Problem 185
#
# Number Mind
#
# The game Number Mind is a variant of the well known game Master
# Mind.
#
# Instead of coloured pegs, you have to guess a secret sequence of
# digits. After each guess you're only told in how many places you've
# guessed the correct digit. So, if the sequence was 1234 and you
# guessed 2036, you'd be told that you have one correct digit;
# however, you would NOT be told that you also have another digit in
# the wrong place.
#
# For instance, given the following guesses for a 5-digit secret
# sequence,
#
#     90342  2 correct
#     70794  0 correct
#     39458  2 correct
#     34109  1 correct
#     51545  2 correct
#     12531  1 correct
#
# The correct sequence 39542 is unique.
#
# Based on the following guesses,
#
#     5616185650518293  2 correct
#     3847439647293047  1 correct
#     5855462940810587  3 correct
#     9742855507068353  3 correct
#     4296849643607543  3 correct
#     3174248439465858  1 correct
#     4513559094146117  2 correct
#     7890971548908067  3 correct
#     8157356344118483  1 correct
#     2615250744386899  2 correct
#     8690095851526254  3 correct
#     6375711915077050  1 correct
#     6913859173121360  1 correct
#     6442889055042768  2 correct
#     2321386104303845  0 correct
#     2326509471271448  2 correct
#     5251583379644322  2 correct
#     1748270476758276  3 correct
#     4895722652190306  1 correct
#     3041631117224635  3 correct
#     1841236454324589  3 correct
#     2659862637316867  2 correct
#
# Find the unique 16-digit secret sequence.
#
# Solved ??/??/10
# ?? problems solved
# Position #??? on level ?

import sys
import time
import pandas as pd
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=3, suppress=True)

start_time = time.clock()
Test = True
Test = False

if Test:
    Clues = [
        ('90342', 2),
        ('70794', 0),
        ('39458', 2),
        ('34109', 1),
        ('51545', 2),
        ('12531', 1),
    ]
else:
    Clues = [
        ('5616185650518293', 2),
        ('3847439647293047', 1),
        ('5855462940810587', 3),
        ('9742855507068353', 3),
        ('4296849643607543', 3),
        ('3174248439465858', 1),
        ('4513559094146117', 2),
        ('7890971548908067', 3),
        ('8157356344118483', 1),
        ('2615250744386899', 2),
        ('8690095851526254', 3),
        ('6375711915077050', 1),
        ('6913859173121360', 1),
        ('6442889055042768', 2),
        ('2321386104303845', 0),
        ('2326509471271448', 2),
        ('5251583379644322', 2),
        ('1748270476758276', 3),
        ('4895722652190306', 1),
        ('3041631117224635', 3),
        ('1841236454324589', 3),
        ('2659862637316867', 2),
    ]

########################################
# Convert the clue inputs to 1-hot

def onehot(Clue):
    Result = []
    for Char in Clue:
        for N in "0123456789":
            Result.append(1.0 if (Char == N) else 0.0)
    return Result

Inputs = []
Outputs = []
for Clue in Clues:
    Inputs.append(onehot(Clue[0]))
    Outputs.append(Clue[1])

ClueLength = len(Clues[0][0])
NClues = len(Inputs)
NInputs = len(Inputs[0])
TrainFeatures = np.asarray(Inputs)
TrainLabels = np.asarray(Outputs).reshape(len(Outputs), 1)


########################################
# Build a Neural Network to process the data

LearningRate = 0.01
if Test:
    Steps = 5000
else:
    Steps = 100000
tf.set_random_seed(42)
ProbKeepInput = tf.placeholder("float")

# Placeholder for the input data
x = tf.placeholder(tf.float32, shape=[None, NInputs], name='x')
x = tf.nn.dropout(x, keep_prob=ProbKeepInput)  # Dropout

# Build the Neural Network
WInit = (1.0 / NInputs) ** 0.5
W = tf.Variable(tf.random_uniform([NInputs, 1], -WInit, WInit), name='W')  # Weights
y = tf.matmul(x, W)                                                        # No activation function!

# Training data
y_ = tf.placeholder(tf.float32, shape=[None, 1], name='y_')

LossPrediction  = tf.reduce_mean(tf.square(y - y_))  # mean square error
#LossPrediction  = tf.reduce_mean(tf.abs((y - y_) * y))
LossTooBig      = tf.reduce_mean(tf.maximum(W,1.0)-1.0)
LossTooSmall    = tf.reduce_mean(-1.0*tf.minimum(W,0.0))
LossRangeSharp  = tf.reduce_mean(tf.abs((W - 1.0) * W))
LossRangeSmooth = tf.reduce_mean((W - 1.0) * (W - 1.0) * W * W)
LossSums        = tf.reduce_mean(tf.abs(tf.reduce_sum(tf.split(0, ClueLength, W), 1) - 1.0))
#Loss = LossPrediction + 0.5*LossTooBig + 0.5*LossTooSmall + 0.1*LossSums
LossSmooth = LossPrediction + 0.25*LossRangeSmooth + 0.25*LossSums
LossSharp  = LossPrediction + 0.5*LossRangeSharp  + 0.2*LossSums

# Minimize the loss
Optimizer = tf.train.MomentumOptimizer(learning_rate=LearningRate, momentum=0.9)
#Optimizer = tf.train.GradientDescentOptimizer(learning_rate=LearningRate)
TrainSmooth = Optimizer.minimize(loss=LossSmooth)
TrainSharp  = Optimizer.minimize(loss=LossSharp)

# Launch the graph.
Sess = tf.Session()
Sess.run(tf.initialize_all_variables())

# Run training
for Step in range(Steps+1):
    Sess.run(TrainSmooth, feed_dict = {x: TrainFeatures, y_:TrainLabels, ProbKeepInput: 0.8})

    if (Step % 500) == 0:
        TrainLoss = Sess.run(LossSmooth, feed_dict = {x: TrainFeatures, y_:TrainLabels, ProbKeepInput: 1.0})
        TrainLossPrediction = Sess.run(LossPrediction, feed_dict = {x: TrainFeatures, y_: TrainLabels, ProbKeepInput: 1.0})
        TrainLossRange      = Sess.run(LossRangeSmooth)
        TrainLossSums       = Sess.run(LossSums       )
        print("Step {:7,}: Train Loss = {:.4f}, LossPrediction = {:.4f}, LossRange = {:.4f}, LossSums = {:.4f}".format(
            Step, TrainLoss, TrainLossPrediction, TrainLossRange, TrainLossSums))

        #TestLoss  = Sess.run(Loss, feed_dict = {x: TestFeatures, y_: TestLabels})
        #print("    Test Loss = {:.4f}".format(TestLoss))

    if np.isnan(TrainLoss) or np.isinf(TrainLoss):
        Sess.close()
        sys.exit("ERROR, neural network parameters have diverged, aborting training at step {:,}".format(Step))

    if ((Step % 10000) == 0) or (Step == Steps):
        CurrentW = Sess.run(W)
        print("    w =")
        print(CurrentW.reshape(ClueLength,10))
        print("   <0>    <1>    <2>    <3>    <4>    <5>    <6>    <7>    <8>    <9>")

for Step in range(5000):
    Sess.run(TrainSharp, feed_dict = {x: TrainFeatures, y_:TrainLabels, ProbKeepInput: 0.8})
    if (Step % 50) == 0:
        TrainLoss = Sess.run(LossSharp, feed_dict = {x: TrainFeatures, y_:TrainLabels, ProbKeepInput: 1.0})
        TrainLossPrediction = Sess.run(LossPrediction, feed_dict = {x: TrainFeatures, y_: TrainLabels, ProbKeepInput: 1.0})
        TrainLossRange      = Sess.run(LossRangeSharp )
        TrainLossSums       = Sess.run(LossSums       )
        print("Step {:7,}: Train Loss = {:.4f}, LossPrediction = {:.4f}, LossRange = {:.4f}, LossSums = {:.4f}".format(
            Step, TrainLoss, TrainLossPrediction, TrainLossRange, TrainLossSums))

CurrentW = Sess.run(W)
print("    w =")
print(CurrentW.reshape(ClueLength,10))
print("   <0>    <1>    <2>    <3>    <4>    <5>    <6>    <7>    <8>    <9>")

np.savetxt("W.csv", CurrentW.reshape(1,ClueLength*10), delimiter=',')
np.savetxt("TrainFeatures.csv", TrainFeatures, delimiter=',')


########################################
# Dump the best solution for the training vectors
Results = Sess.run(y, feed_dict = {x: TrainFeatures, ProbKeepInput: 1.0})
for Clue, Result in zip(Clues, Results.reshape(NClues)):
    print("Clue = {} match = {} NN = {:.6f}, delta = {:.6f}".format(
        Clue[0], Clue[1], Result, Clue[1]-Result))


########################################
# Print the solution
if Test:
    print("Expected solution = 39542")

Answer = 0
print("Answer =", Answer)
now_time = time.clock()
print("Total time taken = {:,.2f} seconds".format(now_time - start_time))

commentary = '''
Solution log:

- Found solutions for the simultaneous equations that made no sense
because some elements of W were < 0.0 or > 1.0, so I had to add
LossTooSmall & LossTooLarge loss function to penalize elements of W
that were > 1.0 or < 0.0.

- Found solutions where each of the parameters for the one-hot
encoding of a single digit didn't add up to 1.0.  Added LossSums to
the loss function to penalize this.

- Found solutions where some of the parameters for a single one-hot
encoding added to 1.0 but were distributed between multiple values.
Replaced LossTooSmall and LossTooLarge with LossRange to penalise
this.

- Found solid solutions to the test problem, but not quite there for
the real problem.  LossPrediction is essentially 0, but LossRange
stalls at about 0.0232.  The W coefficients show high confidence for
many digits in the solution, but some digits are still not clear.

- Tried a smoother loss function to drive coefficients towards 0.0 or
1.0, I used...
    LossRange = tf.reduce_mean((W - 1.0) * (W - 1.0) * W * W)
instead of...
    LossRange = tf.reduce_mean(tf.abs((W - 1.0) * W))


     01 23 45 67  89 ab cd ef
     -- -- -- --  -- -- -- --
 1   38 47 43 96  47 29 _0 _7  1 correct
 5   31 74 24 84  39 46 5_ 58  1 correct
 8   81 57 _5 _3  4_ 11 84 83  1 correct
 b   6_ 75 71 19  15 07 70 50  1 correct
 c   69 13 85 9_  73 12 13 60  1 correct
 i   48 95 72 26  52 19 03 06  1 correct

 0   56 16 1_ 56  50 51 82 93  2 correct
 6   45 13 55 90  9_ 14 61 17  2 correct
 9   _6 15 25 07  4_ _8 68 99  2 correct
 d   64 42 8_ 90  55 04 27 68  2 correct
 f   __ _6 50 94  71 27 14 _8  2 correct
 g   52 5_ 5_ 33  79 64 43 22  2 correct
 l   _6 59 86 26  37 _1 6_ 67  2 correct

 2   58 55 46 29  40 81 05 87  3 correct
 3   97 42 85 55  _7 06 83 53  3 correct
 4   42 96 84 96  43 6_ 75 _3  3 correct
 7   78 90 97 15  48 9_ 80 67  3 correct
 a   86 90 09 58  51 52 62 54  3 correct
 h   17 48 27 04  76 75 82 76  3 correct
 j   30 4_ 63 1_  17 22 46 3_  3 correct
 k   18 4_ 23 _4  5_ _2 45 89  3 correct

     00 00 00 00  .0 0. 00 00
     11 1. 11 1.  11 11 11 1?
     .2 .2 22 22  22 22 22 22
     3. 33 .3 33  33 .3 .3 33
     44 44 44 44  4. 44 44 .4
     55 55 55 55  55 55 55 5.
     66 66 66 .6  66 66 66 66
     77 77 77 77  77 77 77 77
     88 88 8. 88  88 88 8. 88
     99 99 99 99  99 99 99 99

 e   23 21 38 61  04 30 38 45  0 correct

Possible algorithm to solve

- Set up a list for each digit in each location, and mark digits as
    * definitely true
    * possibly true
    * unknown
    * possibly false
    * definitely false

- For each unknown digit in each of the clues with 1 match, set the digit
  to possibly true, and look for logical impossibilities.  If any are found
  then that digit id definitely false.

- For each unknown digit in each of the clues with 1 match, set the digit
  to possibly false, and look for logical impossibilities.  If any are found
  then that digit id definitely true.

- Whenever we make any progress, restart with the simpler problem.


With Dropout

    w =
 <0> +5+ (4)[[-0.    -0.001 -0.     0.001 -0.     1.     0.001 -0.    -0.    -0.001]
 <1> +7+ (6) [ 0.     0.001  0.     0.001  0.001  0.     0.001  1.     0.002  0.   ]
 <2>     (4) [-0.009 -0.073 -0.082 -0.009  0.251  0.    -0.009 -0.    -0.009  0.945]
 <3> +2+ (0) [ 0.    -0.     1.001 -0.    -0.     0.001 -0.001  0.001 -0.    -0.   ]
 <4>     (2) [-0.    -0.002 -0.001 -0.001  0.109  0.898 -0.002 -0.001 -0.    -0.002]
 <5>     (6) [-0.004 -0.001 -0.001  0.    -0.001 -0.068  0.999 -0.064  0.139 -0.   ]
 <6>     (1) [ 0.966 -0.125 -0.    -0.    -0.03  -0.015 -0.002 -0.03  -0.001  0.245]
 <7> +4+ (5) [ 0.    -0.001 -0.001 -0.     0.999 -0.001  0.    -0.001 -0.     0.   ]
 <8>     (7) [-0.054  0.886 -0.001 -0.001  0.166  0.052 -0.002 -0.047 -0.002 -0.002]
 <9>     (1) [-0.    -0.001 -0.001 -0.046 -0.     0.047 -0.001 -0.     0.999 -0.   ]
 <a> +9+ (8) [ 0.002 -0.     0.001  0.001  0.     0.001 -0.    -0.     0.001  0.999]
 <b> +2+ (4) [-0.001 -0.     1.    -0.     0.002 -0.001 -0.001 -0.    -0.     0.   ]
 <c> +6+ (9) [-0.    -0.001  0.098  0.    -0.    -0.     1.    -0.    -0.097 -0.   ]
 <d>     (5) [ 0.183 -0.001 -0.001 -0.001 -0.001  0.704 -0.001  0.115 -0.    -0.001]
 <e> +3+ (3) [ 0.    -0.    -0.     1.    -0.    -0.     0.    -0.     0.    -0.   ]
 <f> +3+ (3) [-0.001 -0.001 -0.001  0.999 -0.    -0.001 -0.001  0.001  0.001 -0.   ]]
              <0>    <1>    <2>    <3>    <4>    <5>    <6>    <7>    <8>    <9>
  ^   ^   ^
  |   |   +-- Actual solution
  |   +------ NN thinks that the solution is
  +---------- Which digit of the clue we're talking about

Without Dropout

    w =
 <0>     (4)[[ 0.     0.01  -0.    -0.     0.699  0.544  0.     0.    -0.251  0.   ]
 <1>     (6) [-0.001 -0.001  0.202 -0.    -0.     0.001  0.795  0.    -0.     0.   ]
 <2>     (4) [ 0.     0.014 -0.     0.     1.025  0.131  0.     0.     0.    -0.171]
 <3> +0+ (0) [ 0.999 -0.    -0.     0.    -0.001 -0.001 -0.    -0.001  0.     0.   ]
 <4>     (2) [ 0.001  0.001  0.012 -0.     0.002  0.002  0.001  0.972  0.021  0.002]
 <5>     (6) [-0.001 -0.    -0.002 -0.    -0.001 -0.     1.001  0.    -0.001 -0.001]
 <6> +0+ (1) [ 1.    -0.001 -0.002 -0.001 -0.001 -0.003 -0.001 -0.001 -0.001  0.   ]
 <7> +5+ (5) [ 0.001  0.     0.     0.     0.001  1.001 -0.02   0.001  0.     0.019]
 <8>     (7) [-0.    -0.001 -0.    -0.     0.14  -0.215 -0.     0.003 -0.     1.064]
 <9>     (1) [-0.     0.999 -0.002  0.001  0.     0.001  0.    -0.     0.    -0.   ]
 <a> +6+ (8) [ 0.001 -0.    -0.     0.03   0.    -0.031  1.001  0.     0.     0.   ]
 <b>     (4) [-0.    -0.001  0.999 -0.     0.166  0.    -0.     0.     0.    -0.167]
 <c>     (9) [ 0.     0.     0.    -0.     0.     0.     0.     0.001  1.     0.   ]
 <d>     (5) [-0.     0.    -0.067 -0.047 -0.     1.117 -0.     0.    -0.    -0.   ]
 <e> +3+ (3) [-0.002  0.001  0.     1.    -0.    -0.     0.001  0.001  0.    -0.   ]
 <f> +8+ (3) [ 0.     0.     0.     0.    -0.022 -0.009 -0.     0.031  1.     0.001]]
              <0>    <1>    <2>    <3>    <4>    <5>    <6>    <7>    <8>    <9>
  ^   ^   ^
  |   |   +-- Actual solution
  |   +------ NN thinks that the solution is
  +---------- Which digit of the clue we're talking about


With Dropout
Step  50,000: Train Loss = 0.0097, LossPrediction = 0.0002, LossRange = 0.0160, LossSums = 0.0030
Step  50,000: Train Loss = 0.0111, LossPrediction = 0.0003, LossRange = 0.0174, LossSums = 0.0043
Without Dropout

Dropout probably helps, but it's not conclusive.

LossPrediction = loss function for solving the clue equations
LossRange      = loss function for weights being close to 0.0 or 1.0
LossSums       = loss function for each character weights adding to 1.0
Loss = LossPrediction + 0.25*LossRange + 0.25*LossSums

My problem appears to be that I have too many local minima in the Loss
function, where non-integer Weights solve the clues, and I'm not able
to climb out to find a solution to the clues with integer weights.

I could try adjusting the relative scales of LossPrediction &
LossRange, but too high on either one will lock me in to a local
minima, and finding the right balance is hard.
'''
