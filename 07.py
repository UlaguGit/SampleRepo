numes=range(1,100)
print("NUMBERSs:", list(numes), "\n")

def prime(num):
    for i in range(2, num):
        if (num%i==0):
            return False
    return True
primes=(list(filter(prime, numes)))
print("PRIME NUMBERS: ", primes)