def deBruijnFromString(k: int, text: str) -> dict[str:list[str]]:
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    # Find all kmers in the original text
    kmers = []

    for i in range(len(text)-k+1):
        kmers.append(text[i:i+k])

    # Extract the deBruijn graph
    deBruijn = {}

    for kmer in kmers:
        if kmer[:-1] not in deBruijn:
            deBruijn[kmer[:-1]] = [kmer[1:]]
        else:
            deBruijn[kmer[:-1]].append(kmer[1:])

    return deBruijn

with open("data/rosalind_ba3d.txt", "r") as file:
    inputs = []
    for line in file:
        line = line.rstrip()
        inputs.append(line)

k = int(inputs[0])
text = inputs[1]

output = deBruijnFromString(k, text)

with open("output/rosalind_ba3d_output.txt", "w", encoding="utf-8") as f:
    for key in output.keys():
        overlaps = ",".join(map(str, output[key]))
        f.write(f"{key} -> {overlaps}\n")
