# Nano_Hack

### DATA INPUT FILE FORMATTING

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

	cat *.fasta > all_reads.fasta
------------------------------------------------------------------------------------------------------------------

### NCBI Blast
![NCBI Logo](https://blast.ncbi.nlm.nih.gov/images/nucleutide-blast-cover.png)

https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch

Permissions on BLAST Recently changed - therefore Biopython no longer able to link in to Blast
So we will take a subset of plasmids and compare against them 

Library to use:

	all_ref.fasta

Code was written to linearise the refernces so that searches could me made without missing hits which **span across lines**

See file **______________.py**

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


### Tablet

Files to use:

	reads_aln.sorted.bam.bai
	
	all_ref_join.fasta

Files related to plasmids and genes like so:

	gi|21190.... = GFP gene seq
	ENA|AF246... = Gacs gene seq
	gi|437877... = pME6010 plasmid seq
	gi|209211... = pUC18 plasmid seq
	gi|130693... = Decoy plasmid seq

### Gacs

Search for the reads that align with the beginning of PU18 backbone but code for an **inserted gene**.
See file **insert.fasta**


Blast results:

	Pseudomonas protegens CHA0, complete genome 2645    2645    87% 0.0 82% 
	Pseudomonas fluorescens sensor kinase GacS (gacS) gene, complete cds 2645   2645    87% 0.0 82% 

See file **insert.fasta**
	
**Blast results:**

	Pseudomonas protegens CHA0, complete genome	2645	2645	87%	0.0	82%	
	Pseudomonas fluorescens sensor kinase GacS (gacS) gene, complete cds 2645	2645	87%	0.0	82%	
# EMBOSS Backtranseq

We know the amino acid sequence of the Δ76 Gacs mutated pUC18 plasmid.
We identified the amino acids surrounding the deletion site.

	…AGTALLAVRM   GRTINNPLTQIKQAVAQLKDGNLETRLPPLGSQELDELASGI
	NRMASTLQNAQEELQHSIDQATEDVRQNLETIEIQNI   ELDLARKEAL…
	
This information was obtained from the following academic paper:

	GacS Sensor Domains Pertinent to the Regulation of Exoproduct Formation and 
	to the Biocontrol Potential of Pseudomonas fluorescens CHA0
	
	ZubeR et al., 2002

*Available at*: http://apsjournals.apsnet.org/doi/pdf/10.1094/MPMI.2003.16.7.634

This **amino acid sequence** was converted back into a **DNA sequence** using EMBOSS Backtranseq

![EMBOSSS](https://www.ebi.ac.uk/web_guidelines/images/logos/EMBL-EBI/EMBL_EBI_Logo_black.png)

https://www.ebi.ac.uk/Tools/st/emboss_backtranseq/

The results were saved in **bases_around_deletion_Gacs.fasta**:

	>predicted sequence around the delta 76 delection site in Gacs
	GCCGGCACCGCCCTGCTGGCCGTGCGCATGGAGCTGGACCTGGCCCGCAAGGAGGCCCTG

This sequence was used to identify reads which related to the Δ76 Gacs mutated pUC18 plasmid.

*In the future, similar processes will be used to identify the H294R mutation and wild type reads and therefore, classify reads to each plasmid.




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





