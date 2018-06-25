def invert(items: list):
    inverse = []
    for item in items:
        inverse.append(item * -1)
    return inverse


# Best Practice
def invert(lst: list):
    return [-x for x in lst]
