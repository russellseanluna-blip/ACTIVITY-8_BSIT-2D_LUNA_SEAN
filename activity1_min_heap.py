class Heap:
    def __init__(self, is_min=True):
        self.heap = []
        self.is_min = is_min

    def size(self):
        return len(self.heap)

    def higher_priority(self, a, b):
        if self.is_min:
            return a < b
        return a > b

    def insert(self, value):
        self.heap.append(value)
        self._up(len(self.heap) - 1)

    def _up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.higher_priority(self.heap[index], self.heap[parent]):
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract(self):
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._down(0)

        return root

    def _down(self, index):
        n = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            best = index

            if left < n and self.higher_priority(
                self.heap[left], self.heap[best]
            ):
                best = left

            if right < n and self.higher_priority(
                self.heap[right], self.heap[best]
            ):
                best = right

            if best == index:
                break

            self.heap[index], self.heap[best] = self.heap[best], self.heap[index]
            index = best

numbers = [5, 9, 11, 14, 19, 17, 18, 13]

min_heap = Heap(is_min=True)

for number in numbers:
    min_heap.insert(number)

print("Min-Heap:")
while min_heap.size() > 0:
    print(min_heap.extract(), end=" ")
print()
