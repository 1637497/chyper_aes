def keytransform(clau, sbox, racon):
    claus = [clau.copy()]
    for iteracio in range(10):
        ultima_col = np.roll(clau[:, -1], -1)
        for i in range(4):
            valor = hex(ultima_col[i])[2:].zfill(2)
            ultima_col[i] = sbox[int(valor[0], 16)][int(valor[1], 16)]
        clau[:, 0] = np.bitwise_xor(clau[:, 0], np.bitwise_xor(ultima_col, racon[:, iteracio]))
        for col in range(1, 4):
            clau[:, col] = np.bitwise_xor(clau[:, col], clau[:, col-1])
        claus.append(clau.copy())
    return claus
