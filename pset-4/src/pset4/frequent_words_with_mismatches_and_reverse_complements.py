import itertools

def hammingDistance(p: str, q: str) -> int:
    count = 0

    # This is based on the assumption that p and q have the same length
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1

    return count

def reverseComplement(text: str) -> str:
    """Return the reverse complement of an uppercase DNA string.

    A pairs with T, and C pairs with G. Return the complementary
    nucleotides in reverse order.
    """
    # From the tail of text, append its reverse
    reverse = ""

    i = len(text) - 1

    while i >= 0:
        if text[i] == "A":
            reverse += "T"

        if text[i] == "T":
            reverse += "A"

        if text[i] == "C":
            reverse += "G"

        if text[i] == "G":
            reverse += "C"

        i -= 1

    return reverse

def approximatePatternMatching(pattern: str, text: str, d: int) -> int:
    # This incorporates reverse complement
    count = 0

    for i in range(len(text)-len(pattern)+1):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            count += 1

        reverse = reverseComplement(pattern)

        if hammingDistance(reverse, text[i:i+len(reverse)]) <= d:
            count += 1

    return count

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    all_kmer = {}

    # Generate all possible kmers 
    for kmer in itertools.product("ACGT", repeat = k):
        all_kmer["".join(kmer)] = 0

    for kmer in all_kmer.keys():
        all_kmer[kmer] = approximatePatternMatching(kmer, text, d)

    max_pattern = set()
    max_count = max(all_kmer.values())

    for kmer in all_kmer.keys():
        if all_kmer[kmer] == max_count:
            max_pattern.add(kmer)

    return max_pattern


with open("tests/rosalind_ba1j.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	text = str_list[0]
	numbers = str_list[1]
	k, d = numbers.split()

print(" ".join(map(str, frequentWordsWithMismatchesAndReverseComplements(text, int(k), int(d)))))
