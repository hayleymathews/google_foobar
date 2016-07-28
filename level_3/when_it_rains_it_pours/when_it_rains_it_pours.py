def answer(heights):
    if len(heights) < 3:
        return 0
    answer = 0
    position = 0
    while position < len(heights) - 1:
        target = position + 1
        for stack in range(position + 1, len(heights)):
            if heights[stack] >= heights[position]:
                target = stack
                break
            if heights[stack] > heights[target]:
                target = stack
        if target == position:
            return(answer)
        top = min(heights[position], heights[target])
        position += 1
        while position < target:
            answer += top - heights[position]
            position += 1
    return(answer)
