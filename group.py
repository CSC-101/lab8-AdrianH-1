
#TASK 1
def groups_of_3(numbers: list[int]) -> list[list[int]]:
    result = []
    i = 0  #starting index

    while i < len(numbers):
        result.append(numbers[i:i + 3])  # sublist of 3 element long list
        i += 3  #go on to next group of 3

    return result

