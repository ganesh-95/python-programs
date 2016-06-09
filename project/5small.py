def solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in range(1,20)):
            return num
        else:
            pass
    return None

print  solution(20)
