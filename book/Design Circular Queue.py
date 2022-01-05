class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True
            
    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]
    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None
    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None

circularQueue = MyCircularQueue(5)
print(circularQueue.isEmpty())
print(circularQueue.enQueue(10))
print(circularQueue.enQueue(20))
print(circularQueue.enQueue(30))
print(circularQueue.enQueue(40))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.deQueue())
print(circularQueue.enQueue(50))
print(circularQueue.enQueue(60))
print(circularQueue.Rear())
print(circularQueue.Front())
print(circularQueue.isEmpty())
    