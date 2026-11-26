def heap_sort(arr):
    heap = Heap(is_min=False)

    for number in arr:
        heap.insert(number)

    result = [0] * heap.size()

    for i in range(len(result) - 1, -1, -1):
        result[i] = heap.extract()

    return result


print("Heap Sort:", heap_sort([4, 10, 3, 5, 1]))
print("Sorted:", heap_sort([1, 2, 3, 4, 5]))
print("Reverse:", heap_sort([5, 4, 3, 2, 1]))
print("Duplicates:", heap_sort([4, 2, 4, 1, 2]))
print("Empty:", heap_sort([]))
