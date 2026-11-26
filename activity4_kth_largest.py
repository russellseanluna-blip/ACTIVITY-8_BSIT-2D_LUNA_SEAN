def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    heap = Heap(is_min=True)

    for number in numbers:
        heap.insert(number)

        if heap.size() > k:
            heap.extract()

    return heap.peek()


numbers = [7, 2, 9, 4, 1, 6]
k = 3

print("Kth Largest:", kth_largest(numbers, k))
print("Verified:", sorted(numbers, reverse=True)[k - 1])
