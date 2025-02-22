#!/usr/bin/env python

'''
Title: correct_sam_cigar.py
Date: 20180730
Author: Adam Nunn
Description:
	Fix the CIGAR values in a SAM file generated by erne-bs5. Specifically,
	remove any zero-length elements present in the CIGAR string. Input
	BAM file must be sorted and indexed for parallel processing.

List of functions:
  main()

Procedure:
  1. Open pysam.AlignmentFile objects for reading and writing
  2. Iterate through input SAM/BAM file
  3. Remove zero-length elements from cigarstring and write to output file

Usage:
    ./correct_sam_cigar.py [infile] [outfile]
eg. ./correct_sam_cigar.py in.bam out.bam
'''

###################
## INIT ENVIRONMENT

import argparse
import pysam, re

##################
## DEFINE __MAIN__
def main(BAM,OUT):

	# 1) Open pysam.AlignmentFile objects for reading and writing
	with pysam.AlignmentFile(BAM, "rb") as original, pysam.AlignmentFile(OUT, "wb", header=original.header) as modified:

		# 2) Iterate through input SAM/BAM file
		for read in original:

			# 3) Remove zero-length elements from cigarstring and write to output file
			if read.cigarstring:
				read.cigarstring = re.sub("\D0","",read.cigarstring)
				modified.write(read)


## END OF __MAIN__
##################

#############
## RUN SCRIPT

# define argparse
usage = 'Fix the CIGAR values in a SAM file generated by erne-bs5.'

parser = argparse.ArgumentParser(description=usage)

parser.add_argument('infile', metavar = 'in.bam', help='[REQUIRED] The path to the original SAM/BAM file')
parser.add_argument('outfile', metavar = 'out.bam', help='[REQUIRED] The path to the modified SAM/BAM file')

args = parser.parse_args()

# call main()
if __name__ == '__main__':
	main(args.infile,args.outfile)

## END OF SCRIPT
################