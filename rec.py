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
# Call counter proves O(log n) for recursive binary search:

result, calls = binary_search_rec(scores, 0, n - 1, target)
print('Recursive search : index =', result, '| calls =', calls)

# Output: Recursive search : index = 9 | calls = 4

# For n=10:   calls = 4   (log2(10) = 3.32, rounded up)
# For n=100:  calls = 7   (log2(100) = 6.64)
# For n=1000: calls = 10  (log2(1000) = 9.97)
# Total calls grow logarithmically -- O(log n)
