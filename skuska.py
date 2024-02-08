import sys

class Stack:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return len(self.values) == 0

    def push(self,value):
        self.values.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.values.pop()

    def peek(self):
        return self.values[-1]

def precedence(op):
    if op in ['*', '/']:
        return 2
    elif op in ['+', '-']:
        return 1
    else:
        return 0

op_stack = Stack()
x = input("zadaj priklad: ")

output_list = []
buffer = []

for i in x:
    if i.isalnum():  # if the character is a number or a letter
        buffer.append(i)
    else:
        if buffer:  # if the buffer is not empty
            output_list.append(''.join(buffer))
            buffer = []
        if i == '(':
            op_stack.push(i)
        elif i == ')':
            while op_stack.peek() != '(':
                output_list.append(op_stack.pop())
            op_stack.pop()
        elif i in '+-*/':
            while not op_stack.isEmpty() and op_stack.peek() != '(' and precedence(i) <= precedence(op_stack.peek()):
                output_list.append(op_stack.pop())
            op_stack.push(i)


if buffer:
    output_list.append(''.join(buffer))

while not op_stack.isEmpty():
    output_list.append(op_stack.pop())

print(' '.join(output_list))

