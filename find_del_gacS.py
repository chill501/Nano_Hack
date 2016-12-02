#program to find reads that cover pME6010 and CasG gene
import re
f = open("2dolder_reads.fa", "r")
g = open("output_for_del_gacS_pME6010.txt", "w")
linear_ref = open("linear_all_ref.fa", "r")
content = [x.strip('\n') for x in f.readlines()]
linear_ref_2 = linear_ref.readlines()


seq_before = []

for i, element in enumerate(content):   
        if element.startswith(">"):
            seq = content[i+1]                
            if re.search(r"AAGAAGGTGTTG", seq): #finding reads that cover 3' of plasmid (pME6010) 
                    r = seq.find("AAGAAGGTGTTG")
                    print "Hi" #finding reads that cover 5' end of casG gene
                    if re.search(r"CATG.........GAGC", seq):    
#                            print q, "", r                          
                            print element
 #                           print q-r
#                            if q-r > 0:
                            g.write(element + "\n")
                            g.write(seq + "\n")
#                                g.write(seq[q:r] + "\n")

linear_ref.close()
f.close()
g.close()  #saving reads to output.txt 
