def sum(l, i, n):
    return l[i] + sum(l, i + 1, n) if i != n \
        else 0