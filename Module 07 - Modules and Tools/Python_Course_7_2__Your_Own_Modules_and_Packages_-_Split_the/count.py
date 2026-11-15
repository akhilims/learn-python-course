from collections import Counter
from parse import level_of

def count_levels(lines):
    counts = Counter()
    for line in lines:
        counts[level_of(line)] += 1
    return counts
