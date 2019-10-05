import hashlib
import string
import time


def get_hashes(fname):
    a = []
    with open(fname) as f:
        text = f.readlines()
        for i in text:
            # print(i)
            j = i.strip('\n').strip()
            a.append(j)
    return a


def compute_hash(b_raw):
    return hashlib.md5(b_raw).hexdigest()


def main():
    pws = get_hashes("./hash5.txt")
    # print(pws)
    searchspace = string.printable[0:36][::-1]
    # print(searchspace)
    start_time = time.process_time()
    d_keys = {}
    for l1 in searchspace:
        for l2 in searchspace:
            for l3 in searchspace:
                for l4 in searchspace:
                    for l5 in searchspace:
                        # print(l1+l2+l3+l4+l5)
                        inp = (l1+l2+l3+l4+l5).encode('utf-8')
                        h_inp = compute_hash(inp)
                        if h_inp in pws:
                            idex = pws.index(h_inp)
                            d_keys[inp] = h_inp
                            print(
                                "Password: {} generates hash {} at position {}".format(inp, h_inp, idex))
    t_taken = time.process_time() - start_time
    print("All hashes broken in: {}s".format(t_taken))
    for i in d_keys.keys():
        print("PW: {} | HASH: {}".format(i, d_keys[i]))


main()
