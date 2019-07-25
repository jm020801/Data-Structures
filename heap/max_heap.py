class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) == 0:
            return
        if len(self.storage) == 1:
            return self.storage.pop()
        old_root = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return old_root

    def get_max(self):
        return self.storage[0]  # biggest thing will always be the root

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index <= 0:
            return
        parent_index = (index - 1) // 2
        if self.storage[index] > self.storage[parent_index]:
            temp = self.storage[index]
            self.storage[index] = self.storage[parent_index]
            self.storage[parent_index] = temp
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        left_index = 2 * index + 1  # child on the left
        right_index = 2 * index + 2  # child on the right
        # need to find the larger child value,
        #  as the largest value in general has to be at the top
        comparison_index = index
        # make sure that there are children that we can compare to, first
        if len(self.storage) > left_index and self.storage[left_index] > self.storage[comparison_index]:
            comparison_index = left_index
        if len(self.storage) > right_index and self.storage[right_index] > self.storage[comparison_index]:
            comparison_index = right_index
        if index is not comparison_index:
            temp = self.storage[index]
            self.storage[index] = self.storage[comparison_index]
            self.storage[comparison_index] = temp
            self._sift_down(comparison_index)
