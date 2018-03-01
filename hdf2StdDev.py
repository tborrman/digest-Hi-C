#!/usr/bin/env python
import argparse
import matrix_functions as mf 
import numpy as np 
import h5py

parser=argparse.ArgumentParser(description='Get standard deviation of cis interactions' +
' for each row of Hi-C matrix')
parser.add_argument('-i', help='input hdf5 Hi-C file', type=str, required=True)
args=parser.parse_args()





def main():
	# Get hdf file
	f = h5py.File(args.i, 'r')
	std = mf.get_std(f)
	# Write output
	OUT = open('test_std.txt', 'w')
	for i, b in enumerate(f['bin_positions'][:][:6087]):
		if b[0] == 22:
			chrom = 'chrX'
		else:
			chrom = 'chr' + str(b[0]+1)
		OUT.write(chrom+'\t'+str(b[1])+'\t'+str(b[2])+
		'\t'+ str(std[i])+'\n')
	OUT.close()





if __name__ == '__main__':
	main()
