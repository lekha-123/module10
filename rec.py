def binary_search_rec(scores, lo, hi, target, calls=0):
    calls += 1                        # count this call
    if lo > hi:
        return -1, calls              # base case: not found
    mid = (lo + hi) // 2
    if scores[mid] == target:
        return mid, calls             # base case: found
    elif scores[mid] < target:
        return binary_search_rec(scores, mid + 1, hi, target, calls)
    else:
        return binary_search_rec(scores, lo, mid - 1, target, calls)

result, calls = binary_search_rec(scores, 0, 9, 98)
# Output: index = 9, calls = 4
