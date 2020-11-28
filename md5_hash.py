import hashlib
import os

folder = input("Input folder: ")

for file in os.listdir(folder):
	fhash = hashlib.md5(open(folder + "\\" + file, 'rb').read()).hexdigest()
	print("File: {}\t\t\tMD5 Hash: {}".format(file, fhash.upper()))