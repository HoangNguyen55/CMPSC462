# LAST IN FIRST OUT

class stack():
    def __init__(self) -> None:
        self._internal_list = []

    def isEmpty(self):
        return not bool(len(self._internal_list))

    def push(self, item):
        self._internal_list.append(item)

    def pop(self):
        return self._internal_list.pop()

    def peek(self):
        return self._internal_list[-1]

    def size(self):
        return len(self._internal_list)


# a = stack()
# a.push('a')
# print(f"{a.peek() = }")
# print(f"{a.isEmpty() = }")
# print(f"{a.size() = }")
# print(f"{a.pop() = }")
# print(f"{a.isEmpty() = }")


class queue():
    def __init__(self) -> None:
        self._list = []

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        return self._list.pop(0)

    def isEmpty(self):
        return not bool(len(self._list))
    def size(self):
        return len(self._list)


a = queue()
a.enqueue('a')
print(f"{a.isEmpty() = }")
print(f"{a.size() = }")
print(f"{a.dequeue() = }")
print(f"{a.isEmpty() = }")


# TOWER OF HANOI, CANNOT PUT BIGGER BLOCK ON TOP OF SMALLER BLOCK
