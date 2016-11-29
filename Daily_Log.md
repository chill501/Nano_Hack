# Nano_Hack

## 27th 
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

 
###Notes 
which poretools *shows where poretools instaleled*

ls -lct | head *view files by time*

grep -A 1 Barcoding_2d ___.fasta > 2d____.fasta  *print out line matched and 1st line after*

#Fast5 --> Fasta 

poretools fasta BC04 > BC04.fasta

- [x] Each fasta file now created (Claire and Hayley)

#Fasta --> Extracting 2D reads

See program **code.py**

- [ ] Check with Sam if we use 2D reads (Hayley and Claire)

Combine all reads into single file

cat *.fasta > all.fasta

# Blast
Recently changed - therefore Biopython no longer able to link in to Blast
So we will take a subset of plasmids and compare against them

- [x] find alternative to Blast 

Going to locally install databases 

### TASKS

- [x] read the fast5 format document sent by Sam (Claire and Hayley)
- [ ] work out Biopython and how to link to NCBI Blast (Alex and Emma)
- [ ] COmbine fast5 and fasta programs into one program
- [ ] Live demo for local library for BLAST
- [ ] rather than waiting until end - untils - analyse as you go - run until you get answer you want
