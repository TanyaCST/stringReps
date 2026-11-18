# Counting DNA Nucleorides
def count_nucleotides(text):
	dict = {} 

	for nucleotide in text:
		if nucleotide == "A":
			if "A" not in dict.keys():
				dict[nucleotide] = 1
			else:
				dict[nucleotide] += 1
		if nucleotide == "T":
                        if "T" not in dict.keys():
                                dict[nucleotide] = 1
                        else:
                                dict[nucleotide] += 1
		if nucleotide == "C":
                        if "C" not in dict.keys():
                                dict[nucleotide] = 1
                        else:
                                dict[nucleotide] += 1
		if nucleotide == "G":
                        if "G" not in dict.keys():
                                dict[nucleotide] = 1
                        else:
                                dict[nucleotide] += 1
		
	return dict.values()

