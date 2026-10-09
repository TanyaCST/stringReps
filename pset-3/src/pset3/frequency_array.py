"""Rosalind BA1K: Generate the Frequency Array of a String."""


def PatternCount(text: str, pattern: str) -> int:
    """Return the number of occurrences of pattern in text.

    Matches are case-sensitive and may overlap. Assume pattern is nonempty.
    Return 0 if pattern is longer than text or text is empty.

    Example:
        PatternCount("AAAA", "AA") returns 3.
    """
    # TODO: Implement this function.

    count = 0

    for i in range(len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1

    return count

    # raise NotImplementedError("Implement PatternCount")

def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    frequency = []
    nuc = ["A", "C", "G", "T"]
    for i in nuc:
        for j in nuc:
            for m in nuc:
                for n in nuc:
                    frequency.append(PatternCount(text, i+j+m+n))

    return frequency


result = frequencyArray("ACGCGGCTCTGAAA", 4)
print(result)

    # TODO: Implement the frequency array.
    #raise NotImplementedError("Implement frequencyArray for Rosalind BA1K.")
