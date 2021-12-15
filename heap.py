def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]


class Heap:
    def __init__(self):
        self.data = []
        self.last = -1

    def insert(self, object):
        self.data.append(object)
        self.last += 1

        i = self.last
        while i > 0:
            if self.data[(i - 1) // 2] > self.data[i]:
                swap(self.data, (i - 1) // 2, i)
                i = (i - 1) // 2
            else:
                return

    def deletemin(self):
        object = self.data[0]
        self.data[0] = self.data[self.last]
        self.data.pop(self.last)
        self.last -= 1

        i = 0
        while (i * 2) + 1 <= self.last:
            is_right_child_out_of_range = (i * 2) + 2 <= self.last
            if self.data[i] > self.data[(i * 2) + 1]:
                if (
                    is_right_child_out_of_range
                    and self.data[(i * 2) + 2] < self.data[(i * 2) + 1]
                ):
                    swap(self.data, i, (i * 2) + 2)
                    i = (i * 2) + 2
                else:
                    swap(self.data, i, (i * 2) + 1)
                    i = (i * 2) + 1
            elif is_right_child_out_of_range and self.data[i] > self.data[(i * 2) + 2]:
                swap(self.data, i, (i * 2) + 1)
                i = (i * 2) + 2
            else:
                break

        return object
