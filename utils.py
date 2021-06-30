def multi_split(seq, indices):
    """Split sequence at indices"""
    prev_split_point = 0
    for split_point in indices:
        yield seq[prev_split_point:split_point]
        prev_split_point = split_point
    yield seq[prev_split_point:]