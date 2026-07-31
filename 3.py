# Asymptotic simplification — keep the dominant term:

# 3n^2 + 5n + 9   ->  O(n^2)   (n^2 dominates for large n)
# 7n + 100        ->  O(n)     (n dominates, constant 100 drops)
# n*(n-1)/2       ->  O(n^2)   (expand: n^2/2 - n/2, dominant = n^2)
# 500             ->  O(1)     (no n at all, always constant)

# Proof for n = 1000:
n = 1000
full  = 3*n**2 + 5*n + 9
dominant = n**2
print('Full expression :', full)      # 3,005,009
print('Dominant term   :', dominant)  # 1,000,000
print('Ratio           :', round(full / dominant, 2))  # ~3.0
# The ratio stays near a constant — the shape is the same.


# Big-O: worst case for linear search
names = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']
n = len(names)        # n = 5

# Worst case: target is the LAST element
target = 'Kabir'
steps  = 0
for name in names:
    steps += 1
    if name == target:
        break

print('Target   :', target)
print('Steps    :', steps, '(worst case = n =', n, ')')
print('Big-O    : O(n)')   # upper bound -- never more than n steps

# Output:
# Target   : Kabir
# Steps    : 5  (worst case = n = 5)
# Big-O    : O(n)


# Omega: best case for linear search
names = ['Aarav', 'Priya', 'Dev', 'Meera', 'Kabir']

# Best case: target is the FIRST element
target = 'Aarav'
steps  = 0
for name in names:
    steps += 1
    if name == target:
        break

print('Target   :', target)
print('Steps    :', steps, '(best case = 1)')
print('Omega    : Omega(1)')  # lower bound -- can be as fast as 1 step

# Output:
# Target   : Aarav
# Steps    : 1  (best case = 1)
# Omega    : Omega(1)


# Theta(1): direct index access -- always exactly 1 step
scores = [90, 75, 88, 62, 95]

steps = 1
top_score = scores[0]   # one operation, always
print('Score   :', top_score)
print('Steps   :', steps)
print('Theta   : Theta(1) -- best case = worst case = 1 step')

# Output:
# Score   : 90
# Steps   : 1
# Theta   : Theta(1) -- best case = worst case = 1 step

# Theta(n): a loop with NO early exit always runs exactly n times
n = len(scores)
total = 0
for score in scores:       # always runs exactly n times
    total += score
print('Total   :', total)  # always n additions -- Theta(n)
