#Original DNA sequence

dna_seq = input("Enter the sequence:")

seq_list = list(dna_seq)

print (seq_list)

#To be mutated

pos = int(input("Enter the position to be mutated:"))

print ("The nucleotide base that has been changed is:" ,seq_list.pop(pos - 1))
next = input("Enter the nucleotide base that is set to be replacing the changed one:")
seq_list.insert ( pos-1,next)
print ("The sequence of DNA after mutation is:")
#for i in range (len(seq_list)):
  #print(seq_list[i])
print (' '.join(map(str,seq_list)))

