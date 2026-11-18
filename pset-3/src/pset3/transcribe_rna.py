"""Rosalind RNA: Transcribing DNA into RNA."""


def transcribeRNA(text: str) -> str:
    """Return the RNA string corresponding to an uppercase DNA coding strand.

    Replace each T with U, retaining the order of the other nucleotides.
    """
    rna = ""
    for i in range(len(text)):
        if text[i] == "T":
            rna += "U"
        else:
            rna += text[i]

    return rna
