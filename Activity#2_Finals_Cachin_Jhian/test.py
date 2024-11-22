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
    S = Stack()
    result = ""

    for i in range(len(s)):
        c = s[i]


        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            result += c


        elif c == '(':
            s.append('(')



        elif c == ')':
            while s and s[-1] != '(':
                result += s.pop()
            s.pop()


        else:
            while s and (prec(c) <= prec(s[-1])):
                result += s.pop()
            s.append(c)


    while s:
        result += s.pop()

    return result


exp = input("Enter an infix expression: ")


postfix = PostfixConversion(exp)
print("Postfix notation:", postfix)
print()