def hammingDistance(p: str, q: str) -> int:
    count = 0

    # This is based on the assumption that p and q have the same length
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1

    return count

def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    indices = []

    for i in range(len(text)-len(pattern)+1):
        if hammingDistance(pattern, text[i:i+len(pattern)]) <= d:
            indices.append(i)

    return indices

with open("tests/rosalind_ba1h.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	pattern = str_list[0]
	text = str_list[1]

print(" ".join(map(str, approximatePatternMatching(pattern, text, int(str_list[2])))))