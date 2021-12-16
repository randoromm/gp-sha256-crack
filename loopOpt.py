import hashlib
import string
import sys
import timeit
import numpy as np
from itertools import chain, product

def encrypt_string(hash_string):
    #sha_signature = \
    #    hashlib.sha256(hash_string.encode()).hexdigest()
    sha_signature = hash_string
    #print(sha_signature)
    return

def coordinate(prefix):
    for n in range(19000, 21000):
        for e in range(43000, 46400):
            encryptedString = encrypt_string(prefix + " N59 " + "{:.3f}".format(n/1000) + " E024 " + "{:.3f}".format(e/1000))

def coordinate_opt(prefix):
    north = np.arange(19.000,21.000,0.001)
    east = np.arange(43.000,46.400,0.001)
    for n in north:
        for e in east:
            encryptedString = encrypt_string(prefix + " N59 " + str(n) + " E024 " + str(e))
    return

if __name__ == "__main__":
    #57.96 sec
    #without prints: 7.0371 sec
    #print(timeit.timeit(lambda: coordinate('ABCD'), number = 1))
    float_formatter = "{:.3f}".format
    np.set_printoptions(formatter={'float_kind':float_formatter})
    print(timeit.timeit(lambda: coordinate_opt('ABCD')))
