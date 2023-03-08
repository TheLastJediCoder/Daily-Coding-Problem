"""
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements,
return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""

case_one = [-6, 0, 2, 40]
case_two = [1, 5, 7, 8]


def find_fix_point_in_array(arr: list) -> int:
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(find_fix_point_in_array(case_one))
print(find_fix_point_in_array(case_two))
