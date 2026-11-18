def overlapGraph(patterns: list[str]) -> dict[str:list[str]]:
    """Return the overlap graph as rows [source, destination] (BA3C).

    Each row contains one directed edge, with the source first.
    Row order does not matter.
    """

    # Set up 2 dictionaries that match prefixes and suffixes with their indices
    prefix = {}
    suffix = {}

    for i in range(len(patterns)):
        if pattern[i][:-1] not in prefix:
            prefix[pattern[i][:-1]] = [i]
        else:
            prefix[pattern[i][:-1]].append(i)

        if pattern[i][1:] not in suffix:
            suffix[pattern[i][1:]] = [i]
        else:
            suffix[pattern[i][1:]].append(i)

    overlap = {}

    for p in prefix.keys():
        if p in suffix:
            for s_index in suffix[p]:
                for p_index in prefix[p]:
                    if patterns[s_index] not in overlap:
                        overlap[patterns[s_index]] = [patterns[p_index]]
                    else:
                        overlap[patterns[s_index]].append(patterns[p_index])
    
    return overlap


with open("data/rosalind_ba3c.txt", "r") as file:
    pattern = []
    for line in file:
        line = line.rstrip()
        pattern.append(line)

output = overlapGraph(pattern)

with open("output/rosalind_ba3c_output.txt", "w", encoding="utf-8") as f:
    for key in output.keys():
        overlaps = ",".join(map(str, output[key]))
        f.write(f"{key} -> {overlaps}\n")