"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""

def frequency_table(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    
    frequency_dict = {}
    
    for i in range(len(text)):
        pattern = text[i:i+k]
        if pattern not in frequency_dict.keys():
            frequency_dict[pattern] = 1
        else:
            frequency_dict[pattern] += 1
    
    return frequency_dict

def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    """Return distinct k-mers appearing at least t times in any length-L window.

    Count overlapping occurrences fully contained within each window.
    Assume uppercase DNA, 1 <= k <= L <= len(genome), and t >= 1.
    Each qualifying k-mer appears only once in the returned set.
    """
    clumps = set()

    for i in range(len(genome)):
        window = genome[i:i+L]
        curr_f_table = frequency_table(window, k)

        for key in curr_f_table.keys():
            if curr_f_table[key] >= t:
                if key not in clumps:
                    clumps.add(key)
        
    return clumps


with open("rosalind_test/rosalind_ba1e.txt", "r") as file:
	str_list = []
	for line in file:
		line = line.rstrip()
		str_list.append(line)

	text = str_list[0]
	numbers = str_list[1]
	k, L, t = numbers.split()

print(" ".join(sorted(findClumps(text, int(k), int(L), int(t)))))