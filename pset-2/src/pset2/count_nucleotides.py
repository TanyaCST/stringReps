def countNucleotides(text: str):
	dictionary = {"A" : 0, "T":0, "C":0, "G":0} 

	for nucleotide in text:
		if nucleotide == "A":
			dictionary[nucleotide] += 1
		if nucleotide == "T":
			dictionary[nucleotide] += 1
		if nucleotide == "C":
			dictionary[nucleotide] += 1
		if nucleotide == "G":
			dictionary[nucleotide] += 1
		
	string = str(dictionary["A"]) + " " + str(dictionary["C"]) + " " + str(dictionary["G"]) + " " + str(dictionary["T"])
	return string


with open("rosalind_dna.txt", "r") as f:
    text = f.read()

print(countNucleotides(text))