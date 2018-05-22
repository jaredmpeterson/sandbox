def sq_in_rect(length, width):
    long = max(length, width)
    print('long', long)
    short = min(length, width)
    print('short', short)
    mod = long % short
    return mod


print(sq_in_rect(2, 1))
print(sq_in_rect(3, 2))
