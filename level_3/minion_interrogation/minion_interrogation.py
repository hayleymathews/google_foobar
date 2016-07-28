from __future__ import division

def answer(minions):
    expected_time = [time / (numerator / denominator)
                     for time, numerator, denominator in minions]
    answer = sorted(range(len(minions)), key = expected_time.__getitem__)
    return(answer)
