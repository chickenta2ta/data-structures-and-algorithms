class BubbleSort:
    def sort(self, array: list):
        array_length = len(array)
        for i in range(array_length - 1):
            for j in range(array_length - 1, i, -1):
                if array[j] < array[j - 1]:
                    self.swap(array, j, j - 1)

    def swap(self, array: list, i: int, j: int):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
