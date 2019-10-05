#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG + Bowen, 2019
# Done by Lee Gui An, 1002651 - github.com/piroton

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote

# pass two bytestrings to this function


def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def generate_ngram(s, n):
    s = s.lower()
    ngrams = zip(*[s[i:] for i in range(n)])
    return ["".join(ngram) for ngram in ngrams]


def generate_freq(text):
    d = {}
    for i in text:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    freq = [[v, k] for k, v in d.items()]
    return sorted(freq)


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # print(challenge)
    challenged = challenge.decode('utf-8')
    d = generate_freq(challenged)
    print(d)
    # print(sorted(freq))
    maps = [(' ', "G"), ("2", " "), ('E', 'S'), ('O', 'E'), ('.', 'T'), ('t', 'H'), ('c', 'O'), ('I', 'A'), ('K', 'N'), ('|', 'D'), ('Y', 'C'), ('W', '.'), (';', 'W'), ('R', 'J'), ('\x0c', 'R'), ('_', 'M'), ('-', 'L'),
            ('F', 'U'), ('e', 'F'), ('s', 'V'), ('>', 'I'), ('X', 'P'), ('K', 'N'), ('V', 'K'), ('-', 'L'), ('<', 'B'), ('p', ','), ('\'', 'Y'), ('3', '\"'), ('{', 'Q'), ('u', '-'), ('f', '?'), ('v', '\''), ('\t', '\n')]
    di = {i[0]: i[1] for i in maps}
    clean = ""
    for i in challenged:
        if i in di.keys():
            clean += (di[i])
        else:
            clean += i
    # cleansplit = clean.split()
    # # print(challenged)
    # cleand = generate_freq(cleansplit)
    # print(cleand)
    # print(clean)
    clean = clean.lower()
    solution = clean.encode('utf-8')
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # print(challenge, len(challenge))
    chad = challenge.decode('utf-8')
    # print(chad)
    # some all zero mask.
    # TODO: find the magic mask!
    mask = XOR(b'Student ID 1002651 gets 4 points',
               b'Student ID 1000000 gets 0 points')
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'points' in message:
        print(message, len(message))
    conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '34.239.117.115'
    PORT = 1337

    sol1()
    sol2()
