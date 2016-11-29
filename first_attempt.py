#I will try to extract sequences from bc04_reads.fasta and feed them to BioPython
from Bio.Blast import NCBIWWW


f = open("bc04_reads.fasta", "r")
g = open("output.txt", "w")

content = [x.strip('\n') for x in f.readlines()]
for i, element in enumerate(content):
    if element.startswith(">"):
        sequence = content[i+1]
#        g.write(sequence)
#        g.write("\n")
        result_handle = NCBIWWW.qblast("blastn", "nt", sequence, entrez_query="36549[taxid]")
        print result_handle
#        print sequence # works, we extracted the sequence from fasta file and saved in output.txt
g.close()
