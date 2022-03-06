class HeapSort:
    def sort(self, array: list):
        array_length = len(array)
        for i in range((array_length - 1) // 2, -1, -1):
            self.pushdown(array, i, array_length - 1)

        for i in range(array_length - 1, 0, -1):
            self.swap(array, 0, i)
            self.pushdown(array, 0, i - 1)

    def pushdown(self, array: list, first: int, last: int):
        i = first
        while i <= (last - 1) // 2:
            if (2 * i) + 2 > last or array[(2 * i) + 1] < array[(2 * i) + 2]:
                j = (2 * i) + 1
            else:
                j = (2 * i) + 2
            if array[j] < array[i]:
                self.swap(array, i, j)
                i = j
            else:
                return

    def swap(self, array: list, i: int, j: int):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
