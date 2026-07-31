# Space comparison from the activity:

# Iterative binary search -- O(1) space:
lo, hi, steps = 0, n - 1, 0       # only 3 variables, always
# same lo, hi, mid reused every loop iteration

# Recursive binary search -- O(log n) space:
result, calls = binary_search_rec(scores, 0, n - 1, target)
print('Iterative : O(1) space  -- only lo, hi, mid')
print('Recursive : O(log n) space --', calls, 'stack frames for n =', n)

# Output:
# Iterative : O(1) space  -- only lo, hi, mid
# Recursive : O(log n) space -- 4 stack frames for n = 10
