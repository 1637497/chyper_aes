def mixcolumn(M, A):
    m = np.zeros((4,4),dtype=int)
    for i in range(0,4):
        for j in range(0,4):
            e = 0
            for k in range(0,4):
                if A[i][k] == 1:
                    e ^= M[k][j]

                elif A[i][k] == 2:
                    aux = M[k][j] << 1
                    e ^= aux

                else:
                    aux = M[k][j] << 1
                    e ^= aux + M[k][j]

            m[i][j] = e

    return m
