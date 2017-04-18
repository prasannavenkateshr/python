def MatrixLeftRotate(matrix):
    resultantMatrix = []
    for i in matrix: resultantMatrix.append(i[::-1])
    return map(list, zip(*resultantMatrix))

def MatrixRightRotate(matrix):
    resultantMatrix = []
    for i in map(list, zip(*matrix)): resultantMatrix.append(i[::-1])
    return resultantMatrix

def Display(m,n, matrix):
    for i in xrange(m):
        for j in xrange(n):
            print matrix[i][j],
        print ""
