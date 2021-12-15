import hashlib
import string
import sys
import ray
from itertools import chain, product

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
        
bf_list = list(bruteforce(string.ascii_uppercase + string.digits, 4))
print("Length of BF list: " + str(len(bf_list)))
print("------")
print("GCAA: " + str(bf_list.index('GCAA')))
print("GC99: " + str(bf_list.index('GC99')))
print("GPAA: " + str(bf_list.index('GPAA')))
print("SALT: " + str(bf_list.index('SALT')))
print("GP99: " + str(bf_list.index('GP99')))
print("SHAA: " + str(bf_list.index('SHAA')))
print("SHA9: " + str(bf_list.index('SHA9')))
print("----YLEMISED V2LISTATUD--------")
print("----Ideed-----------")
print("GEOA: " + str(bf_list.index('GEOA')))
print("GEO9: " + str(bf_list.index('GEO9')))
#Otsida mis on tüüpilised soolad mis pannakse ette.
pattern1 = input("Enter pattern 1 (from):")
pattern2 = input("Enter pattern 2 (to):")
print(pattern1 + ": " + str(bf_list.index(pattern1)) + " TO " + pattern2 + ": " + str(bf_list.index(pattern2)))
