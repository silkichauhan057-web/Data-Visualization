# Find union of two sets

set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))

union_set = set1 | set2

print(union_set)