def answer(x):
    count = 0
    powers = []
    quotient, remainder = (x-1) / 3, (x-1)  % 3
    while quotient >= 0:
        powers.append([count, remainder])
        if remainder == 0:
            quotient -= 1
        quotient, remainder = quotient / 3, quotient  % 3
        count += 1
    answer = []
    for power in powers:
        if power[1] == 1:
            answer.append("L")
        elif power[1] == 0:
            answer.append("R")
        else:
            answer.append("-")
    return(answer)
