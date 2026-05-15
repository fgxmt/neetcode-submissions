class DynamicArray:
    capacity = 0
    numElements = 0
    array = {}

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.numElements >= self.capacity:
            self.resize()
        self.array[self.numElements] = n
        self.numElements += 1

    def popback(self) -> int:
        self.numElements -= 1
        return self.array[self.numElements]

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.numElements
    
    def getCapacity(self) -> int:
        return self.capacity