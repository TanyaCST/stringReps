"""Count occurrences of a pattern in text."""


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
