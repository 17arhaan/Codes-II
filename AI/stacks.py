class Stack:
    def __init__(self):
        self.stackk = []
    
    def push(self,item):
        self.stackk.append(item)
    
    def pop(self):
        return len(self.stack)
    
    def display(self):
        for i in range(len(self.stackk)):
            print(self.stackk[i])
    
def main():
    stack_object = Stack()
    ch = 0
    print("____ MENU ____")
    print("1.Push\n2.Pop\n3.Display\n4.Exit\n")
    while ch != 4:
        ch = int(input("Enter Choice: "))
        if ch == 1:
            inputt = int(input("Enter Element: "))
            stack_object.push(inputt)
            print(f"{inputt} pushed.\n")
        elif ch == 2:
            popped_item = stack_object.pop()
            if popped_item is not None:
                print(f"{popped_item} popped.\n")
        elif ch == 3:
            print("The Stack Is :-")
            stack_object.display()
        elif ch == 4:
            print(" --- Exiting ---")
        else:
            print("Try Again..")
if __name__ == "__main__":
    main()
