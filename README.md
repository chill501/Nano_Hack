# Nano_Hack

## Part of the Oxford DTP Hackathon for Bioinformatics.

We are stranded on the moon...
Someone has been compromised by a pathogenic moon bacterium 
This bacterium carries a mutated plasmid now encoding a toxic protein 
To make it home safely we need to identify…
	Who has been infected?
	

#### Our Mission
Analyse reads from multiple bacterial plasmids altogether 

#### How it works
We sequenced all the bacterial plasmid DNA extracted from our blood samples using Nanopore.  
No access to barcoding.  
Unable to isolate each bacterial species.  
We need to identify which plasmids are present in each sample.  



#### Where are we now

These plasmids are present in our sample:  
pUC18 plasmid with wild type GacS.    
pUC18 plasmid with Δ76 mutated GacS.   
pUC18 plasmid with H294R mutated Gacs.   
pME6010 plasmid with GacS.    
pME6010 plasmid with GFP.      
Identify and classify a number of reads from unique features:  
Identified three categories


#### Where we want to go

Further classify reads for each plasmid:  
Identifying specific mutations in read data.   
Allowing accurate assembly and identification.   
Utilise the entire NCBI Blast database:    
Not limited to our reference library of suspected plasmids.   



 
	



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

### ANALYSIS AND ALIGNMENT 

### NCBI Blast
![NCBI Logo](https://blast.ncbi.nlm.nih.gov/images/nucleutide-blast-cover.png)

https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch

Permissions on BLAST Recently changed - therefore Biopython no longer able to link in to Blast
So we will take a subset of plasmids and compare against them 

Library to use:

	all_ref.fasta

Code was written to linearise the refernces so that searches could me made without missing hits which **span across lines**

See file **linearize_plasmid.py**

This produced the file:
	
	linar_all_ref.fasta

### BWA

For long read **alignment** you need another software tool. Use bwa like this:

    git clone https://github.com/lh3/bwa.git

 Copy **input files** into bwa folder:
 
 > 2dolder_read.fasta
 
 > all_ref.fasta
 
 > all_ref_join.fasta
    
    cd bwa

    make 

    bwa index all_ref.fasta

    bwa mem -x ont2d all_ref.fasta 2dolder_reads.fasta > bigreads_aln.sam

    samtools view -bS bigreads_aln.sam > bigreads_aln.bam

    samtools sort bigreads_aln.bam -o bigreads_aln.sorted.bam
    
    samtools index bigreads_aln.sorted.bam

  You can look at these alignments with a software package called **Tablet**

Important **Output files** form bwa:
	
	bigreads_aln.sorted.bam
	
	bigreads_aln.sorted.bam.bai

	
### Tablet

Files to use:

	bigreads_aln.sorted.bam.bai
	
	all_ref_join.fasta

Files related to plasmids and genes like so:

	gi|21190.... = GFP gene seq
	ENA|AF246... = Gacs gene seq
	gi|437877... = pME6010 plasmid seq
	gi|209211... = pUC18 plasmid seq
	gi|130693... = Decoy plasmid seq
	
For **example Tablet outputs** see files:

	GFP.png
	GacS.png
	pME6010.png
	pUC18.png
	DECOY.png
	
------------------------------------------------------------------------------------------------------------------

### EVALUATION 

### Gacs and GFP inserts

Three Gacs versions are present in the sample:
	
	wild type
	Δ76 deletion
	H294R mutation
	
One version of GRP is present.
	
Searching for the reads that align with the plasmid backbone but code for an **inserted gene**.

- Identify reads which abruptly start in the plasmid backbone.
- Take the sequence at the beginning of these reads
- Use the python code **find_gacs_in_pME6010.py** to search reads with this sequence and report the sequence of bases beside.
- **Blast** these sequences to see what they encode for.

**e.g. Blast results:**

	Pseudomonas protegens CHA0, complete genome                          2645    2645   87%    0.0    82% 
	Pseudomonas fluorescens sensor kinase GacS (gacS) gene, complete cds 2645   2645    87%    0.0    82% 
	
This identifies the presence of the pME6010 genome with a Gacs insert - 5 reads came up.

**find_gacs_in_pME6010.py** can be easily modiifed to search for seq present in reads which cover both plasmid and insert.


### EMBOSS Backtranseq

![EMBOSSS](https://www.ebi.ac.uk/web_guidelines/images/logos/EMBL-EBI/EMBL_EBI_Logo_black.png)

https://www.ebi.ac.uk/Tools/st/emboss_backtranseq/

We know the amino acid sequence of the Δ76 Gacs mutated pUC18 plasmid.
We identified the amino acids surrounding the deletion site.

	…AGTALLAVRM   GRTINNPLTQIKQAVAQLKDGNLETRLPPLGSQELDELASGI
	NRMASTLQNAQEELQHSIDQATEDVRQNLETIEIQNI   ELDLARKEAL…
	
This information was obtained from the following academic paper:

> GacS Sensor Domains Pertinent to the Regulation of Exoproduct Formation and 
> to the Biocontrol Potential of Pseudomonas fluorescens CHA0
	
> ZubeR et al., 2002

> Available at: http://apsjournals.apsnet.org/doi/pdf/10.1094/MPMI.2003.16.7.634

This **amino acid sequence** was converted back into a **DNA sequence** using EMBOSS Backtranseq


The results were saved in **bases_around_deletion_Gacs.fasta**:

	>predicted sequence around the delta 76 delection site in Gacs
	GCCGGCACCGCCCTGCTGGCCGTGCGCATGGAGCTGGACCTGGCCCGCAAGGAGGCCCTG

This sequence was used to identify reads which related to the Δ76 Gacs mutated pUC18 plasmid.

We also developed a program to search for the specific delta 76 mutation in GacS
**find_del_gacS.py**

*In the future, similar processes will be used to identify the H294R mutation and wild type reads and therefore, classify reads to each plasmid.*
