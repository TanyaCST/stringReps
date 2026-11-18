def stringSpelledByGenomePath(patterns: list[str]) -> str:
    """Return the string spelled by the ordered genome path (BA3B)."""
    output = patterns[0]

    for kmer in patterns[1:]:
        output = output + kmer[len(kmer)-1]

    return output

with open("data/rosalind_ba3b.txt", "r") as file:
	pattern = []
	for line in file:
		line = line.rstrip()
		pattern.append(line)

print(stringSpelledByGenomePath(pattern))