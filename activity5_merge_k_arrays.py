def merge_k_sorted(arrays):
    heap = Heap(is_min=True)
    result = []

    for i in range(len(arrays)):
        if arrays[i]:
            heap.insert((arrays[i][0], i, 0))

    while heap.size() > 0:
        value, array_index, element_index = heap.extract()
        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heap.insert((next_value, array_index, next_index))

    return result


arrays = [
    [1, 4, 7],
    [2, 5],
    [3, 6, 8, 9]
]

print("Merged:", merge_k_sorted(arrays))
