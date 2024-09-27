from sys import maxsize
#Simulation 1
print("For Simulation 1:")
def Stack():
    S=[]
    return S
def isEmpty(S):
    return len(S)==0
def push (S, element):
    S.append(element)
    print(element +" pushed to the stack")
def pop(S):
    if(isEmpty(S)):
        return str(-maxsize-1)
    return S.pop()
def peek(S):
    if(isEmpty(S)):
        return str(-maxsize-1)
    return S[len(S)-1]
def empty(S):
    if len(S)<0:
        return S[len(S)]

S=Stack()
push(S, str(5))
push(S, str(3))
print("The current stack: ", S)
print("Length of the stack: ", len(S))
print(pop(S)+" popped from stack")
print("The current stack: ", S)
print("Is the stack empty: ", isEmpty(S))
print(pop(S)+" popped from stack")
print("The current stack: ", S)
print("Is the stack empty: ", isEmpty(S))
print(empty(S))
push(S, str(7))
push(S, str(9))
print("The current stack: ", S)
print("Value at the top is: ", peek(S))
push(S, str(4))
print("The current stack: ", S)
print("Length of the stack: ", len(S))
print(pop(S)+" popped from stack")
push(S, str(6))
push(S, str(8))
print("The current stack: ", S)
print(pop(S)+" popped from stack")
print("The Values Returned Are: ")
print(S)
print()

#Simulation 2
print("For Simulation 2: ")
def StackA():
    P=[]
    return P
def isEmpty(P):
    return len(P)==0
def push (P, element):
    P.append(element)
    print(element +" pushed to the stack")
def pop(P):
    if(isEmpty(P)):
        return str(-maxsize-1)
    return P.pop()
def peek(P):
    if(isEmpty(P)):
        return str(-maxsize-1)
    return P[len(P)-1]
def empty(P):
    if len(P)<0:
        return P[len(P)]

P=StackA()
push(P, str(5))
push(P, str(3))
print("The current stack: ", P)
print(pop(P)+" popped from stack")
push(P, str(2))
push(P, str(8))
print("The current stack: ", P)
print(pop(P)+" popped from stack")
print(pop(P)+" popped from stack")
print("The current stack: ", P)
push(P, str(9))
push(P, str(1))
print("The current stack: ", P)
print(pop(P)+" popped from stack")
print("The current stack: ", P)
push(P, str(7))
push(P, str(6))
print("The current stack: ", P)
print(pop(P)+" popped from stack")
print(pop(P)+" popped from stack")
print("The current stack: ", P)
push(P, str(4))
print("The current stack: ", P)
print(pop(P)+" popped from stack")
print(pop(P)+" popped from stack")
print("The Values Returned Are: ")
print(P)
print()