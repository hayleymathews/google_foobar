def answer(heights):
    max_height = max(heights)
    level_height = 1
    answer = 0
    while level_height <= max_height -1:
        level = []
        count = 1
        for height in heights:
            if height >= level_height:
                level.append(count)
            count +=1
        start, end = level[0], level[-1]
        full_level = range(start, end + 1)
        gaps = [x for x in full_level if not x in level]
        answer += len(gaps)
        level_height += 1
    return(answer)
