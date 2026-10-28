def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    print(list_sum([2, 4, 6, 8]))
    print(list_sum([-5, 10, -2]))
    print(list_sum([]))
