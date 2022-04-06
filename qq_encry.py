def hash33(t):
    e = 0
    for i in range(len(t)):
        e += (e << 5) + ord(t[i])
    return 2147483647 & e

def gtk(p_skey):
    t = 5381
    for i in p_skey:
        t += (t << 5) + ord(i)
    return t & 2147483647