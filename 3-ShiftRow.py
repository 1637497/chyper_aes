def ShiftRow(m):
    print('Entrada:', m)
    #segona fila
    aux = m[1,0]
    m[1,0:3] = m[1,1:4]
    m[1,3] = aux

    #terceta fila
    m2 = list(m[2])
    m2[0:2], m2[2:4] = m2[2:4], m2[0:2]
    m[2][:] = m2

    #quarta fila
    aux = m[3,3]
    m[3,1:4] = m[3,0:3]
    m[3,0] = aux
    print('Sortida:', m)
    return m
