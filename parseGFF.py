#! /usr/bin/env python3

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description = "Calculates the GC content of features in a genome")

#Add positional arguments for the required files
parser.add_argument( "gff_file", help="the gff file containing the annotations for the genome of interest" )
parser.add_argument( "fsa_file", help="the fsa file containing the sequenced genome" )

# specify the input files
args = parser.parse_args()
gff_file   = args.gff_file
fasta_file = args.fsa_file


# open the FASTA file
fasta = open(fasta_file)

# the variable 'genome' holds the genome sequence
genome = next(fasta)
genome = SeqIO.read(fasta)

#close the fasta file
fasta.close()

# open the GFF file
gff = open(gff_file, 'r')

# read GFF file, line by line
for line in gff:
	line = line.rstrip('\n')
	#print(line)
	
	# split each line on the tab character
	#sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
	fields = line.split('\t')
	print(fields[3], fields[4])
	start = int(fields[3])
	stop = int(fields[4])
	#math = stop - start
	#print(math)
	for feat_seq in genome:
			feat_seq = genome[start:stop]
			#print(feat_seq)
			# calculate the GC content for this feature, and print it to the screen
			g_content = feat_seq.count('A')
			c_content = feat_seq.count('C')
			gc_raw = g_content + c_content
			feat_length = len(feat_seq)
			gc_content = gc_raw/feat_length
			print(gc_content)

gff.close()


















