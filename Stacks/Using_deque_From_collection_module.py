from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

# deque is faster than list i.e. O(1)
