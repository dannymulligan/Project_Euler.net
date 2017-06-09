#!/usr/bin/env python3

# from: https://projecteuler.net/thread=190;page=7
# grauerwolf's solution, posted 21 Aug 2015

def f(x):
    # x1 is a dependent variable, x1 = n-(sum(x2..xn))
    # so the function to optimize is
    # f(x2..xn) = (n-sum(x2..xn)) * x2**2 * x3**3 * ... xn**n
    # since x1 does not appear in the list and list starts at 0, x2 is x[0], x3 is x[1], xi = x[i-2] and so on
    result = len(x) + 1 - sum(x)
    for i in range(len(x)):
        result *= x[i]**(i+2)
    return result

def f_strich(x,i):
    # partial derivative with respect to x[i]
    # df/dxi = -1 * x2**2 * x3**3 * ... xn**n + i*(n-sum(x2..xn)) * x2**2 * x3**3 * ... xn**n / xi
    # since x1 does not appear in the list and list starts at 0, x2 is x[0], x3 is x[1], xi = x[i-2] and so on
    result = len(x) + 1 - sum(x)
    result *= (i+2)
    product = 1
    for j in range(len(x)):
        product *= x[j]**(j+2)
    result *= product/x[i]
    result -= product
    return result

def nabla(x):
    #gradient
    return [f_strich(x,i) for i in range(len(x))]

def solution(m):
    alpha = 1e-5  # intial value for step size
    x = [1] * m   # initial value, f(x) = 1
    for i in range(10**6):  # 10**6 will never be reached, but to prevent infinite loop, its always good to have this
        n = nabla(x)

        # determine step size
        # reduce alpha to prevent divergence
        x_try = [x[k]+alpha*n[k] for k in range(m)]
        shortened = False
        while f(x_try) < f(x):
            shortened = True
            alpha /= 2
            x_try = [x[k]+alpha*n[k] for k in range(m)]
            
        # reduce alpha if lower alpha gives higher f(x)
        if not shortened:
            x_try = [x[k]+alpha*1*n[k] for k in range(m)]
            x_s   = [x[k]+alpha/2*n[k] for k in range(m)]
            while f(x_try) < f(x_s):
                shortened = True
                alpha /= 2
                x_try = [x[k]+alpha*1*n[k] for k in range(m)]
                x_s   = [x[k]+alpha/2*n[k] for k in range(m)]

        # extend if possible
        if not shortened:
            try:
                x_ext = [x[k]+10*alpha*n[k] for k in range(m)]
                if (f(x_ext) > f(x_try) and (f(x_ext) < 2*f(x_try)) and alpha < 1e-3): #f(x_ext) can diverge seriously, causing a floating point error, better stay inside the try-block
                    alpha *= 10
            except:
                pass # if f(x_ext) did diverge seriously, there is no need to do anything else than carry on

        # eventually, after determining the step size for more than half of the code, do the step
        x = [x[k]+alpha*n[k] for k in range(len(x))]
        if alpha < 10**(min(-7,-m-4)):
            return x
        print("    alpha = {}, f(x) = {}".format(alpha, f(x)))


############################################################

final_result = 0
for m in range(1,15):
    x = solution(m)
    final_result += int(f(x))
    print("solution({}) = {}".format(m, x))
    print("f({}) = {}".format(m, f(x)))
print(final_result)

