#Push and pop program

stack = []

def push():
    element = input("Enter the element:")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty!")
    else:
        e = stack.pop()
        print(F"{e} is removed")
        print(stack)

while True:
    print('SELECT THE OPERATION')
    print('1 push')
    print('2 pop')
    print('3 quite')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Fool...!") 

