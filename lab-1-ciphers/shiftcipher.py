#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out


# Import libraries
import sys
import argparse
import string


def encodeText(textin, shift, mode):
    out = ""
    for cha in textin:
        enc = cha
        if cha in string.printable:
            cha_pt = string.printable.index(cha)+(shift*mode)
            # print(cha_pt)
            enc = string.printable[cha_pt % 100]
        out += enc
        # print(out)
    return out


def processFiles(filein, fileout, shift, mode):
    textout = ""
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        textin = fin.read()
        # print(textin)
        modevar = (-1, 1)[mode == "e"]
        textout = encodeText(textin, shift, modevar)
        # print(textout)

    with open(fileout, mode='w', encoding='utf-8', newline='\n') as fout:
        fout.write(textout)
    return


def validKey(key):
    keyOk = False
    if (key.isdigit()):
        keyval = int(key)
        keyOk = (keyval > 0 and keyval < len(string.printable))
    else:
        print("Invalid Key size")

    return keyOk


def validMode(mode):
    mode = mode.lower()
    modeOk = False
    if mode != 'd' and mode != 'e':
        print("Invalid mode")
    else:
        modeOk = True
    return (modeOk)


# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein', help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument(
        '-k', dest='key', help='key')
    parser.add_argument('-m', dest='mode',
                        help='mode: d - decrypt; e - encrypt')

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    key = args.key
    mode = args.mode

    # input sanity and defaults
    if validKey(key):
        key_shift = int(key)
    else:
        key_shift = 1
    if validMode(mode):
        prog_mode = mode.lower()
    else:
        prog_mode = "d"

    processFiles(filein, fileout, key_shift, prog_mode)

    # all done
