"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

sums = {}
diffs = {}

for i in q:
    for j in q:
        add = f(i) + f(j)
        diff = f(i) - f(j)
        if (i, j) not in sums:
            sums[(i, j)] = add
        if (i, j) not in diffs:
            diffs[(i, j)] = diff

# print(sums)
# print(diffs)

ind_sum = 0
ind_diff = 0

for i in sums:
    for j in diffs:
        if sums[i] == diffs[j] and not i == j:
            print(f"f({i[0]}) + f({i[1]}) = f({j[0]}) - f({j[1]})    {f(i[0])} + {f(i[1])} = {f(j[0])} - {f(j[1])}")