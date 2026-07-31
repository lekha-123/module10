n = 4

# Formula way — total = n*(n+1)//2: 1 step always
total = n * (n + 1) // 2
print("Formula way  : total =", total, "| steps = 1")

# Loop way — single loop: n steps
total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print("Loop way     : total =", total, "| steps =", steps)

# Nested loop — two loops: roughly n*n steps
total = 0
steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        total += 1
        steps += 1
print("Nested loop  : total =", total, "| steps =", steps)

# Output:
# Formula way  : total = 10 | steps = 1
# Loop way     : total = 10 | steps = 4
# Nested loop  : total = 10 | steps = 10
