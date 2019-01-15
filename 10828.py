def push(n):
    stack.append(n)
def pop():
    try:
        print(stack.pop())
    except:
        print(-1)
def size():
    return len(stack)
def empty():
    a = 1 if size() == 0 else 0
    print(a)
def top():
    try:
        print(stack[-1])
    except:
        print(-1)

n = int(input())
stack = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'top':
        top()
