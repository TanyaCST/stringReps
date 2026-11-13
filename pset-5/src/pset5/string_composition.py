def stringComposition(k: int, text: str) -> list[str]:
    """Return the k-mer composition of text, including repeated k-mers (BA3A)."""
    composition = []

    for i in range(len(text)-k+1):
        composition.append(text[i:i+k])

    sorted_composition = sorted(composition)

    return sorted_composition

with open("data/rosalind_ba3a.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	k = int(str_list[0])
	text = str_list[1]

composition = stringComposition(k, text)
for kmer in composition:
    print(kmer)