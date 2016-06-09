def nth_prime(n):
    b = []
    b.append(2)
    while len(b)<n:
        for num in range(3, n*11, 2):
            if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
                b.append(num)


    print list(sorted(b))[n-1]

print nth_prime(10001)
