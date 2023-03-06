# This problem was asked by Apple.
# A fixed point in an array is an element whose value is equal to its index. 
# Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
case_one = [-6, 0, 2, 40]
case_two = [1, 5, 7, 8]

def solve(arr: list) -> int:
    for index, number in enumerate(arr):
        if number == index:
            return index
    return False

print(solve(case_one))
print(solve(case_two))