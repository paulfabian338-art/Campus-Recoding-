def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest


def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest


def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count


def find_number(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index
    return -1


def reverse_list(items):
    result = []
    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])
    return result


def has_duplicates(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False


def first_duplicate(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return number
        seen.add(number)
    return None


def move_zeros(numbers):
    result = []
    zero_count = 0
    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)
    for _ in range(zero_count):
        result.append(0)
    return result


if __name__ == "__main__":
    print("find_largest:", find_largest([3, 41, 56, 21, 76, 9]))
    print("find_largest:", find_largest([-10, -5, -2, -18]))
    print("find_largest:", find_largest([]))
    print("find_smallest:", find_smallest([8, 3, 12, 1, 7]))
    print("find_smallest:", find_smallest([-3, -10, -1, -6]))
    print("list_sum:", list_sum([2, 4, 6, 8]))
    print("list_sum:", list_sum([-5, 10, -2]))
    print("list_sum:", list_sum([]))
    print("count_even:", count_even([1, 2, 3, 4, 6]))
    print("count_even:", count_even([1, 3, 5, 7]))
    print("count_occurrences:", count_occurrences([2, 5, 2, 8, 2], 2))
    print("count_occurrences:", count_occurrences([1, 4, 7], 10))
    print("find_number:", find_number([10, 25, 30, 45], 30))
    print("find_number:", find_number([5, 8, 5, 9], 5))
    print("find_number:", find_number([10, 20, 30], 99))
    print("reverse_list:", reverse_list([1, 2, 3, 4]))
    print("reverse_list:", reverse_list(["a", "b", "c"]))
    print("has_duplicates:", has_duplicates([1, 2, 3, 2]))
    print("has_duplicates:", has_duplicates([1, 2, 3, 4]))
    print("has_duplicates:", has_duplicates([]))
    print("first_duplicate:", first_duplicate([4, 7, 2, 7, 5, 4]))
    print("first_duplicate:", first_duplicate([1, 2, 3, 4]))
    print("first_duplicate:", first_duplicate([5, 5, 3]))
    print("move_zeros:", move_zeros([0, 1, 0, 3, 12]))
    print("move_zeros:", move_zeros([1, 2, 3]))
    print("move_zeros:", move_zeros([0, 0, 5]))
