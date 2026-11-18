"""Rosalind BA1C: Find the Reverse Complement of a String."""


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
