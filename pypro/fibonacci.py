n = int(raw_input())
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

values = [str(f(x)) for x in range(0,n+1)]

print ",".join(values)
