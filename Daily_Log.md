# Nano_Hack

## 27th 

###Ideas
Combine two fasta files

Search the plasmid database for hits - hit that keeps coming up and up.

Use longer reads - so that the seq dont hit a load of stuff 

Blast against just plasmids

ncbiwww module in Pyhton

## 28th

Use fast5 files 
Poretool to process fast5 files

Use BLAST
BLASTING AGAINST PLASMIDS
Type **plasmids (taxid:36549)** in organisms 

PLASMID SEARCH TOOLS:
https://plasmid.med.harvard.edu/PLASMID/PrepareBlast.do

http://blog.addgene.org/tips-for-using-blast-to-verify-plasmids

which poretools *shows where poretools installed*

ls -lct | head *view files by time*

grep -A 1 Barcoding_2d ___.fasta > 2d____.fasta  *prints out line matched and 1st line after*

### Fast5 --> Fasta 

    poretools fasta BC04 > BC04.fasta

- [x] Each fasta file now created (Claire and Hayley)

### Fasta --> Extracting 2D reads

**code.py**

    #!/usr/bin/env python

    import sys
    inFile = sys.argv[1]
    outFile = '2d' + inFile

    with open(inFile,'r') as i, open(outFile, 'w') as o:
    	for line in i:
	    	if line.startswith(">") and ("Barcoding_2d" in line):
		    	o.write(line)
		    	o.write(next(i))

### Combine all reads into single file

    cat *.fasta > all.fasta

### Blast
Recently changed - therefore Biopython no longer able to link in to Blast
So we will take a subset of plasmids and compare against them 

Library to use:

	all_ref.fasta

 

### BWA

For long read **alignment** you need another software tool. Use bwa like this:

    git clone https://github.com/lh3/bwa.git

    cd bwa

    make

    bwa index all_ref.fasta

    bwa mem -x ont2d all_ref.fasta all_reads.fasta > reads_aln.sam

    samtools view -bS reads_aln.sam > reads_aln.bam

    samtools sort reads_aln.bam -o reads_aln.sorted.bam
    
    samtools index reads_aln.sorted.bam

  You can look at these alignments with a software package called **Tablet**

Important **Output files** form bwa:
	
	reads_aln.sorted.bam
	
	reads_aln.sorted.bam.bai
 
  
## 29th

### Tablet

Files to use:

	reads_aln.sorted.bam
	
	all_ref_join.fasta


- [x] add GFP into all_ref.fasta
- [ ] Ask Sam about Tablet
- [ ] What info can we extract from Blast - eg. shows us what plasmids are present


### General Tasks
- [x] read the fast5 format document sent by Sam (Claire and Hayley)
- [x] work out Biopython and how to link to NCBI Blast (Alex and Emma)
- [ ] Combine fast5 and fasta programs into one program
- [ ] Live demo for local library for BLAST
- [ ] rather than waiting until end - untils - analyse as you go - run until you get answer you want
