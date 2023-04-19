class Heap:
    heap = list()

    def __init__(self, *args):
        elems = list(args)
        for element in elems:
            self.add_elem(element)

    def add_elem(self, elem):
        self.heap.append(elem)
        pos = len(self.heap)
        # новый элемент больше предка => поднимаем элемент по дереву
        while (pos > 1) and (self.heap[pos-1] > self.heap[(pos // 2) - 1]):
            self.heap[pos-1], self.heap[(pos // 2) -
                                        1] = self.heap[(pos // 2) - 1], self.heap[pos - 1]
            pos = pos // 2

    def get_sorted(self):
        sorted_list = list()
        while len(self.heap) > 0:
            sorted_list.append(self.heap[0])
            self.del_first()
        return sorted_list

    def del_first(self):
        pos = 1
        while (pos * 2 < len(self.heap)):
            # 2 потомка и правый больше => поднимаем правый.
            if (len(self.heap) > pos * 2 - 1) and (self.heap[pos * 2 - 1] < self.heap[pos * 2]):
                self.heap[pos - 1] = self.heap[pos * 2]
                pos = pos * 2 + 1
            else:
                # тогда поднимаем левый
                self.heap[pos - 1] = self.heap[pos * 2 - 1]
                pos = pos * 2
        self.heap.pop(pos-1)

    def show_heap(self):
        return self.heap


new_heap = Heap(1, 3, 7, 2, -5, 1, 45, 12, 10.5, 19,
                107, 0, 9, -20, 18, 25, 1.5, -1, 6, 99)
print(new_heap.get_sorted())
