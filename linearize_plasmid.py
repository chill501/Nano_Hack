f = open("all_ref.fa", "r")
linear_ref = open("linear_all_ref.fa", "w")
linear_GFP = ''
linear_gacS = ''
linear_pME6010 = ''
linear_pUC18 = ''
linear_control = ''
content = [x.strip('\n') for x in f.readlines()]

for i, line in enumerate(content):
    if line.startswith(">gi|211909964"):
#        print line
        linear_ref.write(line +"\n")
        while not content[i+1].startswith(">"):
            linear_GFP += content[i+1]
            i += 1
        linear_ref.write(linear_GFP+ "\n")

    elif line.startswith(">ENA|AF246292|"):
#        print line
        linear_ref.write(line +"\n")
        while not content[i+1].startswith(">"):        
            linear_gacS += content[i+1]
            i += 1
        linear_ref.write(linear_gacS + "\n")        
    elif line.startswith(">gi|130693907|gb"):
#        print line
        linear_ref.write(line +"\n")
        while not content[i+1].startswith(">"):        
            linear_control += content[i+1]
            i += 1
        linear_ref.write(linear_control+ "\n")        
    elif line.startswith(">gi|4378778|gb|"):
#        print line
        linear_ref.write(line+"\n")
        while not content[i+1].startswith(">"):        
            linear_pME6010 += content[i+1]
            i += 1
        linear_ref.write(linear_pME6010+ "\n") 
    elif line.startswith(">gi|209211|gb|L08752.1"):
#        print line
        linear_ref.write(line+"\n")
        while not content[i+1].startswith(">"):        
            linear_pUC18 += content[i+1]
            i += 1
        linear_ref.write(linear_pUC18+ "\n") 

linear_ref.close()
