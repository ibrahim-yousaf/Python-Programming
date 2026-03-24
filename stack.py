#Queue : First Come First Serve
#Stack : First Come Last Serve

stack = []

while True :
    q = input("Enter 1 to push \n Enter 2 to pop \n Enter 0 to exit")
    if q == '0' :
        break
    elif q == '1':
        name = input("Enter item to push:")
        stack.append(name)
    elif q == '2':
        if len( stack ) <= 0:
            print("Stack is empty , you cannot pop any item")
        else:
            x = stack.pop()
            print(f"Pop item is {x}")
    else:
        print("Invalid Option")
    print(stack)

print(stack)

queue = []

while True:
    q = input("Enter 1 to push \n Enter 2 to pop \n Enter 0 to exit")
    if q == '0':
        break
    elif q == '1':
        name = input("Please enter any item to push:")
        queue.append(name)
    elif q == '2':
        if len( queue ) <= 0:
            print("queue is empty you cannot pop any item")
        else:
            x = queue.pop(0)
            print(f"Pop item is {x}")
    else:
        print("Invalid Input")
    print(queue)
