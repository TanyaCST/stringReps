import itertools

def hammingDistance(p: str, q: str) -> int:
    count = 0

    # This is based on the assumption that p and q have the same length
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1

    return count

def approximatePatternMatching(pattern: str, text: str, d: int) -> int:
    count = 0

    for i in range(len(text)-len(pattern)+1):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            count += 1

    return count

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    all_kmer = {}

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


with open("tests/rosalind_ba1i.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	text = str_list[0]
	numbers = str_list[1]
	k, d = numbers.split()

print(" ".join(map(str, frequentWordsWithMismatches(text, int(k), int(d)))))
