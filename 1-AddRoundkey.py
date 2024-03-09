def addroundkey(matriu, round_key):
    print('Entrada:', matriu)
    state = np.bitwise_xor(matriu, round_key)
    print('Sortida:', state)
    return state
