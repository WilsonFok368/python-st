import hashlib
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-folder", help="test: point to Files_Siam folder")
args = parser.parse_args()

siam_md5 = { #grabbed a set from grants tutorial spreadsheet
    "mt7612_ExtPwrTable_FCC.dat": "991476d8c0a244082e42707722a07172",
    "mt7612_ExtPwrTable_IC.dat": "2c41e14e66d89df4a24483f4d9c6a2f6",
    "mt7612_ExtPwrTable_NCC.dat": "991476d8c0a244082e42707722a07172",
    "mt7612_ExtPwrTable_BG.dat": "dcd9409fde3e8132f6b12da3f7452aa4",
    "mt7612_ExtPwrTable_JP.dat": "a4f1d7d57523aa63c4632bae2034eb64",
    "mt7612_ExtPwrTable_AR.dat": "cc0af531ee55e05fa86d0c8bb437a1f9",
    "mt7612_ExtPwrTable_MX.dat": "120ea2e38bf63531cdd71a39b091e3ac",
    "mt7612_ExtPwrTable_KR.dat": "6b55037cfb91a70e62dcf7dddf6295f1",
    "mt7612_ExtPwrTable_CE.dat": "8dc26b4c6d0a181e5fe369ee8a639cfb",
    "mt7612_ExtPwrTable_IS.dat": "8dc26b4c6d0a181e5fe369ee8a639cfb",
    "mt7612_ExtPwrTable_ASNZS.dat": "770e00da4137e634e861fa3531fb6f67",
    "mt7612_ExtPwrTable_CL.dat": "cd6fb577047b7a33b4580edbf43a87d7"
    }

for files in os.listdir(args.folder):
    if ".dat" in files:
        check = "\033[31mFAIL\033[0m"
        hash = hashlib.md5(open(args.folder + "/" + files,"rb").read()).hexdigest()
        if hash == siam_md5[files]:
            check = "\033[32mPASS\033[0m"
        print("File:\t{}\tMD5 Checksum:\t{}\tCHECK: {}".format(files, hash, check))