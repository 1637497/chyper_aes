def addroundkey(matriu, round_key):
    return np.bitwise_xor(matriu, round_key)
