def answer(digest):
    message = []
    lower =   0 / 256 + 1
    upper = 256*129 / 256 + 1
    for index, value in enumerate(digest):
        if index == 0:
            previous = 0
        else:
            previous = message[index - 1]
        possibilities = [x * 256 + value for x in range(lower, upper)]
        for possibility in possibilities:
            if (possibility ^ previous) % 129 == 0:
                message.append(((possibility ^ previous) / 129) % 256)
    return(message)
