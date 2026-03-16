def adjust_difficulty(current_difficulty, correct):

    order = ["easy", "medium", "hard"]

    index = order.index(current_difficulty)

    if correct and index < 2:
        return order[index + 1]

    if not correct and index > 0:
        return order[index - 1]

    return current_difficulty