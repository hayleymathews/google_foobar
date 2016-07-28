from __future__ import division
from functools import wraps

def answer(N, K):
    return(str(get_graphs(N, K)))

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def get_graphs(N, K):
    edges = get_combos_count(N, 2)
    graphs = get_combos_count(edges, K)
    for x in range(1, N):
        y = get_combos_count(N - 1, x - 1)
        max_edges = min(get_combos_count(x, 2), K)
        for edge in range(x - 1, max_edges + 1):
            bad_graphs = (y * get_graphs(x, edge) * get_combos_count(get_combos_count(N - x, 2), K - edge))
            graphs -= bad_graphs
    return(graphs)

@memo
def get_combos_count(N, K):
    if K == N or K == 0:
        return 1
    nom = 1
    denom = 1
    count = 1
    while count <= K:
        nom *= N
        denom *= count
        count += 1
        N -= 1
    combos_count = nom // denom
    return(combos_count)
