# Nano_Hack

Nanopore outputs files in **Fast5** format. This must first be converted to **fasta** format.

### Fast5 --> Fasta 

	poretools fasta BC04 > BC04.fasta

### Fasta --> Extracting 2D reads

See file **code.py**

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

### NCBI Blast
![NCBI Logo](https://blast.ncbi.nlm.nih.gov/images/nucleutide-blast-cover.png)

Permissions on BLAST Recently changed - therefore Biopython no longer able to link in to Blast
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
 
  
## 29th Nov

### Tablet

Files to use:

	reads_aln.sorted.bam.bai
	
	all_ref_join.fasta

## 30th Nov 

	gi|21190.... = GFP gene seq
	ENA|AF246... = Gacs gene seq
	gi|437877... = pME6010 plasmid seq
	gi|209211... = pUC18 plasmid seq
	gi|130693... = Decoy plasmid seq
	
### Hind III

Detla 76 inserted plasmid - it has 2 Hind III restriction sites - other plasmids has one site

### Tn7

Reads hit this section of the decoy plasmid - this is common in plasmids. 

### GacS

Numerous versions of this - WILD TYPE, H294R mutation and detal76 insertion.

- [x] search for the reads that align with the beginning of PU18 backbone but code for an inserted gene (Alex)

See file **insert.fasta**
	
**Blast results:**

	Pseudomonas protegens CHA0, complete genome	2645	2645	87%	0.0	82%	
	Pseudomonas fluorescens sensor kinase GacS (gacS) gene, complete cds 2645	2645	87%	0.0	82%	
- [ ] align reads against it?

# 1st Dec
- [ ] isolate names from bam file - samtools - that covers certian area
- [x] research role of TN7
- [ ] read file sent by Sam on Wednesday - talks about Gacs http://apsjournals.apsnet.org/doi/pdf/10.1094/MPMI.2003.16.7.634
- [ ] find mutations in Gacs alignment in Tablet - H294R / Delta 76 

- [ ] identify reads which align with GFP
- [ ] use Samtools to see which reads present at certian sequences - this way we can categorise reads into plasmid type
- [ ] Screenshots of Tablet at important stages for presentation


### General Tasks
- [x] add GFP into all_ref.fasta
- [x] Ask Sam about Tablet
- [ ] What info can we extract from Blast - eg. shows us what plasmids are present
- [ ] rather than waiting until end - untils - analyse as you go - run until you get answer you want
- [x] read the fast5 format document sent by Sam (Claire and Hayley)
- [x] work out Biopython and how to link to NCBI Blast (Alex and Emma)
- [ ] Decide on live demo 





