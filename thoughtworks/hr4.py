
'''
add numbers which are in the position of prime numbers
'''
N =int(raw_input())

marks = map(int, raw_input().split())


total = 0
for num in xrange(1,N+1):
    if all(num%i!=0 for i in xrange(2,num)):
        total += marks[num-1]
print total

           
