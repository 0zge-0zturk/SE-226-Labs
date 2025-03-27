import math

def factorial (x):
    fact = 1
    if x > 1:
        fact = x * factorial(x-1)

    return fact

step = lambda x,n : (((-1)**n)*(x**(2*n+1)))/factorial((2*n+1))

def sine_x(x,n):
    sum = 0
    if x > -1:
        sum = sum + step(x,n)

    return sum * (math.pi/180)

print(sine_x(0,0))

h = 0
def harmonic(n):
    """Calculates the first n components of harmonic series of H = 1 + 1/2 + 1/3 +...+ 1/n """
    global h
    if 0 == n:
        return
    h += 1/n
    harmonic(n-1)
