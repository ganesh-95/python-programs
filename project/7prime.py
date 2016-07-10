"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""def nth_prime(n):
    b = []
    b.append(2)
    while len(b)<n:
        for num in range(3, n*11, 2):
            if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
                b.append(num)


    print list(sorted(b))[n-1]

print nth_prime(10001)
