import math
number=100

sieve = []
sieve = [True for i in range(number)]

sieve[0] = False
sieve[1] = False

for i in range(2, int(math.ceil(math.sqrt(number)))):
    if sieve[i]:
        k = 2
        j = k * i
        while j < number:
            sieve[j] = False
            k = k + 1
            j = i * k

primes = [idx for idx, element in enumerate(sieve) if element == True]
print(primes)
