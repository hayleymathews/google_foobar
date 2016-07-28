from itertools import combinations
from itertools import chain
from pprint import pprint
from functools import wraps



def answer(N, K):
    edges = list(combinations(range(0,N), 2))
    edges_combos = list(combinations(edges, K))
    count = len(edges_combos)
    for edges_combo in edges_combos:
        items = list(chain.from_iterable(edges_combo))
        if len(set(items)) != N:
            count -= 1
    return(count)
