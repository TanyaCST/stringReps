def deBruijnFromKmers(patterns: list[str]) -> dict[str:list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    deBruijn = {}

    for kmer in patterns:
        if kmer[:-1] not in deBruijn:
            deBruijn[kmer[:-1]] = [kmer[1:]]
        else:
            deBruijn[kmer[:-1]].append(kmer[1:])

    sorted_keys = sorted(deBruijn)

    new_deBruijn = {}

    for key in sorted_keys:
        new_deBruijn[key] = sorted(deBruijn[key])
    
    return new_deBruijn

with open("data/rosalind_ba3e.txt", "r") as file:
    patterns = []
    for line in file:
        line = line.rstrip()
        patterns.append(line)

output = deBruijnFromKmers(patterns)

with open("output/rosalind_ba3e_output.txt", "w", encoding="utf-8") as f:
    for key in output.keys():
        overlaps = ",".join(map(str, output[key]))
        f.write(f"{key} -> {overlaps}\n")
