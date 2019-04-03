#! /usr/bin/env python3

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'


# open the FASTA file
fasta = open(fasta_file)

# the variable 'genome' holds the genome sequence
genome = fasta.read()

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


















