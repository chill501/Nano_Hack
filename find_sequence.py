#program to find "CACTGGCCGTGGTTTT" SEQUENCE IN ALL.FASTA FILe and return sequence before it + sequence itself

k = 0
f = open("all.fasta", "r")
g = open("output.txt", "w")
content = [x.strip('\n') for x in f.readlines()]
for i, element in enumerate(content):
#    if element.startswith(">"):
#        sequence = content[i+1]
#        for nucleotide in range(0,len(sequence)):
#            if sequence[nucleotide:nucleotide+8] == "CGTGGTTTT":
#                print "Yes" 

    if element.startswith(">"):        
        sequence = content[i+1]
        for nucl in range(0,len(sequence)):
            if sequence[nucl:nucl+13] == "CCGTCGTTTTACA":
                p = sequence.find("CCGTCGTTTTACA")
                print sequence[0:p+13]
                print element                
                k += 1
print k
