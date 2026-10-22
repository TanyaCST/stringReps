"""Rosalind BA1K: Generate the Frequency Array of a String."""
import itertools

def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    # Pseudocode
    # 1. Create a frequency table of all kmers with f=0
    # Reference: https://docs.python.org/3/library/itertools.html
    #            https://www.geeksforgeeks.org/python/python-itertools-product/
    # 2. Traverse the text to fill in the actual frequency
    # 3. Sort the keys of the table with python sorted (abandoned)
    # 4. Create a empty frequency arraylist (abandoned)
    #    --> Iterate through the sorted keys and append them into the arraylist

    # Set up a frequency table for all k mer e
    all_kmers = {}

    for kmer in itertools.product("ACGT", repeat = k):
        all_kmers["".join(kmer)] = 0

    # Update kmer frequency based on the text
    for i in range(len(text)-k+1):
        all_kmers[text[i:i+k]] += 1

    return all_kmers.values()

with open("rosalind_test/rosalind_ba1k.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	text = str_list[0]
	k = int(str_list[1])

print(" ".join(map(str, frequencyArray(text, k))))