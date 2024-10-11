#Actvity#2_Cachin_J

class Queue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):

        if (self.tail == self.k - 1):
            print("The queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp

    def first(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def len(self):
        if self.is_empty():
            return 0
        return self.tail - self.head + 1
    def __str__(self):
        return "Queue: [" + ", ".join(
            str(self.queue[i]) for i in range(self.head, self.tail + 1) if self.queue[i] is not None) + "]"


#Simulation 1
Q = Queue(10)
Q.enqueue(5)
Q.enqueue(3)
print("The current size of the Queue is:",Q.len())
print("Dequeued:",Q.dequeue())
print("Is the Queue Empty?:",Q.is_empty())
print("Dequeued:", Q.dequeue())
print("Is the Queue Empty?:",Q.is_empty())
print("Dequeued:",Q.dequeue())
Q.enqueue(7)
Q.enqueue(9)
print("The first element is:",Q.first())
Q.enqueue(4)
print("The current size of the Queue is:",Q.len())
print("Dequeued:",Q.dequeue())
print("The final:", Q)
print()

#Simulation 2
Q = Queue(10)
Q.enqueue(5)
Q.enqueue(3)
print("Dequeued:",Q.dequeue())
Q.enqueue(2)
Q.enqueue(8)
print("Dequeued:",Q.dequeue())
print("Dequeued:",Q.dequeue())
Q.enqueue(9)
Q.enqueue(1)
print("Dequeued:",Q.dequeue())
Q.enqueue(7)
Q.enqueue(6)
print("Dequeued:",Q.dequeue())
print("Dequeued:",Q.dequeue())
Q.enqueue(4)
print("Dequeued:",Q.dequeue())
print("Dequeued:",Q.dequeue())
print("The final:",Q)

