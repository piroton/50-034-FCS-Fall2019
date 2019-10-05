#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse


def doStuff(mode, key, filein, fileout):
    print("Key:", key, "Mode:", mode)
    with open(filein, mode="rb") as fin:
        text = bytearray(fin.read())

        if mode == "e":
            print("DE:", text[:100])
            encrypted_chars = bytearray([])
            for char in text:
                en_char = (char + key) % 256
                encrypted_chars.append(en_char)
            print("EN:", encrypted_chars[:100])
            output_bytes = encrypted_chars

        elif mode == "d":
            # print("EN:", text[:100])
            decrypted_chars = bytearray([])
            for char in text:
                de_char = (char - key) % 256
                decrypted_chars.append(de_char)
            # print("DE:", decrypted_chars[:100])

            output_bytes = decrypted_chars

        f = open(fileout, 'wb')
        f.write(output_bytes)
        f.close()
        # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein', help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    key = args.key
    mode = args.mode

    try:
        key = int(key)
        assert 0 < key <= 255
    except Exception as e:
        print("Error: key is not an integer between 0-255 (inclusive)")
        print(e)
        exit()

    if mode == "d" or mode == "e":
        doStuff(mode, key, filein, fileout)
    else:
        print("Error: mode is not either `d` or `e`!")
        exit()

    # all done
