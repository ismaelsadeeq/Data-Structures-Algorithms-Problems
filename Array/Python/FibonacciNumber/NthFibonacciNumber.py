def getNthFib(n):
    # Write your code here.
    seq = [0, 1]
    for i in range(n):
        if i == 0 or i == 1:
            continue
        seq.append(seq[-1] + seq[-2])

    return seq[n-1]