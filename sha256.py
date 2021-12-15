import hashlib
import string
import sys
import ray
from itertools import chain, product

#USE "less shalogi.log | grep SUCCESS" TO VIEW IF SOLUTION HAS BEEN FOUND.

sha256 = '8c9204c0c8d8fdde878f90df7eb22259d599621fe916666919f6f44c5e3195d1'
#sha256 = '446332180480b6bf6e930a92dd0749cc0266184eaa5c90dcbdfeee0f24e0321b'
start = 896868
stop = 896906
cpu_cores = 4
treasure_found = "False: "

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    if sha_signature == sha256:
        global treasure_found
        treasure_found = "True: "
        print("<---------SUCCESS--------->")
        print("String: " + hash_string)
        print(sha256)
        print("<---------YOU DID IT!-------->")
        f = open("shalogi.log", "a")
        f.write("SUCCESS: " + hash_string + "\n")
        f.close()
        ray.shutdown()
        exit()
    return treasure_found + hash_string

def coordinate(prefix):
    f = open("shalogi.log", "a")
    f.write("Processing: " + prefix + "@N59" + "\n")
    print("Processing: " + prefix + "@N59" + "\n")
    f.close()
    for n in range(19000, 21000):
        for e in range(43000, 46400):
            encryptedString = encrypt_string(prefix + " N59 " + "{:.3f}".format(n/1000) + " E024 " + "{:.3f}".format(e/1000))
    return encryptedString

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))
        
bf_list = list(bruteforce(string.ascii_uppercase + string.digits, 4))
print("Length of BF list: " + str(len(bf_list)))
print("------")
count = start

@ray.remote
def computeSha(start, stop, step):
    for i in range(start, stop, step):
        cordRes = coordinate(ray.get(bf_list_id)[i])
        #ray.get(coordinate.remote(bf_list[i]))
    return cordRes

ray.init()
bf_list_id = ray.put(bf_list)
# Start (stop-start) tasks in parallel.
results = []
for i in range(stop - start):
    results.append(computeSha.remote(start + i, stop, stop - start))
    
try:   
    # Wait for the tasks to complete and retrieve the results.
    # With at least 4 cores, this will take 1 second.
    if treasure_found == "False: ":
        reslis = ray.get(results)  # [0, 1, 2, 3]
        for i in reslis:
            print(i)
    else:
        print("Solution found. Check the logs.")
        ray.shutdown()
except KeyboardInterrupt:
    print("Stopped process manually! Check the logs!")
    f = open("shalogi.log", "a")
    f.write("Process stopped manually. Re run the previous 4 combinations when restarting." + "\n")
    f.close()
    ray.shutdown()
