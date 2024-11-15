#Activity #1 Finals
from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque


D = Deque
S = Stack
Q = Queue

D = Deque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("Initial Deque")
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())

print()
Q = Queue()
print("The Queue is empty?", Q.is_empty())

#For Deque
D = Deque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
D.insert_last(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())

print()
print("Sorted Deque:")
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())

while not D.is_empty():
    print(D.delete_first())
print()

#For Stack
D = Deque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("Initial Stack")
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())
print(D.delete_first())

print()
S = Stack()
print("The Stack is empty?", Q.is_empty())
print()

print("Sorted Deque:")
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
S.push(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(S.pop())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())

while not D.is_empty():
    print(D.delete_first())
























