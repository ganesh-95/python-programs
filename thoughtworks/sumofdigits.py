

# sum of digits 



def sum_of_digits(N):
    sum = 0
    while N:
        sum += N % 10
        N = N / 10
    return sum

print sum_of_digits(2345678901)
    
