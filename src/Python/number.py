#!/usr/bin/python3
import math
import performances

log = performances.logger(show_ram_time=False, debug=False)
d = log.debug
def diviseurs(n):
    """Find all multiples of a integer n."""
    divisors = list()
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def check_perfect(n):
    """Check if a integer n is perfect. """
    divisors = diviseurs(n)
    somme = 0
    for x in divisors[:-1]:
        somme += x
    if divisors.pop() == somme:
        log.debug(str(divisors))
        return True
    else:
        return False
