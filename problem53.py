# Problem 53 - Combinatoric selections
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, (5 3)=10.
# In general, (n r) = n! / [ r! * (n−r)! ] , where r ≤ n, n!=n×(n−1)×...×3×2×1, and 0!=1.
# It is not until n=23, that a value exceeds one-million: (2310)=1144066.
# How many, not necessarily distinct, values of (nr) for 1 ≤ n ≤ 100, are greater than one-million?
#
# Answer: 4075

import math


def problem53():
    n = 1
    counter = 0
    while n <= 100:
        r = 1
        while r <= n:
            x = math.factorial(r) * math.factorial(n - r)
            kappa = math.factorial(n) / x
            if kappa > 1000000:
                counter = counter + 1
            r = r + 1
        n = n + 1
    print(counter)


problem53()