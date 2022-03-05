class MergeSort:
    def sort(self, array: list):
        array_length = len(array)
        if array_length <= 1:
            return array

        array0 = self.sort(array[: array_length // 2])
        array1 = self.sort(array[array_length // 2 :])

        merged_array = self.merge(array0, array1)
        return merged_array

    def merge(self, array0: list, array1: list):
        i = 0
        j = 0
        array0_length = len(array0)
        array1_length = len(array1)
        merged_array = []

        while True:
            if i < array0_length and (j >= array1_length or array0[i] < array1[j]):
                merged_array.append(array0[i])
                i += 1
            if j < array1_length and (i >= array0_length or array0[i] > array1[j]):
                merged_array.append(array1[j])
                j += 1
            if i == array0_length and j == array1_length:
                return merged_array
