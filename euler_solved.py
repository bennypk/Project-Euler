from Euler.euler_tools import *

def problem_31(): # solved
    # Remember +1    
    cnt = 1
    for a in range(200 / 100 + 1):
        for b in range((200 - a * 100) / 50 + 1):
            for c in range((200 - a * 100 - b * 50) / 20 + 1):
                for d in range((200 - a * 100 - b * 50 - c * 20) / 10 + 1):
                    for e in range((200 - a * 100 - b * 50 - c * 20 - d * 10) / 5 + 1):
                        for f in range((200 - a * 100 - b * 50 - c * 20 - d * 10 - e * 5) / 2 + 1):
                            pennies = 200 - (a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2)
                            cnt += 1
                            print cnt, a, b, c, d, e, f, pennies, a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f * 2 + pennies

    print cnt

def problem_38(): # solved
    for i in [1, 10, 100]:
        for x in range(90 * i, 100 * i):
            for k in range(1, 9):
                sum = ''
                for n in range(1, k):
                    sum += str(x * n)
                if len(set(sum)) == len(sum) == 9 and not '0' in set(sum):
                    print x, n, sum


def problem_62(): # solved

    def get_key(s):
        return ''.join(sorted(str(s)))

    d = dict()
    for x in range(9000):
        k = get_key(x * x * x)
        if k not in d:
            d[k] = list()
            d[k].append([])
            d[k].append(0)
        d[k][0].append([x, x * x * x])
        d[k][1] += 1

    for k in d:
        if d[k][1] == 5:
            print d[k]


def problem_62_(): #solved
    cnt = 0
    for x in range(1, 300):
        for y in range(80):
            prod = 1
            for _i in range(y):
                prod *= x
            if len(str(prod)) == y:
                cnt += 1
                print x, y, prod
    print cnt

def num_sundays():
    months = [31, # Jan
              28, # Feb
              31, # Mar
              30, # Apr
              31, # May
              30, # Jun
              31, # Jul
              31, # Aug
              30, # Sep 
              31, # Oct
              30, # Nov
              31] # Dec

    day = 1
    cnt = 0
    for year in range(1900, 2001):
        for i, m in enumerate(months):
            leap_year = False
            if year % 100 == 0:
                if year % 400 == 0:
                    leap_year = True
            else:
                if year % 4 == 0:
                    leap_year = True

            ndays = m + int(i == 1 and leap_year)
            print year, i + 1, day + 1, ndays

            day = (day + ndays) % 7
            if year > 1900 and day == 0:
                cnt += 1

    print cnt

def problem_74(): # solved

    fact_dict = dict()
    def fact(n):
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod

    for i in range(10):
        fact_dict[i] = fact(i)

    def fact_sum(n):
        s = map(int, str(n))
        sum_ = 0
        for x in s:
            sum_ += fact_dict[x]

        return sum_

    def fact_conv(n):
        s = set()
        while 1:
            s.add(n)
            n = fact_sum(n)
            if n in s:
                return len(s)

    c = 0
    for x in range(1000000):
        print x
        l = fact_conv(x)
        if l == 60:
            c += 1

    print c



def problem_60(): # solved

    import itertools


    def concat_primes(x, y):
        return isprime(int(str(x) + str(y))) and isprime(int(str(y) + str(x)))

    def concat_prime_list(lst, new):
        for x in lst:
            if not concat_primes(x, new):
                return False
        return True

    primes_list = gen_primes(1, 10000)
    print "%d primes" % len(primes_list)
    list_of_prime_pairs = list()
    for prime_pair in itertools.combinations(primes_list, 2):
        if concat_primes(prime_pair[0], prime_pair[1]):
            print prime_pair
            list_of_prime_pairs.append([prime_pair[0], prime_pair[1]])
    print "%d Pairs" % len(list_of_prime_pairs)

    def append_primes_to_lst(prime_lst, lst):
        new_lst = list()
        for p in primes_list:
            for q in lst:
                if concat_prime_list(q, p):
                    new_lst.append(q + [p])
        return new_lst

    list_of_four_primes = list()
    for prime_pair in itertools.combinations(list_of_prime_pairs, 2):
        if concat_prime_list(prime_pair[0], prime_pair[1][0]) and concat_prime_list(prime_pair[0], prime_pair[1][1]):
            list_of_four_primes.append(prime_pair[0] + prime_pair[1])
    #append_primes_to_lst(primes_list, list_of_prime_pairs)
    #print "%d Three" % len(list_of_three_primes)

    #list_of_four_primes = append_primes_to_lst(primes_list, list_of_three_primes)
    print "%d Quads" % len(list_of_four_primes)
    print list_of_four_primes

    list_of_five_primes = append_primes_to_lst(primes_list, list_of_four_primes)
    print "%d Fives" % len(list_of_five_primes)
    print list_of_five_primes

    min_sum = 1000000
    for l in list_of_five_primes:
        sum = reduce(lambda x, y: x + y, l)
        if sum < min_sum:
            min_sum = sum
    print min_sum


import itertools



def problem_57(): # solved

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

    d = dict()
    def calc_iter(n, arg):
        if n in d:
            return d[n]
        if n == 0:
            d[0] = 2
            return 2
        res = add_frac(arg, div_frac(1, calc_iter(n - 1, 2)))
        return res

    cnt = 0
    import sys
    sys.setrecursionlimit(10000)
    for i in range(1, 1000):
        res = calc_iter(i, 1)
        if len(str(res[0])) > len(str(res[1])):
            print res
            cnt += 1
    print cnt


def problem_26(): # solved

    import sys
    sys.setrecursionlimit(10000)

    def frac(a, b, n = 2000):
        if a == 0 or n == 0:
            return ''
        newa = a
        while newa < b:
            newa = newa * 10
        return str(int(newa / b)) + frac(newa % b, b, n - 1)

    def long_seq(s):

        q = 1
        maxq = 0
        while q < len(s):
            i = 0
            prev = s[0:q]
            i += q
            rep = True
            rep_times = 0
            while i < len(s):
                next = s[i:i + q]
                # print prev, next
                if len(prev) == len(next) and prev != next:
                    # print "rep False q = %d" % q
                    rep = False
                    break
                rep_times += 1
                i += q
                prev = next
            if rep and rep_times > 1:
                # print "Updating maxq = %d" % q
                maxq = q
                return maxq
            q += 1
        return maxq


    print long_seq(frac(1, 6))

    res_dict = dict()
    max_res = 0
    for i, d in enumerate(range(2, 1000)):
        res_dict[i + 2] = long_seq(frac(1, d))
        print '1/%d = %s' % (i + 2, res_dict[i + 2])
        if res_dict[i + 2] > max_res:
            max_res = res_dict[i + 2]
            print "Found new max %d" % (i + 2)


def problem_51(): #solved
    primes = map(str, gen_primes(1, 1000000))
    d = dict()

    def is_pattern(num, pattern):
        p1 = map(str, pattern)
        s1 = map(str, num)
        s = set()
        for pat_char, c1 in zip(p1, s1):
            if pat_char == ' ':
                s.add(c1)
            else:
                if c1 != pat_char:
                    return False
        return len(s) == 1

    import math

    def get_pattern(s, mask):
       s1 = map(str, s)
       m = map(str, mask)
       res = ''
       for c1, m1 in zip(s, mask):
           if m1 == '0':
               res += ' '
           else:
                res += c1
       return res

    for p in primes:
        for i in range(1, int(math.pow(2, len(p)) - 1)):
            mask = ('000000000000' + bin(i)[2:])[-len(p):]
            num_1 = reduce(lambda x, y: x + y, map(int, mask))
           # print mask, num_1
            pattern = get_pattern(p, mask)
            if is_pattern(p, pattern):
                if not pattern in d:
                    d[pattern] = [0, []]
                d[pattern][0] += 1
                d[pattern][1].append(p)
                print pattern, d[pattern]
                if d[pattern][0] == 8:
                    return

    for k in d:
        if d[k][0] > 7:
            print k, d[k]


def problem_58(): # solved
    ratio = 1
    side = 1
    diags = [1]
    num_diag_primes = 0
    num_diag = 1
    while ratio >= 0.1:
        side += 2
        last_val = side * side
        addition = map(lambda i: last_val - (side - 1) * i, [3, 2, 1, 0])
        num_diag_primes += len(filter(isprime, addition))
        num_diag += 4
        ratio = float(num_diag_primes) / float(num_diag)
        print ratio, side


def problem_119(): # solved
    import math

    d = dict()
    for i in range(1, 100):
        d[i] = set()
        prod = 1
        for j in range(1, 100):
            prod *= i
            d[i].add(prod)

    candidate = list()
    for k in d:
        for l in d[k]:
            digsum = reduce(lambda x, y: x + y, map(int, str(l)))
            if digsum == k and l >= 10:
                candidate.append(l)
    for i, c in enumerate(sorted(candidate)):
        print i + 1, c

def problem_121(): # solved
    n = 15
    p = 1
    for i, x in enumerate(range(2, n + 2)):
        print i + 1, x
        p *= x

    sum = 0
    for i in range(1, int(math.pow(2, n))):
        b = '0000000000000000' + bin(i)[2:]
        b = b[-n:]
        if reduce(lambda x, y: x + y, map(int, b)) > n / 2:
            optsum = 1
            for turn in range(n):
                win = b[turn] == '1'
                if not win:
                    optsum *= (turn + 1)
            print b, optsum
            sum += optsum

    print sum, p, math.floor(float((p - sum)) / float(sum))


def problem_125(): # solved
    sqrs = list()
    sqrs_sum = list()
    i = 0
    sum = 0

    def is_palin(n):
        s = str(n)
        return s[::-1] == s

    limit = math.pow(10, 8)
    cnt = 0
    cand_sum = 0
    s = 0

    cand_set = set()
    while s <= limit:
        s = i * i
        sqrs.append(s)
        sum += s
        sqrs_sum.append(sum)
        lenlst = len(sqrs_sum)
        for idx in range(1, lenlst - 1):
            candidate = sum - sqrs_sum[idx - 1]

            if candidate <= limit and is_palin(candidate) and not candidate in cand_set:
                cnt += 1
                print cnt, cand_sum, "palin: ", candidate, "sqrs: ", range(idx, lenlst), sqrs[idx:lenlst]
                cand_set.add(candidate)

        i += 1
    print reduce(lambda x, y: x + y, list(cand_set))


def problem_54(): # solved


    def get_hand(hand1):
        card_dict = dict()
        flush_dict = dict()
        high_card = 0
        for card in hand1.split(' '):
            cardord = card[0]
            if cardord == 'T':
                cardord = 10
            else:
                if cardord == 'J':
                    cardord = 11
                else:
                    if cardord == 'Q':
                        cardord = 12
                    else:
                        if cardord == 'K':
                            cardord = 13
                        else:
                            if cardord == 'A':
                                cardord = 14
                            else:
                                cardord = int(cardord)
            if not cardord in card_dict:
                card_dict[cardord] = 0
            card_dict[cardord] += 1
            if card[1] not in flush_dict:
                flush_dict[card[1]] = 0
            flush_dict[card[1]] += 1

        pairs = 0
        threes = 0
        fours = 0
        full_house = 0
        cards_seen = sorted(card_dict.keys())
        straight = 0
        flush = 0
        if len(flush_dict) == 1:
            flush = cards_seen[-1]
        for card in cards_seen:
            if card_dict[card] == 2:
                if pairs > 0:
                    pairs = card * 100 + pairs
                else:
                    pairs = card
            if card_dict[card] == 3:
                threes = card
            if card_dict[card] == 4:
                fours = card
            if card_dict[card] == 1:
                high_card = card

        if pairs > 0 and threes > 0:
            full_house = threes * 100 + pairs

        if len(cards_seen) == 5:
            if cards_seen[-1] - cards_seen[0] == 4:
                straight = cards_seen[-1]

            if cards_seen[3] == 4 and cards_seen[4] == 13:
                straight = 1

        straight_flush = 0
        if flush > 0 and straight > 0:
            straight_flush = straight
        return [high_card, pairs, threes, straight, flush, full_house, fours, straight_flush]
        # print pairs, threes, fours, flush, straight


    def compare_hands(hand1, hand2):
        v1 = get_hand(hand1)
        v2 = get_hand(hand2)
        print v1, v2
        for h1, h2 in zip(v1[::-1], v2[::-1]):
            if h1 > h2:
                return 1
            if h2 > h1:
                return 2
        return 0


    def process_round(s):
        player1 = ' '.join(s.split(' ')[:5])
        player2 = ' '.join(s.split(' ')[5:])
        print player1, ' | ', player2
        return compare_hands(player1, player2)

    f = open('c:/poker.txt')
    cnt = 0
    round = 0
    for line in f:
        round += 1
        print 'Round %d' % round
        print '========='
        res = process_round(line)
        print res
        if res == 1:
            cnt += 1
    print cnt
    #process_round('5H 5C 6S 7S KD 2C 3S 8S 8D TD')
    #process_round('5D 8C 9S JS AC 2C 5C 7D 8S QH')
    #process_round('2D 9C AS AH AC 3D 6D 7D TD QD')
    #process_round('4D 6S 9H QH QC 3D 6D 7H QD QS')
    #process_round('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D')


def problem_59(): # solved
    c = [79, 59, 12, 2, 79, 35, 8, 28, 20, 2, 3, 68, 8, 9, 68, 45, 0, 12, 9, 67, 68, 4, 7, 5, 23, 27, 1, 21, 79, 85, 78, 79, 85, 71, 38, 10, 71, 27, 12, 2, 79, 6, 2, 8, 13, 9, 1, 13, 9, 8, 68, 19, 7, 1, 71, 56, 11, 21, 11, 68, 6, 3, 22, 2, 14, 0, 30, 79, 1, 31, 6, 23, 19, 10, 0, 73, 79, 44, 2, 79, 19, 6, 28, 68, 16, 6, 16, 15, 79, 35, 8, 11, 72, 71, 14, 10, 3, 79, 12, 2, 79, 19, 6, 28, 68, 32, 0, 0, 73, 79, 86, 71, 39, 1, 71, 24, 5, 20, 79, 13, 9, 79, 16, 15, 10, 68, 5, 10, 3, 14, 1, 10, 14, 1, 3, 71, 24, 13, 19, 7, 68, 32, 0, 0, 73, 79, 87, 71, 39, 1, 71, 12, 22, 2, 14, 16, 2, 11, 68, 2, 25, 1, 21, 22, 16, 15, 6, 10, 0, 79, 16, 15, 10, 22, 2, 79, 13, 20, 65, 68, 41, 0, 16, 15, 6, 10, 0, 79, 1, 31, 6, 23, 19, 28, 68, 19, 7, 5, 19, 79, 12, 2, 79, 0, 14, 11, 10, 64, 27, 68, 10, 14, 15, 2, 65, 68, 83, 79, 40, 14, 9, 1, 71, 6, 16, 20, 10, 8, 1, 79, 19, 6, 28, 68, 14, 1, 68, 15, 6, 9, 75, 79, 5, 9, 11, 68, 19, 7, 13, 20, 79, 8, 14, 9, 1, 71, 8, 13, 17, 10, 23, 71, 3, 13, 0, 7, 16, 71, 27, 11, 71, 10, 18, 2, 29, 29, 8, 1, 1, 73, 79, 81, 71, 59, 12, 2, 79, 8, 14, 8, 12, 19, 79, 23, 15, 6, 10, 2, 28, 68, 19, 7, 22, 8, 26, 3, 15, 79, 16, 15, 10, 68, 3, 14, 22, 12, 1, 1, 20, 28, 72, 71, 14, 10, 3, 79, 16, 15, 10, 68, 3, 14, 22, 12, 1, 1, 20, 28, 68, 4, 14, 10, 71, 1, 1, 17, 10, 22, 71, 10, 28, 19, 6, 10, 0, 26, 13, 20, 7, 68, 14, 27, 74, 71, 89, 68, 32, 0, 0, 71, 28, 1, 9, 27, 68, 45, 0, 12, 9, 79, 16, 15, 10, 68, 37, 14, 20, 19, 6, 23, 19, 79, 83, 71, 27, 11, 71, 27, 1, 11, 3, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 6, 13, 11, 18, 27, 68, 19, 7, 1, 71, 3, 13, 0, 7, 16, 71, 28, 11, 71, 27, 12, 6, 27, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 10, 6, 3, 15, 27, 68, 5, 10, 8, 14, 10, 18, 2, 79, 6, 2, 12, 5, 18, 28, 1, 71, 0, 2, 71, 7, 13, 20, 79, 16, 2, 28, 16, 14, 2, 11, 9, 22, 74, 71, 87, 68, 45, 0, 12, 9, 79, 12, 14, 2, 23, 2, 3, 2, 71, 24, 5, 20, 79, 10, 8, 27, 68, 19, 7, 1, 71, 3, 13, 0, 7, 16, 92, 79, 12, 2, 79, 19, 6, 28, 68, 8, 1, 8, 30, 79, 5, 71, 24, 13, 19, 1, 1, 20, 28, 68, 19, 0, 68, 19, 7, 1, 71, 3, 13, 0, 7, 16, 73, 79, 93, 71, 59, 12, 2, 79, 11, 9, 10, 68, 16, 7, 11, 71, 6, 23, 71, 27, 12, 2, 79, 16, 21, 26, 1, 71, 3, 13, 0, 7, 16, 75, 79, 19, 15, 0, 68, 0, 6, 18, 2, 28, 68, 11, 6, 3, 15, 27, 68, 19, 0, 68, 2, 25, 1, 21, 22, 11, 9, 10, 72, 71, 24, 5, 20, 79, 3, 8, 6, 10, 0, 79, 16, 8, 79, 7, 8, 2, 1, 71, 6, 10, 19, 0, 68, 19, 7, 1, 71, 24, 11, 21, 3, 0, 73, 79, 85, 87, 79, 38, 18, 27, 68, 6, 3, 16, 15, 0, 17, 0, 7, 68, 19, 7, 1, 71, 24, 11, 21, 3, 0, 71, 24, 5, 20, 79, 9, 6, 11, 1, 71, 27, 12, 21, 0, 17, 0, 7, 68, 15, 6, 9, 75, 79, 16, 15, 10, 68, 16, 0, 22, 11, 11, 68, 3, 6, 0, 9, 72, 16, 71, 29, 1, 4, 0, 3, 9, 6, 30, 2, 79, 12, 14, 2, 68, 16, 7, 1, 9, 79, 12, 2, 79, 7, 6, 2, 1, 73, 79, 85, 86, 79, 33, 17, 10, 10, 71, 6, 10, 71, 7, 13, 20, 79, 11, 16, 1, 68, 11, 14, 10, 3, 79, 5, 9, 11, 68, 6, 2, 11, 9, 8, 68, 15, 6, 23, 71, 0, 19, 9, 79, 20, 2, 0, 20, 11, 10, 72, 71, 7, 1, 71, 24, 5, 20, 79, 10, 8, 27, 68, 6, 12, 7, 2, 31, 16, 2, 11, 74, 71, 94, 86, 71, 45, 17, 19, 79, 16, 8, 79, 5, 11, 3, 68, 16, 7, 11, 71, 13, 1, 11, 6, 1, 17, 10, 0, 71, 7, 13, 10, 79, 5, 9, 11, 68, 6, 12, 7, 2, 31, 16, 2, 11, 68, 15, 6, 9, 75, 79, 12, 2, 79, 3, 6, 25, 1, 71, 27, 12, 2, 79, 22, 14, 8, 12, 19, 79, 16, 8, 79, 6, 2, 12, 11, 10, 10, 68, 4, 7, 13, 11, 11, 22, 2, 1, 68, 8, 9, 68, 32, 0, 0, 73, 79, 85, 84, 79, 48, 15, 10, 29, 71, 14, 22, 2, 79, 22, 2, 13, 11, 21, 1, 69, 71, 59, 12, 14, 28, 68, 14, 28, 68, 9, 0, 16, 71, 14, 68, 23, 7, 29, 20, 6, 7, 6, 3, 68, 5, 6, 22, 19, 7, 68, 21, 10, 23, 18, 3, 16, 14, 1, 3, 71, 9, 22, 8, 2, 68, 15, 26, 9, 6, 1, 68, 23, 14, 23, 20, 6, 11, 9, 79, 11, 21, 79, 20, 11, 14, 10, 75, 79, 16, 15, 6, 23, 71, 29, 1, 5, 6, 22, 19, 7, 68, 4, 0, 9, 2, 28, 68, 1, 29, 11, 10, 79, 35, 8, 11, 74, 86, 91, 68, 52, 0, 68, 19, 7, 1, 71, 56, 11, 21, 11, 68, 5, 10, 7, 6, 2, 1, 71, 7, 17, 10, 14, 10, 71, 14, 10, 3, 79, 8, 14, 25, 1, 3, 79, 12, 2, 29, 1, 71, 0, 10, 71, 10, 5, 21, 27, 12, 71, 14, 9, 8, 1, 3, 71, 26, 23, 73, 79, 44, 2, 79, 19, 6, 28, 68, 1, 26, 8, 11, 79, 11, 1, 79, 17, 9, 9, 5, 14, 3, 13, 9, 8, 68, 11, 0, 18, 2, 79, 5, 9, 11, 68, 1, 14, 13, 19, 7, 2, 18, 3, 10, 2, 28, 23, 73, 79, 37, 9, 11, 68, 16, 10, 68, 15, 14, 18, 2, 79, 23, 2, 10, 10, 71, 7, 13, 20, 79, 3, 11, 0, 22, 30, 67, 68, 19, 7, 1, 71, 8, 8, 8, 29, 29, 71, 0, 2, 71, 27, 12, 2, 79, 11, 9, 3, 29, 71, 60, 11, 9, 79, 11, 1, 79, 16, 15, 10, 68, 33, 14, 16, 15, 10, 22, 73]

    def decrypt(c, passwd):
        print map(chr, passwd)
        d = ''
        for i in range(len(c)):
            d += chr(c[i] ^ passwd[i % 3])
        return d

    #for c1 in range(ord('a'), ord('z') + 1):
    #    for c2 in range(ord('a'), ord('z') + 1):
    #        for c3 in range(ord('a'), ord('z') + 1):
    #            passwd = [c1, c2, c3]
    #            print decrypt(c, passwd)
    s = decrypt(c, map(ord, map(str, 'god')))
    print sum(map(ord, map(str, s)))


def problem_75(): #solved


    def l(L): #attempt 1
        sqr_map = dict()
        for i in range(100000):
            sqr_map[i * i] = i
        print "Done"
        d = dict()
        for a in range(1, L / 2 + 1):
            asqr = a * a
            for b in range(max(a / 2, 1), a):
                csqr = asqr - b * b
                if csqr in sqr_map:
                    c = sqr_map[csqr]
                    if a + b > c and a + c > b and b + c > a:
                        p = a + b + c
                        if p not in d:
                            d[p] = set()
                        d[p].update(set([a, b, c]))
                        print a, b, c, a + b + c
                    else:
                        print "invalid: ", a, b, c

        return d

    import math
    def j(L): #attempt 2
        d = dict()
        for b in range(1, L / 2 + 1):
            B = b
            if B % 2 != 0:
                B *= 2

            for i in range(1, int(math.sqrt(B)) + 1):
                if B % i == 0:
                    m = B / i
                    n = i
                    print "A=", B, m, n
                    a = m * m - n * n
                    c = m * m + n * n
                    p = a + B + c
                    if p > L:
                        continue
                    if p not in d:
                        d[p] = set()
                    d[p].update(set([a, B, c]))
                    print B, a, c, a + B + c
        return d

    def k(L): #successful attempt
        Ldict = dict()
        import math
        limit = int(math.sqrt(L / 2) + 1)
        for n in xrange(limit):
            for m in xrange(1, n):
                a = n * n - m * m
                b = 2 * n * m
                c = n * n + m * m
                p = a + b + c
                # print p, L
                if p > L:
                    continue
                P = A = B = C = 0
                factor = 2
                while P <= L:
                    A += a
                    B += b
                    C += c
                    P += p

                    if P > L:
                        break

                    # print (A, B, C, P)
                    if not P in Ldict:
                        Ldict[P] = set()
                    Ldict[P].add('_'.join(map(str, sorted([A, B, C]))))

        cnt = 0
        for k in Ldict:
            if len(Ldict[k]) == 1:
                cnt += 1
        print cnt
       #print sum(filter(lambda x: len(x) == 1, Ldict.values()))



    d = k(1500000)

def problem_99(): #solved
    f = open('c:/base_exp.txt')
    line_no = 0
    max_fig = 0
    max_line = 0
    for line in f:
        line_no += 1
        arr = line.split(',')
        res = math.log(float(arr[0])) * float(arr[1])
        if max_fig < res:
            max_fig = res
            max_line = line_no
        print line
    print max_line


def problem_61(): # solved

    l = range(1, 142)
    d = dict(A = map(lambda n: n * (n + 1) / 2, l), B = map(lambda n: n * n, l), C = map(lambda n: n * (3 * n - 1) / 2, l),
             D = map(lambda n: n * (2 * n - 1), l), E = map(lambda n: n * (5 * n - 3) / 2, l), F = map(lambda n: n * (3 * n - 2), l))
    new_d = dict()

    for k in d:
        for i, x in enumerate(d[k]):
            if x >= 1000 and x <= 9999:
                new_d['%s_%d_%s' % (k, i + 1, str(x))] = list()

    def can_connect(n1, n2):
        N1 = n1.split('_')
        N2 = n2.split('_')
        if N1[0] == N2[0] or N1[1] == N2[1]:
            return False
        t = N1[2][2:] == N2[2][0:2]
        return t


    import itertools
    for keys in itertools.combinations(new_d.keys(), 2):
        if can_connect(keys[0], keys[1]):
            new_d[keys[0]].append(keys[1])
        if can_connect(keys[1], keys[0]):
            new_d[keys[1]].append(keys[0])

    import copy
    def traverse(path, type_set, idx_set):
        if len(path) == 6:
            if can_connect(path[-1], path[0]):
                print path, sum(map(lambda x: int(x.split('_')[2]), path))
            return
        for candidate in new_d[path[-1]]:
            lll = candidate.split('_')
            cand_type = lll[0]
            if cand_type in type_set:
                return None
            idx = lll[1]
            if idx in idx_set:
                return None
            new_idx_set = copy.copy(idx_set)
            new_type_set = copy.copy(type_set)
            new_type_set.add(cand_type)
            new_idx_set.add(idx)
            new_path = copy.copy(path)
            new_path.append(candidate)
            traverse(new_path, new_type_set, new_idx_set)

    for k in new_d:
        traverse([k], set([]), set([]))

def problem_49(): # solved

    d = dict()
    for i in range(1000, 10000):
        if isprime(i):
            key = ''.join(sorted(str(i)))
            if not key in d:
                d[key] = set()
            d[key].add(i)

    for k in sorted(d.keys()):
        l = list(d[k])
        p = dict()
        for a in l:
            for b in l:
                key = a - b
                if key > 0:
                    if not key in p:
                        p[key] = set()
                    p[key].add(a)
                    p[key].add(b)

        for key in p:
            if len(p[key]) >= 3 and key == 3330:
                print k, d[k], p

def problem_44(): # solved

    p_set = set()
    p_list = list()
    for i in range(1, 10000 + 1):
        n = i * (3 * i - 1) / 2
        p_set.add(n)
        p_list.append(n)

    for i in range(1, 10000):
        for j in range(1, 10000):

            sum = p_list[i] + p_list[j]
            diff = p_list[j] - p_list[i]
            if sum in p_set and diff in p_set:
                print i, j, diff

def problem_92(): # solved

    sum_sqr_dict = dict()

    def sum_square_digits(n):
        s = map(int, str(n))
        sqr_dig = map(lambda x: x * x, s)
        newnum = reduce(lambda x, y: x + y, sqr_dig)
        return newnum

    cnt = 0
    for x in xrange(1, 10000000):
        print x
        n = x
        while 1:
            if n == 89:
                cnt += 1
            if n == 1 or n == 89:
                break
            n = sum_square_digits(n)

    print cnt


def problem_69(): # solved

    n = 1000000
    totient = create_totient(n)
    max_ratio = 1
    for i in range(2, n + 1):
        t = totient(i)
        ratio = float(i) / float(t)
        print i, t, ratio
        if ratio > 5.53938:
            print i
            return
        if max_ratio < ratio:
            max_ratio = ratio
            print "New max ", max_ratio
    print max_ratio


def problem_81(): # solved

    l1 = [131, 673, 234, 103, 18, 201, 96, 342, 965, 150, 630, 803, 746, 422, 111, 537, 699, 497, 121, 956, 805, 732, 524, 37, 331]
    l = [4445, 2697, 5115, 718, 2209, 2212, 654, 4348, 3079, 6821, 7668, 3276, 8874, 4190, 3785, 2752, 9473, 7817, 9137, 496, 7338, 3434, 7152, 4355, 4552, 7917, 7827, 2460, 2350, 691, 3514, 5880, 3145, 7633, 7199, 3783, 5066, 7487, 3285, 1084, 8985, 760, 872, 8609, 8051, 1134, 9536, 5750, 9716, 9371, 7619, 5617, 275, 9721, 2997, 2698, 1887, 8825, 6372, 3014, 2113, 7122, 7050, 6775, 5948, 2758, 1219, 3539, 348, 7989, 2735, 9862, 1263, 8089, 6401, 9462, 3168, 2758, 3748, 5870, 1096, 20, 1318, 7586, 5167, 2642, 1443, 5741, 7621, 7030, 5526, 4244, 2348, 4641, 9827, 2448, 6918, 5883, 3737, 300, 7116, 6531, 567, 5997, 3971, 6623, 820, 6148, 3287, 1874, 7981, 8424, 7672, 7575, 6797, 6717, 1078, 5008, 4051, 8795, 5820, 346, 1851, 6463, 2117, 6058, 3407, 8211, 117, 4822, 1317, 4377, 4434, 5925, 8341, 4800, 1175, 4173, 690, 8978, 7470, 1295, 3799, 8724, 3509, 9849, 618, 3320, 7068, 9633, 2384, 7175, 544, 6583, 1908, 9983, 481, 4187, 9353, 9377,
9607, 7385, 521, 6084, 1364, 8983, 7623, 1585, 6935, 8551, 2574, 8267, 4781, 3834, 2764, 2084, 2669, 4656, 9343, 7709, 2203, 9328, 8004, 6192, 5856, 3555, 2260, 5118, 6504, 1839, 9227, 1259, 9451, 1388, 7909, 5733, 6968, 8519, 9973, 1663, 5315, 7571, 3035, 4325, 4283, 2304, 6438, 3815, 9213, 9806, 9536, 196, 5542, 6907, 2475, 1159, 5820, 9075, 9470, 2179, 9248, 1828, 4592, 9167, 3713, 4640, 47, 3637, 309, 7344, 6955, 346, 378, 9044, 8635, 7466, 5036, 9515, 6385, 9230,
7206, 3114, 7760, 1094, 6150, 5182, 7358, 7387, 4497, 955, 101, 1478, 7777, 6966, 7010, 8417, 6453, 4955, 3496, 107, 449, 8271, 131, 2948, 6185, 784, 5937, 8001, 6104, 8282, 4165, 3642, 710, 2390, 575, 715, 3089, 6964, 4217, 192, 5949, 7006, 715, 3328, 1152, 66, 8044, 4319, 1735, 146, 4818, 5456, 6451, 4113, 1063, 4781, 6799, 602, 1504, 6245, 6550, 1417, 1343, 2363, 3785, 5448, 4545, 9371, 5420, 5068, 4613, 4882, 4241, 5043, 7873, 8042, 8434, 3939, 9256, 2187,
3620, 8024, 577, 9997, 7377, 7682, 1314, 1158, 6282, 6310, 1896, 2509, 5436, 1732, 9480, 706, 496, 101, 6232, 7375, 2207, 2306, 110, 6772, 3433, 2878, 8140, 5933, 8688, 1399, 2210, 7332, 6172, 6403, 7333, 4044, 2291, 1790, 2446, 7390, 8698, 5723, 3678, 7104, 1825, 2040, 140, 3982, 4905, 4160, 2200, 5041, 2512, 1488, 2268, 1175, 7588, 8321, 8078, 7312, 977, 5257, 8465, 5068, 3453, 3096, 1651, 7906, 253, 9250, 6021, 8791, 8109, 6651, 3412, 345, 4778, 5152, 4883, 7505,
1074, 5438, 9008, 2679, 5397, 5429, 2652, 3403, 770, 9188, 4248, 2493, 4361, 8327, 9587, 707, 9525, 5913, 93, 1899, 328, 2876, 3604, 673, 8576, 6908, 7659, 2544, 3359, 3883, 5273, 6587, 3065, 1749, 3223, 604, 9925, 6941, 2823, 8767, 7039, 3290, 3214, 1787, 7904, 3421, 7137, 9560, 8451, 2669, 9219, 6332, 1576, 5477, 6755, 8348, 4164, 4307, 2984, 4012, 6629, 1044, 2874, 6541, 4942, 903, 1404, 9125, 5160, 8836, 4345, 2581, 460, 8438, 1538, 5507, 668, 3352, 2678, 6942,
4295, 1176, 5596, 1521, 3061, 9868, 7037, 7129, 8933, 6659, 5947, 5063, 3653, 9447, 9245, 2679, 767, 714, 116, 8558, 163, 3927, 8779, 158, 5093, 2447, 5782, 3967, 1716, 931, 7772, 8164, 1117, 9244, 5783, 7776, 3846, 8862, 6014, 2330, 6947, 1777, 3112, 6008, 3491, 1906, 5952, 314, 4602, 8994, 5919, 9214, 3995, 5026, 7688, 6809, 5003, 3128, 2509, 7477, 110, 8971, 3982, 8539, 2980, 4689, 6343, 5411, 2992, 5270, 5247, 9260, 2269, 7474, 1042, 7162, 5206, 1232, 4556, 4757,
510, 3556, 5377, 1406, 5721, 4946, 2635, 7847, 4251, 8293, 8281, 6351, 4912, 287, 2870, 3380, 3948, 5322, 3840, 4738, 9563, 1906, 6298, 3234, 8959, 1562, 6297, 8835, 7861, 239, 6618, 1322, 2553, 2213, 5053, 5446, 4402, 6500, 5182, 8585, 6900, 5756, 9661, 903, 5186, 7687, 5998, 7997, 8081, 8955, 4835, 6069, 2621, 1581, 732, 9564, 1082, 1853, 5442, 1342, 520, 1737, 3703, 5321, 4793, 2776, 1508, 1647, 9101, 2499, 6891, 4336, 7012, 3329, 3212, 1442, 9993, 3988, 4930, 7706,
9444, 3401, 5891, 9716, 1228, 7107, 109, 3563, 2700, 6161, 5039, 4992, 2242, 8541, 7372, 2067, 1294, 3058, 1306, 320, 8881, 5756, 9326, 411, 8650, 8824, 5495, 8282, 8397, 2000, 1228, 7817, 2099, 6473, 3571, 5994, 4447, 1299, 5991, 543, 7874, 2297, 1651, 101, 2093, 3463, 9189, 6872, 6118, 872, 1008, 1779, 2805, 9084, 4048, 2123, 5877, 55, 3075, 1737, 9459, 4535, 6453, 3644, 108, 5982, 4437, 5213, 1340, 6967, 9943, 5815, 669, 8074, 1838, 6979, 9132, 9315, 715, 5048,
3327, 4030, 7177, 6336, 9933, 5296, 2621, 4785, 2755, 4832, 2512, 2118, 2244, 4407, 2170, 499, 7532, 9742, 5051, 7687, 970, 6924, 3527, 4694, 5145, 1306, 2165, 5940, 2425, 8910, 3513, 1909, 6983, 346, 6377, 4304, 9330, 7203, 6605, 3709, 3346, 970, 369, 9737, 5811, 4427, 9939, 3693, 8436, 5566, 1977, 3728, 2399, 3985, 8303, 2492, 5366, 9802, 9193, 7296, 1033, 5060, 9144, 2766, 1151, 7629, 5169, 5995, 58, 7619, 7565, 4208, 1713, 6279, 3209, 4908, 9224, 7409, 1325, 8540,
6882, 1265, 1775, 3648, 4690, 959, 5837, 4520, 5394, 1378, 9485, 1360, 4018, 578, 9174, 2932, 9890, 3696, 116, 1723, 1178, 9355, 7063, 1594, 1918, 8574, 7594, 7942, 1547, 6166, 7888, 354, 6932, 4651, 1010, 7759, 6905, 661, 7689, 6092, 9292, 3845, 9605, 8443, 443, 8275, 5163, 7720, 7265, 6356, 7779, 1798, 1754, 5225, 6661, 1180, 8024, 5666, 88, 9153, 1840, 3508, 1193, 4445, 2648, 3538, 6243, 6375, 8107, 5902, 5423, 2520, 1122, 5015, 6113, 8859, 9370, 966, 8673, 2442,
7338, 3423, 4723, 6533, 848, 8041, 7921, 8277, 4094, 5368, 7252, 8852, 9166, 2250, 2801, 6125, 8093, 5738, 4038, 9808, 7359, 9494, 601, 9116, 4946, 2702, 5573, 2921, 9862, 1462, 1269, 2410, 4171, 2709, 7508, 6241, 7522, 615, 2407, 8200, 4189, 5492, 5649, 7353, 2590, 5203, 4274, 710, 7329, 9063, 956, 8371, 3722, 4253, 4785, 1194, 4828, 4717, 4548, 940, 983, 2575, 4511, 2938, 1827, 2027, 2700, 1236, 841, 5760, 1680, 6260, 2373, 3851, 1841, 4968, 1172, 5179, 7175, 3509,
4420, 1327, 3560, 2376, 6260, 2988, 9537, 4064, 4829, 8872, 9598, 3228, 1792, 7118, 9962, 9336, 4368, 9189, 6857, 1829, 9863, 6287, 7303, 7769, 2707, 8257, 2391, 2009, 3975, 4993, 3068, 9835, 3427, 341, 8412, 2134, 4034, 8511, 6421, 3041, 9012, 2983, 7289, 100, 1355, 7904, 9186, 6920, 5856, 2008, 6545, 8331, 3655, 5011, 839, 8041, 9255, 6524, 3862, 8788, 62, 7455, 3513, 5003, 8413, 3918, 2076, 7960, 6108, 3638, 6999, 3436, 1441, 4858, 4181, 1866, 8731, 7745, 3744, 1000,
356, 8296, 8325, 1058, 1277, 4743, 3850, 2388, 6079, 6462, 2815, 5620, 8495, 5378, 75, 4324, 3441, 9870, 1113, 165, 1544, 1179, 2834, 562, 6176, 2313, 6836, 8839, 2986, 9454, 5199, 6888, 1927, 5866, 8760, 320, 1792, 8296, 7898, 6121, 7241, 5886, 5814, 2815, 8336, 1576, 4314, 3109, 2572, 6011, 2086, 9061, 9403, 3947, 5487, 9731, 7281, 3159, 1819, 1334, 3181, 5844, 5114, 9898, 4634, 2531, 4412, 6430, 4262, 8482, 4546, 4555, 6804, 2607, 9421, 686, 8649, 8860, 7794, 6672,
9870, 152, 1558, 4963, 8750, 4754, 6521, 6256, 8818, 5208, 5691, 9659, 8377, 9725, 5050, 5343, 2539, 6101, 1844, 9700, 7750, 8114, 5357, 3001, 8830, 4438, 199, 9545, 8496, 43, 2078, 327, 9397, 106, 6090, 8181, 8646, 6414, 7499, 5450, 4850, 6273, 5014, 4131, 7639, 3913, 6571, 8534, 9703, 4391, 7618, 445, 1320, 5, 1894, 6771, 7383, 9191, 4708, 9706, 6939, 7937, 8726, 9382, 5216, 3685, 2247, 9029, 8154, 1738, 9984, 2626, 9438, 4167, 6351, 5060, 29, 1218, 1239, 4785,
192, 5213, 8297, 8974, 4032, 6966, 5717, 1179, 6523, 4679, 9513, 1481, 3041, 5355, 9303, 9154, 1389, 8702, 6589, 7818, 6336, 3539, 5538, 3094, 6646, 6702, 6266, 2759, 4608, 4452, 617, 9406, 8064, 6379, 444, 5602, 4950, 1810, 8391, 1536, 316, 8714, 1178, 5182, 5863, 5110, 5372, 4954, 1978, 2971, 5680, 4863, 2255, 4630, 5723, 2168, 538, 1692, 1319, 7540, 440, 6430, 6266, 7712, 7385, 5702, 620, 641, 3136, 7350, 1478, 3155, 2820, 9109, 6261, 1122, 4470, 14, 8493, 2095,
1046, 4301, 6082, 474, 4974, 7822, 2102, 5161, 5172, 6946, 8074, 9716, 6586, 9962, 9749, 5015, 2217, 995, 5388, 4402, 7652, 6399, 6539, 1349, 8101, 3677, 1328, 9612, 7922, 2879, 231, 5887, 2655, 508, 4357, 4964, 3554, 5930, 6236, 7384, 4614, 280, 3093, 9600, 2110, 7863, 2631, 6626, 6620, 68, 1311, 7198, 7561, 1768, 5139, 1431, 221, 230, 2940, 968, 5283, 6517, 2146, 1646, 869, 9402, 7068, 8645, 7058, 1765, 9690, 4152, 2926, 9504, 2939, 7504, 6074, 2944, 6470, 7859,
4659, 736, 4951, 9344, 1927, 6271, 8837, 8711, 3241, 6579, 7660, 5499, 5616, 3743, 5801, 4682, 9748, 8796, 779, 1833, 4549, 8138, 4026, 775, 4170, 2432, 4174, 3741, 7540, 8017, 2833, 4027, 396, 811, 2871, 1150, 9809, 2719, 9199, 8504, 1224, 540, 2051, 3519, 7982, 7367, 2761, 308, 3358, 6505, 2050, 4836, 5090, 7864, 805, 2566, 2409, 6876, 3361, 8622, 5572, 5895, 3280, 441, 7893, 8105, 1634, 2929, 274, 3926, 7786, 6123, 8233, 9921, 2674, 5340, 1445, 203, 4585, 3837,
5759, 338, 7444, 7968, 7742, 3755, 1591, 4839, 1705, 650, 7061, 2461, 9230, 9391, 9373, 2413, 1213, 431, 7801, 4994, 2380, 2703, 6161, 6878, 8331, 2538, 6093, 1275, 5065, 5062, 2839, 582, 1014, 8109, 3525, 1544, 1569, 8622, 7944, 2905, 6120, 1564, 1839, 5570, 7579, 1318, 2677, 5257, 4418, 5601, 7935, 7656, 5192, 1864, 5886, 6083, 5580, 6202, 8869, 1636, 7907, 4759, 9082, 5854, 3185, 7631, 6854, 5872, 5632, 5280, 1431, 2077, 9717, 7431, 4256, 8261, 9680, 4487, 4752, 4286,
1571, 1428, 8599, 1230, 7772, 4221, 8523, 9049, 4042, 8726, 7567, 6736, 9033, 2104, 4879, 4967, 6334, 6716, 3994, 1269, 8995, 6539, 3610, 7667, 6560, 6065, 874, 848, 4597, 1711, 7161, 4811, 6734, 5723, 6356, 6026, 9183, 2586, 5636, 1092, 7779, 7923, 8747, 6887, 7505, 9909, 1792, 3233, 4526, 3176, 1508, 8043, 720, 5212, 6046, 4988, 709, 5277, 8256, 3642, 1391, 5803, 1468, 2145, 3970, 6301, 7767, 2359, 8487, 9771, 8785, 7520, 856, 1605, 8972, 2402, 2386, 991, 1383, 5963,
1822, 4824, 5957, 6511, 9868, 4113, 301, 9353, 6228, 2881, 2966, 6956, 9124, 9574, 9233, 1601, 7340, 973, 9396, 540, 4747, 8590, 9535, 3650, 7333, 7583, 4806, 3593, 2738, 8157, 5215, 8472, 2284, 9473, 3906, 6982, 5505, 6053, 7936, 6074, 7179, 6688, 1564, 1103, 6860, 5839, 2022, 8490, 910, 7551, 7805, 881, 7024, 1855, 9448, 4790, 1274, 3672, 2810, 774, 7623, 4223, 4850, 6071, 9975, 4935, 1915, 9771, 6690, 3846, 517, 463, 7624, 4511, 614, 6394, 3661, 7409, 1395, 8127,
8738, 3850, 9555, 3695, 4383, 2378, 87, 6256, 6740, 7682, 9546, 4255, 6105, 2000, 1851, 4073, 8957, 9022, 6547, 5189, 2487, 303, 9602, 7833, 1628, 4163, 6678, 3144, 8589, 7096, 8913, 5823, 4890, 7679, 1212, 9294, 5884, 2972, 3012, 3359, 7794, 7428, 1579, 4350, 7246, 4301, 7779, 7790, 3294, 9547, 4367, 3549, 1958, 8237, 6758, 3497, 3250, 3456, 6318, 1663, 708, 7714, 6143, 6890, 3428, 6853, 9334, 7992, 591, 6449, 9786, 1412, 8500, 722, 5468, 1371, 108, 3939, 4199, 2535,
7047, 4323, 1934, 5163, 4166, 461, 3544, 2767, 6554, 203, 6098, 2265, 9078, 2075, 4644, 6641, 8412, 9183, 487, 101, 7566, 5622, 1975, 5726, 2920, 5374, 7779, 5631, 3753, 3725, 2672, 3621, 4280, 1162, 5812, 345, 8173, 9785, 1525, 955, 5603, 2215, 2580, 5261, 2765, 2990, 5979, 389, 3907, 2484, 1232, 5933, 5871, 3304, 1138, 1616, 5114, 9199, 5072, 7442, 7245, 6472, 4760, 6359, 9053, 7876, 2564, 9404, 3043, 9026, 2261, 3374, 4460, 7306, 2326, 966, 828, 3274, 1712, 3446,
3975, 4565, 8131, 5800, 4570, 2306, 8838, 4392, 9147, 11, 3911, 7118, 9645, 4994, 2028, 6062, 5431, 2279, 8752, 2658, 7836, 994, 7316, 5336, 7185, 3289, 1898, 9689, 2331, 5737, 3403, 1124, 2679, 3241, 7748, 16, 2724, 5441, 6640, 9368, 9081, 5618, 858, 4969, 17, 2103, 6035, 8043, 7475, 2181, 939, 415, 1617, 8500, 8253, 2155, 7843, 7974, 7859, 1746, 6336, 3193, 2617, 8736, 4079, 6324, 6645, 8891, 9396, 5522, 6103, 1857, 8979, 3835, 2475, 1310, 7422, 610, 8345, 7615,
9248, 5397, 5686, 2988, 3446, 4359, 6634, 9141, 497, 9176, 6773, 7448, 1907, 8454, 916, 1596, 2241, 1626, 1384, 2741, 3649, 5362, 8791, 7170, 2903, 2475, 5325, 6451, 924, 3328, 522, 90, 4813, 9737, 9557, 691, 2388, 1383, 4021, 1609, 9206, 4707, 5200, 7107, 8104, 4333, 9860, 5013, 1224, 6959, 8527, 1877, 4545, 7772, 6268, 621, 4915, 9349, 5970, 706, 9583, 3071, 4127, 780, 8231, 3017, 9114, 3836, 7503, 2383, 1977, 4870, 8035, 2379, 9704, 1037, 3992, 3642, 1016, 4303,
5093, 138, 4639, 6609, 1146, 5565, 95, 7521, 9077, 2272, 974, 4388, 2465, 2650, 722, 4998, 3567, 3047, 921, 2736, 7855, 173, 2065, 4238, 1048, 5, 6847, 9548, 8632, 9194, 5942, 4777, 7910, 8971, 6279, 7253, 2516, 1555, 1833, 3184, 9453, 9053, 6897, 7808, 8629, 4877, 1871, 8055, 4881, 7639, 1537, 7701, 2508, 7564, 5845, 5023, 2304, 5396, 3193, 2955, 1088, 3801, 6203, 1748, 3737, 1276, 13, 4120, 7715, 8552, 3047, 2921, 106, 7508, 304, 1280, 7140, 2567, 9135, 5266,
6237, 4607, 7527, 9047, 522, 7371, 4883, 2540, 5867, 6366, 5301, 1570, 421, 276, 3361, 527, 6637, 4861, 2401, 7522, 5808, 9371, 5298, 2045, 5096, 5447, 7755, 5115, 7060, 8529, 4078, 1943, 1697, 1764, 5453, 7085, 960, 2405, 739, 2100, 5800, 728, 9737, 5704, 5693, 1431, 8979, 6428, 673, 7540, 6, 7773, 5857, 6823, 150, 5869, 8486, 684, 5816, 9626, 7451, 5579, 8260, 3397, 5322, 6920, 1879, 2127, 2884, 5478, 4977, 9016, 6165, 6292, 3062, 5671, 5968, 78, 4619, 4763,
9905, 7127, 9390, 5185, 6923, 3721, 9164, 9705, 4341, 1031, 1046, 5127, 7376, 6528, 3248, 4941, 1178, 7889, 3364, 4486, 5358, 9402, 9158, 8600, 1025, 874, 1839, 1783, 309, 9030, 1843, 845, 8398, 1433, 7118, 70, 8071, 2877, 3904, 8866, 6722, 4299, 10, 1929, 5897, 4188, 600, 1889, 3325, 2485, 6473, 4474, 7444, 6992, 4846, 6166, 4441, 2283, 2629, 4352, 7775, 1101, 2214, 9985, 215, 8270, 9750, 2740, 8361, 7103, 5930, 8664, 9690, 8302, 9267, 344, 2077, 1372, 1880, 9550,
5825, 8517, 7769, 2405, 8204, 1060, 3603, 7025, 478, 8334, 1997, 3692, 7433, 9101, 7294, 7498, 9415, 5452, 3850, 3508, 6857, 9213, 6807, 4412, 7310, 854, 5384, 686, 4978, 892, 8651, 3241, 2743, 3801, 3813, 8588, 6701, 4416, 6990, 6490, 3197, 6838, 6503, 114, 8343, 5844, 8646, 8694, 65, 791, 5979, 2687, 2621, 2019, 8097, 1423, 3644, 9764, 4921, 3266, 3662, 5561, 2476, 8271, 8138, 6147, 1168, 3340, 1998, 9874, 6572, 9873, 6659, 5609, 2711, 3931, 9567, 4143, 7833, 8887,
6223, 2099, 2700, 589, 4716, 8333, 1362, 5007, 2753, 2848, 4441, 8397, 7192, 8191, 4916, 9955, 6076, 3370, 6396, 6971, 3156, 248, 3911, 2488, 4930, 2458, 7183, 5455, 170, 6809, 6417, 3390, 1956, 7188, 577, 7526, 2203, 968, 8164, 479, 8699, 7915, 507, 6393, 4632, 1597, 7534, 3604, 618, 3280, 6061, 9793, 9238, 8347, 568, 9645, 2070, 5198, 6482, 5000, 9212, 6655, 5961, 7513, 1323, 3872, 6170, 3812, 4146, 2736, 67, 3151, 5548, 2781, 9679, 7564, 5043, 8587, 1893, 4531,
5826, 3690, 6724, 2121, 9308, 6986, 8106, 6659, 2142, 1642, 7170, 2877, 5757, 6494, 8026, 6571, 8387, 9961, 6043, 9758, 9607, 6450, 8631, 8334, 7359, 5256, 8523, 2225, 7487, 1977, 9555, 8048, 5763, 2414, 4948, 4265, 2427, 8978, 8088, 8841, 9208, 9601, 5810, 9398, 8866, 9138, 4176, 5875, 7212, 3272, 6759, 5678, 7649, 4922, 5422, 1343, 8197, 3154, 3600, 687, 1028, 4579, 2084, 9467, 4492, 7262, 7296, 6538, 7657, 7134, 2077, 1505, 7332, 6890, 8964, 4879, 7603, 7400, 5973, 739,
1861, 1613, 4879, 1884, 7334, 966, 2000, 7489, 2123, 4287, 1472, 3263, 4726, 9203, 1040, 4103, 6075, 6049, 330, 9253, 4062, 4268, 1635, 9960, 577, 1320, 3195, 9628, 1030, 4092, 4979, 6474, 6393, 2799, 6967, 8687, 7724, 7392, 9927, 2085, 3200, 6466, 8702, 265, 7646, 8665, 7986, 7266, 4574, 6587, 612, 2724, 704, 3191, 8323, 9523, 3002, 704, 5064, 3960, 8209, 2027, 2758, 8393, 4875, 4641, 9584, 6401, 7883, 7014, 768, 443, 5490, 7506, 1852, 2005, 8850, 5776, 4487, 4269,
4052, 6687, 4705, 7260, 6645, 6715, 3706, 5504, 8672, 2853, 1136, 8187, 8203, 4016, 871, 1809, 1366, 4952, 9294, 5339, 6872, 2645, 6083, 7874, 3056, 5218, 7485, 8796, 7401, 3348, 2103, 426, 8572, 4163, 9171, 3176, 948, 7654, 9344, 3217, 1650, 5580, 7971, 2622, 76, 2874, 880, 2034, 9929, 1546, 2659, 5811, 3754, 7096, 7436, 9694, 9960, 7415, 2164, 953, 2360, 4194, 2397, 1047, 2196, 6827, 575, 784, 2675, 8821, 6802, 7972, 5996, 6699, 2134, 7577, 2887, 1412, 4349, 4380,
4629, 2234, 6240, 8132, 7592, 3181, 6389, 1214, 266, 1910, 2451, 8784, 2790, 1127, 6932, 1447, 8986, 2492, 5476, 397, 889, 3027, 7641, 5083, 5776, 4022, 185, 3364, 5701, 2442, 2840, 4160, 9525, 4828, 6602, 2614, 7447, 3711, 4505, 7745, 8034, 6514, 4907, 2605, 7753, 6958, 7270, 6936, 3006, 8968, 439, 2326, 4652, 3085, 3425, 9863, 5049, 5361, 8688, 297, 7580, 8777, 7916, 6687, 8683, 7141, 306, 9569, 2384, 1500, 3346, 4601, 7329, 9040, 6097, 2727, 6314, 4501, 4974, 2829,
8316, 4072, 2025, 6884, 3027, 1808, 5714, 7624, 7880, 8528, 4205, 8686, 7587, 3230, 1139, 7273, 6163, 6986, 3914, 9309, 1464, 9359, 4474, 7095, 2212, 7302, 2583, 9462, 7532, 6567, 1606, 4436, 8981, 5612, 6796, 4385, 5076, 2007, 6072, 3678, 8331, 1338, 3299, 8845, 4783, 8613, 4071, 1232, 6028, 2176, 3990, 2148, 3748, 103, 9453, 538, 6745, 9110, 926, 3125, 473, 5970, 8728, 7072, 9062, 1404, 1317, 5139, 9862, 6496, 6062, 3338, 464, 1600, 2532, 1088, 8232, 7739, 8274, 3873,
2341, 523, 7096, 8397, 8301, 6541, 9844, 244, 4993, 2280, 7689, 4025, 4196, 5522, 7904, 6048, 2623, 9258, 2149, 9461, 6448, 8087, 7245, 1917, 8340, 7127, 8466, 5725, 6996, 3421, 5313, 512, 9164, 9837, 9794, 8369, 4185, 1488, 7210, 1524, 1016, 4620, 9435, 2478, 7765, 8035, 697, 6677, 3724, 6988, 5853, 7662, 3895, 9593, 1185, 4727, 6025, 5734, 7665, 3070, 138, 8469, 6748, 6459, 561, 7935, 8646, 2378, 462, 7755, 3115, 9690, 8877, 3946, 2728, 8793, 244, 6323, 8666, 4271,
6430, 2406, 8994, 56, 1267, 3826, 9443, 7079, 7579, 5232, 6691, 3435, 6718, 5698, 4144, 7028, 592, 2627, 217, 734, 6194, 8156, 9118, 58, 2640, 8069, 4127, 3285, 694, 3197, 3377, 4143, 4802, 3324, 8134, 6953, 7625, 3598, 3584, 4289, 7065, 3434, 2106, 7132, 5802, 7920, 9060, 7531, 3321, 1725, 1067, 3751, 444, 5503, 6785, 7937, 6365, 4803, 198, 6266, 8177, 1470, 6390, 1606, 2904, 7555, 9834, 8667, 2033, 1723, 5167, 1666, 8546, 8152, 473, 4475, 6451, 7947, 3062, 3281,
2810, 3042, 7759, 1741, 2275, 2609, 7676, 8640, 4117, 1958, 7500, 8048, 1757, 3954, 9270, 1971, 4796, 2912, 660, 5511, 3553, 1012, 5757, 4525, 6084, 7198, 8352, 5775, 7726, 8591, 7710, 9589, 3122, 4392, 6856, 5016, 749, 2285, 3356, 7482, 9956, 7348, 2599, 8944, 495, 3462, 3578, 551, 4543, 7207, 7169, 7796, 1247, 4278, 6916, 8176, 3742, 8385, 2310, 1345, 8692, 2667, 4568, 1770, 8319, 3585, 4920, 3890, 4928, 7343, 5385, 9772, 7947, 8786, 2056, 9266, 3454, 2807, 877, 2660,
6206, 8252, 5928, 5837, 4177, 4333, 207, 7934, 5581, 9526, 8906, 1498, 8411, 2984, 5198, 5134, 2464, 8435, 8514, 8674, 3876, 599, 5327, 826, 2152, 4084, 2433, 9327, 9697, 4800, 2728, 3608, 3849, 3861, 3498, 9943, 1407, 3991, 7191, 9110, 5666, 8434, 4704, 6545, 5944, 2357, 1163, 4995, 9619, 6754, 4200, 9682, 6654, 4862, 4744, 5953, 6632, 1054, 293, 9439, 8286, 2255, 696, 8709, 1533, 1844, 6441, 430, 1999, 6063, 9431, 7018, 8057, 2920, 6266, 6799, 356, 3597, 4024, 6665,
3847, 6356, 8541, 7225, 2325, 2946, 5199, 469, 5450, 7508, 2197, 9915, 8284, 7983, 6341, 3276, 3321, 16, 1321, 7608, 5015, 3362, 8491, 6968, 6818, 797, 156, 2575, 706, 9516, 5344, 5457, 9210, 5051, 8099, 1617, 9951, 7663, 8253, 9683, 2670, 1261, 4710, 1068, 8753, 4799, 1228, 2621, 3275, 6188, 4699, 1791, 9518, 8701, 5932, 4275, 6011, 9877, 2933, 4182, 6059, 2930, 6687, 6682, 9771, 654, 9437, 3169, 8596, 1827, 5471, 8909, 2352, 123, 4394, 3208, 8756, 5513, 6917, 2056,
5458, 8173, 3138, 3290, 4570, 4892, 3317, 4251, 9699, 7973, 1163, 1935, 5477, 6648, 9614, 5655, 9592, 975, 9118, 2194, 7322, 8248, 8413, 3462, 8560, 1907, 7810, 6650, 7355, 2939, 4973, 6894, 3933, 3784, 3200, 2419, 9234, 4747, 2208, 2207, 1945, 2899, 1407, 6145, 8023, 3484, 5688, 7686, 2737, 3828, 3704, 9004, 5190, 9740, 8643, 8650, 5358, 4426, 1522, 1707, 3613, 9887, 6956, 2447, 2762, 833, 1449, 9489, 2573, 1080, 4167, 3456, 6809, 2466, 227, 7125, 2759, 6250, 6472, 8089,
3266, 7025, 9756, 3914, 1265, 9116, 7723, 9788, 6805, 5493, 2092, 8688, 6592, 9173, 4431, 4028, 6007, 7131, 4446, 4815, 3648, 6701, 759, 3312, 8355, 4485, 4187, 5188, 8746, 7759, 3528, 2177, 5243, 8379, 3838, 7233, 4607, 9187, 7216, 2190, 6967, 2920, 6082, 7910, 5354, 3609, 8958, 6949, 7731, 494, 8753, 8707, 1523, 4426, 3543, 7085, 647, 6771, 9847, 646, 5049, 824, 8417, 5260, 2730, 5702, 2513, 9275, 4279, 2767, 8684, 1165, 9903, 4518, 55, 9682, 8963, 6005, 2102, 6523,
1998, 8731, 936, 1479, 5259, 7064, 4085, 91, 7745, 7136, 3773, 3810, 730, 8255, 2705, 2653, 9790, 6807, 2342, 355, 9344, 2668, 3690, 2028, 9679, 8102, 574, 4318, 6481, 9175, 5423, 8062, 2867, 9657, 7553, 3442, 3920, 7430, 3945, 7639, 3714, 3392, 2525, 4995, 4850, 2867, 7951, 9667, 486, 9506, 9888, 781, 8866, 1702, 3795, 90, 356, 1483, 4200, 2131, 6969, 5931, 486, 6880, 4404, 1084, 5169, 4910, 6567, 8335, 4686, 5043, 2614, 3352, 2667, 4513, 6472, 7471, 5720, 1616,
8878, 1613, 1716, 868, 1906, 2681, 564, 665, 5995, 2474, 7496, 3432, 9491, 9087, 8850, 8287, 669, 823, 347, 6194, 2264, 2592, 7871, 7616, 8508, 4827, 760, 2676, 4660, 4881, 7572, 3811, 9032, 939, 4384, 929, 7525, 8419, 5556, 9063, 662, 8887, 7026, 8534, 3111, 1454, 2082, 7598, 5726, 6687, 9647, 7608, 73, 3014, 5063, 670, 5461, 5631, 3367, 9796, 8475, 7908, 5073, 1565, 5008, 5295, 4457, 1274, 4788, 1728, 338, 600, 8415, 8535, 9351, 7750, 6887, 5845, 1741, 125,
3637, 6489, 9634, 9464, 9055, 2413, 7824, 9517, 7532, 3577, 7050, 6186, 6980, 9365, 9782, 191, 870, 2497, 8498, 2218, 2757, 5420, 6468, 586, 3320, 9230, 1034, 1393, 9886, 5072, 9391, 1178, 8464, 8042, 6869, 2075, 8275, 3601, 7715, 9470, 8786, 6475, 8373, 2159, 9237, 2066, 3264, 5000, 679, 355, 3069, 4073, 494, 2308, 5512, 4334, 9438, 8786, 8637, 9774, 1169, 1949, 6594, 6072, 4270, 9158, 7916, 5752, 6794, 9391, 6301, 5842, 3285, 2141, 3898, 8027, 4310, 8821, 7079, 1307,
8497, 6681, 4732, 7151, 7060, 5204, 9030, 7157, 833, 5014, 8723, 3207, 9796, 9286, 4913, 119, 5118, 7650, 9335, 809, 3675, 2597, 5144, 3945, 5090, 8384, 187, 4102, 1260, 2445, 2792, 4422, 8389, 9290, 50, 1765, 1521, 6921, 8586, 4368, 1565, 5727, 7855, 2003, 4834, 9897, 5911, 8630, 5070, 1330, 7692, 7557, 7980, 6028, 5805, 9090, 8265, 3019, 3802, 698, 9149, 5748, 1965, 9658, 4417, 5994, 5584, 8226, 2937, 272, 5743, 1278, 5698, 8736, 2595, 6475, 5342, 6596, 1149, 6920,
8188, 8009, 9546, 6310, 8772, 2500, 9846, 6592, 6872, 3857, 1307, 8125, 7042, 1544, 6159, 2330, 643, 4604, 7899, 6848, 371, 8067, 2062, 3200, 7295, 1857, 9505, 6936, 384, 2193, 2190, 301, 8535, 5503, 1462, 7380, 5114, 4824, 8833, 1763, 4974, 8711, 9262, 6698, 3999, 2645, 6937, 7747, 1128, 2933, 3556, 7943, 2885, 3122, 9105, 5447, 418, 2899, 5148, 3699, 9021, 9501, 597, 4084, 175, 1621, 1, 1079, 6067, 5812, 4326, 9914, 6633, 5394, 4233, 6728, 9084, 1864, 5863, 1225,
9935, 8793, 9117, 1825, 9542, 8246, 8437, 3331, 9128, 9675, 6086, 7075, 319, 1334, 7932, 3583, 7167, 4178, 1726, 7720, 695, 8277, 7887, 6359, 5912, 1719, 2780, 8529, 1359, 2013, 4498, 8072, 1129, 9998, 1147, 8804, 9405, 6255, 1619, 2165, 7491, 1, 8882, 7378, 3337, 503, 5758, 4109, 3577, 985, 3200, 7615, 8058, 5032, 1080, 6410, 6873, 5496, 1466, 2412, 9885, 5904, 4406, 3605, 8770, 4361, 6205, 9193, 1537, 9959, 214, 7260, 9566, 1685, 100, 4920, 7138, 9819, 5637, 976,
3466, 9854, 985, 1078, 7222, 8888, 5466, 5379, 3578, 4540, 6853, 8690, 3728, 6351, 7147, 3134, 6921, 9692, 857, 3307, 4998, 2172, 5783, 3931, 9417, 2541, 6299, 13, 787, 2099, 9131, 9494, 896, 8600, 1643, 8419, 7248, 2660, 2609, 8579, 91, 6663, 5506, 7675, 1947, 6165, 4286, 1972, 9645, 3805, 1663, 1456, 8853, 5705, 9889, 7489, 1107, 383, 4044, 2969, 3343, 152, 7805, 4980, 9929, 5033, 1737, 9953, 7197, 9158, 4071, 1324, 473, 9676, 3984, 9680, 3606, 8160, 7384, 5432,
1005, 4512, 5186, 3953, 2164, 3372, 4097, 3247, 8697, 3022, 9896, 4101, 3871, 6791, 3219, 2742, 4630, 6967, 7829, 5991, 6134, 1197, 1414, 8923, 8787, 1394, 8852, 5019, 7768, 5147, 8004, 8825, 5062, 9625, 7988, 1110, 3992, 7984, 9966, 6516, 6251, 8270, 421, 3723, 1432, 4830, 6935, 8095, 9059, 2214, 6483, 6846, 3120, 1587, 6201, 6691, 9096, 9627, 6671, 4002, 3495, 9939, 7708, 7465, 5879, 6959, 6634, 3241, 3401, 2355, 9061, 2611, 7830, 3941, 2177, 2146, 5089, 7079, 519, 6351,
7280, 8586, 4261, 2831, 7217, 3141, 9994, 9940, 5462, 2189, 4005, 6942, 9848, 5350, 8060, 6665, 7519, 4324, 7684, 657, 9453, 9296, 2944, 6843, 7499, 7847, 1728, 9681, 3906, 6353, 5529, 2822, 3355, 3897, 7724, 4257, 7489, 8672, 4356, 3983, 1948, 6892, 7415, 4153, 5893, 4190, 621, 1736, 4045, 9532, 7701, 3671, 1211, 1622, 3176, 4524, 9317, 7800, 5638, 6644, 6943, 5463, 3531, 2821, 1347, 5958, 3436, 1438, 2999, 994, 850, 4131, 2616, 1549, 3465, 5946, 690, 9273, 6954, 7991,
9517, 399, 3249, 2596, 7736, 2142, 1322, 968, 7350, 1614, 468, 3346, 3265, 7222, 6086, 1661, 5317, 2582, 7959, 4685, 2807, 2917, 1037, 5698, 1529, 3972, 8716, 2634, 3301, 3412, 8621, 743, 8001, 4734, 888, 7744, 8092, 3671, 8941, 1487, 5658, 7099, 2781, 99, 1932, 4443, 4756, 4652, 9328, 1581, 7855, 4312, 5976, 7255, 6480, 3996, 2748, 1973, 9731, 4530, 2790, 9417, 7186, 5303, 3557, 351, 7182, 9428, 1342, 9020, 7599, 1392, 8304, 2070, 9138, 7215, 2008, 9937, 1106, 7110,
7444, 769, 9688, 632, 1571, 6820, 8743, 4338, 337, 3366, 3073, 1946, 8219, 104, 4210, 6986, 249, 5061, 8693, 7960, 6546, 1004, 8857, 5997, 9352, 4338, 6105, 5008, 2556, 6518, 6694, 4345, 3727, 7956, 20, 3954, 8652, 4424, 9387, 2035, 8358, 5962, 5304, 5194, 8650, 8282, 1256, 1103, 2138, 6679, 1985, 3653, 2770, 2433, 4278, 615, 2863, 1715, 242, 3790, 2636, 6998, 3088, 1671, 2239, 957, 5411, 4595, 6282, 2881, 9974, 2401, 875, 7574, 2987, 4587, 3147, 6766, 9885, 2965,
3287, 3016, 3619, 6818, 9073, 6120, 5423, 557, 2900, 2015, 8111, 3873, 1314, 4189, 1846, 4399, 7041, 7583, 2427, 2864, 3525, 5002, 2069, 748, 1948, 6015, 2684, 438, 770, 8367, 1663, 7887, 7759, 1885, 157, 7770, 4520, 4878, 3857, 1137, 3525, 3050, 6276, 5569, 7649, 904, 4533, 7843, 2199, 5648, 7628, 9075, 9441, 3600, 7231, 2388, 5640, 9096, 958, 3058, 584, 5899, 8150, 1181, 9616, 1098, 8162, 6819, 8171, 1519, 1140, 7665, 8801, 2632, 1299, 9192, 707, 9955, 2710, 7314,
1772, 2963, 7578, 3541, 3095, 1488, 7026, 2634, 6015, 4633, 4370, 2762, 1650, 2174, 909, 8158, 2922, 8467, 4198, 4280, 9092, 8856, 8835, 5457, 2790, 8574, 9742, 5054, 9547, 4156, 7940, 8126, 9824, 7340, 8840, 6574, 3547, 1477, 3014, 6798, 7134, 435, 9484, 9859, 3031, 4, 1502, 4133, 1738, 1807, 4825, 463, 6343, 9701, 8506, 9822, 9555, 8688, 8168, 3467, 3234, 6318, 1787, 5591, 419, 6593, 7974, 8486, 9861, 6381, 6758, 194, 3061, 4315, 2863, 4665, 3789, 2201, 1492, 4416,
126, 8927, 6608, 5682, 8986, 6867, 1715, 6076, 3159, 788, 3140, 4744, 830, 9253, 5812, 5021, 7616, 8534, 1546, 9590, 1101, 9012, 9821, 8132, 7857, 4086, 1069, 7491, 2988, 1579, 2442, 4321, 2149, 7642, 6108, 250, 6086, 3167, 24, 9528, 7663, 2685, 1220, 9196, 1397, 5776, 1577, 1730, 5481, 977, 6115, 199, 6326, 2183, 3767, 5928, 5586, 7561, 663, 8649, 9688, 949, 5913, 9160, 1870, 5764, 9887, 4477, 6703, 1413, 4995, 5494, 7131, 2192, 8969, 7138, 3997, 8697, 646, 1028,
8074, 1731, 8245, 624, 4601, 8706, 155, 8891, 309, 2552, 8208, 8452, 2954, 3124, 3469, 4246, 3352, 1105, 4509, 8677, 9901, 4416, 8191, 9283, 5625, 7120, 2952, 8881, 7693, 830, 4580, 8228, 9459, 8611, 4499, 1179, 4988, 1394, 550, 2336, 6089, 6872, 269, 7213, 1848, 917, 6672, 4890, 656, 1478, 6536, 3165, 4743, 4990, 1176, 6211, 7207, 5284, 9730, 4738, 1549, 4986, 4942, 8645, 3698, 9429, 1439, 2175, 6549, 3058, 6513, 1574, 6988, 8333, 3406, 5245, 5431, 7140, 7085, 6407,
7845, 4694, 2530, 8249, 290, 5948, 5509, 1588, 5940, 4495, 5866, 5021, 4626, 3979, 3296, 7589, 4854, 1998, 5627, 3926, 8346, 6512, 9608, 1918, 7070, 4747, 4182, 2858, 2766, 4606, 6269, 4107, 8982, 8568, 9053, 4244, 5604, 102, 2756, 727, 5887, 2566, 7922, 44, 5986, 621, 1202, 374, 6988, 4130, 3627, 6744, 9443, 4568, 1398, 8679, 397, 3928, 9159, 367, 2917, 6127, 5788, 3304, 8129, 911, 2669, 1463, 9749, 264, 4478, 8940, 1109, 7309, 2462, 117, 4692, 7724, 225, 2312,
4164, 3637, 2000, 941, 8903, 39, 3443, 7172, 1031, 3687, 4901, 8082, 4945, 4515, 7204, 9310, 9349, 9535, 9940, 218, 1788, 9245, 2237, 1541, 5670, 6538, 6047, 5553, 9807, 8101, 1925, 8714, 445, 8332, 7309, 6830, 5786, 5736, 7306, 2710, 3034, 1838, 7969, 6318, 7912, 2584, 2080, 7437, 6705, 2254, 7428, 820, 782, 9861, 7596, 3842, 3631, 8063, 5240, 6666, 394, 4565, 7865, 4895, 9890, 6028, 6117, 4724, 9156, 4473, 4552, 602, 470, 6191, 4927, 5387, 884, 3146, 1978, 3000,
4258, 6880, 1696, 3582, 5793, 4923, 2119, 1155, 9056, 9698, 6603, 3768, 5514, 9927, 9609, 6166, 6566, 4536, 4985, 4934, 8076, 9062, 6741, 6163, 7399, 4562, 2337, 5600, 2919, 9012, 8459, 1308, 6072, 1225, 9306, 8818, 5886, 7243, 7365, 8792, 6007, 9256, 6699, 7171, 4230, 7002, 8720, 7839, 4533, 1671, 478, 7774, 1607, 2317, 5437, 4705, 7886, 4760, 6760, 7271, 3081, 2997, 3088, 7675, 6208, 3101, 6821, 6840, 122, 9633, 4900, 2067, 8546, 4549, 2091, 7188, 5605, 8599, 6758, 5229,
7854, 5243, 9155, 3556, 8812, 7047, 2202, 1541, 5993, 4600, 4760, 713, 434, 7911, 7426, 7414, 8729, 322, 803, 7960, 7563, 4908, 6285, 6291, 736, 3389, 9339, 4132, 8701, 7534, 5287, 3646, 592, 3065, 7582, 2592, 8755, 6068, 8597, 1982, 5782, 1894, 2900, 6236, 4039, 6569, 3037, 5837, 7698, 700, 7815, 2491, 7272, 5878, 3083, 6778, 6639, 3589, 5010, 8313, 2581, 6617, 5869, 8402, 6808, 2951, 2321, 5195, 497, 2190, 6187, 1342, 1316, 4453, 7740, 4154, 2959, 1781, 1482, 8256,
7178, 2046, 4419, 744, 8312, 5356, 6855, 8839, 319, 2962, 5662, 47, 6307, 8662, 68, 4813, 567, 2712, 9931, 1678, 3101, 8227, 6533, 4933, 6656, 92, 5846, 4780, 6256, 6361, 4323, 9985, 1231, 2175, 7178, 3034, 9744, 6155, 9165, 7787, 5836, 9318, 7860, 9644, 8941, 6480, 9443, 8188, 5928, 161, 6979, 2352, 5628, 6991, 1198, 8067, 5867, 6620, 3778, 8426, 2994, 3122, 3124, 6335, 3918, 8897, 2655, 9670, 634, 1088, 1576, 8935, 7255, 474, 8166, 7417, 9547, 2886, 5560, 3842,
6957, 3111, 26, 7530, 7143, 1295, 1744, 6057, 3009, 1854, 8098, 5405, 2234, 4874, 9447, 2620, 9303, 27, 7410, 969, 40, 2966, 5648, 7596, 8637, 4238, 3143, 3679, 7187, 690, 9980, 7085, 7714, 9373, 5632, 7526, 6707, 3951, 9734, 4216, 2146, 3602, 5371, 6029, 3039, 4433, 4855, 4151, 1449, 3376, 8009, 7240, 7027, 4602, 2947, 9081, 4045, 8424, 9352, 8742, 923, 2705, 4266, 3232, 2264, 6761, 363, 2651, 3383, 7770, 6730, 7856, 7340, 9679, 2158, 610, 4471, 4608, 910, 6241,
4417, 6756, 1013, 8797, 658, 8809, 5032, 8703, 7541, 846, 3357, 2920, 9817, 1745, 9980, 7593, 4667, 3087, 779, 3218, 6233, 5568, 4296, 2289, 2654, 7898, 5021, 9461, 5593, 8214, 9173, 4203, 2271, 7980, 2983, 5952, 9992, 8399, 3468, 1776, 3188, 9314, 1720, 6523, 2933, 621, 8685, 5483, 8986, 6163, 3444, 9539, 4320, 155, 3992, 2828, 2150, 6071, 524, 2895, 5468, 8063, 1210, 3348, 9071, 4862, 483, 9017, 4097, 6186, 9815, 3610, 5048, 1644, 1003, 9865, 9332, 2145, 1944, 2213,
9284, 3803, 4920, 1927, 6706, 4344, 7383, 4786, 9890, 2010, 5228, 1224, 3158, 6967, 8580, 8990, 8883, 5213, 76, 8306, 2031, 4980, 5639, 9519, 7184, 5645, 7769, 3259, 8077, 9130, 1317, 3096, 9624, 3818, 1770, 695, 2454, 947, 6029, 3474, 9938, 3527, 5696, 4760, 7724, 7738, 2848, 6442, 5767, 6845, 8323, 4131, 2859, 7595, 2500, 4815, 3660, 9130, 8580, 7016, 8231, 4391, 8369, 3444, 4069, 4021, 556, 6154, 627, 2778, 1496, 4206, 6356, 8434, 8491, 3816, 8231, 3190, 5575, 1015,
3787, 7572, 1788, 6803, 5641, 6844, 1961, 4811, 8535, 9914, 9999, 1450, 8857, 738, 4662, 8569, 6679, 2225, 7839, 8618, 286, 2648, 5342, 2294, 3205, 4546, 176, 8705, 3741, 6134, 8324, 8021, 7004, 5205, 7032, 6637, 9442, 5539, 5584, 4819, 5874, 5807, 8589, 6871, 9016, 983, 1758, 3786, 1519, 6241, 185, 8398, 495, 3370, 9133, 3051, 4549, 9674, 7311, 9738, 3316, 9383, 2658, 2776, 9481, 7558, 619, 3943, 3324, 6491, 4933, 153, 9738, 4623, 912, 3595, 7771, 7939, 1219, 4405,
2650, 3883, 4154, 5809, 315, 7756, 4430, 1788, 4451, 1631, 6461, 7230, 6017, 5751, 138, 588, 5282, 2442, 9110, 9035, 6349, 2515, 1570, 6122, 4192, 4174, 3530, 1933, 4186, 4420, 4609, 5739, 4135, 2963, 6308, 1161, 8809, 8619, 2796, 3819, 6971, 8228, 4188, 1492, 909, 8048, 2328, 6772, 8467, 7671, 9068, 2226, 7579, 6422, 7056, 8042, 3296, 2272, 3006, 2196, 7320, 3238, 3490, 3102, 37, 1293, 3212, 4767, 5041, 8773, 5794, 4456, 6174, 7279, 7054, 2835, 7053, 9088, 790, 6640,
3101, 1057, 7057, 3826, 6077, 1025, 2955, 1224, 1114, 6729, 5902, 4698, 6239, 7203, 9423, 1804, 4417, 6686, 1426, 6941, 8071, 1029, 4985, 9010, 6122, 6597, 1622, 1574, 3513, 1684, 7086, 5505, 3244, 411, 9638, 4150, 907, 9135, 829, 981, 1707, 5359, 8781, 9751, 5, 9131, 3973, 7159, 1340, 6955, 7514, 7993, 6964, 8198, 1933, 2797, 877, 3993, 4453, 8020, 9349, 8646, 2779, 8679, 2961, 3547, 3374, 3510, 1129, 3568, 2241, 2625, 9138, 5974, 8206, 7669, 7678, 1833, 8700, 4480,
4865, 9912, 8038, 8238, 782, 3095, 8199, 1127, 4501, 7280, 2112, 2487, 3626, 2790, 9432, 1475, 6312, 8277, 4827, 2218, 5806, 7132, 8752, 1468, 7471, 6386, 739, 8762, 8323, 8120, 5169, 9078, 9058, 3370, 9560, 7987, 8585, 8531, 5347, 9312, 1058, 4271, 1159, 5286, 5404, 6925, 8606, 9204, 7361, 2415, 560, 586, 4002, 2644, 1927, 2824, 768, 4409, 2942, 3345, 1002, 808, 4941, 6267, 7979, 5140, 8643, 7553, 9438, 7320, 4938, 2666, 4609, 2778, 8158, 6730, 3748, 3867, 1866, 7181,
171, 3771, 7134, 8927, 4778, 2913, 3326, 2004, 3089, 7853, 1378, 1729, 4777, 2706, 9578, 1360, 5693, 3036, 1851, 7248, 2403, 2273, 8536, 6501, 9216, 613, 9671, 7131, 7719, 6425, 773, 717, 8803, 160, 1114, 7554, 7197, 753, 4513, 4322, 8499, 4533, 2609, 4226, 8710, 6627, 644, 9666, 6260, 4870, 5744, 7385, 6542, 6203, 7703, 6130, 8944, 5589, 2262, 6803, 6381, 7414, 6888, 5123, 7320, 9392, 9061, 6780, 322, 8975, 7050, 5089, 1061, 2260, 3199, 1150, 1865, 5386, 9699, 6501,
3744, 8454, 6885, 8277, 919, 1923, 4001, 6864, 7854, 5519, 2491, 6057, 8794, 9645, 1776, 5714, 9786, 9281, 7538, 6916, 3215, 395, 2501, 9618, 4835, 8846, 9708, 2813, 3303, 1794, 8309, 7176, 2206, 1602, 1838, 236, 4593, 2245, 8993, 4017, 10, 8215, 6921, 5206, 4023, 5932, 6997, 7801, 262, 7640, 3107, 8275, 4938, 7822, 2425, 3223, 3886, 2105, 8700, 9526, 2088, 8662, 8034, 7004, 5710, 2124, 7164, 3574, 6630, 9980, 4242, 2901, 9471, 1491, 2117, 4562, 1130, 9086, 4117, 6698,
2810, 2280, 2331, 1170, 4554, 4071, 8387, 1215, 2274, 9848, 6738, 1604, 7281, 8805, 439, 1298, 8318, 7834, 9426, 8603, 6092, 7944, 1309, 8828, 303, 3157, 4638, 4439, 9175, 1921, 4695, 7716, 1494, 1015, 1772, 5913, 1127, 1952, 1950, 8905, 4064, 9890, 385, 9357, 7945, 5035, 7082, 5369, 4093, 6546, 5187, 5637, 2041, 8946, 1758, 7111, 6566, 1027, 1049, 5148, 7224, 7248, 296, 6169, 375, 1656, 7993, 2816, 3717, 4279, 4675, 1609, 3317, 42, 6201, 3100, 3144, 163, 9530, 4531,
7096, 6070, 1009, 4988, 3538, 5801, 7149, 3063, 2324, 2912, 7911, 7002, 4338, 7880, 2481, 7368, 3516, 2016, 7556, 2193, 1388, 3865, 8125, 4637, 4096, 8114, 750, 3144, 1938, 7002, 9343, 4095, 1392, 4220, 3455, 6969, 9647, 1321, 9048, 1996, 1640, 6626, 1788, 314, 9578, 6630, 2813, 6626, 4981, 9908, 7024, 4355, 3201, 3521, 3864, 3303, 464, 1923, 595, 9801, 3391, 8366, 8084, 9374, 1041, 8807, 9085, 1892, 9431, 8317, 9016, 9221, 8574, 9981, 9240, 5395, 2009, 6310, 2854, 9255,
8830, 3145, 2960, 9615, 8220, 6061, 3452, 2918, 6481, 9278, 2297, 3385, 6565, 7066, 7316, 5682, 107, 7646, 4466, 68, 1952, 9603, 8615, 54, 7191, 791, 6833, 2560, 693, 9733, 4168, 570, 9127, 9537, 1925, 8287, 5508, 4297, 8452, 8795, 6213, 7994, 2420, 4208, 524, 5915, 8602, 8330, 2651, 8547, 6156, 1812, 6271, 7991, 9407, 9804, 1553, 6866, 1128, 2119, 4691, 9711, 8315, 5879, 9935, 6900, 482, 682, 4126, 1041, 428, 6247, 3720, 5882, 7526, 2582, 4327, 7725, 3503, 2631,
2738, 9323, 721, 7434, 1453, 6294, 2957, 3786, 5722, 6019, 8685, 4386, 3066, 9057, 6860, 499, 5315, 3045, 5194, 7111, 3137, 9104, 941, 586, 3066, 755, 4177, 8819, 7040, 5309, 3583, 3897, 4428, 7788, 4721, 7249, 6559, 7324, 825, 7311, 3760, 6064, 6070, 9672, 4882, 584, 1365, 9739, 9331, 5783, 2624, 7889, 1604, 1303, 1555, 7125, 8312, 425, 8936, 3233, 7724, 1480, 403, 7440, 1784, 1754, 4721, 1569, 652, 3893, 4574, 5692, 9730, 4813, 9844, 8291, 9199, 7101, 3391, 8914,
6044, 2928, 9332, 3328, 8588, 447, 3830, 1176, 3523, 2705, 8365, 6136, 5442, 9049, 5526, 8575, 8869, 9031, 7280, 706, 2794, 8814, 5767, 4241, 7696, 78, 6570, 556, 5083, 1426, 4502, 3336, 9518, 2292, 1885, 3740, 3153, 9348, 9331, 8051, 2759, 5407, 9028, 7840, 9255, 831, 515, 2612, 9747, 7435, 8964, 4971, 2048, 4900, 5967, 8271, 1719, 9670, 2810, 6777, 1594, 6367, 6259, 8316, 3815, 1689, 6840, 9437, 4361, 822, 9619, 3065, 83, 6344, 7486, 8657, 8228, 9635, 6932, 4864,
8478, 4777, 6334, 4678, 7476, 4963, 6735, 3096, 5860, 1405, 5127, 7269, 7793, 4738, 227, 9168, 2996, 8928, 765, 733, 1276, 7677, 6258, 1528, 9558, 3329, 302, 8901, 1422, 8277, 6340, 645, 9125, 8869, 5952, 141, 8141, 1816, 9635, 4025, 4184, 3093, 83, 2344, 2747, 9352, 7966, 1206, 1126, 1826, 218, 7939, 2957, 2729, 810, 8752, 5247, 4174, 4038, 8884, 7899, 9567, 301, 5265, 5752, 7524, 4381, 1669, 3106, 8270, 6228, 6373, 754, 2547, 4240, 2313, 5514, 3022, 1040, 9738,
2265, 8192, 1763, 1369, 8469, 8789, 4836, 52, 1212, 6690, 5257, 8918, 6723, 6319, 378, 4039, 2421, 8555, 8184, 9577, 1432, 7139, 8078, 5452, 9628, 7579, 4161, 7490, 5159, 8559, 1011, 81, 478, 5840, 1964, 1334, 6875, 8670, 9900, 739, 1514, 8692, 522, 9316, 6955, 1345, 8132, 2277, 3193, 9773, 3923, 4177, 2183, 1236, 6747, 6575, 4874, 6003, 6409, 8187, 745, 8776, 9440, 7543, 9825, 2582, 7381, 8147, 7236, 5185, 7564, 6125, 218, 7991, 6394, 391, 7659, 7456, 5128, 5294,
2132, 8992, 8160, 5782, 4420, 3371, 3798, 5054, 552, 5631, 7546, 4716, 1332, 6486, 7892, 7441, 4370, 6231, 4579, 2121, 8615, 1145, 9391, 1524, 1385, 2400, 9437, 2454, 7896, 7467, 2928, 8400, 3299, 4025, 7458, 4703, 7206, 6358, 792, 6200, 725, 4275, 4136, 7390, 5984, 4502, 7929, 5085, 8176, 4600, 119, 3568, 76, 9363, 6943, 2248, 9077, 9731, 6213, 5817, 6729, 4190, 3092, 6910, 759, 2682, 8380, 1254, 9604, 3011, 9291, 5329, 9453, 9746, 2739, 6522, 3765, 5634, 1113, 5789,
5304, 5499, 564, 2801, 679, 2653, 1783, 3608, 7359, 7797, 3284, 796, 3222, 437, 7185, 6135, 8571, 2778, 7488, 5746, 678, 6140, 861, 7750, 803, 9859, 9918, 2425, 3734, 2698, 9005, 4864, 9818, 6743, 2475, 132, 9486, 3825, 5472, 919, 292, 4411, 7213, 7699, 6435, 9019, 6769, 1388, 802, 2124, 1345, 8493, 9487, 8558, 7061, 8777, 8833, 2427, 2238, 5409, 4957, 8503, 3171, 7622, 5779, 6145, 2417, 5873, 5563, 5693, 9574, 9491, 1937, 7384, 4563, 6842, 5432, 2751, 3406, 7981]


    n = 80

    def get(l, x, y):
        if y < 1 or x < 1 or y > n or x > n:
            return 0
        return l[y * n + x - n - 1]

    def _set(l, x, y, v):
        l[y * n + x - n - 1] = v

    min_sum = list()
    for _i in range(len(l)):
        min_sum.append(0)

    def get_min(l, x, y):
        if x < 1 or y < 1:
            return 0
        v = get(min_sum, x, y)
        if v != 0:
            return v
        left = get_min(l, x - 1, y)
        top = get_min(l, x, y - 1)
        minleftorup = min(left, top)
        if left == 0 or top == 0:
            minleftorup = max(left, top)
        print "left(%d,%d) = %d top(%d,%d) = %d  min = %d" % (x - 1, y, left, x, y - 1, top, minleftorup)

        v = minleftorup + get(l, x, y)
        _set(min_sum, x, y, v)
        print x, y, get(l, x, y), minleftorup, v

        return v

    print get_min(l, n, n)



def problem_71(): # solved 
    min_n = 1
    min_d = 3
    for d in xrange(1, 1000000):
        for n in xrange(max(1, int(0.428571 * float(d))), int(0.43 * d)):
            if 3 * d - n * 7 <= 0:
                break

            left = d * (3 * min_d - 7 * min_n)
            right = min_d * (3 * d - 7 * n)
            if left > right:
                min_n = n
                min_d = d
                print min_n, min_d, float(min_n) / float(min_d), float(3) / float(7)


def problem_73(): # solved - 7295372    
    cnt = 0
    for d in xrange(4, 12000 + 1):
        for n in xrange(int(max(0.32 * d, 1)), d / 2 + 1):
            if d < 3 * n and 2 * n < d and gcd(d, n) == 1:
                cnt += 1
                print '%d/%d' % (n, d)

    print cnt


def problem_76(): # solved
    d = dict()
    def ways(goal, weight):
        key = '%d_%d' % (goal, weight)
        if key in d:
            return d[key]
        if weight == 1:
            return 1
        n = 0
        for i in range(0, goal / weight + 1):
            n += ways(goal - i * weight, weight - 1)
        d[key] = n
        return n

    print ways(100, 99)

def problem_206(): # solved

    # 1_2_3_4_5_6_7_8_9_0
    import math
    l1 = math.sqrt(1020304050607080900)
    l2 = math.sqrt(1929394959697989990)
    x = int(l1) + 20
#    print x
#    return
    i = 0
    while x <= l2:
        print x, l2
        if str(x * x)[::2] == '1234567890':
            print x
            break
        if i % 2 == 0:
            x += 40
        else:
            x += 60
        i += 1

    # print str(1929394959697989990)[::2]

def problem_87(): #solved
    primes3 = gen_primes(2, 8000)

    limit = 50 * 10 ** 6 - 1
    cnt = 0
    a = set()
    for p1 in primes3:
        quad = p1 ** 4
        for p2 in primes3:
            cube = p2 ** 3
            if quad + cube > limit:
                break
            l = math.sqrt(limit - quad - cube)
            for p3 in primes3:
                if p3 < l:
                    a.add(cube + quad + p3 * p3)
                else:
                    break
    print len(a)


def problem_112(): # solved

    bouncy_cnt = 0
    n = 1
    while 1:
        if is_bouncy(n):
            bouncy_cnt += 1
        ratio = float(bouncy_cnt) / float(n)
        print n, bouncy_cnt, ratio
        if ratio > 0.50:
            break
        n += 1

def problem_113(): # solved

    d = dict()

    def num_ways(dig, num_left):
        key = '%s_%s' % (dig, num_left)
        if key in d:
            return d[key]
        if num_left == 0:
            if dig == 0 or dig == 9:
                #print num
                return 1
            else:
                #print num
                return 2
        v = 0
        for l in range(0, dig + 1):
            v += num_ways(l, num_left - 1)
        d[key] = v
        return v

    sum = 0
    for i in range(1, 101):
        sum += num_ways(9, i) - 9

    print sum

    cnt = 0
    for i in range(1, 10):
        if not is_bouncy(i):
            cnt += 1
    print cnt

def problem_65(): #solved

    def calc(i, n):
        a = 1
        if i % 3 == 2:
            a = 2 * (1 + i / 3)

        if i >= n:
            return a

        return add_frac(a, div_frac(1, calc(i + 1, n)))


    f = add_frac(2, div_frac(1, calc(1, 99)))
    print sum(map(int, str(f[0])))
   # print add_frac(2, div_frac(1, add_frac(1, div_frac(1, add_frac(2, div_frac(1, 1))))))

def problem_145(): # solved

    def is_reversible(n):
        rev = str(n)[::-1]
        if rev[0] == '0':
            return False
        s = str(n + int(rev))

        for i in range(len(s)):
            if s[i] in ['0', '2', '4', '6', '8']:
                return False
        print n, rev
        return True

    cnt = 0
    i = 1
    while i < 10 ** 9:
        # print i
        cnt += int(is_reversible(i)) * 2
        i += 2
        s = str(i)
        if len(s) > 1 and s[0] in ['1', '3', '5', '7']:
            c = int(s[0]) + 1
            new_s = str(c)
            for k in range(1, len(s) - 1):
                new_s += '0'
            new_s += '1'
            i = int(new_s)
            print i


    print cnt

def problem_124(): # solved

    limit = 100000
    primes = gen_primes(2, limit)

    def rad(n):
        prod = 1
        for p in primes:
            if n % p == 0:
                prod *= p
                while n % p == 0:
                    n /= p
            if n <= 1:
                break
        return prod

    l = list()
    for i in range(1, limit + 1):
        print i
        l.append((i, rad(i)))

    def get_key(t):
        return t[1]

    print "Done"
    print l
    newl = sorted(l, key = get_key)
    print newl[9999]


def problem_85(): #solved
    import math
    def num_rect(w, h, bW, bH):
        k = (bW - w + 1) * (bH - h + 1)
       # print w, h, k
        return k


    def get_num_rect(bW, bH):
        s = 0
        for w in range(1, bW + 1):
            for h in range(1, bH + 1):
                s += num_rect(w, h, bW, bH)
        return s

    def get_new_num_rect(W, H):
        W = float(W)
        H = float(H)
        f2 = float(2)
        A = W * H * (W * H + H + W + 1)
        B = (1 + H) * W * W * H / f2 + (1 + W) * H * H * W / f2
        C = (1 + H) * (1 + W) * H * W / (f2 * f2)
        D = (1 + W) * W * H / f2 + (1 + H) * H * W / f2
        result = A - B + C - D
        return result

   # print get_new_num_rect(2, 3)
   # return

    my_bW = my_bH = 0
    n = 1
    for bW in xrange(2, 1000000):
        hStart = 1
        hEnd = 200000
        a1 = get_new_num_rect(bW, hStart)
        a2 = get_new_num_rect(bW, hEnd)
        nIter = 0
        while hEnd - hStart > 1:
            nIter += 1
            hMid = (hEnd + hStart) / 2
            l = get_new_num_rect(bW, hMid)
            if l < 2000000:
                hStart = hMid
            if l > 2000000:
                hEnd = hMid
            if abs(2000000 - l) < abs(2000000 - n):
                n = l
                my_bW = bW
                my_bH = hMid
                print "NewMin: ", my_bW, my_bH, n, hStart, hEnd
        # print bW, a1, a2, nIter

def problem_66():

    import math

    maxx = 0
    for D in range(1, 1000 + 1):
        l = sqrt_continuous_frac(D, 1000)
        # print "l", l
        found = False
        for iter in range(1, min(len(l), 1000)):
            pair = expand_frac(l, iter)
            # print  pair, pair[0] * pair[0] - D * pair[1] * pair[1]
            if pair[0] ** 2 - D * pair[1] ** 2 == 1:
                # print "Found solution for %d: x=%d, y=%d" % (D, pair[0], pair[1])
                found = True
                if maxx < pair[0]:
                    maxx = pair[0]
                    print "maxx,D" , maxx, D
                break
        if not found:
            print "Not found for D = ", D, math.sqrt(D)
            #print p
    print maxx


def problem_64(): #solved
    cnt = 0
    for d in xrange(2, 10000 + 1):
        l = sqrt_continuous_frac(d, 1000)[1:]
        for i in range(1, len(l)):
            pattern = l[0:i]
            j = 0
            a = True
            while j < len(l) - len(pattern):
                if l[j:j + len(pattern)] != pattern:
                    a = False
                    break
                j += len(pattern)
            if a:
                print d, pattern, len(pattern)
                if len(pattern) % 2 == 1:
                    cnt += 1
                break
    print cnt

def problem_80(): #solved
    import math
    sss = 0
    for i in range(2, 100):
        root = math.sqrt(i)
        if int(root) == root:
            continue
        l = sqrt_continuous_frac(i, 700)
        fraction = expand_frac(l, 670)
        s = str(10 ** 200 * fraction[0] / fraction[1])
        sss += sum(map(int, s[0:100]))

      #  print s
      #  print len(str(s))
    print sss



def problem_98(): # solved

    import itertools
    f = open('c:/words.txt')
    l = []
    for line in f:
        l = line.replace('"', '').split(',')
    d = dict()
    for w in l:
        key = ''
        for ch in sorted(map(str, w)):
            key += ch
        if not key in d:
            d[key] = []
        d[key].append(w)

    m = 1
    for k in d:
        if len(d[k]) > 1:
            if d[k][0] == d[k][1]:
                print "PALIN", d[k][0]
            s = set(d[k][0])

            print d[k]
            for selected_digs in itertools.combinations(map(str, range(10)), len(s)):
                for digs in itertools.permutations(selected_digs):
                    #print digs
                    char_dict = dict()
                    #print digs
                    for i, letter in enumerate(s):
                        char_dict[letter] = digs[i]

                  #  print char_dict
                    word1 = ''
                    for aa in d[k][0]:
                        word1 += char_dict[aa]
                    word2 = ''
                    for aa in d[k][1]:
                        word2 += char_dict[aa]

                    # print d[k][0], word1, d[k][1], word2

                    if word1[0] == '0' or word2[0] == '0':
                        continue

                    num1 = int(word1)
                    num2 = int(word2)
                    sqrt1 = math.sqrt(num1)
                    sqrt2 = math.sqrt(num2)
                    if sqrt1 == int(sqrt1) and sqrt2 == int(sqrt2):
                        if m < num1:
                            m = num1
                        if m < num2:
                            m = num2
                        print "Hurray", d[k][0], word1, d[k][1], word2
            #for ch in s:

            # print d[k], s
    print m


def problem_93(): # solved
    import itertools
    max = 0
    maxdigits = set()
    def divide(x, y):
        if y != 0:
            return x / y
        return 0

    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': divide}
    alldigits = set(range(1, 10))
    print alldigits

    m = 1
    # alldigits = set([2, 6, 7, 9])
    for digits in itertools.combinations(alldigits, 4):
        results = set()
        # print digits
        for p in itertools.permutations(digits):
            p = map(float, p)
            for f0 in ['-', '+']:
                s0 = ops[f0](0, p[0])
                for f1 in ops.keys():
                    s1 = ops[f1](s0, p[1])
                    for f2 in ops.keys():
                        s2 = ops[f2](s1, p[2])
                        for f3 in ops.keys():
                            s3 = ops[f3](s2, p[3])
                            if s3 > 0 and int(s3) == s3:
                                #print p[0], f1, p[1], '=', s1, ' ', f2, p[2], '=', s2, ' ', f3, p[3], '=', s3
                                results.add(int(s3))
        results = sorted(list(results))
        for i, num in enumerate(results):
            if i + 1 != num:
                print i, digits
                if i > m:
                    m = i
                    print "NEWMAX", m, digits
                break


def problem_79():
    l = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389,
         162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

    l = map(str, l)
    left = dict()
    right = dict()
    for t in l:
        d1 = t[0]
        d2 = t[1]
        d3 = t[2]
        if d1 not in right:
            right[d1] = set()
        right[d1].add(d2)
        right[d1].add(d3)
        if d2 not in right:
            right[d2] = set()
        right[d2].add(d3)
        if d2 not in left:
            left[d2] = set()
        left[d2].add(d1)
        if d3 not in left:
            left[d3] = set()
        left[d3].add(d2)
        left[d3].add(d1)

    res = dict()
    for x in left:
        r = set()
        if x in right:
            r = right[x]
        print len(left[x]), x, len(r)
        res[len(left[x])] = x
    s = ''
    for k in res.keys():
        s += res[k]
    print s


def problem_77(): # solved


    d = dict()
    def ways(goal, primes):
        if goal == 0:
            return 1
        if len(primes) == 0:
            return 0
        weight = primes[-1]
        key = '%d_%d' % (goal, weight)
        if key in d:
            return d[key]
        #if weight == 2 and goal == 2:
        #    return 1
        n = 0
        for i in range(0, goal / weight + 1):
            n += ways(goal - i * weight, primes[:-1])
        d[key] = n
        return n

    #for i in range(2, 500):
    #    print ways(i, primes)

    primes = gen_primes(2, 1000)
    print ways(71, primes)

def problem_78(): # solved 

    # only ways3 which was taken from http://www.numericana.com/answer/numbers.htm#partitions
    # could finish that quickly

    import sys
    sys.setrecursionlimit(10000)
    d = dict()
    def ways(goal, weight):
        if weight == 1:
            return 1
        key = '%d_%d' % (goal, weight)
        if key in d:
            return d[key]
        n = 0
        for i in xrange(0, goal / weight + 1):
            n += ways(goal - i * weight, weight - 1)
        d[key] = n
        return n

    d1 = dict()
    def ways2(k, n):
        if k > n:
            return 0
        if k == n:
            return 1
        key = '%s_%s' % (k, n)
        if key in d1:
            return d1[key]
        v = ways2(k + 1, n) + ways2(k, n - k)
        d1[key] = v
        return v

    d3 = dict()
    d3[0] = 1
    def ways3(m):
        if m in d3:
            return d3[m]
        for i in range(m, m + 1):
            j = k = 1
            s = 0
            while j > 0:
                j = i - (3 * k ** 2 + k) / 2
                if j >= 0:
                    s = s - (-1) ** k * d3[j]
                j = i - (3 * k ** 2 - k) / 2
                if j >= 0:
                    s = s - (-1) ** k * d3[j]
                k += 1
            d3[i] = s
        return d3[m]


   # print ways2(1, 5)
   # return
    i = 0
    while 1:
        k = i #5 * i + 4
        #w = ways(1, k)
        w = ways3(k)
       # w1 = ways(i, i)
        r = w % 1000000
        print i, k, w, r, w % 5
        if r == 0:
            break
        i += 1


def problem_102(): # solved with http://en.wikipedia.org/wiki/Barycentric_coordinate_system_(mathematics)

    def in_triangle(x1, y1, x2, y2, x3, y3, x, y):
        detT = float((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3))
        l1 = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / detT
        l2 = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / detT
        l3 = 1 - l2 - l1
        if l1 >= 1 or l1 < 0:
            return False
        if l2 >= 1 or l2 < 0:
            return False
        if l3 >= 1 or l3 < 0:
            return False
        return True

    f = open('c:/triangles.txt')
    cnt = 0
    for line in f:
        a = map(int, line.split(','))
        res = in_triangle(a[0], a[1], a[2], a[3], a[4], a[5], 0, 0)
        print res, int(res)
        cnt += int(res)
    print in_triangle(-340, 495, -153, -910, 835, -947, 0, 0)
    print in_triangle(-175, 41, -421, -714, 574, -645, 0, 0)
    print cnt

def problem_72(): # solved - 303963552391    
    t = create_totient(10 ** 6)
    print "Done"
    cnt = 0
    for d in xrange(2, 10 ** 6 + 1):
        cnt += t(d)
        print d, cnt

    print cnt


def problem_70(): # solved - 8319823

    def isperm(a, b):
        A = ''.join(sorted(map(str, str(a))))
        B = ''.join(sorted(map(str, str(b))))
        return A == B

    totient_dict = dict()
    primes = set()
    def mytotient(n):
        if n == 1:
            return 1
        if n in totient_dict:
            return totient_dict[n]
        if n in primes:
            totient_dict[n] = n - 1
            return n - 1
        if MillerRabin(n, 50):
            primes.add(n)
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
                v = totient_dict[calc_n] * totient_prod
                totient_dict[n] = v
                return v
        #  print "Crap"
        v = totient(n)
        totient_dict[n] = v
        return v

    # print isperm(87109, totient(87109))
    # print isperm(87109, mytotient(87109))
    # return    
    #   return
    # t = create_totient(10 ** 7)
    min_ratio = 10 ** 7
    min_i = 0
    for i in xrange(2, 10 ** 7):
        to = mytotient(i)        
        is_perm = isperm(i, to)
        # print "Checking ", i, to, org, org == to, is_perm, float(i) / float(to), min_ratio

        #=======================================================================
        # if to != totient(i):
        #    print "Found diff", to, totient(i)
        #    mytotient(i)
        #    break
        #=======================================================================
        #print i, to
        if is_perm:
            ratio = float(i) / float(to)
            if ratio < min_ratio:
                min_ratio = ratio
                print "Updating ", i, to, ratio
                min_i = i

    print min_i




def problem_134(): # 18613426663617118

    d = dict()
    for a in range(10, 100):
        for b in range(10, 100):
            print a, b, a * b % 100
            if a * b % 100 > 9:
                if a * b % 100 not in d:
                    d[a * b % 100] = dict()

                if not a in d[a * b % 100]:
                    d[a * b % 100][a] = set()

                d[a * b % 100][a].add(b)


    d2 = dict()
    for a in range(0, 10):
        for b in range(0, 10):
            key = a * b % 10
            if key not in d2:
                d2[key] = dict()
            if a not in d2[key]:
                d2[key][a] = dict()
            d2[key][a] = b

    for k in d:
        if k % 2 != 0:
            print k, d[k], list(d[k])[0]




    primes = gen_primes(5, 10 ** 6 + 10)[1:]

    print 'Done'
    s = 0
    for i in range(len(primes) - 1):

        p1 = primes[i]
        p2 = primes[i + 1]
        #if p1 == 3 and p2 == 5:
        #    continue
        #print "primes: ", p1, p2
        p1_str = str(p1)
        p1_len = len(p1_str)
        modulo = 10 ** p1_len

        base = delta = 1
        if p1 % 100 > 9 and p2 % 100 > 9 and p1 % 100 in d and p2 % 100 in d[p1 % 100]:
            ssss = d[p1 % 100][p2 % 100]
            if len(ssss) == 1:
                base = list(ssss)[0]
                delta = 100

        if base == 1 and delta == 1:
            delta = 10
            base = d2[p1 % 10][p2 % 10]

        iter_ = 0
        while 1:
            iter_ += 1
            candidate = p2 * base
            lastdigits = candidate % modulo
            if lastdigits == p1:
                s += candidate
                print p1, p2, '*', base, '=', candidate, 'iter=', iter_, 'sum=', s
                break
            base += delta
    print s

def problem_179(): # solved - answer: 986262

    def num_divisors(n):
        cnt = 2
        k = math.sqrt(n)
        intk = int(k)
        if k == intk:
            cnt -= 1
        for i in range(2, intk + 1):
            if n % i == 0:
                cnt += 2
        return cnt

    prev = 0
    cnt = 0
    for i in xrange(2, 10 ** 7):
        n = num_divisors(i)
        print i, n
        if n == prev:
            cnt += 1
            print i, n, cnt
        prev = n

def problem_94(): # solved

#===============================================================================
#    1 1 2 4 1 - Not valid because it's area is 0
# 5 5 6 16 5.0
# 17 17 16 50 3.4
# 65 65 66 196 3.82352941176
# 241 241 240 722 3.70769230769
# 901 901 902 2704 3.73858921162
# 3361 3361 3360 10082 3.73029966704
# 12545 12545 12546 37636 3.73252008331
# 46817 46817 46816 140450 3.73192506975
# 174725 174725 174726 524176 3.73208449922
# 652081 652081 652080 1956242 3.73204177994
# 2433601 2433601 2433602 7300804 3.73205322652
# 9082321 9082321 9082320 27246962 3.73205015941
# 33895685 33895685 33895686 101687056 3.73205098124
# 126500417 126500417 126500416 379501250 3.73205076103
# 518408350 - 4 (drop the first result)
#===============================================================================    

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

    def is_int_area(a, b, c):
        s = (a + b + c) / 2
        res = s * (s - a) * (s - b) * (s - c)

        isqrt_res = isqrt(res)
        return isqrt_res ** 2 == res

    p_sum = 0    
    prev = 1
    i = 1
    while i <= 3333333333:
        p = 3 * i - 1
        if is_int_area(i, i, i - 1):
            print i, i, i - 1, p, i / prev
            prev = float(i)
            i = int(float(i) * 3)
            if i % 2 == 0:
                i += 1
            p_sum += p
        p += 2
        if is_int_area(i, i, i + 1):
            print i, i, i + 1, p, i / prev
            prev = float(i)
            i = int(float(i) * 3)
            if i % 2 == 0:
                i += 1
            p_sum += p
        i += 2

    print p_sum


def problem_82(): # solved 260324

    l1 = [131, 673, 234, 103, 18, 201, 96, 342, 965, 150, 630, 803, 746, 422, 111, 537, 699, 497, 121, 956, 805, 732, 524, 37, 331]
    l = [4445, 2697, 5115, 718, 2209, 2212, 654, 4348, 3079, 6821, 7668, 3276, 8874, 4190, 3785, 2752, 9473, 7817, 9137, 496, 7338, 3434, 7152, 4355, 4552, 7917, 7827, 2460, 2350, 691, 3514, 5880, 3145, 7633, 7199, 3783, 5066, 7487, 3285, 1084, 8985, 760, 872, 8609, 8051, 1134, 9536, 5750, 9716, 9371, 7619, 5617, 275, 9721, 2997, 2698, 1887, 8825, 6372, 3014, 2113, 7122, 7050, 6775, 5948, 2758, 1219, 3539, 348, 7989, 2735, 9862, 1263, 8089, 6401, 9462, 3168, 2758, 3748,
         5870, 1096, 20, 1318, 7586, 5167, 2642, 1443, 5741, 7621, 7030, 5526, 4244, 2348, 4641, 9827, 2448, 6918, 5883, 3737, 300, 7116, 6531, 567, 5997, 3971, 6623, 820, 6148, 3287, 1874, 7981, 8424, 7672, 7575, 6797, 6717, 1078, 5008, 4051, 8795, 5820, 346, 1851, 6463, 2117, 6058, 3407, 8211, 117, 4822, 1317, 4377, 4434, 5925, 8341, 4800, 1175, 4173, 690, 8978, 7470, 1295, 3799, 8724, 3509, 9849, 618, 3320, 7068, 9633, 2384, 7175, 544, 6583, 1908, 9983, 481, 4187, 9353, 9377,
9607, 7385, 521, 6084, 1364, 8983, 7623, 1585, 6935, 8551, 2574, 8267, 4781, 3834, 2764, 2084, 2669, 4656, 9343, 7709, 2203, 9328, 8004, 6192, 5856, 3555, 2260, 5118, 6504, 1839, 9227, 1259, 9451, 1388, 7909, 5733, 6968, 8519, 9973, 1663, 5315, 7571, 3035, 4325, 4283, 2304, 6438, 3815, 9213, 9806, 9536, 196, 5542, 6907, 2475, 1159, 5820, 9075, 9470, 2179, 9248, 1828, 4592, 9167, 3713, 4640, 47, 3637, 309, 7344, 6955, 346, 378, 9044, 8635, 7466, 5036, 9515, 6385, 9230,
7206, 3114, 7760, 1094, 6150, 5182, 7358, 7387, 4497, 955, 101, 1478, 7777, 6966, 7010, 8417, 6453, 4955, 3496, 107, 449, 8271, 131, 2948, 6185, 784, 5937, 8001, 6104, 8282, 4165, 3642, 710, 2390, 575, 715, 3089, 6964, 4217, 192, 5949, 7006, 715, 3328, 1152, 66, 8044, 4319, 1735, 146, 4818, 5456, 6451, 4113, 1063, 4781, 6799, 602, 1504, 6245, 6550, 1417, 1343, 2363, 3785, 5448, 4545, 9371, 5420, 5068, 4613, 4882, 4241, 5043, 7873, 8042, 8434, 3939, 9256, 2187,
3620, 8024, 577, 9997, 7377, 7682, 1314, 1158, 6282, 6310, 1896, 2509, 5436, 1732, 9480, 706, 496, 101, 6232, 7375, 2207, 2306, 110, 6772, 3433, 2878, 8140, 5933, 8688, 1399, 2210, 7332, 6172, 6403, 7333, 4044, 2291, 1790, 2446, 7390, 8698, 5723, 3678, 7104, 1825, 2040, 140, 3982, 4905, 4160, 2200, 5041, 2512, 1488, 2268, 1175, 7588, 8321, 8078, 7312, 977, 5257, 8465, 5068, 3453, 3096, 1651, 7906, 253, 9250, 6021, 8791, 8109, 6651, 3412, 345, 4778, 5152, 4883, 7505,
1074, 5438, 9008, 2679, 5397, 5429, 2652, 3403, 770, 9188, 4248, 2493, 4361, 8327, 9587, 707, 9525, 5913, 93, 1899, 328, 2876, 3604, 673, 8576, 6908, 7659, 2544, 3359, 3883, 5273, 6587, 3065, 1749, 3223, 604, 9925, 6941, 2823, 8767, 7039, 3290, 3214, 1787, 7904, 3421, 7137, 9560, 8451, 2669, 9219, 6332, 1576, 5477, 6755, 8348, 4164, 4307, 2984, 4012, 6629, 1044, 2874, 6541, 4942, 903, 1404, 9125, 5160, 8836, 4345, 2581, 460, 8438, 1538, 5507, 668, 3352, 2678, 6942,
4295, 1176, 5596, 1521, 3061, 9868, 7037, 7129, 8933, 6659, 5947, 5063, 3653, 9447, 9245, 2679, 767, 714, 116, 8558, 163, 3927, 8779, 158, 5093, 2447, 5782, 3967, 1716, 931, 7772, 8164, 1117, 9244, 5783, 7776, 3846, 8862, 6014, 2330, 6947, 1777, 3112, 6008, 3491, 1906, 5952, 314, 4602, 8994, 5919, 9214, 3995, 5026, 7688, 6809, 5003, 3128, 2509, 7477, 110, 8971, 3982, 8539, 2980, 4689, 6343, 5411, 2992, 5270, 5247, 9260, 2269, 7474, 1042, 7162, 5206, 1232, 4556, 4757,
510, 3556, 5377, 1406, 5721, 4946, 2635, 7847, 4251, 8293, 8281, 6351, 4912, 287, 2870, 3380, 3948, 5322, 3840, 4738, 9563, 1906, 6298, 3234, 8959, 1562, 6297, 8835, 7861, 239, 6618, 1322, 2553, 2213, 5053, 5446, 4402, 6500, 5182, 8585, 6900, 5756, 9661, 903, 5186, 7687, 5998, 7997, 8081, 8955, 4835, 6069, 2621, 1581, 732, 9564, 1082, 1853, 5442, 1342, 520, 1737, 3703, 5321, 4793, 2776, 1508, 1647, 9101, 2499, 6891, 4336, 7012, 3329, 3212, 1442, 9993, 3988, 4930, 7706,
9444, 3401, 5891, 9716, 1228, 7107, 109, 3563, 2700, 6161, 5039, 4992, 2242, 8541, 7372, 2067, 1294, 3058, 1306, 320, 8881, 5756, 9326, 411, 8650, 8824, 5495, 8282, 8397, 2000, 1228, 7817, 2099, 6473, 3571, 5994, 4447, 1299, 5991, 543, 7874, 2297, 1651, 101, 2093, 3463, 9189, 6872, 6118, 872, 1008, 1779, 2805, 9084, 4048, 2123, 5877, 55, 3075, 1737, 9459, 4535, 6453, 3644, 108, 5982, 4437, 5213, 1340, 6967, 9943, 5815, 669, 8074, 1838, 6979, 9132, 9315, 715, 5048,
3327, 4030, 7177, 6336, 9933, 5296, 2621, 4785, 2755, 4832, 2512, 2118, 2244, 4407, 2170, 499, 7532, 9742, 5051, 7687, 970, 6924, 3527, 4694, 5145, 1306, 2165, 5940, 2425, 8910, 3513, 1909, 6983, 346, 6377, 4304, 9330, 7203, 6605, 3709, 3346, 970, 369, 9737, 5811, 4427, 9939, 3693, 8436, 5566, 1977, 3728, 2399, 3985, 8303, 2492, 5366, 9802, 9193, 7296, 1033, 5060, 9144, 2766, 1151, 7629, 5169, 5995, 58, 7619, 7565, 4208, 1713, 6279, 3209, 4908, 9224, 7409, 1325, 8540,
6882, 1265, 1775, 3648, 4690, 959, 5837, 4520, 5394, 1378, 9485, 1360, 4018, 578, 9174, 2932, 9890, 3696, 116, 1723, 1178, 9355, 7063, 1594, 1918, 8574, 7594, 7942, 1547, 6166, 7888, 354, 6932, 4651, 1010, 7759, 6905, 661, 7689, 6092, 9292, 3845, 9605, 8443, 443, 8275, 5163, 7720, 7265, 6356, 7779, 1798, 1754, 5225, 6661, 1180, 8024, 5666, 88, 9153, 1840, 3508, 1193, 4445, 2648, 3538, 6243, 6375, 8107, 5902, 5423, 2520, 1122, 5015, 6113, 8859, 9370, 966, 8673, 2442,
7338, 3423, 4723, 6533, 848, 8041, 7921, 8277, 4094, 5368, 7252, 8852, 9166, 2250, 2801, 6125, 8093, 5738, 4038, 9808, 7359, 9494, 601, 9116, 4946, 2702, 5573, 2921, 9862, 1462, 1269, 2410, 4171, 2709, 7508, 6241, 7522, 615, 2407, 8200, 4189, 5492, 5649, 7353, 2590, 5203, 4274, 710, 7329, 9063, 956, 8371, 3722, 4253, 4785, 1194, 4828, 4717, 4548, 940, 983, 2575, 4511, 2938, 1827, 2027, 2700, 1236, 841, 5760, 1680, 6260, 2373, 3851, 1841, 4968, 1172, 5179, 7175, 3509,
4420, 1327, 3560, 2376, 6260, 2988, 9537, 4064, 4829, 8872, 9598, 3228, 1792, 7118, 9962, 9336, 4368, 9189, 6857, 1829, 9863, 6287, 7303, 7769, 2707, 8257, 2391, 2009, 3975, 4993, 3068, 9835, 3427, 341, 8412, 2134, 4034, 8511, 6421, 3041, 9012, 2983, 7289, 100, 1355, 7904, 9186, 6920, 5856, 2008, 6545, 8331, 3655, 5011, 839, 8041, 9255, 6524, 3862, 8788, 62, 7455, 3513, 5003, 8413, 3918, 2076, 7960, 6108, 3638, 6999, 3436, 1441, 4858, 4181, 1866, 8731, 7745, 3744, 1000,
356, 8296, 8325, 1058, 1277, 4743, 3850, 2388, 6079, 6462, 2815, 5620, 8495, 5378, 75, 4324, 3441, 9870, 1113, 165, 1544, 1179, 2834, 562, 6176, 2313, 6836, 8839, 2986, 9454, 5199, 6888, 1927, 5866, 8760, 320, 1792, 8296, 7898, 6121, 7241, 5886, 5814, 2815, 8336, 1576, 4314, 3109, 2572, 6011, 2086, 9061, 9403, 3947, 5487, 9731, 7281, 3159, 1819, 1334, 3181, 5844, 5114, 9898, 4634, 2531, 4412, 6430, 4262, 8482, 4546, 4555, 6804, 2607, 9421, 686, 8649, 8860, 7794, 6672,
9870, 152, 1558, 4963, 8750, 4754, 6521, 6256, 8818, 5208, 5691, 9659, 8377, 9725, 5050, 5343, 2539, 6101, 1844, 9700, 7750, 8114, 5357, 3001, 8830, 4438, 199, 9545, 8496, 43, 2078, 327, 9397, 106, 6090, 8181, 8646, 6414, 7499, 5450, 4850, 6273, 5014, 4131, 7639, 3913, 6571, 8534, 9703, 4391, 7618, 445, 1320, 5, 1894, 6771, 7383, 9191, 4708, 9706, 6939, 7937, 8726, 9382, 5216, 3685, 2247, 9029, 8154, 1738, 9984, 2626, 9438, 4167, 6351, 5060, 29, 1218, 1239, 4785,
192, 5213, 8297, 8974, 4032, 6966, 5717, 1179, 6523, 4679, 9513, 1481, 3041, 5355, 9303, 9154, 1389, 8702, 6589, 7818, 6336, 3539, 5538, 3094, 6646, 6702, 6266, 2759, 4608, 4452, 617, 9406, 8064, 6379, 444, 5602, 4950, 1810, 8391, 1536, 316, 8714, 1178, 5182, 5863, 5110, 5372, 4954, 1978, 2971, 5680, 4863, 2255, 4630, 5723, 2168, 538, 1692, 1319, 7540, 440, 6430, 6266, 7712, 7385, 5702, 620, 641, 3136, 7350, 1478, 3155, 2820, 9109, 6261, 1122, 4470, 14, 8493, 2095,
1046, 4301, 6082, 474, 4974, 7822, 2102, 5161, 5172, 6946, 8074, 9716, 6586, 9962, 9749, 5015, 2217, 995, 5388, 4402, 7652, 6399, 6539, 1349, 8101, 3677, 1328, 9612, 7922, 2879, 231, 5887, 2655, 508, 4357, 4964, 3554, 5930, 6236, 7384, 4614, 280, 3093, 9600, 2110, 7863, 2631, 6626, 6620, 68, 1311, 7198, 7561, 1768, 5139, 1431, 221, 230, 2940, 968, 5283, 6517, 2146, 1646, 869, 9402, 7068, 8645, 7058, 1765, 9690, 4152, 2926, 9504, 2939, 7504, 6074, 2944, 6470, 7859,
4659, 736, 4951, 9344, 1927, 6271, 8837, 8711, 3241, 6579, 7660, 5499, 5616, 3743, 5801, 4682, 9748, 8796, 779, 1833, 4549, 8138, 4026, 775, 4170, 2432, 4174, 3741, 7540, 8017, 2833, 4027, 396, 811, 2871, 1150, 9809, 2719, 9199, 8504, 1224, 540, 2051, 3519, 7982, 7367, 2761, 308, 3358, 6505, 2050, 4836, 5090, 7864, 805, 2566, 2409, 6876, 3361, 8622, 5572, 5895, 3280, 441, 7893, 8105, 1634, 2929, 274, 3926, 7786, 6123, 8233, 9921, 2674, 5340, 1445, 203, 4585, 3837,
5759, 338, 7444, 7968, 7742, 3755, 1591, 4839, 1705, 650, 7061, 2461, 9230, 9391, 9373, 2413, 1213, 431, 7801, 4994, 2380, 2703, 6161, 6878, 8331, 2538, 6093, 1275, 5065, 5062, 2839, 582, 1014, 8109, 3525, 1544, 1569, 8622, 7944, 2905, 6120, 1564, 1839, 5570, 7579, 1318, 2677, 5257, 4418, 5601, 7935, 7656, 5192, 1864, 5886, 6083, 5580, 6202, 8869, 1636, 7907, 4759, 9082, 5854, 3185, 7631, 6854, 5872, 5632, 5280, 1431, 2077, 9717, 7431, 4256, 8261, 9680, 4487, 4752, 4286,
1571, 1428, 8599, 1230, 7772, 4221, 8523, 9049, 4042, 8726, 7567, 6736, 9033, 2104, 4879, 4967, 6334, 6716, 3994, 1269, 8995, 6539, 3610, 7667, 6560, 6065, 874, 848, 4597, 1711, 7161, 4811, 6734, 5723, 6356, 6026, 9183, 2586, 5636, 1092, 7779, 7923, 8747, 6887, 7505, 9909, 1792, 3233, 4526, 3176, 1508, 8043, 720, 5212, 6046, 4988, 709, 5277, 8256, 3642, 1391, 5803, 1468, 2145, 3970, 6301, 7767, 2359, 8487, 9771, 8785, 7520, 856, 1605, 8972, 2402, 2386, 991, 1383, 5963,
1822, 4824, 5957, 6511, 9868, 4113, 301, 9353, 6228, 2881, 2966, 6956, 9124, 9574, 9233, 1601, 7340, 973, 9396, 540, 4747, 8590, 9535, 3650, 7333, 7583, 4806, 3593, 2738, 8157, 5215, 8472, 2284, 9473, 3906, 6982, 5505, 6053, 7936, 6074, 7179, 6688, 1564, 1103, 6860, 5839, 2022, 8490, 910, 7551, 7805, 881, 7024, 1855, 9448, 4790, 1274, 3672, 2810, 774, 7623, 4223, 4850, 6071, 9975, 4935, 1915, 9771, 6690, 3846, 517, 463, 7624, 4511, 614, 6394, 3661, 7409, 1395, 8127,
8738, 3850, 9555, 3695, 4383, 2378, 87, 6256, 6740, 7682, 9546, 4255, 6105, 2000, 1851, 4073, 8957, 9022, 6547, 5189, 2487, 303, 9602, 7833, 1628, 4163, 6678, 3144, 8589, 7096, 8913, 5823, 4890, 7679, 1212, 9294, 5884, 2972, 3012, 3359, 7794, 7428, 1579, 4350, 7246, 4301, 7779, 7790, 3294, 9547, 4367, 3549, 1958, 8237, 6758, 3497, 3250, 3456, 6318, 1663, 708, 7714, 6143, 6890, 3428, 6853, 9334, 7992, 591, 6449, 9786, 1412, 8500, 722, 5468, 1371, 108, 3939, 4199, 2535,
7047, 4323, 1934, 5163, 4166, 461, 3544, 2767, 6554, 203, 6098, 2265, 9078, 2075, 4644, 6641, 8412, 9183, 487, 101, 7566, 5622, 1975, 5726, 2920, 5374, 7779, 5631, 3753, 3725, 2672, 3621, 4280, 1162, 5812, 345, 8173, 9785, 1525, 955, 5603, 2215, 2580, 5261, 2765, 2990, 5979, 389, 3907, 2484, 1232, 5933, 5871, 3304, 1138, 1616, 5114, 9199, 5072, 7442, 7245, 6472, 4760, 6359, 9053, 7876, 2564, 9404, 3043, 9026, 2261, 3374, 4460, 7306, 2326, 966, 828, 3274, 1712, 3446,
3975, 4565, 8131, 5800, 4570, 2306, 8838, 4392, 9147, 11, 3911, 7118, 9645, 4994, 2028, 6062, 5431, 2279, 8752, 2658, 7836, 994, 7316, 5336, 7185, 3289, 1898, 9689, 2331, 5737, 3403, 1124, 2679, 3241, 7748, 16, 2724, 5441, 6640, 9368, 9081, 5618, 858, 4969, 17, 2103, 6035, 8043, 7475, 2181, 939, 415, 1617, 8500, 8253, 2155, 7843, 7974, 7859, 1746, 6336, 3193, 2617, 8736, 4079, 6324, 6645, 8891, 9396, 5522, 6103, 1857, 8979, 3835, 2475, 1310, 7422, 610, 8345, 7615,
9248, 5397, 5686, 2988, 3446, 4359, 6634, 9141, 497, 9176, 6773, 7448, 1907, 8454, 916, 1596, 2241, 1626, 1384, 2741, 3649, 5362, 8791, 7170, 2903, 2475, 5325, 6451, 924, 3328, 522, 90, 4813, 9737, 9557, 691, 2388, 1383, 4021, 1609, 9206, 4707, 5200, 7107, 8104, 4333, 9860, 5013, 1224, 6959, 8527, 1877, 4545, 7772, 6268, 621, 4915, 9349, 5970, 706, 9583, 3071, 4127, 780, 8231, 3017, 9114, 3836, 7503, 2383, 1977, 4870, 8035, 2379, 9704, 1037, 3992, 3642, 1016, 4303,
5093, 138, 4639, 6609, 1146, 5565, 95, 7521, 9077, 2272, 974, 4388, 2465, 2650, 722, 4998, 3567, 3047, 921, 2736, 7855, 173, 2065, 4238, 1048, 5, 6847, 9548, 8632, 9194, 5942, 4777, 7910, 8971, 6279, 7253, 2516, 1555, 1833, 3184, 9453, 9053, 6897, 7808, 8629, 4877, 1871, 8055, 4881, 7639, 1537, 7701, 2508, 7564, 5845, 5023, 2304, 5396, 3193, 2955, 1088, 3801, 6203, 1748, 3737, 1276, 13, 4120, 7715, 8552, 3047, 2921, 106, 7508, 304, 1280, 7140, 2567, 9135, 5266,
6237, 4607, 7527, 9047, 522, 7371, 4883, 2540, 5867, 6366, 5301, 1570, 421, 276, 3361, 527, 6637, 4861, 2401, 7522, 5808, 9371, 5298, 2045, 5096, 5447, 7755, 5115, 7060, 8529, 4078, 1943, 1697, 1764, 5453, 7085, 960, 2405, 739, 2100, 5800, 728, 9737, 5704, 5693, 1431, 8979, 6428, 673, 7540, 6, 7773, 5857, 6823, 150, 5869, 8486, 684, 5816, 9626, 7451, 5579, 8260, 3397, 5322, 6920, 1879, 2127, 2884, 5478, 4977, 9016, 6165, 6292, 3062, 5671, 5968, 78, 4619, 4763,
9905, 7127, 9390, 5185, 6923, 3721, 9164, 9705, 4341, 1031, 1046, 5127, 7376, 6528, 3248, 4941, 1178, 7889, 3364, 4486, 5358, 9402, 9158, 8600, 1025, 874, 1839, 1783, 309, 9030, 1843, 845, 8398, 1433, 7118, 70, 8071, 2877, 3904, 8866, 6722, 4299, 10, 1929, 5897, 4188, 600, 1889, 3325, 2485, 6473, 4474, 7444, 6992, 4846, 6166, 4441, 2283, 2629, 4352, 7775, 1101, 2214, 9985, 215, 8270, 9750, 2740, 8361, 7103, 5930, 8664, 9690, 8302, 9267, 344, 2077, 1372, 1880, 9550,
5825, 8517, 7769, 2405, 8204, 1060, 3603, 7025, 478, 8334, 1997, 3692, 7433, 9101, 7294, 7498, 9415, 5452, 3850, 3508, 6857, 9213, 6807, 4412, 7310, 854, 5384, 686, 4978, 892, 8651, 3241, 2743, 3801, 3813, 8588, 6701, 4416, 6990, 6490, 3197, 6838, 6503, 114, 8343, 5844, 8646, 8694, 65, 791, 5979, 2687, 2621, 2019, 8097, 1423, 3644, 9764, 4921, 3266, 3662, 5561, 2476, 8271, 8138, 6147, 1168, 3340, 1998, 9874, 6572, 9873, 6659, 5609, 2711, 3931, 9567, 4143, 7833, 8887,
6223, 2099, 2700, 589, 4716, 8333, 1362, 5007, 2753, 2848, 4441, 8397, 7192, 8191, 4916, 9955, 6076, 3370, 6396, 6971, 3156, 248, 3911, 2488, 4930, 2458, 7183, 5455, 170, 6809, 6417, 3390, 1956, 7188, 577, 7526, 2203, 968, 8164, 479, 8699, 7915, 507, 6393, 4632, 1597, 7534, 3604, 618, 3280, 6061, 9793, 9238, 8347, 568, 9645, 2070, 5198, 6482, 5000, 9212, 6655, 5961, 7513, 1323, 3872, 6170, 3812, 4146, 2736, 67, 3151, 5548, 2781, 9679, 7564, 5043, 8587, 1893, 4531,
5826, 3690, 6724, 2121, 9308, 6986, 8106, 6659, 2142, 1642, 7170, 2877, 5757, 6494, 8026, 6571, 8387, 9961, 6043, 9758, 9607, 6450, 8631, 8334, 7359, 5256, 8523, 2225, 7487, 1977, 9555, 8048, 5763, 2414, 4948, 4265, 2427, 8978, 8088, 8841, 9208, 9601, 5810, 9398, 8866, 9138, 4176, 5875, 7212, 3272, 6759, 5678, 7649, 4922, 5422, 1343, 8197, 3154, 3600, 687, 1028, 4579, 2084, 9467, 4492, 7262, 7296, 6538, 7657, 7134, 2077, 1505, 7332, 6890, 8964, 4879, 7603, 7400, 5973, 739,
1861, 1613, 4879, 1884, 7334, 966, 2000, 7489, 2123, 4287, 1472, 3263, 4726, 9203, 1040, 4103, 6075, 6049, 330, 9253, 4062, 4268, 1635, 9960, 577, 1320, 3195, 9628, 1030, 4092, 4979, 6474, 6393, 2799, 6967, 8687, 7724, 7392, 9927, 2085, 3200, 6466, 8702, 265, 7646, 8665, 7986, 7266, 4574, 6587, 612, 2724, 704, 3191, 8323, 9523, 3002, 704, 5064, 3960, 8209, 2027, 2758, 8393, 4875, 4641, 9584, 6401, 7883, 7014, 768, 443, 5490, 7506, 1852, 2005, 8850, 5776, 4487, 4269,
4052, 6687, 4705, 7260, 6645, 6715, 3706, 5504, 8672, 2853, 1136, 8187, 8203, 4016, 871, 1809, 1366, 4952, 9294, 5339, 6872, 2645, 6083, 7874, 3056, 5218, 7485, 8796, 7401, 3348, 2103, 426, 8572, 4163, 9171, 3176, 948, 7654, 9344, 3217, 1650, 5580, 7971, 2622, 76, 2874, 880, 2034, 9929, 1546, 2659, 5811, 3754, 7096, 7436, 9694, 9960, 7415, 2164, 953, 2360, 4194, 2397, 1047, 2196, 6827, 575, 784, 2675, 8821, 6802, 7972, 5996, 6699, 2134, 7577, 2887, 1412, 4349, 4380,
4629, 2234, 6240, 8132, 7592, 3181, 6389, 1214, 266, 1910, 2451, 8784, 2790, 1127, 6932, 1447, 8986, 2492, 5476, 397, 889, 3027, 7641, 5083, 5776, 4022, 185, 3364, 5701, 2442, 2840, 4160, 9525, 4828, 6602, 2614, 7447, 3711, 4505, 7745, 8034, 6514, 4907, 2605, 7753, 6958, 7270, 6936, 3006, 8968, 439, 2326, 4652, 3085, 3425, 9863, 5049, 5361, 8688, 297, 7580, 8777, 7916, 6687, 8683, 7141, 306, 9569, 2384, 1500, 3346, 4601, 7329, 9040, 6097, 2727, 6314, 4501, 4974, 2829,
8316, 4072, 2025, 6884, 3027, 1808, 5714, 7624, 7880, 8528, 4205, 8686, 7587, 3230, 1139, 7273, 6163, 6986, 3914, 9309, 1464, 9359, 4474, 7095, 2212, 7302, 2583, 9462, 7532, 6567, 1606, 4436, 8981, 5612, 6796, 4385, 5076, 2007, 6072, 3678, 8331, 1338, 3299, 8845, 4783, 8613, 4071, 1232, 6028, 2176, 3990, 2148, 3748, 103, 9453, 538, 6745, 9110, 926, 3125, 473, 5970, 8728, 7072, 9062, 1404, 1317, 5139, 9862, 6496, 6062, 3338, 464, 1600, 2532, 1088, 8232, 7739, 8274, 3873,
2341, 523, 7096, 8397, 8301, 6541, 9844, 244, 4993, 2280, 7689, 4025, 4196, 5522, 7904, 6048, 2623, 9258, 2149, 9461, 6448, 8087, 7245, 1917, 8340, 7127, 8466, 5725, 6996, 3421, 5313, 512, 9164, 9837, 9794, 8369, 4185, 1488, 7210, 1524, 1016, 4620, 9435, 2478, 7765, 8035, 697, 6677, 3724, 6988, 5853, 7662, 3895, 9593, 1185, 4727, 6025, 5734, 7665, 3070, 138, 8469, 6748, 6459, 561, 7935, 8646, 2378, 462, 7755, 3115, 9690, 8877, 3946, 2728, 8793, 244, 6323, 8666, 4271,
6430, 2406, 8994, 56, 1267, 3826, 9443, 7079, 7579, 5232, 6691, 3435, 6718, 5698, 4144, 7028, 592, 2627, 217, 734, 6194, 8156, 9118, 58, 2640, 8069, 4127, 3285, 694, 3197, 3377, 4143, 4802, 3324, 8134, 6953, 7625, 3598, 3584, 4289, 7065, 3434, 2106, 7132, 5802, 7920, 9060, 7531, 3321, 1725, 1067, 3751, 444, 5503, 6785, 7937, 6365, 4803, 198, 6266, 8177, 1470, 6390, 1606, 2904, 7555, 9834, 8667, 2033, 1723, 5167, 1666, 8546, 8152, 473, 4475, 6451, 7947, 3062, 3281,
2810, 3042, 7759, 1741, 2275, 2609, 7676, 8640, 4117, 1958, 7500, 8048, 1757, 3954, 9270, 1971, 4796, 2912, 660, 5511, 3553, 1012, 5757, 4525, 6084, 7198, 8352, 5775, 7726, 8591, 7710, 9589, 3122, 4392, 6856, 5016, 749, 2285, 3356, 7482, 9956, 7348, 2599, 8944, 495, 3462, 3578, 551, 4543, 7207, 7169, 7796, 1247, 4278, 6916, 8176, 3742, 8385, 2310, 1345, 8692, 2667, 4568, 1770, 8319, 3585, 4920, 3890, 4928, 7343, 5385, 9772, 7947, 8786, 2056, 9266, 3454, 2807, 877, 2660,
6206, 8252, 5928, 5837, 4177, 4333, 207, 7934, 5581, 9526, 8906, 1498, 8411, 2984, 5198, 5134, 2464, 8435, 8514, 8674, 3876, 599, 5327, 826, 2152, 4084, 2433, 9327, 9697, 4800, 2728, 3608, 3849, 3861, 3498, 9943, 1407, 3991, 7191, 9110, 5666, 8434, 4704, 6545, 5944, 2357, 1163, 4995, 9619, 6754, 4200, 9682, 6654, 4862, 4744, 5953, 6632, 1054, 293, 9439, 8286, 2255, 696, 8709, 1533, 1844, 6441, 430, 1999, 6063, 9431, 7018, 8057, 2920, 6266, 6799, 356, 3597, 4024, 6665,
3847, 6356, 8541, 7225, 2325, 2946, 5199, 469, 5450, 7508, 2197, 9915, 8284, 7983, 6341, 3276, 3321, 16, 1321, 7608, 5015, 3362, 8491, 6968, 6818, 797, 156, 2575, 706, 9516, 5344, 5457, 9210, 5051, 8099, 1617, 9951, 7663, 8253, 9683, 2670, 1261, 4710, 1068, 8753, 4799, 1228, 2621, 3275, 6188, 4699, 1791, 9518, 8701, 5932, 4275, 6011, 9877, 2933, 4182, 6059, 2930, 6687, 6682, 9771, 654, 9437, 3169, 8596, 1827, 5471, 8909, 2352, 123, 4394, 3208, 8756, 5513, 6917, 2056,
5458, 8173, 3138, 3290, 4570, 4892, 3317, 4251, 9699, 7973, 1163, 1935, 5477, 6648, 9614, 5655, 9592, 975, 9118, 2194, 7322, 8248, 8413, 3462, 8560, 1907, 7810, 6650, 7355, 2939, 4973, 6894, 3933, 3784, 3200, 2419, 9234, 4747, 2208, 2207, 1945, 2899, 1407, 6145, 8023, 3484, 5688, 7686, 2737, 3828, 3704, 9004, 5190, 9740, 8643, 8650, 5358, 4426, 1522, 1707, 3613, 9887, 6956, 2447, 2762, 833, 1449, 9489, 2573, 1080, 4167, 3456, 6809, 2466, 227, 7125, 2759, 6250, 6472, 8089,
3266, 7025, 9756, 3914, 1265, 9116, 7723, 9788, 6805, 5493, 2092, 8688, 6592, 9173, 4431, 4028, 6007, 7131, 4446, 4815, 3648, 6701, 759, 3312, 8355, 4485, 4187, 5188, 8746, 7759, 3528, 2177, 5243, 8379, 3838, 7233, 4607, 9187, 7216, 2190, 6967, 2920, 6082, 7910, 5354, 3609, 8958, 6949, 7731, 494, 8753, 8707, 1523, 4426, 3543, 7085, 647, 6771, 9847, 646, 5049, 824, 8417, 5260, 2730, 5702, 2513, 9275, 4279, 2767, 8684, 1165, 9903, 4518, 55, 9682, 8963, 6005, 2102, 6523,
1998, 8731, 936, 1479, 5259, 7064, 4085, 91, 7745, 7136, 3773, 3810, 730, 8255, 2705, 2653, 9790, 6807, 2342, 355, 9344, 2668, 3690, 2028, 9679, 8102, 574, 4318, 6481, 9175, 5423, 8062, 2867, 9657, 7553, 3442, 3920, 7430, 3945, 7639, 3714, 3392, 2525, 4995, 4850, 2867, 7951, 9667, 486, 9506, 9888, 781, 8866, 1702, 3795, 90, 356, 1483, 4200, 2131, 6969, 5931, 486, 6880, 4404, 1084, 5169, 4910, 6567, 8335, 4686, 5043, 2614, 3352, 2667, 4513, 6472, 7471, 5720, 1616,
8878, 1613, 1716, 868, 1906, 2681, 564, 665, 5995, 2474, 7496, 3432, 9491, 9087, 8850, 8287, 669, 823, 347, 6194, 2264, 2592, 7871, 7616, 8508, 4827, 760, 2676, 4660, 4881, 7572, 3811, 9032, 939, 4384, 929, 7525, 8419, 5556, 9063, 662, 8887, 7026, 8534, 3111, 1454, 2082, 7598, 5726, 6687, 9647, 7608, 73, 3014, 5063, 670, 5461, 5631, 3367, 9796, 8475, 7908, 5073, 1565, 5008, 5295, 4457, 1274, 4788, 1728, 338, 600, 8415, 8535, 9351, 7750, 6887, 5845, 1741, 125,
3637, 6489, 9634, 9464, 9055, 2413, 7824, 9517, 7532, 3577, 7050, 6186, 6980, 9365, 9782, 191, 870, 2497, 8498, 2218, 2757, 5420, 6468, 586, 3320, 9230, 1034, 1393, 9886, 5072, 9391, 1178, 8464, 8042, 6869, 2075, 8275, 3601, 7715, 9470, 8786, 6475, 8373, 2159, 9237, 2066, 3264, 5000, 679, 355, 3069, 4073, 494, 2308, 5512, 4334, 9438, 8786, 8637, 9774, 1169, 1949, 6594, 6072, 4270, 9158, 7916, 5752, 6794, 9391, 6301, 5842, 3285, 2141, 3898, 8027, 4310, 8821, 7079, 1307,
8497, 6681, 4732, 7151, 7060, 5204, 9030, 7157, 833, 5014, 8723, 3207, 9796, 9286, 4913, 119, 5118, 7650, 9335, 809, 3675, 2597, 5144, 3945, 5090, 8384, 187, 4102, 1260, 2445, 2792, 4422, 8389, 9290, 50, 1765, 1521, 6921, 8586, 4368, 1565, 5727, 7855, 2003, 4834, 9897, 5911, 8630, 5070, 1330, 7692, 7557, 7980, 6028, 5805, 9090, 8265, 3019, 3802, 698, 9149, 5748, 1965, 9658, 4417, 5994, 5584, 8226, 2937, 272, 5743, 1278, 5698, 8736, 2595, 6475, 5342, 6596, 1149, 6920,
8188, 8009, 9546, 6310, 8772, 2500, 9846, 6592, 6872, 3857, 1307, 8125, 7042, 1544, 6159, 2330, 643, 4604, 7899, 6848, 371, 8067, 2062, 3200, 7295, 1857, 9505, 6936, 384, 2193, 2190, 301, 8535, 5503, 1462, 7380, 5114, 4824, 8833, 1763, 4974, 8711, 9262, 6698, 3999, 2645, 6937, 7747, 1128, 2933, 3556, 7943, 2885, 3122, 9105, 5447, 418, 2899, 5148, 3699, 9021, 9501, 597, 4084, 175, 1621, 1, 1079, 6067, 5812, 4326, 9914, 6633, 5394, 4233, 6728, 9084, 1864, 5863, 1225,
9935, 8793, 9117, 1825, 9542, 8246, 8437, 3331, 9128, 9675, 6086, 7075, 319, 1334, 7932, 3583, 7167, 4178, 1726, 7720, 695, 8277, 7887, 6359, 5912, 1719, 2780, 8529, 1359, 2013, 4498, 8072, 1129, 9998, 1147, 8804, 9405, 6255, 1619, 2165, 7491, 1, 8882, 7378, 3337, 503, 5758, 4109, 3577, 985, 3200, 7615, 8058, 5032, 1080, 6410, 6873, 5496, 1466, 2412, 9885, 5904, 4406, 3605, 8770, 4361, 6205, 9193, 1537, 9959, 214, 7260, 9566, 1685, 100, 4920, 7138, 9819, 5637, 976,
3466, 9854, 985, 1078, 7222, 8888, 5466, 5379, 3578, 4540, 6853, 8690, 3728, 6351, 7147, 3134, 6921, 9692, 857, 3307, 4998, 2172, 5783, 3931, 9417, 2541, 6299, 13, 787, 2099, 9131, 9494, 896, 8600, 1643, 8419, 7248, 2660, 2609, 8579, 91, 6663, 5506, 7675, 1947, 6165, 4286, 1972, 9645, 3805, 1663, 1456, 8853, 5705, 9889, 7489, 1107, 383, 4044, 2969, 3343, 152, 7805, 4980, 9929, 5033, 1737, 9953, 7197, 9158, 4071, 1324, 473, 9676, 3984, 9680, 3606, 8160, 7384, 5432,
1005, 4512, 5186, 3953, 2164, 3372, 4097, 3247, 8697, 3022, 9896, 4101, 3871, 6791, 3219, 2742, 4630, 6967, 7829, 5991, 6134, 1197, 1414, 8923, 8787, 1394, 8852, 5019, 7768, 5147, 8004, 8825, 5062, 9625, 7988, 1110, 3992, 7984, 9966, 6516, 6251, 8270, 421, 3723, 1432, 4830, 6935, 8095, 9059, 2214, 6483, 6846, 3120, 1587, 6201, 6691, 9096, 9627, 6671, 4002, 3495, 9939, 7708, 7465, 5879, 6959, 6634, 3241, 3401, 2355, 9061, 2611, 7830, 3941, 2177, 2146, 5089, 7079, 519, 6351,
7280, 8586, 4261, 2831, 7217, 3141, 9994, 9940, 5462, 2189, 4005, 6942, 9848, 5350, 8060, 6665, 7519, 4324, 7684, 657, 9453, 9296, 2944, 6843, 7499, 7847, 1728, 9681, 3906, 6353, 5529, 2822, 3355, 3897, 7724, 4257, 7489, 8672, 4356, 3983, 1948, 6892, 7415, 4153, 5893, 4190, 621, 1736, 4045, 9532, 7701, 3671, 1211, 1622, 3176, 4524, 9317, 7800, 5638, 6644, 6943, 5463, 3531, 2821, 1347, 5958, 3436, 1438, 2999, 994, 850, 4131, 2616, 1549, 3465, 5946, 690, 9273, 6954, 7991,
9517, 399, 3249, 2596, 7736, 2142, 1322, 968, 7350, 1614, 468, 3346, 3265, 7222, 6086, 1661, 5317, 2582, 7959, 4685, 2807, 2917, 1037, 5698, 1529, 3972, 8716, 2634, 3301, 3412, 8621, 743, 8001, 4734, 888, 7744, 8092, 3671, 8941, 1487, 5658, 7099, 2781, 99, 1932, 4443, 4756, 4652, 9328, 1581, 7855, 4312, 5976, 7255, 6480, 3996, 2748, 1973, 9731, 4530, 2790, 9417, 7186, 5303, 3557, 351, 7182, 9428, 1342, 9020, 7599, 1392, 8304, 2070, 9138, 7215, 2008, 9937, 1106, 7110,
7444, 769, 9688, 632, 1571, 6820, 8743, 4338, 337, 3366, 3073, 1946, 8219, 104, 4210, 6986, 249, 5061, 8693, 7960, 6546, 1004, 8857, 5997, 9352, 4338, 6105, 5008, 2556, 6518, 6694, 4345, 3727, 7956, 20, 3954, 8652, 4424, 9387, 2035, 8358, 5962, 5304, 5194, 8650, 8282, 1256, 1103, 2138, 6679, 1985, 3653, 2770, 2433, 4278, 615, 2863, 1715, 242, 3790, 2636, 6998, 3088, 1671, 2239, 957, 5411, 4595, 6282, 2881, 9974, 2401, 875, 7574, 2987, 4587, 3147, 6766, 9885, 2965,
3287, 3016, 3619, 6818, 9073, 6120, 5423, 557, 2900, 2015, 8111, 3873, 1314, 4189, 1846, 4399, 7041, 7583, 2427, 2864, 3525, 5002, 2069, 748, 1948, 6015, 2684, 438, 770, 8367, 1663, 7887, 7759, 1885, 157, 7770, 4520, 4878, 3857, 1137, 3525, 3050, 6276, 5569, 7649, 904, 4533, 7843, 2199, 5648, 7628, 9075, 9441, 3600, 7231, 2388, 5640, 9096, 958, 3058, 584, 5899, 8150, 1181, 9616, 1098, 8162, 6819, 8171, 1519, 1140, 7665, 8801, 2632, 1299, 9192, 707, 9955, 2710, 7314,
1772, 2963, 7578, 3541, 3095, 1488, 7026, 2634, 6015, 4633, 4370, 2762, 1650, 2174, 909, 8158, 2922, 8467, 4198, 4280, 9092, 8856, 8835, 5457, 2790, 8574, 9742, 5054, 9547, 4156, 7940, 8126, 9824, 7340, 8840, 6574, 3547, 1477, 3014, 6798, 7134, 435, 9484, 9859, 3031, 4, 1502, 4133, 1738, 1807, 4825, 463, 6343, 9701, 8506, 9822, 9555, 8688, 8168, 3467, 3234, 6318, 1787, 5591, 419, 6593, 7974, 8486, 9861, 6381, 6758, 194, 3061, 4315, 2863, 4665, 3789, 2201, 1492, 4416,
126, 8927, 6608, 5682, 8986, 6867, 1715, 6076, 3159, 788, 3140, 4744, 830, 9253, 5812, 5021, 7616, 8534, 1546, 9590, 1101, 9012, 9821, 8132, 7857, 4086, 1069, 7491, 2988, 1579, 2442, 4321, 2149, 7642, 6108, 250, 6086, 3167, 24, 9528, 7663, 2685, 1220, 9196, 1397, 5776, 1577, 1730, 5481, 977, 6115, 199, 6326, 2183, 3767, 5928, 5586, 7561, 663, 8649, 9688, 949, 5913, 9160, 1870, 5764, 9887, 4477, 6703, 1413, 4995, 5494, 7131, 2192, 8969, 7138, 3997, 8697, 646, 1028,
8074, 1731, 8245, 624, 4601, 8706, 155, 8891, 309, 2552, 8208, 8452, 2954, 3124, 3469, 4246, 3352, 1105, 4509, 8677, 9901, 4416, 8191, 9283, 5625, 7120, 2952, 8881, 7693, 830, 4580, 8228, 9459, 8611, 4499, 1179, 4988, 1394, 550, 2336, 6089, 6872, 269, 7213, 1848, 917, 6672, 4890, 656, 1478, 6536, 3165, 4743, 4990, 1176, 6211, 7207, 5284, 9730, 4738, 1549, 4986, 4942, 8645, 3698, 9429, 1439, 2175, 6549, 3058, 6513, 1574, 6988, 8333, 3406, 5245, 5431, 7140, 7085, 6407,
7845, 4694, 2530, 8249, 290, 5948, 5509, 1588, 5940, 4495, 5866, 5021, 4626, 3979, 3296, 7589, 4854, 1998, 5627, 3926, 8346, 6512, 9608, 1918, 7070, 4747, 4182, 2858, 2766, 4606, 6269, 4107, 8982, 8568, 9053, 4244, 5604, 102, 2756, 727, 5887, 2566, 7922, 44, 5986, 621, 1202, 374, 6988, 4130, 3627, 6744, 9443, 4568, 1398, 8679, 397, 3928, 9159, 367, 2917, 6127, 5788, 3304, 8129, 911, 2669, 1463, 9749, 264, 4478, 8940, 1109, 7309, 2462, 117, 4692, 7724, 225, 2312,
4164, 3637, 2000, 941, 8903, 39, 3443, 7172, 1031, 3687, 4901, 8082, 4945, 4515, 7204, 9310, 9349, 9535, 9940, 218, 1788, 9245, 2237, 1541, 5670, 6538, 6047, 5553, 9807, 8101, 1925, 8714, 445, 8332, 7309, 6830, 5786, 5736, 7306, 2710, 3034, 1838, 7969, 6318, 7912, 2584, 2080, 7437, 6705, 2254, 7428, 820, 782, 9861, 7596, 3842, 3631, 8063, 5240, 6666, 394, 4565, 7865, 4895, 9890, 6028, 6117, 4724, 9156, 4473, 4552, 602, 470, 6191, 4927, 5387, 884, 3146, 1978, 3000,
4258, 6880, 1696, 3582, 5793, 4923, 2119, 1155, 9056, 9698, 6603, 3768, 5514, 9927, 9609, 6166, 6566, 4536, 4985, 4934, 8076, 9062, 6741, 6163, 7399, 4562, 2337, 5600, 2919, 9012, 8459, 1308, 6072, 1225, 9306, 8818, 5886, 7243, 7365, 8792, 6007, 9256, 6699, 7171, 4230, 7002, 8720, 7839, 4533, 1671, 478, 7774, 1607, 2317, 5437, 4705, 7886, 4760, 6760, 7271, 3081, 2997, 3088, 7675, 6208, 3101, 6821, 6840, 122, 9633, 4900, 2067, 8546, 4549, 2091, 7188, 5605, 8599, 6758, 5229,
7854, 5243, 9155, 3556, 8812, 7047, 2202, 1541, 5993, 4600, 4760, 713, 434, 7911, 7426, 7414, 8729, 322, 803, 7960, 7563, 4908, 6285, 6291, 736, 3389, 9339, 4132, 8701, 7534, 5287, 3646, 592, 3065, 7582, 2592, 8755, 6068, 8597, 1982, 5782, 1894, 2900, 6236, 4039, 6569, 3037, 5837, 7698, 700, 7815, 2491, 7272, 5878, 3083, 6778, 6639, 3589, 5010, 8313, 2581, 6617, 5869, 8402, 6808, 2951, 2321, 5195, 497, 2190, 6187, 1342, 1316, 4453, 7740, 4154, 2959, 1781, 1482, 8256,
7178, 2046, 4419, 744, 8312, 5356, 6855, 8839, 319, 2962, 5662, 47, 6307, 8662, 68, 4813, 567, 2712, 9931, 1678, 3101, 8227, 6533, 4933, 6656, 92, 5846, 4780, 6256, 6361, 4323, 9985, 1231, 2175, 7178, 3034, 9744, 6155, 9165, 7787, 5836, 9318, 7860, 9644, 8941, 6480, 9443, 8188, 5928, 161, 6979, 2352, 5628, 6991, 1198, 8067, 5867, 6620, 3778, 8426, 2994, 3122, 3124, 6335, 3918, 8897, 2655, 9670, 634, 1088, 1576, 8935, 7255, 474, 8166, 7417, 9547, 2886, 5560, 3842,
6957, 3111, 26, 7530, 7143, 1295, 1744, 6057, 3009, 1854, 8098, 5405, 2234, 4874, 9447, 2620, 9303, 27, 7410, 969, 40, 2966, 5648, 7596, 8637, 4238, 3143, 3679, 7187, 690, 9980, 7085, 7714, 9373, 5632, 7526, 6707, 3951, 9734, 4216, 2146, 3602, 5371, 6029, 3039, 4433, 4855, 4151, 1449, 3376, 8009, 7240, 7027, 4602, 2947, 9081, 4045, 8424, 9352, 8742, 923, 2705, 4266, 3232, 2264, 6761, 363, 2651, 3383, 7770, 6730, 7856, 7340, 9679, 2158, 610, 4471, 4608, 910, 6241,
4417, 6756, 1013, 8797, 658, 8809, 5032, 8703, 7541, 846, 3357, 2920, 9817, 1745, 9980, 7593, 4667, 3087, 779, 3218, 6233, 5568, 4296, 2289, 2654, 7898, 5021, 9461, 5593, 8214, 9173, 4203, 2271, 7980, 2983, 5952, 9992, 8399, 3468, 1776, 3188, 9314, 1720, 6523, 2933, 621, 8685, 5483, 8986, 6163, 3444, 9539, 4320, 155, 3992, 2828, 2150, 6071, 524, 2895, 5468, 8063, 1210, 3348, 9071, 4862, 483, 9017, 4097, 6186, 9815, 3610, 5048, 1644, 1003, 9865, 9332, 2145, 1944, 2213,
9284, 3803, 4920, 1927, 6706, 4344, 7383, 4786, 9890, 2010, 5228, 1224, 3158, 6967, 8580, 8990, 8883, 5213, 76, 8306, 2031, 4980, 5639, 9519, 7184, 5645, 7769, 3259, 8077, 9130, 1317, 3096, 9624, 3818, 1770, 695, 2454, 947, 6029, 3474, 9938, 3527, 5696, 4760, 7724, 7738, 2848, 6442, 5767, 6845, 8323, 4131, 2859, 7595, 2500, 4815, 3660, 9130, 8580, 7016, 8231, 4391, 8369, 3444, 4069, 4021, 556, 6154, 627, 2778, 1496, 4206, 6356, 8434, 8491, 3816, 8231, 3190, 5575, 1015,
3787, 7572, 1788, 6803, 5641, 6844, 1961, 4811, 8535, 9914, 9999, 1450, 8857, 738, 4662, 8569, 6679, 2225, 7839, 8618, 286, 2648, 5342, 2294, 3205, 4546, 176, 8705, 3741, 6134, 8324, 8021, 7004, 5205, 7032, 6637, 9442, 5539, 5584, 4819, 5874, 5807, 8589, 6871, 9016, 983, 1758, 3786, 1519, 6241, 185, 8398, 495, 3370, 9133, 3051, 4549, 9674, 7311, 9738, 3316, 9383, 2658, 2776, 9481, 7558, 619, 3943, 3324, 6491, 4933, 153, 9738, 4623, 912, 3595, 7771, 7939, 1219, 4405,
2650, 3883, 4154, 5809, 315, 7756, 4430, 1788, 4451, 1631, 6461, 7230, 6017, 5751, 138, 588, 5282, 2442, 9110, 9035, 6349, 2515, 1570, 6122, 4192, 4174, 3530, 1933, 4186, 4420, 4609, 5739, 4135, 2963, 6308, 1161, 8809, 8619, 2796, 3819, 6971, 8228, 4188, 1492, 909, 8048, 2328, 6772, 8467, 7671, 9068, 2226, 7579, 6422, 7056, 8042, 3296, 2272, 3006, 2196, 7320, 3238, 3490, 3102, 37, 1293, 3212, 4767, 5041, 8773, 5794, 4456, 6174, 7279, 7054, 2835, 7053, 9088, 790, 6640,
3101, 1057, 7057, 3826, 6077, 1025, 2955, 1224, 1114, 6729, 5902, 4698, 6239, 7203, 9423, 1804, 4417, 6686, 1426, 6941, 8071, 1029, 4985, 9010, 6122, 6597, 1622, 1574, 3513, 1684, 7086, 5505, 3244, 411, 9638, 4150, 907, 9135, 829, 981, 1707, 5359, 8781, 9751, 5, 9131, 3973, 7159, 1340, 6955, 7514, 7993, 6964, 8198, 1933, 2797, 877, 3993, 4453, 8020, 9349, 8646, 2779, 8679, 2961, 3547, 3374, 3510, 1129, 3568, 2241, 2625, 9138, 5974, 8206, 7669, 7678, 1833, 8700, 4480,
4865, 9912, 8038, 8238, 782, 3095, 8199, 1127, 4501, 7280, 2112, 2487, 3626, 2790, 9432, 1475, 6312, 8277, 4827, 2218, 5806, 7132, 8752, 1468, 7471, 6386, 739, 8762, 8323, 8120, 5169, 9078, 9058, 3370, 9560, 7987, 8585, 8531, 5347, 9312, 1058, 4271, 1159, 5286, 5404, 6925, 8606, 9204, 7361, 2415, 560, 586, 4002, 2644, 1927, 2824, 768, 4409, 2942, 3345, 1002, 808, 4941, 6267, 7979, 5140, 8643, 7553, 9438, 7320, 4938, 2666, 4609, 2778, 8158, 6730, 3748, 3867, 1866, 7181,
171, 3771, 7134, 8927, 4778, 2913, 3326, 2004, 3089, 7853, 1378, 1729, 4777, 2706, 9578, 1360, 5693, 3036, 1851, 7248, 2403, 2273, 8536, 6501, 9216, 613, 9671, 7131, 7719, 6425, 773, 717, 8803, 160, 1114, 7554, 7197, 753, 4513, 4322, 8499, 4533, 2609, 4226, 8710, 6627, 644, 9666, 6260, 4870, 5744, 7385, 6542, 6203, 7703, 6130, 8944, 5589, 2262, 6803, 6381, 7414, 6888, 5123, 7320, 9392, 9061, 6780, 322, 8975, 7050, 5089, 1061, 2260, 3199, 1150, 1865, 5386, 9699, 6501,
3744, 8454, 6885, 8277, 919, 1923, 4001, 6864, 7854, 5519, 2491, 6057, 8794, 9645, 1776, 5714, 9786, 9281, 7538, 6916, 3215, 395, 2501, 9618, 4835, 8846, 9708, 2813, 3303, 1794, 8309, 7176, 2206, 1602, 1838, 236, 4593, 2245, 8993, 4017, 10, 8215, 6921, 5206, 4023, 5932, 6997, 7801, 262, 7640, 3107, 8275, 4938, 7822, 2425, 3223, 3886, 2105, 8700, 9526, 2088, 8662, 8034, 7004, 5710, 2124, 7164, 3574, 6630, 9980, 4242, 2901, 9471, 1491, 2117, 4562, 1130, 9086, 4117, 6698,
2810, 2280, 2331, 1170, 4554, 4071, 8387, 1215, 2274, 9848, 6738, 1604, 7281, 8805, 439, 1298, 8318, 7834, 9426, 8603, 6092, 7944, 1309, 8828, 303, 3157, 4638, 4439, 9175, 1921, 4695, 7716, 1494, 1015, 1772, 5913, 1127, 1952, 1950, 8905, 4064, 9890, 385, 9357, 7945, 5035, 7082, 5369, 4093, 6546, 5187, 5637, 2041, 8946, 1758, 7111, 6566, 1027, 1049, 5148, 7224, 7248, 296, 6169, 375, 1656, 7993, 2816, 3717, 4279, 4675, 1609, 3317, 42, 6201, 3100, 3144, 163, 9530, 4531,
7096, 6070, 1009, 4988, 3538, 5801, 7149, 3063, 2324, 2912, 7911, 7002, 4338, 7880, 2481, 7368, 3516, 2016, 7556, 2193, 1388, 3865, 8125, 4637, 4096, 8114, 750, 3144, 1938, 7002, 9343, 4095, 1392, 4220, 3455, 6969, 9647, 1321, 9048, 1996, 1640, 6626, 1788, 314, 9578, 6630, 2813, 6626, 4981, 9908, 7024, 4355, 3201, 3521, 3864, 3303, 464, 1923, 595, 9801, 3391, 8366, 8084, 9374, 1041, 8807, 9085, 1892, 9431, 8317, 9016, 9221, 8574, 9981, 9240, 5395, 2009, 6310, 2854, 9255,
8830, 3145, 2960, 9615, 8220, 6061, 3452, 2918, 6481, 9278, 2297, 3385, 6565, 7066, 7316, 5682, 107, 7646, 4466, 68, 1952, 9603, 8615, 54, 7191, 791, 6833, 2560, 693, 9733, 4168, 570, 9127, 9537, 1925, 8287, 5508, 4297, 8452, 8795, 6213, 7994, 2420, 4208, 524, 5915, 8602, 8330, 2651, 8547, 6156, 1812, 6271, 7991, 9407, 9804, 1553, 6866, 1128, 2119, 4691, 9711, 8315, 5879, 9935, 6900, 482, 682, 4126, 1041, 428, 6247, 3720, 5882, 7526, 2582, 4327, 7725, 3503, 2631,
2738, 9323, 721, 7434, 1453, 6294, 2957, 3786, 5722, 6019, 8685, 4386, 3066, 9057, 6860, 499, 5315, 3045, 5194, 7111, 3137, 9104, 941, 586, 3066, 755, 4177, 8819, 7040, 5309, 3583, 3897, 4428, 7788, 4721, 7249, 6559, 7324, 825, 7311, 3760, 6064, 6070, 9672, 4882, 584, 1365, 9739, 9331, 5783, 2624, 7889, 1604, 1303, 1555, 7125, 8312, 425, 8936, 3233, 7724, 1480, 403, 7440, 1784, 1754, 4721, 1569, 652, 3893, 4574, 5692, 9730, 4813, 9844, 8291, 9199, 7101, 3391, 8914,
6044, 2928, 9332, 3328, 8588, 447, 3830, 1176, 3523, 2705, 8365, 6136, 5442, 9049, 5526, 8575, 8869, 9031, 7280, 706, 2794, 8814, 5767, 4241, 7696, 78, 6570, 556, 5083, 1426, 4502, 3336, 9518, 2292, 1885, 3740, 3153, 9348, 9331, 8051, 2759, 5407, 9028, 7840, 9255, 831, 515, 2612, 9747, 7435, 8964, 4971, 2048, 4900, 5967, 8271, 1719, 9670, 2810, 6777, 1594, 6367, 6259, 8316, 3815, 1689, 6840, 9437, 4361, 822, 9619, 3065, 83, 6344, 7486, 8657, 8228, 9635, 6932, 4864,
8478, 4777, 6334, 4678, 7476, 4963, 6735, 3096, 5860, 1405, 5127, 7269, 7793, 4738, 227, 9168, 2996, 8928, 765, 733, 1276, 7677, 6258, 1528, 9558, 3329, 302, 8901, 1422, 8277, 6340, 645, 9125, 8869, 5952, 141, 8141, 1816, 9635, 4025, 4184, 3093, 83, 2344, 2747, 9352, 7966, 1206, 1126, 1826, 218, 7939, 2957, 2729, 810, 8752, 5247, 4174, 4038, 8884, 7899, 9567, 301, 5265, 5752, 7524, 4381, 1669, 3106, 8270, 6228, 6373, 754, 2547, 4240, 2313, 5514, 3022, 1040, 9738,
2265, 8192, 1763, 1369, 8469, 8789, 4836, 52, 1212, 6690, 5257, 8918, 6723, 6319, 378, 4039, 2421, 8555, 8184, 9577, 1432, 7139, 8078, 5452, 9628, 7579, 4161, 7490, 5159, 8559, 1011, 81, 478, 5840, 1964, 1334, 6875, 8670, 9900, 739, 1514, 8692, 522, 9316, 6955, 1345, 8132, 2277, 3193, 9773, 3923, 4177, 2183, 1236, 6747, 6575, 4874, 6003, 6409, 8187, 745, 8776, 9440, 7543, 9825, 2582, 7381, 8147, 7236, 5185, 7564, 6125, 218, 7991, 6394, 391, 7659, 7456, 5128, 5294,
2132, 8992, 8160, 5782, 4420, 3371, 3798, 5054, 552, 5631, 7546, 4716, 1332, 6486, 7892, 7441, 4370, 6231, 4579, 2121, 8615, 1145, 9391, 1524, 1385, 2400, 9437, 2454, 7896, 7467, 2928, 8400, 3299, 4025, 7458, 4703, 7206, 6358, 792, 6200, 725, 4275, 4136, 7390, 5984, 4502, 7929, 5085, 8176, 4600, 119, 3568, 76, 9363, 6943, 2248, 9077, 9731, 6213, 5817, 6729, 4190, 3092, 6910, 759, 2682, 8380, 1254, 9604, 3011, 9291, 5329, 9453, 9746, 2739, 6522, 3765, 5634, 1113, 5789,
5304, 5499, 564, 2801, 679, 2653, 1783, 3608, 7359, 7797, 3284, 796, 3222, 437, 7185, 6135, 8571, 2778, 7488, 5746, 678, 6140, 861, 7750, 803, 9859, 9918, 2425, 3734, 2698, 9005, 4864, 9818, 6743, 2475, 132, 9486, 3825, 5472, 919, 292, 4411, 7213, 7699, 6435, 9019, 6769, 1388, 802, 2124, 1345, 8493, 9487, 8558, 7061, 8777, 8833, 2427, 2238, 5409, 4957, 8503, 3171, 7622, 5779, 6145, 2417, 5873, 5563, 5693, 9574, 9491, 1937, 7384, 4563, 6842, 5432, 2751, 3406, 7981]

    l1 = l
    n = 80
    #n = 5

    def isoutofbounds(y, x):
        if y < 1 or x < 1 or y > n or x > n:
            return True
        return False

    def get(l, y, x):
        if isoutofbounds(y, x):
            return 0
        return l[y * n + x - n - 1]

    def set_(l, y, x, v):
        l[y * n + x - n - 1] = v

    def get_min(y, x):
        if isoutofbounds(y, x):
            return 0
        if x == 1:
            return get(l1, y, x)
        v = get(min_sum, y, x)
        if v != 0:
            return v


        min_list = list()
        for y1 in range(1, y + 1):
            s = get_min(y1, x - 1)
            for y2 in range(y1, y):
                s += get(l1, y2, x)
            min_list.append(s)
        for y1 in range(y, n + 1):
            s = get_min(y1, x - 1)
            for y2 in range(y + 1, y1 + 1):
                s += get(l1, y2, x)
            min_list.append(s)

        #left = get_min(y, x - 1)
        #up = get_min(y - 1, x)
        # down = 0
        minimum = sorted(filter(lambda x: x > 0, min_list))[0]
        v = get(l1, y, x) + minimum
        # print 'l1(%d, %d) = %d' % (y, x, get(l1, y, x)), 'min = ', v

        set_(min_sum, y, x, v)
        return v


    min_sum = list()
    for i in range(len(l1)):
        min_sum.append(0)
    m = get_min(1, n)
    for i in range(2, n + 1):
        candidate = get_min(i, n)
        if m > candidate:
            m = candidate
            print 'row=', i


    #print min_sum

    print m

    # print m


def problem_104(): # solved 329467
    a = 1
    b = 0
    i = 1

    last9modulo = 10 ** 9
    while 1:
        i += 1
        a, b = (a + b), a

        last9 = a % last9modulo
        digprod = 1
        digsum = 0
        ndigs = 0
        while digprod > 0 and last9 > 0:
            ndigs += 1
            digprod *= last9 % 10
            digsum += last9 % 10
            last9 /= 10
        if digprod == 362880 and digsum == 45 and ndigs == 9:
            print i, a % last9modulo
            k = set(str(a)[:10])
            if len(k) == 9 and not '0' in k:
                print i, k, a
                break


def problem_83(): # solved - 425185

    l1 = [131, 673, 234, 103, 18, 201, 96, 342, 965, 150, 630, 803, 746, 422, 111, 537, 699, 497, 121, 956, 805, 732, 524, 37, 331]
    l = [4445, 2697, 5115, 718, 2209, 2212, 654, 4348, 3079, 6821, 7668, 3276, 8874, 4190, 3785, 2752, 9473, 7817, 9137, 496, 7338, 3434, 7152, 4355, 4552, 7917, 7827, 2460, 2350, 691, 3514, 5880, 3145, 7633, 7199, 3783, 5066, 7487, 3285, 1084, 8985, 760, 872, 8609, 8051, 1134, 9536, 5750, 9716, 9371, 7619, 5617, 275, 9721, 2997, 2698, 1887, 8825, 6372, 3014, 2113, 7122, 7050, 6775, 5948, 2758, 1219, 3539, 348, 7989, 2735, 9862, 1263, 8089, 6401, 9462, 3168, 2758, 3748,
         5870, 1096, 20, 1318, 7586, 5167, 2642, 1443, 5741, 7621, 7030, 5526, 4244, 2348, 4641, 9827, 2448, 6918, 5883, 3737, 300, 7116, 6531, 567, 5997, 3971, 6623, 820, 6148, 3287, 1874, 7981, 8424, 7672, 7575, 6797, 6717, 1078, 5008, 4051, 8795, 5820, 346, 1851, 6463, 2117, 6058, 3407, 8211, 117, 4822, 1317, 4377, 4434, 5925, 8341, 4800, 1175, 4173, 690, 8978, 7470, 1295, 3799, 8724, 3509, 9849, 618, 3320, 7068, 9633, 2384, 7175, 544, 6583, 1908, 9983, 481, 4187, 9353, 9377,
9607, 7385, 521, 6084, 1364, 8983, 7623, 1585, 6935, 8551, 2574, 8267, 4781, 3834, 2764, 2084, 2669, 4656, 9343, 7709, 2203, 9328, 8004, 6192, 5856, 3555, 2260, 5118, 6504, 1839, 9227, 1259, 9451, 1388, 7909, 5733, 6968, 8519, 9973, 1663, 5315, 7571, 3035, 4325, 4283, 2304, 6438, 3815, 9213, 9806, 9536, 196, 5542, 6907, 2475, 1159, 5820, 9075, 9470, 2179, 9248, 1828, 4592, 9167, 3713, 4640, 47, 3637, 309, 7344, 6955, 346, 378, 9044, 8635, 7466, 5036, 9515, 6385, 9230,
7206, 3114, 7760, 1094, 6150, 5182, 7358, 7387, 4497, 955, 101, 1478, 7777, 6966, 7010, 8417, 6453, 4955, 3496, 107, 449, 8271, 131, 2948, 6185, 784, 5937, 8001, 6104, 8282, 4165, 3642, 710, 2390, 575, 715, 3089, 6964, 4217, 192, 5949, 7006, 715, 3328, 1152, 66, 8044, 4319, 1735, 146, 4818, 5456, 6451, 4113, 1063, 4781, 6799, 602, 1504, 6245, 6550, 1417, 1343, 2363, 3785, 5448, 4545, 9371, 5420, 5068, 4613, 4882, 4241, 5043, 7873, 8042, 8434, 3939, 9256, 2187,
3620, 8024, 577, 9997, 7377, 7682, 1314, 1158, 6282, 6310, 1896, 2509, 5436, 1732, 9480, 706, 496, 101, 6232, 7375, 2207, 2306, 110, 6772, 3433, 2878, 8140, 5933, 8688, 1399, 2210, 7332, 6172, 6403, 7333, 4044, 2291, 1790, 2446, 7390, 8698, 5723, 3678, 7104, 1825, 2040, 140, 3982, 4905, 4160, 2200, 5041, 2512, 1488, 2268, 1175, 7588, 8321, 8078, 7312, 977, 5257, 8465, 5068, 3453, 3096, 1651, 7906, 253, 9250, 6021, 8791, 8109, 6651, 3412, 345, 4778, 5152, 4883, 7505,
1074, 5438, 9008, 2679, 5397, 5429, 2652, 3403, 770, 9188, 4248, 2493, 4361, 8327, 9587, 707, 9525, 5913, 93, 1899, 328, 2876, 3604, 673, 8576, 6908, 7659, 2544, 3359, 3883, 5273, 6587, 3065, 1749, 3223, 604, 9925, 6941, 2823, 8767, 7039, 3290, 3214, 1787, 7904, 3421, 7137, 9560, 8451, 2669, 9219, 6332, 1576, 5477, 6755, 8348, 4164, 4307, 2984, 4012, 6629, 1044, 2874, 6541, 4942, 903, 1404, 9125, 5160, 8836, 4345, 2581, 460, 8438, 1538, 5507, 668, 3352, 2678, 6942,
4295, 1176, 5596, 1521, 3061, 9868, 7037, 7129, 8933, 6659, 5947, 5063, 3653, 9447, 9245, 2679, 767, 714, 116, 8558, 163, 3927, 8779, 158, 5093, 2447, 5782, 3967, 1716, 931, 7772, 8164, 1117, 9244, 5783, 7776, 3846, 8862, 6014, 2330, 6947, 1777, 3112, 6008, 3491, 1906, 5952, 314, 4602, 8994, 5919, 9214, 3995, 5026, 7688, 6809, 5003, 3128, 2509, 7477, 110, 8971, 3982, 8539, 2980, 4689, 6343, 5411, 2992, 5270, 5247, 9260, 2269, 7474, 1042, 7162, 5206, 1232, 4556, 4757,
510, 3556, 5377, 1406, 5721, 4946, 2635, 7847, 4251, 8293, 8281, 6351, 4912, 287, 2870, 3380, 3948, 5322, 3840, 4738, 9563, 1906, 6298, 3234, 8959, 1562, 6297, 8835, 7861, 239, 6618, 1322, 2553, 2213, 5053, 5446, 4402, 6500, 5182, 8585, 6900, 5756, 9661, 903, 5186, 7687, 5998, 7997, 8081, 8955, 4835, 6069, 2621, 1581, 732, 9564, 1082, 1853, 5442, 1342, 520, 1737, 3703, 5321, 4793, 2776, 1508, 1647, 9101, 2499, 6891, 4336, 7012, 3329, 3212, 1442, 9993, 3988, 4930, 7706,
9444, 3401, 5891, 9716, 1228, 7107, 109, 3563, 2700, 6161, 5039, 4992, 2242, 8541, 7372, 2067, 1294, 3058, 1306, 320, 8881, 5756, 9326, 411, 8650, 8824, 5495, 8282, 8397, 2000, 1228, 7817, 2099, 6473, 3571, 5994, 4447, 1299, 5991, 543, 7874, 2297, 1651, 101, 2093, 3463, 9189, 6872, 6118, 872, 1008, 1779, 2805, 9084, 4048, 2123, 5877, 55, 3075, 1737, 9459, 4535, 6453, 3644, 108, 5982, 4437, 5213, 1340, 6967, 9943, 5815, 669, 8074, 1838, 6979, 9132, 9315, 715, 5048,
3327, 4030, 7177, 6336, 9933, 5296, 2621, 4785, 2755, 4832, 2512, 2118, 2244, 4407, 2170, 499, 7532, 9742, 5051, 7687, 970, 6924, 3527, 4694, 5145, 1306, 2165, 5940, 2425, 8910, 3513, 1909, 6983, 346, 6377, 4304, 9330, 7203, 6605, 3709, 3346, 970, 369, 9737, 5811, 4427, 9939, 3693, 8436, 5566, 1977, 3728, 2399, 3985, 8303, 2492, 5366, 9802, 9193, 7296, 1033, 5060, 9144, 2766, 1151, 7629, 5169, 5995, 58, 7619, 7565, 4208, 1713, 6279, 3209, 4908, 9224, 7409, 1325, 8540,
6882, 1265, 1775, 3648, 4690, 959, 5837, 4520, 5394, 1378, 9485, 1360, 4018, 578, 9174, 2932, 9890, 3696, 116, 1723, 1178, 9355, 7063, 1594, 1918, 8574, 7594, 7942, 1547, 6166, 7888, 354, 6932, 4651, 1010, 7759, 6905, 661, 7689, 6092, 9292, 3845, 9605, 8443, 443, 8275, 5163, 7720, 7265, 6356, 7779, 1798, 1754, 5225, 6661, 1180, 8024, 5666, 88, 9153, 1840, 3508, 1193, 4445, 2648, 3538, 6243, 6375, 8107, 5902, 5423, 2520, 1122, 5015, 6113, 8859, 9370, 966, 8673, 2442,
7338, 3423, 4723, 6533, 848, 8041, 7921, 8277, 4094, 5368, 7252, 8852, 9166, 2250, 2801, 6125, 8093, 5738, 4038, 9808, 7359, 9494, 601, 9116, 4946, 2702, 5573, 2921, 9862, 1462, 1269, 2410, 4171, 2709, 7508, 6241, 7522, 615, 2407, 8200, 4189, 5492, 5649, 7353, 2590, 5203, 4274, 710, 7329, 9063, 956, 8371, 3722, 4253, 4785, 1194, 4828, 4717, 4548, 940, 983, 2575, 4511, 2938, 1827, 2027, 2700, 1236, 841, 5760, 1680, 6260, 2373, 3851, 1841, 4968, 1172, 5179, 7175, 3509,
4420, 1327, 3560, 2376, 6260, 2988, 9537, 4064, 4829, 8872, 9598, 3228, 1792, 7118, 9962, 9336, 4368, 9189, 6857, 1829, 9863, 6287, 7303, 7769, 2707, 8257, 2391, 2009, 3975, 4993, 3068, 9835, 3427, 341, 8412, 2134, 4034, 8511, 6421, 3041, 9012, 2983, 7289, 100, 1355, 7904, 9186, 6920, 5856, 2008, 6545, 8331, 3655, 5011, 839, 8041, 9255, 6524, 3862, 8788, 62, 7455, 3513, 5003, 8413, 3918, 2076, 7960, 6108, 3638, 6999, 3436, 1441, 4858, 4181, 1866, 8731, 7745, 3744, 1000,
356, 8296, 8325, 1058, 1277, 4743, 3850, 2388, 6079, 6462, 2815, 5620, 8495, 5378, 75, 4324, 3441, 9870, 1113, 165, 1544, 1179, 2834, 562, 6176, 2313, 6836, 8839, 2986, 9454, 5199, 6888, 1927, 5866, 8760, 320, 1792, 8296, 7898, 6121, 7241, 5886, 5814, 2815, 8336, 1576, 4314, 3109, 2572, 6011, 2086, 9061, 9403, 3947, 5487, 9731, 7281, 3159, 1819, 1334, 3181, 5844, 5114, 9898, 4634, 2531, 4412, 6430, 4262, 8482, 4546, 4555, 6804, 2607, 9421, 686, 8649, 8860, 7794, 6672,
9870, 152, 1558, 4963, 8750, 4754, 6521, 6256, 8818, 5208, 5691, 9659, 8377, 9725, 5050, 5343, 2539, 6101, 1844, 9700, 7750, 8114, 5357, 3001, 8830, 4438, 199, 9545, 8496, 43, 2078, 327, 9397, 106, 6090, 8181, 8646, 6414, 7499, 5450, 4850, 6273, 5014, 4131, 7639, 3913, 6571, 8534, 9703, 4391, 7618, 445, 1320, 5, 1894, 6771, 7383, 9191, 4708, 9706, 6939, 7937, 8726, 9382, 5216, 3685, 2247, 9029, 8154, 1738, 9984, 2626, 9438, 4167, 6351, 5060, 29, 1218, 1239, 4785,
192, 5213, 8297, 8974, 4032, 6966, 5717, 1179, 6523, 4679, 9513, 1481, 3041, 5355, 9303, 9154, 1389, 8702, 6589, 7818, 6336, 3539, 5538, 3094, 6646, 6702, 6266, 2759, 4608, 4452, 617, 9406, 8064, 6379, 444, 5602, 4950, 1810, 8391, 1536, 316, 8714, 1178, 5182, 5863, 5110, 5372, 4954, 1978, 2971, 5680, 4863, 2255, 4630, 5723, 2168, 538, 1692, 1319, 7540, 440, 6430, 6266, 7712, 7385, 5702, 620, 641, 3136, 7350, 1478, 3155, 2820, 9109, 6261, 1122, 4470, 14, 8493, 2095,
1046, 4301, 6082, 474, 4974, 7822, 2102, 5161, 5172, 6946, 8074, 9716, 6586, 9962, 9749, 5015, 2217, 995, 5388, 4402, 7652, 6399, 6539, 1349, 8101, 3677, 1328, 9612, 7922, 2879, 231, 5887, 2655, 508, 4357, 4964, 3554, 5930, 6236, 7384, 4614, 280, 3093, 9600, 2110, 7863, 2631, 6626, 6620, 68, 1311, 7198, 7561, 1768, 5139, 1431, 221, 230, 2940, 968, 5283, 6517, 2146, 1646, 869, 9402, 7068, 8645, 7058, 1765, 9690, 4152, 2926, 9504, 2939, 7504, 6074, 2944, 6470, 7859,
4659, 736, 4951, 9344, 1927, 6271, 8837, 8711, 3241, 6579, 7660, 5499, 5616, 3743, 5801, 4682, 9748, 8796, 779, 1833, 4549, 8138, 4026, 775, 4170, 2432, 4174, 3741, 7540, 8017, 2833, 4027, 396, 811, 2871, 1150, 9809, 2719, 9199, 8504, 1224, 540, 2051, 3519, 7982, 7367, 2761, 308, 3358, 6505, 2050, 4836, 5090, 7864, 805, 2566, 2409, 6876, 3361, 8622, 5572, 5895, 3280, 441, 7893, 8105, 1634, 2929, 274, 3926, 7786, 6123, 8233, 9921, 2674, 5340, 1445, 203, 4585, 3837,
5759, 338, 7444, 7968, 7742, 3755, 1591, 4839, 1705, 650, 7061, 2461, 9230, 9391, 9373, 2413, 1213, 431, 7801, 4994, 2380, 2703, 6161, 6878, 8331, 2538, 6093, 1275, 5065, 5062, 2839, 582, 1014, 8109, 3525, 1544, 1569, 8622, 7944, 2905, 6120, 1564, 1839, 5570, 7579, 1318, 2677, 5257, 4418, 5601, 7935, 7656, 5192, 1864, 5886, 6083, 5580, 6202, 8869, 1636, 7907, 4759, 9082, 5854, 3185, 7631, 6854, 5872, 5632, 5280, 1431, 2077, 9717, 7431, 4256, 8261, 9680, 4487, 4752, 4286,
1571, 1428, 8599, 1230, 7772, 4221, 8523, 9049, 4042, 8726, 7567, 6736, 9033, 2104, 4879, 4967, 6334, 6716, 3994, 1269, 8995, 6539, 3610, 7667, 6560, 6065, 874, 848, 4597, 1711, 7161, 4811, 6734, 5723, 6356, 6026, 9183, 2586, 5636, 1092, 7779, 7923, 8747, 6887, 7505, 9909, 1792, 3233, 4526, 3176, 1508, 8043, 720, 5212, 6046, 4988, 709, 5277, 8256, 3642, 1391, 5803, 1468, 2145, 3970, 6301, 7767, 2359, 8487, 9771, 8785, 7520, 856, 1605, 8972, 2402, 2386, 991, 1383, 5963,
1822, 4824, 5957, 6511, 9868, 4113, 301, 9353, 6228, 2881, 2966, 6956, 9124, 9574, 9233, 1601, 7340, 973, 9396, 540, 4747, 8590, 9535, 3650, 7333, 7583, 4806, 3593, 2738, 8157, 5215, 8472, 2284, 9473, 3906, 6982, 5505, 6053, 7936, 6074, 7179, 6688, 1564, 1103, 6860, 5839, 2022, 8490, 910, 7551, 7805, 881, 7024, 1855, 9448, 4790, 1274, 3672, 2810, 774, 7623, 4223, 4850, 6071, 9975, 4935, 1915, 9771, 6690, 3846, 517, 463, 7624, 4511, 614, 6394, 3661, 7409, 1395, 8127,
8738, 3850, 9555, 3695, 4383, 2378, 87, 6256, 6740, 7682, 9546, 4255, 6105, 2000, 1851, 4073, 8957, 9022, 6547, 5189, 2487, 303, 9602, 7833, 1628, 4163, 6678, 3144, 8589, 7096, 8913, 5823, 4890, 7679, 1212, 9294, 5884, 2972, 3012, 3359, 7794, 7428, 1579, 4350, 7246, 4301, 7779, 7790, 3294, 9547, 4367, 3549, 1958, 8237, 6758, 3497, 3250, 3456, 6318, 1663, 708, 7714, 6143, 6890, 3428, 6853, 9334, 7992, 591, 6449, 9786, 1412, 8500, 722, 5468, 1371, 108, 3939, 4199, 2535,
7047, 4323, 1934, 5163, 4166, 461, 3544, 2767, 6554, 203, 6098, 2265, 9078, 2075, 4644, 6641, 8412, 9183, 487, 101, 7566, 5622, 1975, 5726, 2920, 5374, 7779, 5631, 3753, 3725, 2672, 3621, 4280, 1162, 5812, 345, 8173, 9785, 1525, 955, 5603, 2215, 2580, 5261, 2765, 2990, 5979, 389, 3907, 2484, 1232, 5933, 5871, 3304, 1138, 1616, 5114, 9199, 5072, 7442, 7245, 6472, 4760, 6359, 9053, 7876, 2564, 9404, 3043, 9026, 2261, 3374, 4460, 7306, 2326, 966, 828, 3274, 1712, 3446,
3975, 4565, 8131, 5800, 4570, 2306, 8838, 4392, 9147, 11, 3911, 7118, 9645, 4994, 2028, 6062, 5431, 2279, 8752, 2658, 7836, 994, 7316, 5336, 7185, 3289, 1898, 9689, 2331, 5737, 3403, 1124, 2679, 3241, 7748, 16, 2724, 5441, 6640, 9368, 9081, 5618, 858, 4969, 17, 2103, 6035, 8043, 7475, 2181, 939, 415, 1617, 8500, 8253, 2155, 7843, 7974, 7859, 1746, 6336, 3193, 2617, 8736, 4079, 6324, 6645, 8891, 9396, 5522, 6103, 1857, 8979, 3835, 2475, 1310, 7422, 610, 8345, 7615,
9248, 5397, 5686, 2988, 3446, 4359, 6634, 9141, 497, 9176, 6773, 7448, 1907, 8454, 916, 1596, 2241, 1626, 1384, 2741, 3649, 5362, 8791, 7170, 2903, 2475, 5325, 6451, 924, 3328, 522, 90, 4813, 9737, 9557, 691, 2388, 1383, 4021, 1609, 9206, 4707, 5200, 7107, 8104, 4333, 9860, 5013, 1224, 6959, 8527, 1877, 4545, 7772, 6268, 621, 4915, 9349, 5970, 706, 9583, 3071, 4127, 780, 8231, 3017, 9114, 3836, 7503, 2383, 1977, 4870, 8035, 2379, 9704, 1037, 3992, 3642, 1016, 4303,
5093, 138, 4639, 6609, 1146, 5565, 95, 7521, 9077, 2272, 974, 4388, 2465, 2650, 722, 4998, 3567, 3047, 921, 2736, 7855, 173, 2065, 4238, 1048, 5, 6847, 9548, 8632, 9194, 5942, 4777, 7910, 8971, 6279, 7253, 2516, 1555, 1833, 3184, 9453, 9053, 6897, 7808, 8629, 4877, 1871, 8055, 4881, 7639, 1537, 7701, 2508, 7564, 5845, 5023, 2304, 5396, 3193, 2955, 1088, 3801, 6203, 1748, 3737, 1276, 13, 4120, 7715, 8552, 3047, 2921, 106, 7508, 304, 1280, 7140, 2567, 9135, 5266,
6237, 4607, 7527, 9047, 522, 7371, 4883, 2540, 5867, 6366, 5301, 1570, 421, 276, 3361, 527, 6637, 4861, 2401, 7522, 5808, 9371, 5298, 2045, 5096, 5447, 7755, 5115, 7060, 8529, 4078, 1943, 1697, 1764, 5453, 7085, 960, 2405, 739, 2100, 5800, 728, 9737, 5704, 5693, 1431, 8979, 6428, 673, 7540, 6, 7773, 5857, 6823, 150, 5869, 8486, 684, 5816, 9626, 7451, 5579, 8260, 3397, 5322, 6920, 1879, 2127, 2884, 5478, 4977, 9016, 6165, 6292, 3062, 5671, 5968, 78, 4619, 4763,
9905, 7127, 9390, 5185, 6923, 3721, 9164, 9705, 4341, 1031, 1046, 5127, 7376, 6528, 3248, 4941, 1178, 7889, 3364, 4486, 5358, 9402, 9158, 8600, 1025, 874, 1839, 1783, 309, 9030, 1843, 845, 8398, 1433, 7118, 70, 8071, 2877, 3904, 8866, 6722, 4299, 10, 1929, 5897, 4188, 600, 1889, 3325, 2485, 6473, 4474, 7444, 6992, 4846, 6166, 4441, 2283, 2629, 4352, 7775, 1101, 2214, 9985, 215, 8270, 9750, 2740, 8361, 7103, 5930, 8664, 9690, 8302, 9267, 344, 2077, 1372, 1880, 9550,
5825, 8517, 7769, 2405, 8204, 1060, 3603, 7025, 478, 8334, 1997, 3692, 7433, 9101, 7294, 7498, 9415, 5452, 3850, 3508, 6857, 9213, 6807, 4412, 7310, 854, 5384, 686, 4978, 892, 8651, 3241, 2743, 3801, 3813, 8588, 6701, 4416, 6990, 6490, 3197, 6838, 6503, 114, 8343, 5844, 8646, 8694, 65, 791, 5979, 2687, 2621, 2019, 8097, 1423, 3644, 9764, 4921, 3266, 3662, 5561, 2476, 8271, 8138, 6147, 1168, 3340, 1998, 9874, 6572, 9873, 6659, 5609, 2711, 3931, 9567, 4143, 7833, 8887,
6223, 2099, 2700, 589, 4716, 8333, 1362, 5007, 2753, 2848, 4441, 8397, 7192, 8191, 4916, 9955, 6076, 3370, 6396, 6971, 3156, 248, 3911, 2488, 4930, 2458, 7183, 5455, 170, 6809, 6417, 3390, 1956, 7188, 577, 7526, 2203, 968, 8164, 479, 8699, 7915, 507, 6393, 4632, 1597, 7534, 3604, 618, 3280, 6061, 9793, 9238, 8347, 568, 9645, 2070, 5198, 6482, 5000, 9212, 6655, 5961, 7513, 1323, 3872, 6170, 3812, 4146, 2736, 67, 3151, 5548, 2781, 9679, 7564, 5043, 8587, 1893, 4531,
5826, 3690, 6724, 2121, 9308, 6986, 8106, 6659, 2142, 1642, 7170, 2877, 5757, 6494, 8026, 6571, 8387, 9961, 6043, 9758, 9607, 6450, 8631, 8334, 7359, 5256, 8523, 2225, 7487, 1977, 9555, 8048, 5763, 2414, 4948, 4265, 2427, 8978, 8088, 8841, 9208, 9601, 5810, 9398, 8866, 9138, 4176, 5875, 7212, 3272, 6759, 5678, 7649, 4922, 5422, 1343, 8197, 3154, 3600, 687, 1028, 4579, 2084, 9467, 4492, 7262, 7296, 6538, 7657, 7134, 2077, 1505, 7332, 6890, 8964, 4879, 7603, 7400, 5973, 739,
1861, 1613, 4879, 1884, 7334, 966, 2000, 7489, 2123, 4287, 1472, 3263, 4726, 9203, 1040, 4103, 6075, 6049, 330, 9253, 4062, 4268, 1635, 9960, 577, 1320, 3195, 9628, 1030, 4092, 4979, 6474, 6393, 2799, 6967, 8687, 7724, 7392, 9927, 2085, 3200, 6466, 8702, 265, 7646, 8665, 7986, 7266, 4574, 6587, 612, 2724, 704, 3191, 8323, 9523, 3002, 704, 5064, 3960, 8209, 2027, 2758, 8393, 4875, 4641, 9584, 6401, 7883, 7014, 768, 443, 5490, 7506, 1852, 2005, 8850, 5776, 4487, 4269,
4052, 6687, 4705, 7260, 6645, 6715, 3706, 5504, 8672, 2853, 1136, 8187, 8203, 4016, 871, 1809, 1366, 4952, 9294, 5339, 6872, 2645, 6083, 7874, 3056, 5218, 7485, 8796, 7401, 3348, 2103, 426, 8572, 4163, 9171, 3176, 948, 7654, 9344, 3217, 1650, 5580, 7971, 2622, 76, 2874, 880, 2034, 9929, 1546, 2659, 5811, 3754, 7096, 7436, 9694, 9960, 7415, 2164, 953, 2360, 4194, 2397, 1047, 2196, 6827, 575, 784, 2675, 8821, 6802, 7972, 5996, 6699, 2134, 7577, 2887, 1412, 4349, 4380,
4629, 2234, 6240, 8132, 7592, 3181, 6389, 1214, 266, 1910, 2451, 8784, 2790, 1127, 6932, 1447, 8986, 2492, 5476, 397, 889, 3027, 7641, 5083, 5776, 4022, 185, 3364, 5701, 2442, 2840, 4160, 9525, 4828, 6602, 2614, 7447, 3711, 4505, 7745, 8034, 6514, 4907, 2605, 7753, 6958, 7270, 6936, 3006, 8968, 439, 2326, 4652, 3085, 3425, 9863, 5049, 5361, 8688, 297, 7580, 8777, 7916, 6687, 8683, 7141, 306, 9569, 2384, 1500, 3346, 4601, 7329, 9040, 6097, 2727, 6314, 4501, 4974, 2829,
8316, 4072, 2025, 6884, 3027, 1808, 5714, 7624, 7880, 8528, 4205, 8686, 7587, 3230, 1139, 7273, 6163, 6986, 3914, 9309, 1464, 9359, 4474, 7095, 2212, 7302, 2583, 9462, 7532, 6567, 1606, 4436, 8981, 5612, 6796, 4385, 5076, 2007, 6072, 3678, 8331, 1338, 3299, 8845, 4783, 8613, 4071, 1232, 6028, 2176, 3990, 2148, 3748, 103, 9453, 538, 6745, 9110, 926, 3125, 473, 5970, 8728, 7072, 9062, 1404, 1317, 5139, 9862, 6496, 6062, 3338, 464, 1600, 2532, 1088, 8232, 7739, 8274, 3873,
2341, 523, 7096, 8397, 8301, 6541, 9844, 244, 4993, 2280, 7689, 4025, 4196, 5522, 7904, 6048, 2623, 9258, 2149, 9461, 6448, 8087, 7245, 1917, 8340, 7127, 8466, 5725, 6996, 3421, 5313, 512, 9164, 9837, 9794, 8369, 4185, 1488, 7210, 1524, 1016, 4620, 9435, 2478, 7765, 8035, 697, 6677, 3724, 6988, 5853, 7662, 3895, 9593, 1185, 4727, 6025, 5734, 7665, 3070, 138, 8469, 6748, 6459, 561, 7935, 8646, 2378, 462, 7755, 3115, 9690, 8877, 3946, 2728, 8793, 244, 6323, 8666, 4271,
6430, 2406, 8994, 56, 1267, 3826, 9443, 7079, 7579, 5232, 6691, 3435, 6718, 5698, 4144, 7028, 592, 2627, 217, 734, 6194, 8156, 9118, 58, 2640, 8069, 4127, 3285, 694, 3197, 3377, 4143, 4802, 3324, 8134, 6953, 7625, 3598, 3584, 4289, 7065, 3434, 2106, 7132, 5802, 7920, 9060, 7531, 3321, 1725, 1067, 3751, 444, 5503, 6785, 7937, 6365, 4803, 198, 6266, 8177, 1470, 6390, 1606, 2904, 7555, 9834, 8667, 2033, 1723, 5167, 1666, 8546, 8152, 473, 4475, 6451, 7947, 3062, 3281,
2810, 3042, 7759, 1741, 2275, 2609, 7676, 8640, 4117, 1958, 7500, 8048, 1757, 3954, 9270, 1971, 4796, 2912, 660, 5511, 3553, 1012, 5757, 4525, 6084, 7198, 8352, 5775, 7726, 8591, 7710, 9589, 3122, 4392, 6856, 5016, 749, 2285, 3356, 7482, 9956, 7348, 2599, 8944, 495, 3462, 3578, 551, 4543, 7207, 7169, 7796, 1247, 4278, 6916, 8176, 3742, 8385, 2310, 1345, 8692, 2667, 4568, 1770, 8319, 3585, 4920, 3890, 4928, 7343, 5385, 9772, 7947, 8786, 2056, 9266, 3454, 2807, 877, 2660,
6206, 8252, 5928, 5837, 4177, 4333, 207, 7934, 5581, 9526, 8906, 1498, 8411, 2984, 5198, 5134, 2464, 8435, 8514, 8674, 3876, 599, 5327, 826, 2152, 4084, 2433, 9327, 9697, 4800, 2728, 3608, 3849, 3861, 3498, 9943, 1407, 3991, 7191, 9110, 5666, 8434, 4704, 6545, 5944, 2357, 1163, 4995, 9619, 6754, 4200, 9682, 6654, 4862, 4744, 5953, 6632, 1054, 293, 9439, 8286, 2255, 696, 8709, 1533, 1844, 6441, 430, 1999, 6063, 9431, 7018, 8057, 2920, 6266, 6799, 356, 3597, 4024, 6665,
3847, 6356, 8541, 7225, 2325, 2946, 5199, 469, 5450, 7508, 2197, 9915, 8284, 7983, 6341, 3276, 3321, 16, 1321, 7608, 5015, 3362, 8491, 6968, 6818, 797, 156, 2575, 706, 9516, 5344, 5457, 9210, 5051, 8099, 1617, 9951, 7663, 8253, 9683, 2670, 1261, 4710, 1068, 8753, 4799, 1228, 2621, 3275, 6188, 4699, 1791, 9518, 8701, 5932, 4275, 6011, 9877, 2933, 4182, 6059, 2930, 6687, 6682, 9771, 654, 9437, 3169, 8596, 1827, 5471, 8909, 2352, 123, 4394, 3208, 8756, 5513, 6917, 2056,
5458, 8173, 3138, 3290, 4570, 4892, 3317, 4251, 9699, 7973, 1163, 1935, 5477, 6648, 9614, 5655, 9592, 975, 9118, 2194, 7322, 8248, 8413, 3462, 8560, 1907, 7810, 6650, 7355, 2939, 4973, 6894, 3933, 3784, 3200, 2419, 9234, 4747, 2208, 2207, 1945, 2899, 1407, 6145, 8023, 3484, 5688, 7686, 2737, 3828, 3704, 9004, 5190, 9740, 8643, 8650, 5358, 4426, 1522, 1707, 3613, 9887, 6956, 2447, 2762, 833, 1449, 9489, 2573, 1080, 4167, 3456, 6809, 2466, 227, 7125, 2759, 6250, 6472, 8089,
3266, 7025, 9756, 3914, 1265, 9116, 7723, 9788, 6805, 5493, 2092, 8688, 6592, 9173, 4431, 4028, 6007, 7131, 4446, 4815, 3648, 6701, 759, 3312, 8355, 4485, 4187, 5188, 8746, 7759, 3528, 2177, 5243, 8379, 3838, 7233, 4607, 9187, 7216, 2190, 6967, 2920, 6082, 7910, 5354, 3609, 8958, 6949, 7731, 494, 8753, 8707, 1523, 4426, 3543, 7085, 647, 6771, 9847, 646, 5049, 824, 8417, 5260, 2730, 5702, 2513, 9275, 4279, 2767, 8684, 1165, 9903, 4518, 55, 9682, 8963, 6005, 2102, 6523,
1998, 8731, 936, 1479, 5259, 7064, 4085, 91, 7745, 7136, 3773, 3810, 730, 8255, 2705, 2653, 9790, 6807, 2342, 355, 9344, 2668, 3690, 2028, 9679, 8102, 574, 4318, 6481, 9175, 5423, 8062, 2867, 9657, 7553, 3442, 3920, 7430, 3945, 7639, 3714, 3392, 2525, 4995, 4850, 2867, 7951, 9667, 486, 9506, 9888, 781, 8866, 1702, 3795, 90, 356, 1483, 4200, 2131, 6969, 5931, 486, 6880, 4404, 1084, 5169, 4910, 6567, 8335, 4686, 5043, 2614, 3352, 2667, 4513, 6472, 7471, 5720, 1616,
8878, 1613, 1716, 868, 1906, 2681, 564, 665, 5995, 2474, 7496, 3432, 9491, 9087, 8850, 8287, 669, 823, 347, 6194, 2264, 2592, 7871, 7616, 8508, 4827, 760, 2676, 4660, 4881, 7572, 3811, 9032, 939, 4384, 929, 7525, 8419, 5556, 9063, 662, 8887, 7026, 8534, 3111, 1454, 2082, 7598, 5726, 6687, 9647, 7608, 73, 3014, 5063, 670, 5461, 5631, 3367, 9796, 8475, 7908, 5073, 1565, 5008, 5295, 4457, 1274, 4788, 1728, 338, 600, 8415, 8535, 9351, 7750, 6887, 5845, 1741, 125,
3637, 6489, 9634, 9464, 9055, 2413, 7824, 9517, 7532, 3577, 7050, 6186, 6980, 9365, 9782, 191, 870, 2497, 8498, 2218, 2757, 5420, 6468, 586, 3320, 9230, 1034, 1393, 9886, 5072, 9391, 1178, 8464, 8042, 6869, 2075, 8275, 3601, 7715, 9470, 8786, 6475, 8373, 2159, 9237, 2066, 3264, 5000, 679, 355, 3069, 4073, 494, 2308, 5512, 4334, 9438, 8786, 8637, 9774, 1169, 1949, 6594, 6072, 4270, 9158, 7916, 5752, 6794, 9391, 6301, 5842, 3285, 2141, 3898, 8027, 4310, 8821, 7079, 1307,
8497, 6681, 4732, 7151, 7060, 5204, 9030, 7157, 833, 5014, 8723, 3207, 9796, 9286, 4913, 119, 5118, 7650, 9335, 809, 3675, 2597, 5144, 3945, 5090, 8384, 187, 4102, 1260, 2445, 2792, 4422, 8389, 9290, 50, 1765, 1521, 6921, 8586, 4368, 1565, 5727, 7855, 2003, 4834, 9897, 5911, 8630, 5070, 1330, 7692, 7557, 7980, 6028, 5805, 9090, 8265, 3019, 3802, 698, 9149, 5748, 1965, 9658, 4417, 5994, 5584, 8226, 2937, 272, 5743, 1278, 5698, 8736, 2595, 6475, 5342, 6596, 1149, 6920,
8188, 8009, 9546, 6310, 8772, 2500, 9846, 6592, 6872, 3857, 1307, 8125, 7042, 1544, 6159, 2330, 643, 4604, 7899, 6848, 371, 8067, 2062, 3200, 7295, 1857, 9505, 6936, 384, 2193, 2190, 301, 8535, 5503, 1462, 7380, 5114, 4824, 8833, 1763, 4974, 8711, 9262, 6698, 3999, 2645, 6937, 7747, 1128, 2933, 3556, 7943, 2885, 3122, 9105, 5447, 418, 2899, 5148, 3699, 9021, 9501, 597, 4084, 175, 1621, 1, 1079, 6067, 5812, 4326, 9914, 6633, 5394, 4233, 6728, 9084, 1864, 5863, 1225,
9935, 8793, 9117, 1825, 9542, 8246, 8437, 3331, 9128, 9675, 6086, 7075, 319, 1334, 7932, 3583, 7167, 4178, 1726, 7720, 695, 8277, 7887, 6359, 5912, 1719, 2780, 8529, 1359, 2013, 4498, 8072, 1129, 9998, 1147, 8804, 9405, 6255, 1619, 2165, 7491, 1, 8882, 7378, 3337, 503, 5758, 4109, 3577, 985, 3200, 7615, 8058, 5032, 1080, 6410, 6873, 5496, 1466, 2412, 9885, 5904, 4406, 3605, 8770, 4361, 6205, 9193, 1537, 9959, 214, 7260, 9566, 1685, 100, 4920, 7138, 9819, 5637, 976,
3466, 9854, 985, 1078, 7222, 8888, 5466, 5379, 3578, 4540, 6853, 8690, 3728, 6351, 7147, 3134, 6921, 9692, 857, 3307, 4998, 2172, 5783, 3931, 9417, 2541, 6299, 13, 787, 2099, 9131, 9494, 896, 8600, 1643, 8419, 7248, 2660, 2609, 8579, 91, 6663, 5506, 7675, 1947, 6165, 4286, 1972, 9645, 3805, 1663, 1456, 8853, 5705, 9889, 7489, 1107, 383, 4044, 2969, 3343, 152, 7805, 4980, 9929, 5033, 1737, 9953, 7197, 9158, 4071, 1324, 473, 9676, 3984, 9680, 3606, 8160, 7384, 5432,
1005, 4512, 5186, 3953, 2164, 3372, 4097, 3247, 8697, 3022, 9896, 4101, 3871, 6791, 3219, 2742, 4630, 6967, 7829, 5991, 6134, 1197, 1414, 8923, 8787, 1394, 8852, 5019, 7768, 5147, 8004, 8825, 5062, 9625, 7988, 1110, 3992, 7984, 9966, 6516, 6251, 8270, 421, 3723, 1432, 4830, 6935, 8095, 9059, 2214, 6483, 6846, 3120, 1587, 6201, 6691, 9096, 9627, 6671, 4002, 3495, 9939, 7708, 7465, 5879, 6959, 6634, 3241, 3401, 2355, 9061, 2611, 7830, 3941, 2177, 2146, 5089, 7079, 519, 6351,
7280, 8586, 4261, 2831, 7217, 3141, 9994, 9940, 5462, 2189, 4005, 6942, 9848, 5350, 8060, 6665, 7519, 4324, 7684, 657, 9453, 9296, 2944, 6843, 7499, 7847, 1728, 9681, 3906, 6353, 5529, 2822, 3355, 3897, 7724, 4257, 7489, 8672, 4356, 3983, 1948, 6892, 7415, 4153, 5893, 4190, 621, 1736, 4045, 9532, 7701, 3671, 1211, 1622, 3176, 4524, 9317, 7800, 5638, 6644, 6943, 5463, 3531, 2821, 1347, 5958, 3436, 1438, 2999, 994, 850, 4131, 2616, 1549, 3465, 5946, 690, 9273, 6954, 7991,
9517, 399, 3249, 2596, 7736, 2142, 1322, 968, 7350, 1614, 468, 3346, 3265, 7222, 6086, 1661, 5317, 2582, 7959, 4685, 2807, 2917, 1037, 5698, 1529, 3972, 8716, 2634, 3301, 3412, 8621, 743, 8001, 4734, 888, 7744, 8092, 3671, 8941, 1487, 5658, 7099, 2781, 99, 1932, 4443, 4756, 4652, 9328, 1581, 7855, 4312, 5976, 7255, 6480, 3996, 2748, 1973, 9731, 4530, 2790, 9417, 7186, 5303, 3557, 351, 7182, 9428, 1342, 9020, 7599, 1392, 8304, 2070, 9138, 7215, 2008, 9937, 1106, 7110,
7444, 769, 9688, 632, 1571, 6820, 8743, 4338, 337, 3366, 3073, 1946, 8219, 104, 4210, 6986, 249, 5061, 8693, 7960, 6546, 1004, 8857, 5997, 9352, 4338, 6105, 5008, 2556, 6518, 6694, 4345, 3727, 7956, 20, 3954, 8652, 4424, 9387, 2035, 8358, 5962, 5304, 5194, 8650, 8282, 1256, 1103, 2138, 6679, 1985, 3653, 2770, 2433, 4278, 615, 2863, 1715, 242, 3790, 2636, 6998, 3088, 1671, 2239, 957, 5411, 4595, 6282, 2881, 9974, 2401, 875, 7574, 2987, 4587, 3147, 6766, 9885, 2965,
3287, 3016, 3619, 6818, 9073, 6120, 5423, 557, 2900, 2015, 8111, 3873, 1314, 4189, 1846, 4399, 7041, 7583, 2427, 2864, 3525, 5002, 2069, 748, 1948, 6015, 2684, 438, 770, 8367, 1663, 7887, 7759, 1885, 157, 7770, 4520, 4878, 3857, 1137, 3525, 3050, 6276, 5569, 7649, 904, 4533, 7843, 2199, 5648, 7628, 9075, 9441, 3600, 7231, 2388, 5640, 9096, 958, 3058, 584, 5899, 8150, 1181, 9616, 1098, 8162, 6819, 8171, 1519, 1140, 7665, 8801, 2632, 1299, 9192, 707, 9955, 2710, 7314,
1772, 2963, 7578, 3541, 3095, 1488, 7026, 2634, 6015, 4633, 4370, 2762, 1650, 2174, 909, 8158, 2922, 8467, 4198, 4280, 9092, 8856, 8835, 5457, 2790, 8574, 9742, 5054, 9547, 4156, 7940, 8126, 9824, 7340, 8840, 6574, 3547, 1477, 3014, 6798, 7134, 435, 9484, 9859, 3031, 4, 1502, 4133, 1738, 1807, 4825, 463, 6343, 9701, 8506, 9822, 9555, 8688, 8168, 3467, 3234, 6318, 1787, 5591, 419, 6593, 7974, 8486, 9861, 6381, 6758, 194, 3061, 4315, 2863, 4665, 3789, 2201, 1492, 4416,
126, 8927, 6608, 5682, 8986, 6867, 1715, 6076, 3159, 788, 3140, 4744, 830, 9253, 5812, 5021, 7616, 8534, 1546, 9590, 1101, 9012, 9821, 8132, 7857, 4086, 1069, 7491, 2988, 1579, 2442, 4321, 2149, 7642, 6108, 250, 6086, 3167, 24, 9528, 7663, 2685, 1220, 9196, 1397, 5776, 1577, 1730, 5481, 977, 6115, 199, 6326, 2183, 3767, 5928, 5586, 7561, 663, 8649, 9688, 949, 5913, 9160, 1870, 5764, 9887, 4477, 6703, 1413, 4995, 5494, 7131, 2192, 8969, 7138, 3997, 8697, 646, 1028,
8074, 1731, 8245, 624, 4601, 8706, 155, 8891, 309, 2552, 8208, 8452, 2954, 3124, 3469, 4246, 3352, 1105, 4509, 8677, 9901, 4416, 8191, 9283, 5625, 7120, 2952, 8881, 7693, 830, 4580, 8228, 9459, 8611, 4499, 1179, 4988, 1394, 550, 2336, 6089, 6872, 269, 7213, 1848, 917, 6672, 4890, 656, 1478, 6536, 3165, 4743, 4990, 1176, 6211, 7207, 5284, 9730, 4738, 1549, 4986, 4942, 8645, 3698, 9429, 1439, 2175, 6549, 3058, 6513, 1574, 6988, 8333, 3406, 5245, 5431, 7140, 7085, 6407,
7845, 4694, 2530, 8249, 290, 5948, 5509, 1588, 5940, 4495, 5866, 5021, 4626, 3979, 3296, 7589, 4854, 1998, 5627, 3926, 8346, 6512, 9608, 1918, 7070, 4747, 4182, 2858, 2766, 4606, 6269, 4107, 8982, 8568, 9053, 4244, 5604, 102, 2756, 727, 5887, 2566, 7922, 44, 5986, 621, 1202, 374, 6988, 4130, 3627, 6744, 9443, 4568, 1398, 8679, 397, 3928, 9159, 367, 2917, 6127, 5788, 3304, 8129, 911, 2669, 1463, 9749, 264, 4478, 8940, 1109, 7309, 2462, 117, 4692, 7724, 225, 2312,
4164, 3637, 2000, 941, 8903, 39, 3443, 7172, 1031, 3687, 4901, 8082, 4945, 4515, 7204, 9310, 9349, 9535, 9940, 218, 1788, 9245, 2237, 1541, 5670, 6538, 6047, 5553, 9807, 8101, 1925, 8714, 445, 8332, 7309, 6830, 5786, 5736, 7306, 2710, 3034, 1838, 7969, 6318, 7912, 2584, 2080, 7437, 6705, 2254, 7428, 820, 782, 9861, 7596, 3842, 3631, 8063, 5240, 6666, 394, 4565, 7865, 4895, 9890, 6028, 6117, 4724, 9156, 4473, 4552, 602, 470, 6191, 4927, 5387, 884, 3146, 1978, 3000,
4258, 6880, 1696, 3582, 5793, 4923, 2119, 1155, 9056, 9698, 6603, 3768, 5514, 9927, 9609, 6166, 6566, 4536, 4985, 4934, 8076, 9062, 6741, 6163, 7399, 4562, 2337, 5600, 2919, 9012, 8459, 1308, 6072, 1225, 9306, 8818, 5886, 7243, 7365, 8792, 6007, 9256, 6699, 7171, 4230, 7002, 8720, 7839, 4533, 1671, 478, 7774, 1607, 2317, 5437, 4705, 7886, 4760, 6760, 7271, 3081, 2997, 3088, 7675, 6208, 3101, 6821, 6840, 122, 9633, 4900, 2067, 8546, 4549, 2091, 7188, 5605, 8599, 6758, 5229,
7854, 5243, 9155, 3556, 8812, 7047, 2202, 1541, 5993, 4600, 4760, 713, 434, 7911, 7426, 7414, 8729, 322, 803, 7960, 7563, 4908, 6285, 6291, 736, 3389, 9339, 4132, 8701, 7534, 5287, 3646, 592, 3065, 7582, 2592, 8755, 6068, 8597, 1982, 5782, 1894, 2900, 6236, 4039, 6569, 3037, 5837, 7698, 700, 7815, 2491, 7272, 5878, 3083, 6778, 6639, 3589, 5010, 8313, 2581, 6617, 5869, 8402, 6808, 2951, 2321, 5195, 497, 2190, 6187, 1342, 1316, 4453, 7740, 4154, 2959, 1781, 1482, 8256,
7178, 2046, 4419, 744, 8312, 5356, 6855, 8839, 319, 2962, 5662, 47, 6307, 8662, 68, 4813, 567, 2712, 9931, 1678, 3101, 8227, 6533, 4933, 6656, 92, 5846, 4780, 6256, 6361, 4323, 9985, 1231, 2175, 7178, 3034, 9744, 6155, 9165, 7787, 5836, 9318, 7860, 9644, 8941, 6480, 9443, 8188, 5928, 161, 6979, 2352, 5628, 6991, 1198, 8067, 5867, 6620, 3778, 8426, 2994, 3122, 3124, 6335, 3918, 8897, 2655, 9670, 634, 1088, 1576, 8935, 7255, 474, 8166, 7417, 9547, 2886, 5560, 3842,
6957, 3111, 26, 7530, 7143, 1295, 1744, 6057, 3009, 1854, 8098, 5405, 2234, 4874, 9447, 2620, 9303, 27, 7410, 969, 40, 2966, 5648, 7596, 8637, 4238, 3143, 3679, 7187, 690, 9980, 7085, 7714, 9373, 5632, 7526, 6707, 3951, 9734, 4216, 2146, 3602, 5371, 6029, 3039, 4433, 4855, 4151, 1449, 3376, 8009, 7240, 7027, 4602, 2947, 9081, 4045, 8424, 9352, 8742, 923, 2705, 4266, 3232, 2264, 6761, 363, 2651, 3383, 7770, 6730, 7856, 7340, 9679, 2158, 610, 4471, 4608, 910, 6241,
4417, 6756, 1013, 8797, 658, 8809, 5032, 8703, 7541, 846, 3357, 2920, 9817, 1745, 9980, 7593, 4667, 3087, 779, 3218, 6233, 5568, 4296, 2289, 2654, 7898, 5021, 9461, 5593, 8214, 9173, 4203, 2271, 7980, 2983, 5952, 9992, 8399, 3468, 1776, 3188, 9314, 1720, 6523, 2933, 621, 8685, 5483, 8986, 6163, 3444, 9539, 4320, 155, 3992, 2828, 2150, 6071, 524, 2895, 5468, 8063, 1210, 3348, 9071, 4862, 483, 9017, 4097, 6186, 9815, 3610, 5048, 1644, 1003, 9865, 9332, 2145, 1944, 2213,
9284, 3803, 4920, 1927, 6706, 4344, 7383, 4786, 9890, 2010, 5228, 1224, 3158, 6967, 8580, 8990, 8883, 5213, 76, 8306, 2031, 4980, 5639, 9519, 7184, 5645, 7769, 3259, 8077, 9130, 1317, 3096, 9624, 3818, 1770, 695, 2454, 947, 6029, 3474, 9938, 3527, 5696, 4760, 7724, 7738, 2848, 6442, 5767, 6845, 8323, 4131, 2859, 7595, 2500, 4815, 3660, 9130, 8580, 7016, 8231, 4391, 8369, 3444, 4069, 4021, 556, 6154, 627, 2778, 1496, 4206, 6356, 8434, 8491, 3816, 8231, 3190, 5575, 1015,
3787, 7572, 1788, 6803, 5641, 6844, 1961, 4811, 8535, 9914, 9999, 1450, 8857, 738, 4662, 8569, 6679, 2225, 7839, 8618, 286, 2648, 5342, 2294, 3205, 4546, 176, 8705, 3741, 6134, 8324, 8021, 7004, 5205, 7032, 6637, 9442, 5539, 5584, 4819, 5874, 5807, 8589, 6871, 9016, 983, 1758, 3786, 1519, 6241, 185, 8398, 495, 3370, 9133, 3051, 4549, 9674, 7311, 9738, 3316, 9383, 2658, 2776, 9481, 7558, 619, 3943, 3324, 6491, 4933, 153, 9738, 4623, 912, 3595, 7771, 7939, 1219, 4405,
2650, 3883, 4154, 5809, 315, 7756, 4430, 1788, 4451, 1631, 6461, 7230, 6017, 5751, 138, 588, 5282, 2442, 9110, 9035, 6349, 2515, 1570, 6122, 4192, 4174, 3530, 1933, 4186, 4420, 4609, 5739, 4135, 2963, 6308, 1161, 8809, 8619, 2796, 3819, 6971, 8228, 4188, 1492, 909, 8048, 2328, 6772, 8467, 7671, 9068, 2226, 7579, 6422, 7056, 8042, 3296, 2272, 3006, 2196, 7320, 3238, 3490, 3102, 37, 1293, 3212, 4767, 5041, 8773, 5794, 4456, 6174, 7279, 7054, 2835, 7053, 9088, 790, 6640,
3101, 1057, 7057, 3826, 6077, 1025, 2955, 1224, 1114, 6729, 5902, 4698, 6239, 7203, 9423, 1804, 4417, 6686, 1426, 6941, 8071, 1029, 4985, 9010, 6122, 6597, 1622, 1574, 3513, 1684, 7086, 5505, 3244, 411, 9638, 4150, 907, 9135, 829, 981, 1707, 5359, 8781, 9751, 5, 9131, 3973, 7159, 1340, 6955, 7514, 7993, 6964, 8198, 1933, 2797, 877, 3993, 4453, 8020, 9349, 8646, 2779, 8679, 2961, 3547, 3374, 3510, 1129, 3568, 2241, 2625, 9138, 5974, 8206, 7669, 7678, 1833, 8700, 4480,
4865, 9912, 8038, 8238, 782, 3095, 8199, 1127, 4501, 7280, 2112, 2487, 3626, 2790, 9432, 1475, 6312, 8277, 4827, 2218, 5806, 7132, 8752, 1468, 7471, 6386, 739, 8762, 8323, 8120, 5169, 9078, 9058, 3370, 9560, 7987, 8585, 8531, 5347, 9312, 1058, 4271, 1159, 5286, 5404, 6925, 8606, 9204, 7361, 2415, 560, 586, 4002, 2644, 1927, 2824, 768, 4409, 2942, 3345, 1002, 808, 4941, 6267, 7979, 5140, 8643, 7553, 9438, 7320, 4938, 2666, 4609, 2778, 8158, 6730, 3748, 3867, 1866, 7181,
171, 3771, 7134, 8927, 4778, 2913, 3326, 2004, 3089, 7853, 1378, 1729, 4777, 2706, 9578, 1360, 5693, 3036, 1851, 7248, 2403, 2273, 8536, 6501, 9216, 613, 9671, 7131, 7719, 6425, 773, 717, 8803, 160, 1114, 7554, 7197, 753, 4513, 4322, 8499, 4533, 2609, 4226, 8710, 6627, 644, 9666, 6260, 4870, 5744, 7385, 6542, 6203, 7703, 6130, 8944, 5589, 2262, 6803, 6381, 7414, 6888, 5123, 7320, 9392, 9061, 6780, 322, 8975, 7050, 5089, 1061, 2260, 3199, 1150, 1865, 5386, 9699, 6501,
3744, 8454, 6885, 8277, 919, 1923, 4001, 6864, 7854, 5519, 2491, 6057, 8794, 9645, 1776, 5714, 9786, 9281, 7538, 6916, 3215, 395, 2501, 9618, 4835, 8846, 9708, 2813, 3303, 1794, 8309, 7176, 2206, 1602, 1838, 236, 4593, 2245, 8993, 4017, 10, 8215, 6921, 5206, 4023, 5932, 6997, 7801, 262, 7640, 3107, 8275, 4938, 7822, 2425, 3223, 3886, 2105, 8700, 9526, 2088, 8662, 8034, 7004, 5710, 2124, 7164, 3574, 6630, 9980, 4242, 2901, 9471, 1491, 2117, 4562, 1130, 9086, 4117, 6698,
2810, 2280, 2331, 1170, 4554, 4071, 8387, 1215, 2274, 9848, 6738, 1604, 7281, 8805, 439, 1298, 8318, 7834, 9426, 8603, 6092, 7944, 1309, 8828, 303, 3157, 4638, 4439, 9175, 1921, 4695, 7716, 1494, 1015, 1772, 5913, 1127, 1952, 1950, 8905, 4064, 9890, 385, 9357, 7945, 5035, 7082, 5369, 4093, 6546, 5187, 5637, 2041, 8946, 1758, 7111, 6566, 1027, 1049, 5148, 7224, 7248, 296, 6169, 375, 1656, 7993, 2816, 3717, 4279, 4675, 1609, 3317, 42, 6201, 3100, 3144, 163, 9530, 4531,
7096, 6070, 1009, 4988, 3538, 5801, 7149, 3063, 2324, 2912, 7911, 7002, 4338, 7880, 2481, 7368, 3516, 2016, 7556, 2193, 1388, 3865, 8125, 4637, 4096, 8114, 750, 3144, 1938, 7002, 9343, 4095, 1392, 4220, 3455, 6969, 9647, 1321, 9048, 1996, 1640, 6626, 1788, 314, 9578, 6630, 2813, 6626, 4981, 9908, 7024, 4355, 3201, 3521, 3864, 3303, 464, 1923, 595, 9801, 3391, 8366, 8084, 9374, 1041, 8807, 9085, 1892, 9431, 8317, 9016, 9221, 8574, 9981, 9240, 5395, 2009, 6310, 2854, 9255,
8830, 3145, 2960, 9615, 8220, 6061, 3452, 2918, 6481, 9278, 2297, 3385, 6565, 7066, 7316, 5682, 107, 7646, 4466, 68, 1952, 9603, 8615, 54, 7191, 791, 6833, 2560, 693, 9733, 4168, 570, 9127, 9537, 1925, 8287, 5508, 4297, 8452, 8795, 6213, 7994, 2420, 4208, 524, 5915, 8602, 8330, 2651, 8547, 6156, 1812, 6271, 7991, 9407, 9804, 1553, 6866, 1128, 2119, 4691, 9711, 8315, 5879, 9935, 6900, 482, 682, 4126, 1041, 428, 6247, 3720, 5882, 7526, 2582, 4327, 7725, 3503, 2631,
2738, 9323, 721, 7434, 1453, 6294, 2957, 3786, 5722, 6019, 8685, 4386, 3066, 9057, 6860, 499, 5315, 3045, 5194, 7111, 3137, 9104, 941, 586, 3066, 755, 4177, 8819, 7040, 5309, 3583, 3897, 4428, 7788, 4721, 7249, 6559, 7324, 825, 7311, 3760, 6064, 6070, 9672, 4882, 584, 1365, 9739, 9331, 5783, 2624, 7889, 1604, 1303, 1555, 7125, 8312, 425, 8936, 3233, 7724, 1480, 403, 7440, 1784, 1754, 4721, 1569, 652, 3893, 4574, 5692, 9730, 4813, 9844, 8291, 9199, 7101, 3391, 8914,
6044, 2928, 9332, 3328, 8588, 447, 3830, 1176, 3523, 2705, 8365, 6136, 5442, 9049, 5526, 8575, 8869, 9031, 7280, 706, 2794, 8814, 5767, 4241, 7696, 78, 6570, 556, 5083, 1426, 4502, 3336, 9518, 2292, 1885, 3740, 3153, 9348, 9331, 8051, 2759, 5407, 9028, 7840, 9255, 831, 515, 2612, 9747, 7435, 8964, 4971, 2048, 4900, 5967, 8271, 1719, 9670, 2810, 6777, 1594, 6367, 6259, 8316, 3815, 1689, 6840, 9437, 4361, 822, 9619, 3065, 83, 6344, 7486, 8657, 8228, 9635, 6932, 4864,
8478, 4777, 6334, 4678, 7476, 4963, 6735, 3096, 5860, 1405, 5127, 7269, 7793, 4738, 227, 9168, 2996, 8928, 765, 733, 1276, 7677, 6258, 1528, 9558, 3329, 302, 8901, 1422, 8277, 6340, 645, 9125, 8869, 5952, 141, 8141, 1816, 9635, 4025, 4184, 3093, 83, 2344, 2747, 9352, 7966, 1206, 1126, 1826, 218, 7939, 2957, 2729, 810, 8752, 5247, 4174, 4038, 8884, 7899, 9567, 301, 5265, 5752, 7524, 4381, 1669, 3106, 8270, 6228, 6373, 754, 2547, 4240, 2313, 5514, 3022, 1040, 9738,
2265, 8192, 1763, 1369, 8469, 8789, 4836, 52, 1212, 6690, 5257, 8918, 6723, 6319, 378, 4039, 2421, 8555, 8184, 9577, 1432, 7139, 8078, 5452, 9628, 7579, 4161, 7490, 5159, 8559, 1011, 81, 478, 5840, 1964, 1334, 6875, 8670, 9900, 739, 1514, 8692, 522, 9316, 6955, 1345, 8132, 2277, 3193, 9773, 3923, 4177, 2183, 1236, 6747, 6575, 4874, 6003, 6409, 8187, 745, 8776, 9440, 7543, 9825, 2582, 7381, 8147, 7236, 5185, 7564, 6125, 218, 7991, 6394, 391, 7659, 7456, 5128, 5294,
2132, 8992, 8160, 5782, 4420, 3371, 3798, 5054, 552, 5631, 7546, 4716, 1332, 6486, 7892, 7441, 4370, 6231, 4579, 2121, 8615, 1145, 9391, 1524, 1385, 2400, 9437, 2454, 7896, 7467, 2928, 8400, 3299, 4025, 7458, 4703, 7206, 6358, 792, 6200, 725, 4275, 4136, 7390, 5984, 4502, 7929, 5085, 8176, 4600, 119, 3568, 76, 9363, 6943, 2248, 9077, 9731, 6213, 5817, 6729, 4190, 3092, 6910, 759, 2682, 8380, 1254, 9604, 3011, 9291, 5329, 9453, 9746, 2739, 6522, 3765, 5634, 1113, 5789,
5304, 5499, 564, 2801, 679, 2653, 1783, 3608, 7359, 7797, 3284, 796, 3222, 437, 7185, 6135, 8571, 2778, 7488, 5746, 678, 6140, 861, 7750, 803, 9859, 9918, 2425, 3734, 2698, 9005, 4864, 9818, 6743, 2475, 132, 9486, 3825, 5472, 919, 292, 4411, 7213, 7699, 6435, 9019, 6769, 1388, 802, 2124, 1345, 8493, 9487, 8558, 7061, 8777, 8833, 2427, 2238, 5409, 4957, 8503, 3171, 7622, 5779, 6145, 2417, 5873, 5563, 5693, 9574, 9491, 1937, 7384, 4563, 6842, 5432, 2751, 3406, 7981]

    l1 = l
    n = 80
    #n = 5
    min_sum = 10**6

    def isoutofbounds(y, x):
        if y < 1 or x < 1 or y > n or x > n:
            return True
        return False

    def get(l, y, x):
        if isoutofbounds(y, x):
            return 0
        return l[y * n + x - n - 1]

    def set_(l, y, x, v):
        l[y * n + x - n - 1] = v

    def get_min(y, x):
        if isoutofbounds(y, x):
            return 0
        if x == 1:
            return get(l1, y, x)
        v = get(min_sum, y, x)
        if v != 0:
            return v


        min_list = list()
        for y1 in range(1, y + 1):
            s = get_min(y1, x - 1)
            for y2 in range(y1, y):
                s += get(l1, y2, x)
            min_list.append(s)
        for y1 in range(y, n + 1):
            s = get_min(y1, x - 1)
            for y2 in range(y + 1, y1 + 1):
                s += get(l1, y2, x)
            min_list.append(s)

        for y1 in range(1, y + 1):
            s = get_min(y1, x + 1)
            for y2 in range(y1, y):
                s += get(l1, y2, x)
            min_list.append(s)
        for y1 in range(y, n + 1):
            s = get_min(y1, x + 1)
            for y2 in range(y + 1, y1 + 1):
                s += get(l1, y2, x)
            min_list.append(s)

        #left = get_min(y, x - 1)
        #up = get_min(y - 1, x)
        # down = 0
        minimum = sorted(filter(lambda x: x > 0, min_list))[0]
        v = get(l1, y, x) + minimum
       # print 'l1(%d, %d) = %d' % (y, x, get(l1, y, x)), 'min = ', v

        set_(min_sum, y, x, v)
        return v

    def solution_2():
        min_sum = list()
        for _i in range(len(l1)):
            min_sum.append(0)
        m = get_min(n, n)
        print m

    def solution_1():
        import networkx as nx
        G = nx.Graph()

        def get_node_num(y, x):
            return n * (y - 1) + x

        for y in range(1, n + 1):
            for x in range(1, n + 1):
                if y - 1 > 1:
                    G.add_edge(get_node_num(y - 1, x), get_node_num(y, x), weight = get(l1, y - 1, x) + get(l1, y, x))
                if y + 1 <= n:
                    G.add_edge(get_node_num(y + 1, x), get_node_num(y, x), weight = get(l1, y + 1, x) + get(l1, y, x))
                if x - 1 >= 1:
                    G.add_edge(get_node_num(y, x - 1), get_node_num(y, x), weight = get(l1, y, x - 1) + get(l1, y, x))
                if x + 1 <= n:
                    G.add_edge(get_node_num(y, x + 1), get_node_num(y, x), weight = get(l1, y, x + 1) + get(l1, y, x))

        import networkx.algorithms.shortest_paths
        sum = 0
        for n in networkx.algorithms.shortest_paths.generic.shortest_path(G, get_node_num(1, 1), get_node_num(n, n), True):
            sum += l1[n - 1]
        print sum



def problem_205(): # solved round(0.573144076783) = 0.5731441 

    cnt_1 = 0
    sum_freq_1 = dict()
    for i in range(9, 37):
        sum_freq_1[i] = 0
    for d1 in range(1, 5):
        for d2 in range(1, 5):
            for d3 in range(1, 5):
                for d4 in range(1, 5):
                    for d5 in range(1, 5):
                        for d6 in range(1, 5):
                            for d7 in range(1, 5):
                                for d8 in range(1, 5):
                                    for d9 in range(1, 5):
                                        cnt_1 += 1
                                        sum_freq_1[d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9] += 1

    cnt_2 = 0
    sum_freq_2 = dict()
    for i in range(6, 37):
        sum_freq_2[i] = 0
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                for d4 in range(1, 7):
                    for d5 in range(1, 7):
                        for d6 in range(1, 7):
                            cnt_2 += 1
                            sum_freq_2[d1 + d2 + d3 + d4 + d5 + d6] += 1

    print cnt_1
    print sum_freq_1
    print cnt_2
    print sum_freq_2
    print cnt_1 * cnt_2


    p = 0
    for sum_1 in range(9, 37):
        prob_sum = 0
        for sum_2 in range(6, sum_1):
            prob_sum += sum_freq_2[sum_2]
        p += sum_freq_1[sum_1] * prob_sum

    # print p * 10 ** 9 / (cnt_1 * cnt_2)
    print float(p) / float(cnt_1 * cnt_2)

def problem_204():
    primes = gen_primes(2, 100)
    cnt = 0
    limit = 10 ** 9 + 1
    for i in xrange(1, limit):
        c = i
        for p in primes:
            while c % p == 0 and c > 0:
                c /= p

        if c <= 1:
            cnt += 1
            print i, cnt

def problem_120(): # solved - 333082500

    s = 0
    for a in range(3, 1001):
        n = a / 2
        if a % 2 == 0:
            n -= 1
        rmax = 2 * n * a
        print 'a=%d n=%d, r=%d' % (a, n, rmax)
        s += rmax
    print s

def problem_123(): # solved 
    # for 10**9  n=7037 p=71059 p^2=5049381481 r=1000084366
    # for 10**10 n=21035 p=237737 p^2=56518881169 r=10001595590
    primes = gen_primes(2, 250000)
    for i, p in enumerate(primes):
        n = i + 1
        if n % 2 == 0:
            continue
        r = 2 * n * p
        if r > 10 ** 10:
            print "n=%d p=%d p^2=%d r=%d" % (n, p, p ** 2, r)
            break


def problem_95(): # solved 14316 (len = 27)

    def divisors_sum(n):
        s = 1
        k = math.sqrt(n)
        intk = int(k)
        if k == intk:
            s -= intk
        for i in xrange(2, intk + 1):
            if n % i == 0:
                s += i + n / i
        return s

    def print_chain(n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = divisors_sum(n)

        print seen

    limit = 10 ** 6

    max_len = 0
    max_elem = 0

    for i in xrange(2 , limit + 1):
        n = divisors_sum(i)
        chain_len = 0

        seen = set()
        while n != i and n > 1 and n < limit:
            seen.add(n)
            n = divisors_sum(n)
            if n in seen:
                break
            chain_len += 1

        if n == i and chain_len > max_len:
            max_len = chain_len
            max_elem = i
            print "New Max Chain: Len=%d elem=%d" % (max_len, max_elem)

    print_chain(max_elem)



def problem_96():  # solved - 24702

    example_grid = [ 0, 0, 3, 0, 2, 0, 6, 0, 0,
             9, 0, 0, 3, 0, 5, 0, 0, 1,
             0, 0, 1, 8, 0, 6, 4, 0, 0,
             0, 0, 8, 1, 0, 2, 9, 0, 0,
             7, 0, 0, 0, 0, 0, 0, 0, 8,
             0, 0, 6, 7, 0, 8, 2, 0, 0,
             0, 0, 2, 6, 0, 9, 5, 0, 0,
             8, 0, 0, 2, 0, 3, 0, 0, 9,
             0, 0, 5, 0, 1, 0, 3, 0, 0 ]

    def get_square_values(n):
        start_row = ((n - 1) / 3) * 3
        start_col = 3 * ((n - 1) % 3)
        l = list()
        for y in range(3):
            row = start_row + y
            idx = row * 9 + start_col
            l.extend(grid[idx:idx + 3])
        return l

    def get_row_values(n):
        return grid[(n - 1) * 9:(n - 1) * 9 + 9]

    def get_col_values(n):
        l = list()
        for i in range(9):
            l.append(grid[i * 9 + n - 1])
        return l

    def get_col(idx):
        return idx % 9 + 1

    def get_row(idx):
        return idx / 9 + 1

    def get_square(idx):
        return (idx / 27) * 3 + (idx % 9 / 3) + 1

    def solve(i):
        if i == 81:
            return True

        if grid[i] != 0:
            return solve(i + 1)

        square = get_square(i)
        row = get_row(i)
        col = get_col(i)
        digits_used = set(get_square_values(square) + get_row_values(row) + get_col_values(col))
        candidate_digits = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(digits_used)
        for candidate in candidate_digits:
            if candidate not in digits_used:
                grid[i] = candidate
                if solve(i + 1):
                    return True
        grid[i] = 0
        return False

    f = open("c:/sudoku.txt")
    s = 0
    cnt = 0    
    grid = []
    for l in f:
        cnt += 1
        if cnt % 10 == 1:
            print "Solving %d" % (1 + cnt / 10)
            continue

        grid.extend(map(int, l[:-1]))
        if cnt % 10 == 0:
            solve(0)
            s += grid[0] * 100 + grid[1] * 10 + grid[2]
            grid = []
    print s

def problem_131():

    def brute_force():
        #primes = gen_primes(1, 10 ** 6)
        #print len(primes)
        cnt = 0
        # 70066    
        ratio = 0.3
        a = 1
        while 1:
            if a % 10 not in [0, 2, 6]:
                a += 1
                continue

            afloat = float(a)
            acube = afloat ** 3

            n = max(math.floor(afloat * ratio), 1.0)

            while n < a:
                ncube = n ** 3
                p = math.floor((acube - ncube) / (n * n))
                lside = ncube + p * n * n
                #print "Testing %d" % p
                if acube - lside < 10.0:
                    # print "Checking if %d is prime" % p
                    nint = int(n)
                    pint = int((a ** 3 - nint ** 3) / n ** 2)
                    if nint ** 3 + pint * nint ** 2 == a ** 3 and isprime(pint):
                        cnt += 1
                        ratio = n / afloat
                        print cnt, pint, nint, a, '|', lside, '=', acube, ' new ratio: ', ratio
                        if p >= 10 ** 6:
                            print "Done"
                            return
                n += 1.0
            a += 1
        print cnt

    def hexagonal_solution(): # solved - 173
        n = 1
        cnt = 0
        while 1:
            hexa = 3 * n * (n - 1) + 1
            if hexa > 10 ** 6:
                break
            if isprime(hexa):
                cnt += 1
            n += 1
        print cnt

    hexagonal_solution()


def problem_91(): # solved - 14234

    def dot_product(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]

    def size_sqr(v1):
        return v1[0] * v1[0] + v1[1] * v1[1]

    limit = 2


    def solve(a, b, c):
        d = gcd(a, b)
        if d == 0:
            return (-1, -1)
        if c % d == 0:
            x, lastx = 0, 1
            y, lasty = 1, 0
            while b != 0:
                quotient = a / b
                a, b = b, a % b
                x, lastx = lastx - quotient * x, x
                y, lasty = lasty - quotient * y, y
            if c == 0:
                c = 1
            return (c * lastx, c * lasty)
        return (-1, -1)


    def isvalid(x1, y1):
        return not (x1 == 0 and y1 == 0) and x1 in range(0, limit + 1) and y1 in range(0, limit + 1)

    def all_solutions(x0, y0, a, b):
        gcdab = gcd(a, b)
        sol = []
        if gcdab != 0:
            for k in [0]: # [1]: % range(-limit * 2, limit * 2):
                X = x0 + k * b / gcdab
                Y = y0 - k * a / gcdab
                if isvalid(X, Y):
                    sol.append([X, Y])
        return sol

    def solutions1(x1, y1):
        a = x1
        b = y1
        c = a * a + b * b
        for c in [a * a + b + b, 0]:
            (x0, y0) = solve (a, b, c)
            print '(%d,%d) (%d,%d) (%d,%d)' % (0, 0, x1, y1, x0, y0)
            continue
            sol = all_solutions(x0, y0, a, b)
            for s in sol:
                print x1, y1, s[0], s[1]



    def solutions(v1):
        a = v1[0]
        b = v1[1]
        v2 = [-b, -a]
        gcdab = gcd(a, b)
        if gcdab != 0:
            for k in range(-10, 10):
                X = v2[0] + k * b / gcdab
                Y = v2[1] + k * a / gcdab
                if X in range(0, limit + 1) and Y in range(0, limit + 1):
                    print '%d,%d' % (X, Y)


    def linear_dependent(v1, v2):
        if v1[0] == 0 and v2[0] == 0:
            return True
        if v1[0] != 0:
            r = v2[0] / v1[0]
            return v1[1] * r == v2[1]
        if v1[1] != 0:
            r = v2[1] / v1[1]
            return v1[0] * r == v2[0]
        return False



    limit = 50
    s = set()
    cnt = 0
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    v1a = [x1, y1]
                    v2a = [x2, y2]

                    v1b = [-x1, -y1]
                    v2b = [x2 - x1, y2 - y1]

                    v1c = [-x2, -y2]
                    v2c = [x1 - x2, y1 - y2]

                    if size_sqr(v1a) == 0 or size_sqr(v2a) == 0 or size_sqr(v2b) == 0:
                        continue
                    a = linear_dependent(v1a, v2a)
                    b = linear_dependent(v1a, v2b)
                    c = linear_dependent(v2a, v2b)
                    if  a or b or c:
                        #  print "Linear: ", v1, v2, v3, a, b, c
                        continue
                    if dot_product(v1a, v2a) == 0 or dot_product(v1b, v2b) == 0 or dot_product(v1c, v2c) == 0:
                        u = [x1, y1]
                        v = [x2, y2]
                        if x1 > x2:
                            u, v = v, u
                        if x1 == x2 and y1 > y2:
                            u, v = v, u
                        key = '(%d,%d) (%d,%d)' % (u[0], u[1], v[0], v[1])
                        if key not in s:
                            cnt += 1
                            s.add(key)
                            print cnt, key

    myset = set()
    def addtoset(x1, y1, x2, y2):
        u = [x1, y1]
        v = [x2, y2]
        if x1 > x2:
            u, v = v, u
        key = '(%d,%d) (%d,%d)' % (u[0], u[1], v[0], v[1])
        myset.add(key)

    addtoset(0, 1, 1, 0)
    addtoset(1, 0, 1, 1)
    addtoset(0, 2, 1, 0)
    addtoset(1, 0, 1, 2)
    addtoset(0, 1, 2, 0)
    addtoset(1, 1, 2, 0)
    addtoset(2, 0, 2, 1)
    addtoset(0, 2, 2, 0)
    addtoset(2, 0, 2, 2)
    addtoset(0, 1, 1, 1)
    addtoset(0, 1, 2, 1)
    addtoset(0, 2, 1, 1)
    addtoset(0, 2, 1, 2)
    addtoset(0, 2, 2, 2)

    print len(s)
    #print myset
    #print len(myset), len(s)


def problem_103(): # solved [20, 31, 38, 39, 40, 42, 45]
    
    def is_special_sum_set(candidate_list):
        n = len(l)
        subset_sum = set()        
        sum_list = list()
        for i in range(n):
            minmax_dict = dict()
            minmax_dict['max'] = 0
            minmax_dict['min'] = 1000
            sum_list.append(minmax_dict)

        for i in range(n):
            for choice in itertools.combinations(candidate_list, i + 1):
                s = sum(choice)
                if sum_list[i]['max'] < s:
                    sum_list[i]['max'] = s
                if sum_list[i]['min'] > s:
                    sum_list[i]['min'] = s
                if s in subset_sum:
                    return False
                subset_sum.add(s)
        for i in range(n - 1):
            if sum_list[i]['max'] > sum_list[i + 1]['min']:
                return False

        return True
    
    for a in range(1, 100):
        for b in range(a + 1, 100):
            for c in range(b + 1, a + b):
                for d in range(c + 1, a + b):
                    if a + d == b + c or a + c == b + d:
                        continue
                    for e in range(d + 1, a + b):
                        if a + b + c < d + e:
                            continue
                        for f in range(e + 1, a + b):
                            if e + f > a + b + c:
                                continue
                            for g in range(f + 1, a + b):
                                if f + g > a + b + c:
                                    continue
                                l = [a, b, c, d, e, f, g]
                                if is_special_sum_set(l):
                                    print l
                                    return


def problem_105(): # solved 73702

    def is_special_sum_set(candidate_list):
        n = len(candidate_list)
        subset_sum = set()
        sum_list = list()
        for i in range(n):
            minmax_dict = dict()
            minmax_dict['max'] = 0
            minmax_dict['min'] = 10 ** 10
            sum_list.append(minmax_dict)

        for i in range(n):
            for choice in itertools.combinations(candidate_list, i + 1):
                s = sum(choice)
                if sum_list[i]['max'] < s:
                    sum_list[i]['max'] = s
                if sum_list[i]['min'] > s:
                    sum_list[i]['min'] = s
                if s in subset_sum:
                    print "subset sum %d already exists" % s
                    return False
                subset_sum.add(s)
        for i in range(n - 1):
            prev_max = sum_list[i]['max']
            curr_min = sum_list[i + 1]['min']
            if prev_max > curr_min:
                print "size=%d, prev_max (%d) > curr_min (%d)" % (i + 1, prev_max, curr_min)
                return False

        return True

    f = open('c:/sets.txt')
    s = 0
    i = 0
    for l in f:
        candidate = map(int, l.replace('\n', '').split(','))
        i += 1
        print "Checking candidate %d: " % i, candidate
        if is_special_sum_set(candidate):
            A = sum(candidate)
            print "Found ", candidate, A
            s += A


    print s

def problem_105_(): # solved 73702

    
    def is_special_sum_set(candidate_list):
        n = len(candidate_list)
        subset_sum = set()
        sum_list = list()
        for i in range(n):
            minmax_dict = dict()
            minmax_dict['max'] = 0
            minmax_dict['min'] = 10 ** 10
            sum_list.append(minmax_dict)

        for i in range(n):
            for choice in itertools.combinations(candidate_list, i + 1):
                s = sum(choice)
                if sum_list[i]['max'] < s:
                    sum_list[i]['max'] = s
                if sum_list[i]['min'] > s:
                    sum_list[i]['min'] = s
                if s in subset_sum:
                    print "subset sum %d already exists" % s
                    return False
                subset_sum.add(s)
        for i in range(n - 1):
            prev_max = sum_list[i]['max']
            curr_min = sum_list[i + 1]['min']
            if prev_max > curr_min:
                print "size=%d, prev_max (%d) > curr_min (%d)" % (i + 1, prev_max, curr_min)
                return False

        return True

    f = open('c:/sets.txt')
    s = 0
    i = 0
    for l in f:
        candidate = map(int, l.replace('\n', '').split(','))
        i += 1
        print "Checking candidate %d: " % i, candidate
        if is_special_sum_set(candidate):
            A = sum(candidate)
            print "Found ", candidate, A
            s += A


    print s

def problem_108():
    pass
    #===========================================================================
    # int num_distinct(long long n)
    # {
    #    int cnt = 2;
    #    long long nsqr = n*n;
    #    for (int k = 2; k < n; k++)
    #        if (nsqr % k == 0)
    #            cnt++;
    #    return cnt;
    # }
    # 
    # int main(void)
    # {
    #    int n = 2;
    #    while (1)
    #    {
    #        int cnt = num_distinct(n);
    #        printf("\n%d %d",n,cnt);
    #        if (cnt > 1000)
    #            break;
    #        n++;
    #    }
    #    return 0;
    # }
    #===========================================================================


def problem_118(): # solved - 44680    

    lll = list()
    for eight in range(1):
        for seven in range(1):
            for six in range(2):
                for five in range(2):
                    for four in range(3):
                        for three in range(4):
                            for two in range(5):
                                s = eight * 8 + seven * 7 + six * 6 + five * 5 + four * 4 + three * 3 + two * 2
                                nones = 9 - s
                                if s <= 9:
                                    o = []
                                    for _i_ in range(eight):
                                        o.append(8)
                                    for _i_ in range(seven):
                                        o.append(7)
                                    for _i_ in range(six):
                                        o.append(6)
                                    for _i_ in range(five):
                                        o.append(5)
                                    for _i_ in range(four):
                                        o.append(4)
                                    for _i in range(three):
                                        o.append(3)
                                    for _i in range(two):
                                        o.append(2)
                                    for _i in range(nones):
                                        o.append(1)
                                    lll.append(o)
    print len(lll), lll

    x_dig_primes = [[2, 3, 5, 7]]
    for ndig in range(2, 7):
        print ndig
        x_dig_primes.append([])
        for digits in itertools.combinations(range(1, 10), ndig):
            for p in itertools.permutations(digits):
                num = reduce(lambda x, y: x * 10 + y, p)
                s = set(p)
                if not 0 in s and len(s) == ndig and MillerRabin(num):
                    x_dig_primes[-1].append(num)

    def calculate_2(desc):

        d = dict()
        for l in desc:
            if not l in d:
                d[l] = 0
            d[l] += 1

        m = list()
        for k, v in d.items():
            m.append((k, v))
        # print m

        def calculate_1(set_desc, digits = None):
            if len(set_desc) == 0:
                return 1
            if digits == None:
                digits = set(range(1, 10))
            cnt = 0
            pair = set_desc[0]
            num_digs = pair[0]
            num_elements = pair[1]
            for c in itertools.combinations(x_dig_primes[num_digs - 1], num_elements):
                excluded_digits = set(map(int, map(str, reduce(lambda x, y: x + y, map(str, c)))))
                #print excluded_digits
                if len(excluded_digits) == num_elements * num_digs and len(digits.intersection(excluded_digits)) == len(excluded_digits):
                    new_digits = digits.difference(excluded_digits)
                    cnt += calculate_1(set_desc[1:], new_digits)
            return cnt

        return calculate_1(m)


    cnt = 0
    for k in lll:
        n = calculate_2(k)
        cnt += n
        print k, n, cnt
    print cnt
    # print calculate_2([4, 3, 1, 1])
    #k = [ [(4, 1), (3, 1), (2, 1)], [(4, 1), (3, 1), ]]
    #for l in k:
    #    print l, calculate_1(l)
    return

    def calculate(option):
        p_sets = set()

        def calc(o, digits, p_list):
            if len(o) == 0:
                key = ''
                for p in sorted(p_list):
                    key += '_' + str(p)
                #  print key
                p_sets.add(key)
                return
            cnt = 0
            element_size = o[0]
            for selected_digits in itertools.combinations(digits, element_size):
                excluded_digits = set()
                for d in selected_digits:
                    excluded_digits.add(d)
                new_digits = digits.difference(excluded_digits)
                for perm in itertools.permutations(selected_digits):
                    p = 0
                    for d in perm:
                        p = p * 10 + d
                    is_prime = False
                    if p < 10:
                        if p in [2, 3, 5, 7]:
                            is_prime = True
                    else:
                        if MillerRabin(p):
                            is_prime = True
                    if is_prime:
                        calc(o[1:], new_digits, p_list + [p])


        calc(option, set(range(1, 10)), [])
        return len(p_sets)





    def num_primes(n_dig, excluded_digits):
        cnt = 0
        digits = set(range(1, 10))
        digits.difference_update(excluded_digits)
        for perm in itertools.permutations(digits):
            # print perm
            p = ''
            for d in perm:
                p += str(d)
            p = int(p)
            if MillerRabin(p, 30):
                # print p
                cnt += 1
        return cnt

    cnt = 0
    cnt += 0 # num_primes(9, [])

    cnt += 4192 # num_primes(8, [2])
    cnt += 0 # num_primes(8, [3])
    cnt += 4097 # num_primes(8, [5])
    cnt += 3194 # num_primes(8, [7])


    def get_primes_1(n_dig, prime_list):
        total = 0
        for p in prime_list:
            excluded_digits = set(map(int, str(p)))
            n = num_primes(n_dig, excluded_digits)
            #     # print excluded_digits, n
            total += n
        return total


    total_7_2 = 8844 # get_primes_1(7, x_dig_primes[1])
    cnt += total_7_2

    total_7_1_1 = 2052 # calculate([1, 1, 7])
    cnt += total_7_1_1


def problem_203(): # solved - 34029210557338


    primes = gen_primes(2, 50)

    def factors(n):
        d = dict()
        for p in primes:
            cnt = 0
            while n >= 1 and n % p == 0:
                cnt += 1
                n /= p
            if cnt > 0:
                d[p] = cnt
            if n <= 1:
                break

        return d

    def add_factors(d1, d2):
        d = dict()
        for k in set(d1.keys() + d2.keys()):
            v = 0
            if k in d1:
                v += d1[k]
            if k in d2:
                v += d2[k]
            d[k] = v
        return d

    def sub_factors(d1, d2):
        d = dict()
        for k in d1.keys():
            v1 = d1[k]
            v2 = 0
            if k in d2:
                v2 = d2[k]
            v = v1 - v2
            if v < 0:
                raise
            if v != 0:
                d[k] = v

        return d

    factorials_dict = dict()
    def factorial_factors(n):
        if n <= 1:
            return factors(n)
        if n in factorials_dict:
            return factorials_dict[n]
        d = add_factors(factors(n), factorial_factors(n - 1))
        factorials_dict[n] = d
        return d

    def C(n, k):
        fact_n = factorial_factors(n)
        fact_k = factorial_factors(k)
        fact_n_k = factorial_factors(n - k)
        fact_n_minus_k = sub_factors(fact_n, fact_k)
        fact_n_minus_k_minus_n_k = sub_factors(fact_n_minus_k, fact_n_k)
        return fact_n_minus_k_minus_n_k

    def square_free(e):
        return len(e) == 0 or max(e.values()) < 2

    def calc_num(d):
        prod = 1
        for k in d:
            for _i in range(0, d[k]):
                prod *= k
        return prod

    l = set()
    for n in range(0, 50):
        s = '' + str(n)
        for k in range(0, n + 1):
            Cnk = C(n, k)
            number = calc_num(Cnk)
            if square_free(Cnk):
                l.add(number)
            s += ' ' + str(number)
        print s

    print l
    print sum(l)


def problem_231(): # - solved - 7526965179680

    primes = []
    def legndre(n):
        d = dict()
        for p in primes:
            if p > n:
                break
            test_p = p
            cnt = 0
            while test_p <= n:
                cnt += n / test_p
                test_p *= p
            if cnt > 0:
                d[p] = cnt
        return d

    def add_factors(d1, d2):
        d = dict()
        for k in set(d1.keys() + d2.keys()):
            v = 0
            if k in d1:
                v += d1[k]
            if k in d2:
                v += d2[k]
            d[k] = v
        return d

    def sub_factors(d1, d2):
        d = dict()
        for k in d1.keys():
            v1 = d1[k]
            v2 = 0
            if k in d2:
                v2 = d2[k]
            v = v1 - v2
            if v < 0:
                raise
            if v != 0:
                d[k] = v

        return d

    # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    factors_dict = dict()
    def factors(n):
        orgn = n
        d = dict()
        if n not in primes and n > 23 and MillerRabin(n):
            primes.append(n)
            d[n] = 1
            return d
        nsqrt = math.sqrt(n)
        for p in primes:
            cnt = 0
            if p > nsqrt:
                break
            while n >= 1 and n % p == 0:
                cnt += 1
                n /= p
            if cnt > 0:
                d[p] = cnt
            if n < 500000 and n in factors_dict:
                factors_dict[orgn] = add_factors(factors_dict[n], d)
                return factors_dict[orgn]
            if n <= 1:
                break

        if orgn < 500000:
            factors_dict[orgn] = d
        return d

    factorials_dict = dict()
    def factorial_factors(n):
        if n <= 1:
            return factors(n)
        if n in factorials_dict:
            return factorials_dict[n]
        d = add_factors(factors(n), factorial_factors(n - 1))
        factorials_dict[n] = d
        return d

    def calc_factorials(n, k):
        i = 0
        d = dict()
        f = factors(1)
        for i in xrange(2, n + 1):
            if i % 50000 == 0:
                print i
            f = add_factors(f, factors(i))
            if i == n or i == k or i == n - k:
                d[i] = f
        return d

    def C2(n, k):
        fact_n = legndre(n)
        fact_k = legndre(k)
        fact_n_k = legndre(n - k)
        fact_n_minus_k = sub_factors(fact_n, fact_k)
        fact_n_minus_k_minus_n_k = sub_factors(fact_n_minus_k, fact_n_k)
        return fact_n_minus_k_minus_n_k

    def C1(n, k):
        d = calc_factorials(n, k)
        fact_n = d[n]
        fact_k = d[k]
        fact_n_k = d[n - k]
        fact_n_minus_k = sub_factors(fact_n, fact_k)
        fact_n_minus_k_minus_n_k = sub_factors(fact_n_minus_k, fact_n_k)
        return fact_n_minus_k_minus_n_k

    def C(n, k):
        fact_n = factorial_factors(n)
        fact_k = factorial_factors(k)
        fact_n_k = factorial_factors(n - k)
        fact_n_minus_k = sub_factors(fact_n, fact_k)
        fact_n_minus_k_minus_n_k = sub_factors(fact_n_minus_k, fact_n_k)
        return fact_n_minus_k_minus_n_k

    #  print legndre(limit), legndre(15 * 10 ** 6), legndre(limit - 15 * 10 ** 6)
    #  print factors(10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2), factors(3 * 2), factors(7 * 6 * 5 * 4 * 3 * 2)
    N = 20 * 10 ** 6
    K = 15 * 10 ** 6
    #N = 10
    #K = 3
    primes = gen_primes(2, N)
    #print primes
    res = C2(N, K)
    s = 0
    for k in res:
        s += k * res[k]
    print s


def problem_142(): # solved 434657+420968+150568 = 1006193

    for a1 in xrange(1, 10 ** 6):
        a1sqr = a1 * a1
        start = 1
        if a1 % 2 == 0:
            start = 2
        print a1
        for a2 in xrange(start, a1, 2):
            a2sqr = a2 * a2
            #  print (a1sqr + a2sqr) / 2, (a1sqr - a2sqr) / 2
            a1a2sqrt = int(math.sqrt(a1sqr + a2sqr))
            for a3 in xrange(a2 + 1, a1a2sqrt):
                a3sqr = a3 * a3
                a4 = int(math.sqrt(a1sqr + a2sqr - a3sqr))
                if a4 == 0 or a3 <= a4:
                    continue
                a4sqr = a4 * a4
                if a1sqr + a2sqr == a3sqr + a4sqr and a4sqr != a2sqr:
                    #  if (a1sqr + a2sqr) % 2 != 0 or (a1sqr - a2sqr) % 2 != 0:
                    #      continue
                    X = float((a1sqr + a2sqr)) / float(2)
                    Y = float((a1sqr - a2sqr)) / float(2)
                    #     print "A", a1, a2, a3, a4, X, Y


                    if a1sqr - a2sqr + a3sqr - a4sqr < 0:
                        continue
                    a5 = int(math.sqrt((a1sqr - a2sqr + a3sqr - a4sqr) / 2))
                    if a1sqr - a2sqr - a3sqr + a4sqr < 0:
                        continue
                    a6 = int(math.sqrt((a1sqr - a2sqr - a3sqr + a4sqr) / 2))
                    a5sqr = a5 * a5
                    a6sqr = a6 * a6
                    if a5sqr + a6sqr == a1sqr - a2sqr:
                        print "B", (a1sqr + a2sqr) / 2, (a5sqr + a6sqr) / 2, (a3sqr - a4sqr) / 2
                        if a3sqr - a4sqr == a5sqr - a6sqr:
                            X = float((a1sqr + a2sqr)) / float(2)
                            Y = float((a5sqr + a6sqr)) / float(2)
                            Z = float((a3sqr - a4sqr)) / float(2)
                            print "C", X, Y, Z
                            if X > 0 and Y > 0 and Z > 0 and X > Y and Y > Z:
                                return

def problem_146(): # solved - 676333270

    s = 1242490
    l1 = 10 ** 6
    l2 = 150 * 10 ** 6
    prime_deltas = [1, 3, 7, 9, 13, 27]
    non_prime_deltas = [5, 11, 15, 17, 19, 21, 23, 25]
    joined_deltas = sorted(prime_deltas + non_prime_deltas)
    # 1242490 for n = 1..10**6
    for n in xrange(l1, l2): # int(math.sqrt(150 * 10 ** 6))):
        if n % 500000 == 0:
            print n
        nsqr = n * n
        seq_found = True
        for delta in joined_deltas:
            isP = MillerRabin(nsqr + delta, 4)
            if (delta in prime_deltas and not isP) or (delta in non_prime_deltas and isP):
                seq_found = False
                break
        if seq_found:
            s += n
            print n, s
    print s



def problem_86(): # solved : 1888
    
    def distance(a,b,c,x):
        return math.sqrt((a-x)**2+b**2) + math.sqrt(x**2+c**2)
    
    def is_int(n):
        return math.floor(n) == n
    
    
    def D1(a,b,c):
        A = a*a+b*b+2*b*c+c*c
        F1 = math.sqrt(A)*b 
        B = a*a+(b+c)*(b+c)
        F2 = math.sqrt(B)*c   
        return (F1+F2) / (b+c)
    
    def D2(a,b,c):
        fact_1_sqr = a*a+(b-c)*(b-c)
        fact_1 = math.sqrt(fact_1_sqr)                               
        return ((b+c)*fact_1)/(b-c)
    
    
    def is_min_distance_int(a,b,c):
        if b == c:
            return math.sqrt(a*a+4*b*b)       
    
        d = D1(a,b,c)
        if b>c:
            d = min(d,D2(a,b,c))
        return d
    
        A = float(-2*a*c**2)
        B = float(2*a*b*c)
        C = float(2*(b**2-c**2))
        x1 = (A+B)/C
        x2 = (A-B)/C
    
        d1 = a+b+c
        if x1 > 0:
            d1 = distance(a,b,c,x1)
    
        d2 = d1 + 1
        if x2 > 0:
            d2 = distance(a,b,c,x2)
    
        d_min = min(d1,d2)
        return d_min
           
    
    def calc(a,b,c):
        min_d = a+b+c+1    
        if b == c:
            fact_sqr = a*a+4*b*b
            fact = int(math.sqrt(fact_sqr))
            if fact*fact == fact_sqr:
                min_d = fact
        else:        
            if b > c:            
                fact_1_sqr = a*a+(b-c)*(b-c)
                fact_1 = int(math.sqrt(fact_1_sqr))           
                if fact_1**2 == fact_1_sqr:
                    if ((b+c)*fact_1) % (b-c) == 0:
                        min_d = min(min_d, ((b+c)*fact_1)/(b-c))
    
            fact_1_sqr = a*a+b*b+2*b*c+c*c
            fact_1 = int(math.sqrt(fact_1_sqr))
            fact_2_sqr = a*a+(b+c)*(b+c)
            fact_2 = int(math.sqrt(fact_2_sqr))        
            if fact_1**2 == fact_1_sqr and fact_2**2 == fact_2_sqr:
                if (fact_1*b+fact_2*c) % (b+c) == 0:
                    min_d = min(min_d, (fact_1*b+fact_2*c)/(b+c))
                        
        return min_d
        
    
                   
                               
    def X1(a,b,c):
        return float(a*c)/float(b+c)
    
    def X2(a,b,c):
        return float(a*c)/float(c-b)               
                   
    print X1(6,5,3), X2(6,5,3)
    print D1(6,5,3)
               
    print calc(6,5,3)
    #exit()
    I = calc
    K = is_min_distance_int
    
    M = 1000
    cnt = 0
    a = 0
    while 1:
        a += 1    
        for b in xrange(1, a+1):
            for c in xrange(b, a+1):
                #   v = [I(a,b,c),I(a,c,b),I(b,a,c),I(b,c,a),I(c,a,b),I(c,b,a)]
                #   d = min(I(a,b,c),I(a,c,b),I(b,a,c),I(b,c,a),I(c,a,b),I(c,b,a))
                #  v1 = [K(a,b,c),K(a,c,b),K(b,a,c),K(b,c,a),K(c,a,b),K(c,b,a)]
                d1 = min(K(a,b,c),K(a,c,b),K(b,a,c),K(b,c,a),K(c,a,b),K(c,b,a))
                #print a,b,c,d1
                #d = I(a,b,c)
                #d1 = K(a,b,c)            
                # print a,b,c,d,d1, d <= d1
                # if d <= d1: # a+b+c+1:
                if is_int(d1):
                    
                    cnt += 1
                    #   print cnt,a,b,c,d1
                    #print "#%d (%d,%d,%d) = (%d,%f)" % (cnt,a,b,c,d, d1)       
        print a,cnt
        if cnt > 10**6:
            exit()
    print cnt
    
def problem_111(): # solved - 612407567715

    import datetime    
    
    def A(num_digits,dig, num_reps):
        s = 0
        cnt = 0
        for c in itertools.combinations(range(num_digits),num_digits-num_reps):
            for other_digits in range(10**(num_digits-num_reps)):
                n = ''
                other = str(other_digits)
                while len(other) < (num_digits-num_reps):
                    other = '0' + other
                idx = 0
                for i in range(num_digits):
                    if i in c:
                        n += other[idx]
                        idx += 1                    
                    else:
                        n += str(dig)
                if n[0] == '0':
                    continue
                if len(n) <> num_digits:
                    print "Wrong: ",n
                print n
                if MillerRabin(int(n),1000):
                    print "Prime", n
                    cnt += 1
                    s += int(n)
        print s, cnt
        return s
        
    s = 0
    num_digits = 10
    for d in range(0,10):
        for num_reps in reversed(range(1,num_digits+1)):
            temp_sum = A(num_digits,d,num_reps)
            if temp_sum > 0:
                s += temp_sum
                break    
    
    print s
    return
        
        

    def num_reps(n):
        digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while n > 0:
            d = n % 10
            digits[d] += 1
            n = n / 10
        return digits

    dic = list()
    for x in range(10):
        dic.append(list())
        for _y in range(10):
            dic[x].append(0)

    ndigits = 4
    l1 = 10 ** (ndigits - 1)
    l2 = 10 ** ndigits - 1
   
    p = l1 - 1
    cnt = 0    
    while p <= l2 - 1:
        p += 2
        cnt += 1
        if cnt % 100000 == 0:
            print datetime.datetime.now(), cnt, p
                        
        if MillerRabin(p):
            digits = num_reps(p)
            for i, v in enumerate(digits):                
                dic[i][v] += p
    
    s = 0
    for d in range(10):
        n = ndigits
        while dic[d][n] == 0 and n >= 0:
            n -= 1
        if n >= 0:
            print d, n, dic[d][n]
            s += dic[d][n]
    print s


def problem_138(): # solved - 1118049290473932    
    n = 1
    m = 1
    cnt = 0
    s = 0
    while 1:         
        a = n*n - m*m
        b = 2*n*m
        c = n*n+m*m
        v = sorted([a,b,c])
        a,b,c = v[0], v[1], v[2]
        if abs(a*2-b) == 1:
            cnt += 1                
            print cnt, a,b,c,n,m
            m = n
            n*=4
            s += c
            if cnt == 12:
                break        
        n += 1
        
    print s
    return
        
def problem_197(): # solved - 1.710575329
    
    def f(x):
        ex = 30.403243784 - x*x
        a = math.pow(2,ex)
        floor_a = math.floor(a)
        res = floor_a*10**-9
        return res
    
    u = -1
    n = 0
    s = 0
    while n <= 10**2:
        print n,u
        u = f(u)
        if n >= 10**2-1:
            s += u
            print u,s
        n += 1


def problem_187(): # solved - 17427258
    
    primes = gen_primes(2,10000)
    max_idx = 1228
    num_comp = 1229 + 754606 # (C(1229,2))
    n = primes[-1]+2
    cnt = 0    
    while n < 50000000:
        if n % 3 != 0 and n % 5 != 0 and MillerRabin(n,5):
            while n * primes[max_idx] >= 10**8:
                max_idx -= 1
            num_comp += max_idx+1
            cnt += 1
            if cnt % 50000 == 0:
                print n,num_comp,primes[max_idx], max_idx
        n += 2
    
    print num_comp
    
    
def problem_235(): # solved - 11.002322108633
    
    def u(k,r):
        return (900-3*k)*math.pow(r,k-1)
    
    def s(n,r):
        _s = 0
        for i in xrange(1,n+1):
            _u = u(i,r)        
            _s += _u            
        return _s
    
    print '%1.30f' % s(5000,1.00232210863287607)                            
    # return 
    
    def my_formula(n,r): # formula looses accuracy
        P = math.pow(r,n)
        A = 900*(1-P)/(1-r)
        B = (1-P)/(1-r)*(1-r) - n*P/(1-r)
        return A-3*B
    
    print my_formula(2,2), s(2,2)
        
    r_top    = 1.04
    r_bottom = 1.00000000000001
    n = 0
    wanted = -600000000000
    while n < 100:        
        r_mid = r_top/2+r_bottom/2
        res_mid = s(5000,r_mid)
        print '%d (%1.60f+%1.60f)/2 = %1.60f %1.30f ' % (n,r_top,r_bottom, r_mid, res_mid )
        
        if res_mid > wanted:
            r_bottom = r_mid
        else:
            r_top = r_mid
        
        n += 1
    print '%1.12f %1.12f' % (r_mid, 1)
        
    print '%1.30f' % my_formula(5000,1.002301015375345993874134364887140691280364990234375000000000)
    
    
def problem_191(): # solved - 1918080160
    
    def A(day,WasLate,consecAbs):    
        if day == 30:
            #  print s                        
            return 1
        else:        
            r = A(day+1,WasLate,0)
            if not WasLate:
                r += A(day+1,True,0)
            if consecAbs < 2:
                r += A(day+1,WasLate,consecAbs+1)
            return r
        return 0            
    
    print A(0,False,0)
    
    
def problem_162(): # solved - 4420408745587516162 (3D58725572C62302)
    
    def A(pos,l,IsA,Is0,Is1):
        global cnt
        if pos == l:
            if IsA and Is0 and Is1:              
                return 1            
        else:
            if pos == l - 2 and not IsA and not Is0 and not Is1:
                return 0
            if IsA and Is0 and Is1:
                return 16**(l-pos)
            c = A(pos+1,l,True,Is0,Is1)
            if pos > 0:
                c += A(pos+1,l,IsA,True,Is1)
            c += A(pos+1,l,IsA,Is0,True)
            c += 13*A(pos+1,l,IsA,Is0,Is1)
            return c
        return 0
        
    s = 0
    for i in range(1,16+1):
        r = A(0,i,False,False,False)
        s += r
        print i,r,s
    print s
    
def problem_216(): # solved - 5437849
    
    def t(n):
        return 2*n*n-1
       
    n = 1
    cnt = 0
    while n <= 10**4:
        n += 1
        _t = t(n)
        if _t % 3 == 0 or _t % 5 == 0 or _t % 7 == 0:
            continue
        if MillerRabin(_t,10):
            cnt += 1
            if cnt % 1000 == 0:
                print cnt,n, _t                            
    print cnt


def problem_89(): # solved - 743

    def roman2num(s):
        s = 0
        prev = 1000
        for i in range(len(s)):
            v = 0
            if s[i] == 'M':
                v = 1000
            if s[i] == 'D':
                v = 500
            if s[i] == 'C':
                v = 100
            if s[i] == 'L':
                v = 50
            if s[i] == 'X':
                v = 10
            if s[i] == 'V':
                v = 5
            if s[i] == 'I':
                v = 1
            a = v
            if prev < v:
                v -= prev*2
            prev = a
            s += v
        return s

    def roman(n):
        def create(ch, n):
            s = ''
            for _i in range(1, n + 1):
                s += ch
            return s
        
        #=======================================================================
        # if n > 1000 and n % 1000 == 800:
        #    s += 'CMCM'
        #    n -= 1800
        #=======================================================================

        s = create('M', n / 1000)
        n = n % 1000
        if n >= 900:
            s += 'CM'
            n -= 900
        s += create('D', n / 500)
        n = n % 500
        if n >= 400:
            s += 'CD'
            n -= 400
        #=======================================================================
        # if n > 100 and n % 100 == 80:
        #    s += 'XCXC'
        #    n -= 180
        #=======================================================================
        s += create('C', n / 100)
        n = n % 100
        if n >= 90:
            s += 'XC'
            n -= 90
        s += create('L', n / 50)
        n = n % 50
        if n >= 40:
            s += 'XL'
            n -= 40
            
        #=======================================================================
        # if n > 10 and n % 10 == 8:
        #    s += 'IXIX'
        #    n -= 18
        #=======================================================================

        s += create('X', n / 10)
        n = n % 10
        if n == 9:
            s += 'IX'
            n -= 9
        s += create('V', n / 5)
        n = n % 5
        if n == 4:
            s += 'IV'
            n -= 4
        s += create('I', n)
        return s

    #  print roman(18)
    #  print roman(49)
    #  return
    f = open('e:/roman.txt')
    s = 0
    cnt = 0
    for line in f:
        cnt += 1
        line = line[:-1]
        num = roman2num(line)
        newroman = roman(num)
        diff = len(line) - len(newroman)
        s += diff
        print '#%04d %4d %s(%d) %s(%d) %d %d' % (cnt,num, line, len(line),newroman, len(newroman), diff, s)

    print s
    
def problem_243(): # solved - 892371480
    # primes = gen_primes(2,10**7)
    def prime_factors(n):
        if n in primes:
            return set([n])
        sqr_t = isqrt(n)        
        l = set()       
        for p in primes:
            if p > sqr_t:
                break        
            if n % p == 0:
                l.add(p)
                other = n/p
                if other in primes:
                    l.add(other)           
                
        return l
    
    totient_dict = dict()
    primes_set = set()
    primes_lst = []
    def mytotient(n):
        if n == 1:
            return 1
        if n in totient_dict:
            return totient_dict[n]
        if n in primes_set:
            totient_dict[n] = n - 1
            return n - 1
        if MillerRabin(n, 4):
            primes_set.add(n)
            primes_lst.append(n)
            totient_dict[n] = n - 1
            return n - 1

        totient_prod = 1
        calc_n = n
        for p in primes_lst:
            if p > calc_n:
                break
            prev = 0
            pexp = 1
            while calc_n % p == 0:
                prev = pexp
                pexp *= p
                calc_n = calc_n / p
            totient_prod *= pexp - prev
            if calc_n in totient_dict:
                v = totient_dict[calc_n] * totient_prod
                totient_dict[n] = v
                return v
        #  print "Crap"
        v = totient(n)
        totient_dict[n] = v
        return v 
    

    
    def R(d):
        if d in primes:
            return (1,1)
        cnt = 1
        #AAA = (d-1)*0.17
        #print AAA,d
        s = prime_factors(d)
        #print s
        for i in xrange(2,d):
            cont = False
            for p in s:
                if p > i:
                    break
                if i % p == 0:
                    cont = True
                    break
            if cont:
                continue
            
            cnt += 1
            if cnt > d/5:
                return (1,1)              
        return (cnt,d-1)
        
    primes = gen_primes(2,10000)        
    prod = 1
    _totient = 1
    #k = [2,3,5,7,11,13,17,19,23,27,29]
    ex = [3,1,1,1,1, 1, 1, 1, 1, 1, 1]
    for i,p in enumerate(primes):        
        prod *= p**ex[i]
        _totient *= (p-1)*p**(ex[i]-1)
            
        if _totient*94744 < 15499 * (prod-1):
            print prod
            print _totient
            print p
            break
    
    return 
        
    print mytotient(2*3*5*7*11),2*3*5*7*11,mytotient(2**11),2**11
    return
    # print R(12)
    # return
    d = 2
    # d = 1
    while 1:
        d += 2        
        a = (mytotient(d),d-1)
        if d % 1000 == 0:
            print a,d    
        # if a == (1,1):
        #     continue    
        if 94744*a[0] < 15499*a[1]:
        # if 10*a[0] < 4*a[1]:
            print a,d
            break

def problem_116(): # solved - 20492570929
    
    d = dict()
    def A(left,size):
        if left < 0:
            return 0
        if left == 0:
            return 1
        key = '%d_%d' % (left,size)
        if key in d:
            return d[key]       
        cnt = A(left-size,size)
        cnt += A(left-1,size)
        d[key] = cnt
        return cnt
    
    s = 0
    n = 50
    for i in range(2,5):
        s += A(n,i) - 1
    
    print s

def problem_114(): # solved - 16475640049
    
    d = dict()
    def A(left):
        if left < 0:            
            return 0
        if left == 0:                    
            return 1
        key = '%d' % (left)
        if key in d:
            return d[key]
        cnt = 0
        
        for s in range(3,left+1):
            new_left = 0
            if left > s:
                new_left = 1
            cnt += A(left-s-new_left)
        cnt += A(left-1)
        d[key] = cnt
        return cnt
    
    print A(50)
    
    
def problem_115(): # solved - 168
    
    d = dict()
    def A(m,left):
        if left < 0:            
            return 0
        if left == 0:                    
            return 1
        key = '%d' % (left)
        if key in d:
            return d[key]
        cnt = 0
        
        for s in range(m,left+1):
            new_left = 0
            if left > s:
                new_left = 1
            cnt += A(m,left-s-new_left)
        cnt += A(m,left-1)
        d[key] = cnt
        return cnt
    
    print A(50,168)


def problem_117(): # solved - 100808458960497
    
    d = dict()
    def A(left):
        if left < 0:
            return 0
        if left == 0:
            return 1
        key = '%d' % (left)
        if key in d:
            return d[key]
        cnt = 0
        for i in range(1,5):
            cnt += A(left-i)           
        d[key] = cnt
        return cnt
    
    print A(50)

def problem_173(): # solved - 1572729
    
    def ntiles(n):
        return n*4-4
            
    def calc(max_tiles):
        max_side = max_tiles/4 + 1        
        cnt = 0
        for inner_side_len in xrange(3,max_side+1):
            used_tiles = 0
            #outer_added = False
            for outer_side_len in xrange(inner_side_len,max_side+1,2):
                if used_tiles + ntiles(outer_side_len) > max_tiles:
                    break
                used_tiles += ntiles(outer_side_len)
                cnt += 1                            
                        
        return cnt
        
    print calc(10**6) 
    
    
def problem_164(): # solved - 378158756814587
    
    last_two_d = dict()
    def A1(left,allow_zero,update_dict,last2dig,lastdig):
        if left == 0:
            if update_dict:
                last_two_s = str(last2dig)+str(lastdig)
                if not last_two_s in last_two_d:
                    last_two_d[last_two_s] = 0
                last_two_d[last_two_s] += 1
            # print s
            return 1
        
        start = 0
        if not allow_zero:
            start = 1
        cnt = 0
        for d in range(start,9-last2dig-lastdig+1):
            cnt += A1(left-1,True,update_dict,lastdig,d)
        return cnt
    
    A1(10,False,True,0,0)    
    cnt = 0
    for k in last_two_d:
        cnt += last_two_d[k]*A1(10,True,False,int(k[0]),int(k[1]))
    print cnt
    
    
def problem_174(): # solved - 209566
    
    def ntiles(n):
        return n*4-4
            
    def calc(max_tiles):
        max_side = max_tiles/4 + 1        
        cnt = 0
        for inner_side_len in xrange(3,max_side+1):
            used_tiles = 0
            #outer_added = False
            for outer_side_len in xrange(inner_side_len,max_side+1,2):
                if used_tiles + ntiles(outer_side_len) > max_tiles:
                    break
                used_tiles += ntiles(outer_side_len)
            if used_tiles == max_tiles:
                cnt += 1                            
                        
        return cnt
        
    cnt = 0
    s = 0
    for t in xrange(1,10**6+1):
        r = calc(t)
        if r >= 1 and r <= 10:
            s += 1
        if r == 15:
            cnt += 1
            print cnt,t
    print cnt
    print s
    
def problem_172(): # solved - 227485267000992000
    
    d = dict()
    def A(left,d0,d1,d2,d3,d4,d5,d6,d7,d8,d9):
        v = sorted([d0,d1,d2,d3,d4,d5,d6,d7,d8,d9])
        for e in v:
            if e > 3:
                return 0           
        if left == 0:          
            return 1
        cnt = 0                
        key = '%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d' % (left,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9])
        if key in d:
            return d[key]
        if left < 18:
            cnt += A(left-1,d0+1,d1,d2,d3,d4,d5,d6,d7,d8,d9)        
        cnt += A(left-1,d0,d1+1,d2,d3,d4,d5,d6,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2+1,d3,d4,d5,d6,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3+1,d4,d5,d6,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4+1,d5,d6,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4,d5+1,d6,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4,d5,d6+1,d7,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4,d5,d6,d7+1,d8,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4,d5,d6,d7,d8+1,d9)
        cnt += A(left-1,d0,d1,d2,d3,d4,d5,d6,d7,d8,d9+1)
        d[key] = cnt
        return cnt
        
    print A(18,0,0,0,0,0,0,0,0,0,0)
    
def problem_166(): # solved - 7130034
    
    cnt = 0
    for first_row in xrange(0,9999+1):
        v = map(int,'%04d' % first_row)
        s = sum(v)
        d1,d2,d3,d4 = v[0],v[1],v[2],v[3]
        for first_col in xrange(0,99+1):
            v = map(int,'%02d' % first_col)
            d5,d9 = v[0],v[1]            
            d13 = s - d9 - d5 - d1
            if d13 > 9 or d13 < 0:
                continue
            for d10 in range(0,10):
                d7 = s - d4-d10-d13
                if d7 > 9 or d7 < 0:
                    continue
                for d6 in range(0,10):
                    d8 = s - d7-d6-d5
                    if d8 > 9 or d8 < 0:
                        continue
                    d14 = s - d10-d6-d2
                    if d14 > 9 or d14 < 0:
                        continue
                    for d11 in range(0,10):
                        d15 = s - d11-d7-d3
                        if d15 > 9 or d15 < 0:
                            continue
                        d16 = s - d13 - d14 - d15
                        if d16 > 9 or d16 < 0:
                            continue
                        d12 = s - d9-d10-d11
                        if d12 > 9 or d12 < 0:
                            continue
                        if d4+d8+d12+d16 != s or d1+d6+d11+d16 != s:
                            continue
                        cnt += 1
                        # print cnt
                        
                        if cnt % 10000 == 0:
                            print cnt,s

    print cnt

def problem_140(): # solved - 5673835352990
    
    def is_nugget(y):
        sq_r = 5*y*y+14*y+1
        sqr_t = isqrt(sq_r)
        return sqr_t*sqr_t == sq_r
    
    cnt = 0
    s = 0
    y = 1
    prev_nugget = 1
    while cnt < 30:
        if is_nugget(y):
            s += y
            cnt += 1
            ratio = float(y)/float(prev_nugget)
            print cnt,y,s,ratio
            prev_nugget = y
            if cnt > 10:
                if ratio > 2:
                    y = int(y*1.938748)
                else:
                    y = int(y*3.53532216)
        y += 1

def problem_137(): # solved - 1120149658760
    
    def is_nugget(y):
        sq_r = 5*y*y+2*y+1
        sqr_t = isqrt(sq_r)
        return sqr_t*sqr_t == sq_r
    
    cnt = 0
    #s = 0
    y = 1
    prev_nugget = 1
    while cnt < 15:
        if is_nugget(y):            
            cnt += 1
            ratio = float(y)/float(prev_nugget)
            print cnt,y,ratio
            prev_nugget = y
            if cnt > 4:
                y = int(y*6.8541019)            
        y += 1
def problem_90(): # solved - 1217
    def get_n(cube_rep):
        l = []
        cnt = 0
        k = 1
        while k <= 2**10-1:            
            if cube_rep & k == k:
                if cnt == 9:
                    cnt = 6
                l.append(cnt)
            k *= 2
            cnt += 1
        return l
    
        
    pairs = [ [0,1],[0,4],[0,6],[1,6],[2,5],[3,6],[4,6],[6,4],[8,1] ]
    def A(c1,c2):
        missing = []
        for p in pairs:
            p1 = p[0]
            p2 = p[1]
            if not ((p1 in c1 and p2 in c2) or (p1 in c2 and p2 in c1)):
                missing.append(p)
        return missing
    cnt = 0
    for cube1rep in range(0,2**10):
        c1 = get_n(cube1rep)
        if len(c1) != 6:
            continue            
        for cube2rep in range(cube1rep+1,2**10):            
            c2 = get_n(cube2rep)
            if len(c2) != 6:
                continue          
            missing = A(c1,c2)
            if len(missing) == 0:
                cnt += 1
    print cnt    

def problem_139(): # solved - 10057761  
    cnt = 0
    S = set()
    for n in xrange(1,7071):
        for m in xrange(1,n):             
            a = n*n - m*m
            b = 2*n*m
            c = n*n+m*m
            p = a+b+c
            if p < 10**8:
                v = sorted([a,b,c])
                if v[2] % (v[1]-v[0]) == 0:
                    for k in xrange(1,2+(10**8)/p):
                        if k*p < 10**8:
                            key = '%d_%d_%d' % (k*v[0],k*v[1],k*v[2])
                            S.add(key)                        
                    cnt += 1
                    if cnt % 100 == 0:
                        print cnt,v, p
    print cnt,len(S)
    
def problem_132(): # solved - 843296 
    
    cnt = 0
    s = 0
    e = 2 # don't count 3 because we're not dividing by 9
    while cnt < 40:
        e += 2
        if MillerRabin(e+1,5) and ipow(10,10**9,e+1) == 1: 
            cnt += 1
            s += e+1
            print cnt,e+1,s
            if cnt == 40:
                break
            
            
def problem_129(): # solved - 1000023
    
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
    
    def A(n):
        k = 1
        while 1:
            if ipow(10,k,9*n) == 1:
                return k
            #  print k
            k += 1
    
    n = 10**6-100
    cnt = 0
    while 1:
        if gcd(n,10) == 1:                                    
            res = A(n)
            cnt += 1
            if res > 10**5:            
                print n,res
            if res > 10**6:
                print n,res
                break
        n += 1
        
def problem_130(): # solved -  149253
    
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
    
    def A(n):
        k = 1
        while 1:
            if ipow(10,k,9*n) == 1:
                return k
            #  print k
            k += 1
    
    n = 4
    cnt = 0
    s = 0
    while 1:
        if gcd(n,10) == 1 and not MillerRabin(n,5):
            res = A(n)
            if (n-1) % res == 0:
                cnt += 1
                s += n
                print cnt, n,s
                if cnt == 25:
                    break            
        n += 1           
   
def problem_178(): # solved - 126461847755
    dic = dict()
    def A(left,d,d0,d9):        
        if left == 0:
            if d0 and d9:           
                return 1
            return 0
        if d < 0 or d > 9:
            return 0     
        
        key = '%d_%d_%d_%d' % (left,d,int(d0),int(d9))
        if key in dic:
            return dic[key]
                    
        cnt = 0        
        cnt += A(left-1,d-1,d0 or d == 0,d9 or d==9)
        if left > 1:
            cnt += A(left-1,d+1,d0 or d == 0,d9 or d==9)
        dic[key] = cnt
        return cnt        
          
    cnt = 0
    for n in range(10,41):        
        L = 0
        for d in range(1,10):            
            L += A(n,d,d==0,d==9)
        cnt += L
        print n,L, cnt
    print cnt
    
minsqr_110 = 0       
def problem_110(): # solved - 9350130049860600
    
    # x = ny/(y-n) --> y-n|ny --> y = n+k --> k | n^2  --> 
    # (k-1)/2 + 1 distinct solutions
    # 
    # to solve 108 replace 8*10**6 with 2000  
    
    p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    v = [10,10,10,10,10,10,10,10,10,2,2,2,2,2,2]        
    
    def calc_nsqr(p,v):
        A = 1
        for a,b in zip(p,v):
            A *= a**b
        return A
    
    global minsqr_110
    minsqr_110 = calc_nsqr(p,v)
    
    def calc_possibilities(v):
        A = 1
        for a in v:
            A *= (a+1)
        return A
    
    S = set()
    def G(p,v):
        key = ''
        for a in sorted(v):
            key += '_' + str(a)        
        if key in S:
            return
        S.add(key)
        global minsqr_110
        r = calc_possibilities(v)
        if r < 8*10**6:
            return        
        nsqr = calc_nsqr(p,v)    
        if minsqr_110 > nsqr:
            minsqr_110 = nsqr
            print nsqr,int(math.sqrt(nsqr)),r,v
        for i in reversed(range(len(v))):
            if v[i] > 0:
                v[i] -= 2
                G(p,v)
                v[i] += 2
          
    G(p,v)  
     
     
def problem_169(): # solved - 178653872807
    
    d = dict()
    def A(goal,weight,b):
        if goal > weight*4:
            return 0
        if goal == 0:      
            return 1
        if goal < 0 or weight == 0:
            return 0
        key = '%d_%d' % (goal,b)
        if key in d:
            return d[key]
        cnt = 0   
        for i in range(3):
            cnt += A(goal-i*weight,weight / 2,b-1)
        print key,cnt
        d[key] = cnt
        return cnt
        
    print A(10**25,2**86,86)
    
def problem_347(): # solved - 11109800204052
    L = 10000000
    primes = gen_primes(2,L/2)
    cut = 0
    sqrtL = math.sqrt(L)
    for p in primes:
        if p > sqrtL:
            break
        cut += 1
    
    def max_mul(p,q,N):
        logN = math.log(N)
        A1 = int(logN/math.log(p))
        A2 = int(logN/math.log(q))
        max_mult = 0
        for a1 in range(1,A1+1):
            for a2 in range(1,A2+1):
                n = p**a1 * q**a2
                if n > max_mult and n <= N:
                    max_mult = n
        return max_mult
                
    s = 0  
    for i in range(cut):
        for j in range(i+1,cut):         
            M = max_mul(primes[i],primes[j],L)     
            s += M     
       
    idx = cut        
    for p in primes[cut:]:
        while p*primes[idx] > L:
            idx -= 1
        for i in range(0,idx+1):
            M = max_mul(p,primes[i],L)
            s += M
    
    print s
    #  print len(S),sorted(S)
    return
                    
    N = L+1
    s = 0    
    
    CNT = 0
    dontcheck = set()
    S = set()
    while N > 1:
        cnt = 0
        N -= 1
        Nwork = N
        if N in dontcheck or N in primes:            
            continue                    
        last_pair = []
        for p in primes:
            if Nwork % p == 0:
                cnt += 1                
                if cnt > 2:
                    break      
                while Nwork % p == 0:                    
                    Nwork /= p
                last_pair.append( p )
                
            if Nwork == 1:
                break
        if cnt == 2:
            CNT += 1
            logN = math.log(N)
            p0,p1 = last_pair[0], last_pair[1]            
            A1 = int(logN/math.log(p0))
            A2 = int(logN/math.log(p1))
            for a1 in range(0,A1+1): # last_pair[0][1]+1):
                for a2 in range(0,A2+1): # last_pair[1][1]+1):
                    n = p0**a1 * p1**a2
                    if n < N:
                        #     print 'Exclude', p0,p1,n
                        dontcheck.add(n)
                             
            s += N
            S.add(N)
            print N,s, p0,p1            
        
    
    print s
    print len(S),sorted(S)
    
    return
    
    def M(p,q,N):
        while N > 1:
            a = N
            if a % (p*q) == 0:
                while a % p == 0:
                    a /= p
                while a % q == 0:
                    a /= q
                if a == 1:
                    return N
            N -= 1
        return 0
    
    k = 0
    for p in itertools.combinations(primes,2):
        m = M(p[0],p[1],100)
        print p[0],p[1], m
        k += m        
        
    print k    

def problem_207(): # solved - 44043947822 under 1 minute
    
    def t(k):
        t = math.log(math.sqrt(k*4+1)+1,2) - 1
        return t
    
    
    cnt = 0
    cnt_perf = 0
    prev_m = 1    
    m = 2
    delta = 2
    while 1:    
        m4_1 = m*4+1        
        sqrt1_4m = isqrt(m4_1) # int(math.sqrt(m*4+1))
        if sqrt1_4m*sqrt1_4m == m4_1:
            cnt += 1
            candidate = sqrt1_4m+1
            while candidate % 2 == 0:
                candidate /= 2
            if candidate == 1:            
                cnt_perf += 1
            #         print m,m-prev_m,cnt_perf,cnt
            prev_m = m
            delta += 2
            m += delta
        if cnt_perf * 12345 < cnt:
            print prev_m,cnt_perf,cnt
            break               
        #if m > 20:
        #    break
            
    return
    k = 1    
    while k < 100:    
        t_k = t(k)
        print k,t_k,math.pow(4,t_k),math.pow(2,t_k),k            
        k += 1
        
        

def problem_68(): # solved - 6 5 3; 10 3 1; 9 1 4; 8 4 2; 7 2 5; - 6531031914842725 (under 1 minute)
       
    for i1 in range(1,11):
        for i2 in range(1,11):
            if i2 == i1:
                continue
            for i3 in range(1,11):
                if i3 in [i1,i2]:
                    continue
                s = i1+i2+i3
                for i4 in range(1,11):
                    if i4 in [i1,i2,i3]: 
                        continue
                    i5 = s - i4 - i3
                    if i5 < 1 or i5 > 10 or i5 in [i1,i2,i3,i4]:
                        continue
                    for i6 in range(1,11):
                        if i6 in [i1,i2,i3,i4,i5]:
                            continue
                        i7 = s-i6-i5
                        if i7 < 1 or i7 > 10 or i7 in [i1,i2,i3,i4,i5,i6]:
                            continue
                        for i8 in range(1,11):
                            if i8 in [i1,i2,i3,i4,i5,i6,i7]:
                                continue
                            i9 = s - i7 - i8
                            if i9 < 1 or i9 > 10 or i9 in [i1,i2,i3,i4,i5,i6,i7,i8]: 
                                continue
                            i10 = s - i9 - i2
                            if i10 < 1 or i10 > 10 or i10 in [i1,i2,i3,i4,i5,i6,i7,i8,i9]:
                                continue
                            if i1 < i4 and i1 < i6 and i1 < i8 and i1 < i10:
                                aa = map(str,[i1,i2,i3,i4,i3,i5,i6,i5,i7,i8,i7,i9,i10,i9,i2])
                                aa = reduce(lambda x,y: x+y,aa)
                                print "%d - %d %d %d; %d %d %d; %d %d %d; %d %d %d; %d %d %d; %d" % (s,i1,i2,i3,i4,i3,i5,i6,i5,i7,i8,i7,i9,i10,i9,i2,len(aa))
                                                                

def problem_122(): # solved
    
    d = dict()
    def CreateD(n):
        for x in range(2,n+1):
            d[x] = []
            for i in range(1,x/2 + 1):
                d[x].append([i,x-i])
    sss = {1: [set([1])], 2: [set([1])], 3: [set([1,2])]}
    CreateD(200)
    
    def CreateS(n):
        LLLL = []
        dd = set()
        L = int(2*math.log(n)/math.log(2))
        m = L
        for p in d[n]:
            p0 = min(p[0],p[1])
            p1 = max(p[1],p[0])
            for k in sss[p1]:
                for j in sss[p0]:
                    S = set([p0,p1])
                    S.update(k)
                    S.update(j)

                    len_s = len(S)
                    if len_s > 15:
                        continue 
                    if m > len_s:
                        m = len_s
                    key = ''
                    for ppp in S:
                        key += '%d_' % ppp
                    if key not in dd:
                        LLLL.append(S)
                        dd.add(key)
        sss[n] = []
        for a in LLLL:
            if len(a) <= m:
                sss[n].append(a)
        return m 

    s = 0 + 1 + 2
    for i in range(4,201):
        
        m = CreateS(i)
        s += m
        print i, len(sss[i]), m, s
 
def problem_107():
    f = open('network.txt')
    v = [] 
    for line in f:
        print line
        v.extend(line.replace('\r\n','').split(','))
    
    v2 = v
    
    n = 7 
    
    v = ['-','16','12','21','-','-','-',
         '16','-','-','17','20','-','-',
         '12','-','-','28','-','31','-',
         '21','17','28','-','18','19','23',
         '-','20','-','18','-','-','11',
         '-','-','31','19','-','-','27',
         '-','-','-','23','11','27','-'] 
    
    n = 40
    v = v2
    
    import networkx
    import networkx.algorithms.mst
    G = networkx.Graph()
    S = 0
    EdgeSet = set()
    for i,e in enumerate(v):
        A = i / n 
        B = i % n 
        if e != '-':
            print A,B,e
        K = sorted([A,B])
        key = '%d_%d' % (K[0],K[1])
        if not key in EdgeSet:
            EdgeSet.add(key)
            S += int(e)
            G.add_edge(A,B,weight=int(e))
        
    T = networkx.algorithms.mst.minimum_spanning_tree(G)
    s = 0
    nodeSet = set()
    for e in T.edges():
        nodeSet.add(e[0])
        nodeSet.add(e[1])
        s += T[e[0]][e[1]]['weight'] 
    
    print S,s,S-s
    print len(nodeSet), nodeSet
    
def problem_303(): # solved - 1111981904675169
      
    def f(n):
        t = n
        cnt = 0        
        while t % 10 > 2 or t % 100 > 22 or max(map(int,str(t))) > 2:
            str_t = str(t)
            len_t = len(str_t)
            if len_t > len(str(n))+3:
                for i,c in enumerate(str_t):
                    if int(c) > 2 and int(c) < 8:
                        break
                if len_t - i > len(str(n))+3 and int(c) < 8:
                    next_num = 10**(len_t - i)
                    # round_up = (int(c)+1) * 10 ** (len_t-i-1)
                    round_up = t % (10 ** (len_t - i)) 
                    diff =  next_num-round_up                    
                    times = diff / n
                    t += n*(times-1)
            
            t += n
            cnt += 1
            if cnt % 100000 == 0:
                print cnt,n,t
        return t
    
    #  print (11363107 - 27528 - 1)/99
    #  return
     
    s = 0
    for i in range(1,10001):
        
        F = f(i)
        s += F / i
        print i,F,s


def problem_84(): # solved (under a minute) - 101524 (G2J 7.02%, R2 3.62% R3 3.28%)
    import random
    def get_dice(n):
        return random.randint(1,n)
            
    l = map(lambda x: 0.0,range(40))
    current_pos = 0
    n_doubles = 0
    n_iter = 10**6
    for i in xrange(n_iter):
        d1 = get_dice(4)
        d2 = get_dice(4)
        if d1 == d2:
            n_doubles += 1 
        else:
            n_doubles = 0
        current_pos = (current_pos + d1 + d2) % 40
        if n_doubles == 3:
            current_pos = 10
            n_doubles = 0
        elif current_pos == 30:
            # go 2 jail
            current_pos = 10
        elif current_pos in [2,17,33]:
            # community chest
            r = random.randint(1,16)
            if r == 1:
                # Advance to go
                current_pos = 0
            if r == 2:
                # Go to jail
                current_pos = 10            
        elif current_pos in [7,22,36]:
            # Chance
            r = random.randint(1,16)
            if r == 1:
                # Advance to go
                current_pos = 0
            if r == 2:
                # Go to jail
                current_pos = 10
            if r == 3:                
                current_pos = 11 # C1
            if r == 4:
                current_pos = 24 # E3
            if r == 5:
                current_pos = 38 # H2
            if r == 6:
                current_pos = 5 # R1
            if r == 7 or r == 8:
                if current_pos == 7:
                    current_pos = 15
                if current_pos == 22:
                    current_pos = 25
                if current_pos == 36:
                    current_pos = 5
            if r == 9:
                if current_pos == 7 or current_pos == 36:
                    current_pos = 12
                if current_pos == 22:
                    current_pos = 28
            if r == 10:
                current_pos -= 3
                            
        l[current_pos] += 1
        
    prob = map(lambda x: (x[0],x[1],round(float(x[1])/float(n_iter),4)),enumerate(l))
    sort_prob = sorted(prob,key=lambda x: x[1])
    print sort_prob
    
def problem_88(): # solved (under a minute ~ 20sec) - 7587457
        
    all_factors = dict()
    import math
    all_factors[1] = [[]]
    all_factors[2] = [[2]]
    all_factors[3] = [[3]]
    all_factors[4] = [[4],[2,2]]
    def factors(n):
        if n in all_factors:
            return all_factors[n]        
        all_factors[n] = [[n]]        
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:                
                factors_a = factors(i)
                factors_b = factors(n/i)
                for a in factors_a:
                    for b in factors_b:                               
                        all_factors[n].append(a+b)
        return all_factors[n]
    
    K = dict()
    for m in xrange(2,13001):
        M_factors = factors(m)
        for e in M_factors:
            s = sum(e) 
            k = len(e)+m-s # s + 1*(k-# elements in e) == prod (m)
            if not k in K:
                K[k] = 10**6
            if m < K[k]:
                K[k] = m
                print k,m
                
    S = set()
    for x in xrange(2,12001):
        if x not in K:
            print "%all_factors is missing!" % x
        else:
            S.add(K[x])
    print sum(S),max(S)
    
        


def problem_190(): # solved (using lagrange multipliers) - 371048281
    
    import math
    def Pm(m):                
        x1 = float(m)/float((1+m)*m/2)
        prod = x1
        v = [x1]        
        for i in range(2,m+1):
            v.append(x1*i)            
            prod = prod * math.pow(x1*i,i)
        return prod,v
    
    s = 0
    for m in range(2,16):
        PmVal = Pm(m)
        s += int(PmVal[0])
        print m, PmVal,s
    print s
    
    
def problem_135_(): # solved - 4989
    
    import math
    def num_sol(n):        
        S = set()
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                d = (i + n / i) / 4
                z = 2*d-i
                x = 3*d+z
                if x**2-(x-d)**2-(x-2*d)**2 == n:     
                    key = '%d_%d' % (x,d)
                    S.add(key)                
                z = 2*d - n/i 
                x = 3*d + z
                if x-2*d > 0 and x**2-(x-d)**2-(x-2*d)**2 == n:     
                    key = '%d_%d' % (x,d)
                    S.add(key)
                if len(S) > 10:
                    return 11
                        
        return len(S)
    
    cnt = 0
    for n in range(2,10**6):
        num_solutions = num_sol(n)
        if num_solutions == 10:        
            cnt += 1
            print n,cnt        
    print cnt
    
    
def problem_136(): # solved - 2544559
    
    import math
    def num_sol(n):        
        S = set()
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:
                o = n/i
                d = (i + o) / 4
                z = 2*d-i
                x = 3*d+z
                if x-2*d > 0 and x**2-(x-d)**2-(x-2*d)**2 == n:     
                    key = '%d_%d' % (x,d)
                    S.add(key)                
                z = 2*d - o 
                x = 3*d + z
                if x-2*d > 0 and x**2-(x-d)**2-(x-2*d)**2 == n:     
                    key = '%d_%d' % (x,d)
                    S.add(key)
                if len(S) > 1:
                    return 11
                        
        return len(S)
    
    cnt = 0
    for n in range(1,50*10**6):
        num_solutions = num_sol(n)
        if num_solutions == 1:        
            cnt += 1
            print n,cnt        
    print cnt
    
def problem_128(): # solved - 14516824220 (less than a minute)
    CNT = 0 
    offset = [(0,1),(-1,.5),(1,.5),(-1,-.5),(1,-.5),(0,-1)]
    primediff = set()
    
    import math
    def get_ring(x):
        if x == 1:
            return 0
        if x == 2:
            return 1
        n = int( (-3 + math.sqrt(9+12*(x-2))) / 6)
        return n + 1
    
    def get_pos(x):
        r = get_ring(x)
        p = 0
        if r == 1:
            segment = (x-1) / r
            p = x-1
        else:
            segment = math.ceil(float(x-(r-1)*3-(r-1)**2*3-1) / float(r))
            p = x-(r-1)*3-(r-1)**2*3-1
        
        p = p - (segment-1)*r        
        return r, segment, p
    
    def get_i(pos):
        r = pos[0]
        if r == 0:
            return 1
        s = pos[1]
        p = pos[2]
        i = (r-1)*3+3*(r-1)**2+r*(s-1)+p+1
        return i
    
    def get_neighbors(i,r,s,p):
        r,s,p = get_pos(i)    
        neighs_pos = []
        diffs = []
        if s == 1:
            neighs_pos.append( (r+1,s,p) ) # 1
            diffs.append( (r+1 -1)*3+3*(r+1 -1)**2+(r+1)*(s+0 -1)+p+0+1 )
            neighs_pos.append( (r+1,s,p+1) ) # 2
            diffs.append( (r+1 -1)*3+3*(r+1 -1)**2+(r+1)*(s+0 -1)+p+1+1 )
            if p == r:
                neighs_pos.append ( (r,s+1,1)) # 3
                diffs.append( (r -1)*3+3*(r -1)**2+(r)*(s+1 -1)+1+1 )
            else:
                neighs_pos.append ( (r,s,p+1)) # 3
                diffs.append( (r -1)*3+3*(r -1)**2+(r)*(s+1 -1)+p+1+1 )
            neighs_pos.append( (r-1,s,p) ) # 4
            diffs.append( 1+(r-1 -1)*3+3*(r-1 -1)**2+(r-1)*(s -1)+p )
            if p > 1:
                diffs.append( 1+(r-1 -1)*3+3*(r-1 -1)**2+(r-1)*(s -1)+p-1 )
                neighs_pos.append( (r-1,s,p-1)) # 5
                neighs_pos.append( (r,s,p-1)) # 6
                diffs.append( 1+(r -1)*3+3*(r -1)**2+(r)*(s -1)+p-1 )
            if p == 1:
                neighs_pos.append( (r,6,r)) # 5
                diffs.append( 1+(r -1)*3+3*(r -1)**2+(r)*(6 -1)+r )
                neighs_pos.append( (r+1,6,r+1)) # 6
                diffs.append( 1+(r -1)*3+3*(r -1)**2+(r)*(6 -1)+r )
        if s == 2:
            if p == 1:
                neighs_pos.append( (r+1,s-1,r+1) ) # 1
            else:
                neighs_pos.append( (r,s,p-1) )
            neighs_pos.append( (r+1,s,p) ) # 2
            
            
            neighs_pos.append( (r+1,s,p+1) ) # 3
            if p == r:
                neighs_pos.append( (r,s+1,1)) # 4
            else:
                neighs_pos.append( (r,s,p+1)) # 4
            neighs_pos.append( (r-1, s, p)) # 5
            if p == 1:
                neighs_pos.append( (r,s-1,r) ) # 6
            else:
                neighs_pos.append( (r-1,s,p-1) ) # 6
            
        if s == 3:
            if p == 1:
                neighs_pos.append( (r, s-1, r)) # 1
                neighs_pos.append( (r+1,s-1,r+1)) # 2
            else:
                neighs_pos.append( (r-1, s, p-1)) # 1
                neighs_pos.append( (r, s, p-1)) # 2
            neighs_pos.append( (r+1,s,p)) # 3
            if p == r:
                neighs_pos.append( (r-1,s+1,1)) # 4
                neighs_pos.append( (r,s+1,1)) # 5
            else:
                neighs_pos.append( (r-1,s,p)) # 4
                neighs_pos.append( (r,s,p+1)) # 5
            neighs_pos.append( (r+1,s,p+1) ) # 6
        if s == 4:
            if p == r:
                neighs_pos.append( (r-1,s+1,1)) # 1
            else:
                neighs_pos.append( (r-1,s,p)) # 1
            if p == 1:                
                neighs_pos.append( (r,s-1,r)) # 2
            else:
                neighs_pos.append( (r-1,s,p-1)) # 2
            
            if p > 1:
                neighs_pos.append( (r,s,p-1)) # 3
            else:    
                neighs_pos.append( (r+1,s-1,r+1)) # 3
            
           
            neighs_pos.append( (r+1,s,p)) # 5
            neighs_pos.append( (r+1,s,p+1)) # 6
            if p == r:
                neighs_pos.append( (r,s+1,1) ) # 4
            else:
                neighs_pos.append( (r,s,p+1) ) # 4
        if s == 5:
            if p == r: # 12 o'clock
                neighs_pos.append( (r, s+1, 1)) # 2
            else:
                neighs_pos.append( (r, s, p+1)) # 2
                
            if p < r:
                neighs_pos.append( (r-1,s,p)) # 5
            else:
                neighs_pos.append( (r-1,s+1, 1)) # 5
            
            
            if p == 1: # 8 o'clock
                neighs_pos.append( (r,s-1,r) ) # 1
            else:
                neighs_pos.append( (r-1,s,p-1) ) # 1
                
            if p == 1:
                neighs_pos.append( (r+1,s-1,r+1)) # 6
            else:
                neighs_pos.append( (r,s,p-1)) # 6
            neighs_pos.append( (r+1,s,p)) #3
            
            neighs_pos.append( (r+1,s,p+1)) #4
            
            
            
        if s == 6:
            if p == 1: # 6 o'clock
                neighs_pos.append( (r,s-1,r) ) # 1
            else:
                neighs_pos.append( (r-1,s,p-1)) # 1
            if p == r:
                neighs_pos.append( (r,1,1)) # 2
                neighs_pos.append( (r-1,1,1)) # 3
            else:
                neighs_pos.append( (r,s,p+1)) # 2
                neighs_pos.append( (r-1,s,p)) # 3
            if p == 1:
                neighs_pos.append( (r+1,s-1,r+1)) # 4
            else:
                neighs_pos.append( (r,s,p-1)) # 4
            neighs_pos.append( (r+1,s,p+1)) # 5
            neighs_pos.append( (r+1,s,p)) # 6
            
        return map(get_i, neighs_pos)      
            
  #  return    
    i = 2
    OLDI = 1
    CNT = 1
    primes = dict()
    r = 1
    s = 1
    p = 1
    
    
    
    while 1:        
        i = get_i( (r,1,1) )
        v = get_neighbors(i,r,s,p)     
        
        cnt = 0
        for j,e in enumerate(v):           
            diff = abs(e-i)
            if diff not in primes:            
                primes[diff] = isprime(diff)
            cnt += int(isprime(diff))
            if cnt == 3 or (j+1+(3-cnt) > 6):
                break
                                                        
        if cnt == 3:
            CNT += 1            
            print CNT,i,get_pos(i), v, map(lambda x: (abs(i-x), isprime(abs(i-x))), v), i-OLDI 
            
            OLDI = i            
        if CNT > 2001:
            break
        
        i = get_i( (r,6,r) )
        v = get_neighbors(i,r,s,p)
        cnt = 0
        for j,e in enumerate(v):           
            diff = abs(e-i)
            if diff not in primes:            
                primes[diff] = isprime(diff)
            cnt += int(isprime(diff))
            if cnt == 3 or (j+1+(3-cnt) > 6):
                break
                                                        
        if cnt == 3:
            CNT += 1            
            print CNT,i,get_pos(i), v, map(lambda x: (abs(i-x), isprime(abs(i-x))), v), i-OLDI 
            
            OLDI = i            
        if CNT > 2001:
            break
        r += 1
        
    while 1:            
        v = get_neighbors(i,r,s,p)            
        cnt = 0
        for j,e in enumerate(v):           
            diff = abs(e-i)
            if diff not in primes:            
                primes[diff] = isprime(diff)
            cnt += int(isprime(diff))
            if cnt == 3 or (j+1+(3-cnt) > 6):
                break
                        
                                    
        if cnt == 3:
            CNT += 1            
            print CNT,i,get_pos(i), v, map(lambda x: (abs(i-x), isprime(abs(i-x))), v), i-OLDI 
            
            OLDI = i            
        if CNT > 2001:
            break 
        while 1:
            i += 1
            k = i % 10
            S = get_pos(i)
            if (S[1] == 1 and S[2] == 1) or (S[1] == 6 and S[2] == S[0]):
                break
            if k in [8,7,9,1,0] and get_pos(i)[1] in [1,6]:
                break                


def problem_214(): # solved - 1677366278943 under a minute
    global primes    
    global sorted_primes
        
    totient_dict = dict()
    totient_dict[1] = 1
   # global primes # primes = set(gen_primes(2,4*10**7))
    def mytotient(n):
        if n == 1:
            return 1
        if n in totient_dict:
            return totient_dict[n]
        if n in primes:
            totient_dict[n] = n - 1
            return n - 1
      #  if MillerRabin(n, 50):
      #      primes.add(n)
      #      totient_dict[n] = n - 1
      #      return n - 1

        totient_prod = 1
        calc_n = n
        for p in sorted_primes:
            if p > calc_n:
                break
            prev = 0
            pexp = 1
            while calc_n % p == 0:
                prev = pexp
                pexp *= p
                calc_n = calc_n / p
            totient_prod *= pexp - prev
            if calc_n in totient_dict:
                v = totient_dict[calc_n] * totient_prod
                totient_dict[n] = v
                return v      
        raise "Crap"        

    totient_chain = dict()
    totient_chain[1] = 1
    def A(norg):
        if norg == 1:
            return 1
        cnt = 0
        nvec = [norg]
        n = norg
        while n >= 1:
            cnt += 1            
            if n in totient_chain:
                l = totient_chain[n]
                for i,e in enumerate(reversed(nvec)):
                    totient_chain[e] = l+i
                break            
            n = mytotient(n)
            nvec.append(n)        
        return totient_chain[norg]
    
    s = 0
    oldx = 2
    i = 1
    for x in sorted_primes:
        if i % 10**6 == 0:
            print i, x
        i += 1
        a = A(x)            
        if a == 25:
            s += x            
            print s, x, a, float(x) / float(oldx)
            oldx = x
    print s
