def hammingDistance(p: str, q: str) -> int:
    count = 0

    # This is based on the assumption that p and q have the same length
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1

    return count