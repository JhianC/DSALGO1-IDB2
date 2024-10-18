#Simulation for #1.
from ArrayStack import ArrayStacks as Stack

def is_matched(expression):
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[char]:
                return "the symbols are not balanced"
            stack.pop()

    return "the symbols are balanced" if len(stack) == 0 else "the symbols are not balanced"

print(is_matched("{(Lopit)"))
print(is_matched("{{[Noice]}}"))
print(is_matched(")Imas(( )){([( )])}"))
print(is_matched("({[]})"))
print(is_matched("("))
print(is_matched("(5x+2(3yx))"))
print()

def is_matchedUser(expression):
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[char]:
                return "the symbols are not balanced"
            stack.pop()

    return "the symbols are balanced" if len(stack) == 0 else "the symbols are not balanced"


user_input = input("Enter an expression to check for balanced symbols: ")
result = is_matched(user_input)
print(result)

#Simulation 2.
def reverse_file(myfile):
        stack = []

        with open(myfile, 'r') as file:
            for line in file:
                stack.append(line.rstrip('\n'))

        with open(myfile, 'w') as file:
            while stack:
                file.write(stack.pop() + '\n')

myfile = 'myfile.txt'
reverse_file('myfile.txt')
print("File Contents Reversed!")