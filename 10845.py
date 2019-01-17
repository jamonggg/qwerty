def push(n):
    queue.append(n)
def pop():
    try:
        print(queue.pop())
    except:
        print(-1)
def size():
    return len(queue)
def empty():
    a = 1 if size() == 0 else 0
    print(a)
def front():
    try:
        print(queue[0])
    except:
        print(-1)
def back():
    try:
        print(queue[-1])
    except:
        print(-1)

n = int(input())
queue = []
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
    elif command[0] == 'front':
        front()
