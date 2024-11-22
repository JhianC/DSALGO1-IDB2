from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from CircularQueue import CircularQueue as CircularQueue
from LinkedDeque import LinkedDeque as Deque
from PositionalList import PositionalList as PositionalList

#1. Infix to Postfix Notation

def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1


def PostfixConversion(s):
    S = Stack
    S = []
    result = ""

    for i in range(len(s)):
        c = s[i]


        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            result += c


        elif c == '(':
            S.append('(')



        elif c == ')':
            while S and S[-1] != '(':
                result += S.pop()
            S.pop()


        else:
            while S and (prec(c) <= prec(S[-1])):
                result += S.pop()
            S.append(c)


    while S:
        result += S.pop()

    return result


exp = input("Enter an infix expression: ")


postfix = PostfixConversion(exp)
print("Postfix notation:", postfix)
print()

#2. Positional List Activity
P = PositionalList()
P.add_first(1)
P.add_first(72)
P.add_first(81)
P.add_first(25)
P.add_first(65)
P.add_first(91)
P.add_first(11)
print("Initial List")
for x in P:
    print(x, end=' ')

print()

def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort(P)
print("The sorted list of elements are(Ascending): ")
# Print the sorted elements
for x in P:
    print(x, end=' ')

print()

def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
insertion_sort_descending(P)
print("The sorted list of elements are(Descending): ")
# Print the sorted elements
for x in P:
    print(x, end=' ')






