"""
difference between the sum of diagnols in a matrix
"""
N = int(raw_input())

matrix = [[int(raw_input("element %d %d : " % (row,col)))for col in xrange(N)] for row in xrange(N)]

def diag_dif(matrix):
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N-i-1] for i in range(N))
    return abs(l-r)

print diag_dif(matrix)
