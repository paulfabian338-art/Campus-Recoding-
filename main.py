# def find_largest(numbers):
#     if not numbers:
#         return None
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest:
#            largest = number
#     return largest


# print(find_largest([3, 41, 56, 21, 76, 9]))
# print(find_largest([-10, -5, -2, -18]))
# print(find_largest([]))


# def find_smallest(numbers):
#     if not numbers:
#         return None
#     smallest = numbers[0]
#     for number in numbers:
#         if number < smallest:
#             smallest = number
#     return smallest

# print(find_smallest([8, 3, 12, 1, 7]))
# print(find_smallest([-3, -10, -1, -6]))


# def list_sum(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total

# print(list_sum([2, 4, 6, 8]))
# print(list_sum([-5, 10, -2]))

# def count_even(numbers):
#     count = 0
#     for number in numbers:
#        if number % 2 == 0:
#         count += 1
#     return count

# print(count_even([1, 2, 3, 4, 6]))
# print(count_even([1, 3, 5, 7]))


# def count_occurrences(numbers, target):
#     counter = 0

#     for number in numbers:
#         if number == target:
#            counter += 1
#     return counter

# print(count_occurrences([2, 5, 2, 8, 2],target = 2))
# print(count_occurrences([1, 4, 7],target = 10))

def find_number(numbers, target):
    for idx, number in enumerate(numbers):
        if number == target:
            return idx
    return -1

print(find_number([10, 25, 30, 45], target = 30))
print(find_number([5, 8, 5, 9], target = 5))
print(find_number([10, 20, 30], target = 99))

