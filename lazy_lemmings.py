"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


# def furthest(num_holes, cafes):
#     """Find longest distance between a hole and a cafe."""

#     distances = [cafes[0],
#                  num_holes - cafes[-1] - 1]

#     print distances 
#     for i in range(1, len(cafes)):
#         distances.append((cafes[i] - cafes[i - 1]) // 2)
#     print distances
#     return max(distances)

def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # START SOLUTION

    worst = 0

    for hole in range(num_holes):
        # Looking at all cafes, find distance to this hole,
        # and choose the smallest distance.

        dist = [abs(hole - cafe) for cafe in cafes]

        # Keep track of the longest distance we've seen

        worst = max(worst, dist)

    return worst

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
