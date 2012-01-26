import math
prime_dict = dict()

import fractions
def totient(n):
    cnt = 0
    for i in range(0, n):
        if fractions.gcd(n, i) == 1:
            cnt += 1
    return cnt



def create_totient(max_n):
    totient_dict = {1:1}
    primes = set(gen_primes(1, max_n))

    def totient(n):
        if n == 1:
            return 1
        if n in totient_dict:
            return totient_dict[n]
        if n in primes:
            totient_dict[n] = n - 1
            return n - 1
        totient_prod = 1
        calc_n = n
        for p in primes:
            prev = 0
            pexp = 1
            while calc_n % p == 0:
                prev = pexp
                pexp *= p
                calc_n = calc_n / p
            totient_prod *= pexp - prev
            if calc_n in totient_dict:
                # print "Cache used for ", calc_n, " (", n, ")"
                totient_dict[n] = totient_dict[calc_n] * totient_prod
                return totient_dict[n]

    return totient


def isprime(n):
        if n in prime_dict:
            return prime_dict[n]
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(float(n))) + 1):
            if n % i == 0:
                prime_dict[n] = False
                return False
        prime_dict[n] = True
        return True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_bouncy(n):
        pos = neg = False
        s = str(n)
        for i in range(1, len(s)):
            dig = int(s[i])
            prevdig = int(s[i - 1])
            # print dig, prevdig
            diff = dig - prevdig
            if diff > 0:
                pos = True
            if diff < 0:
                neg = True
            if neg and pos:
                return True

        return False

def add_frac(x, y):
    a = b = c = d = 0
    if isinstance(x, int):
        a = x
        b = 1
    else:
        a = x[0]
        b = x[1]
    if isinstance(y, int):
        c = y
        d = 1
    else:
        c = y[0]
        d = y[1]
    return [a * d + b * c, b * d]

def div_frac(x, y):
    a = b = c = d = 0
    if isinstance(x, int):
        a = x
        b = 1
    else:
        a = x[0]
        b = x[1]
    if isinstance(y, int):
        c = y
        d = 1
    else:
        c = y[0]
        d = y[1]
    return [a * d, b * c]


def sqrt_continuous_frac(N, iterations):
    root = math.sqrt(N)
    integ = int(root)
    pair = [1, -integ]
    l = list()
    for _i in range(iterations):
        l.append(integ)
        denom = N - pair[1] ** 2
        g = gcd(denom, pair[0])
        denom /= g
        pair[0] /= g
        numer = pair[0] * (root - pair[1])
        if denom == 0:
            return l
        integ = int(numer / denom)
        pair[1] = -(denom * integ + pair[1])
        pair[0] = denom
    return l

def expand_frac(l, n, i = 0):
    v = l[i]
    if i == n:
        return v
    return add_frac(v, div_frac(1, expand_frac(l, n, i + 1)))

def gen_primes(start, end):
    #===========================================================================
    # l = range(2, end + 1)
    # newl = list()
    # while len(l) > 0:
    #    v = l[0]
    #    l = filter(lambda x: x % v != 0, l)
    #    newl.append(v)
    # newl = filter(lambda x: x >= start, newl)
    # return newl
    #===========================================================================
    l = [2]
    cnt = 0
    for i in xrange(2 * (max(start, 2) / 2) + 1, end + 1, 2):
        cnt += 1
        if cnt % 10000 == 0:
            print i
        if MillerRabin(i, 20):
        #=======================================================================
        # prime = True
        # for p in l:
        #    if i % p == 0:
        #        prime = False
        #        break
        # #print i
        # if prime:
        #    #print i
        #=======================================================================            
            l.append(i)
    return l


import random


 
_mrpt_num_trials = 6 # number of bases to test
 
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for _i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
    return r  

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)

def C(n,k):
    return fact(n)/fact(n-k)/fact(k)
    
def test(a, n):
    """
    test(a, n) -> bool Tests whether n is complex.
    
    Returns:
      - True, if n is complex.
      - False, if n is probably prime.
    """
    b = toBinary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True # Complex
        if b[i] == 1:
            d = (d * a) % n
    if d != 1:
        return True # Complex
    return False # Prime

def ipow(base,exp,m):
    prod = 1
    while exp > 0:
        if exp % 2 == 1:
            prod *= base
            prod %= m
        exp /= 2
        base *= base
        base %= m
    return prod


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def MillerRabin(n, s = 5):
    """
     MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not

    Returns:
      - True, if n is probably prime.
      - False, if n is complex.
    """
    for _j in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        if (test(a, n)):
            return False # n is complex
    return True # n is prime



