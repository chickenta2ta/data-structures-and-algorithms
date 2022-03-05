class QuickSort:
    def sort(self, array: list):
        self.sort_(array, 0, len(array) - 1)

    def sort_(self, array: list, i: int, j: int):
        if i == j:
            return

        pivot = self.find_pivot(array, i, j)
        k = self.partition(array, i, j, pivot)

        self.sort_(array, i, k - 1)
        self.sort_(array, k, j)

    def find_pivot(self, array: list, i: int, j: int):
        for k in range(i + 1, j + 1):
            if array[k] > array[i]:
                return array[k]
            elif array[k] < array[i]:
                return array[i]
        return array[i]

    def partition(self, array: list, i: int, j: int, pivot: int):
        while True:
            while array[i] < pivot:
                i = i + 1
            while array[j] >= pivot:
                j = j - 1
            if i > j:
                return i
            self.swap(array, i, j)

    def swap(self, array: list, i: int, j: int):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
