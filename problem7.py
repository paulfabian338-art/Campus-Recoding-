def reverse_list(items):
    result = []
    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])
    return result

    print(reverse_list([1, 2, 3, 4]))
    print(reverse_list(["a", "b", "c"]))
