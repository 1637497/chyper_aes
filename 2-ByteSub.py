def bytesub(sbox, text):
    print('Entrada:', text)
    matriu = np.zeros((4,4))
    for i in range(4):
      for j in range(4):
        valor = text[i][j]
        matriu[i][j] = sbox[int(valor[0], 16)][int(valor[1], 16)]
    print('Sortida:', matriu)
    return matriu
