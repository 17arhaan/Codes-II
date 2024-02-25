class TwoStacksQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack1 else "Queue is Empty..."

    def display(self):
        print("Stack 1 ---->")
        print(self.stack1)
        print("Stack 2 ---->")
        print(self.stack2)

def main():
    queue_obj = TwoStacksQueue()
    ch = 0  
    while (ch != 4):                         
        print("\n____ MENU ____")
        print("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n")
        ch = int(input(f"Enter Choice : "))
        if ch == 1:
            element = int(input(f"Enter Element To Enqueue : "))
            queue_obj.enqueue(element)
            print(f"{element} pushed enqueued.")
        elif ch == 2:
            queue_obj.dequeue()
            print(f"{element} pushed dequeued.")
        elif ch == 3:
            queue_obj.display()
        elif ch == 4:
            print(" ~ Exiting ~")
            break
        else :
            print ("Try Again.")
            
if __name__ == "__main__":
    main()







# def enqueue(st1, st2, ele):
#     if not st1:
#         st2.append(ele)
#     else:
#         st1.append(ele)
#     return


# def dequeue(st1, st2):
#     if not st1:
#         for i in range(len(st2)):
#             st1.append(st2.pop())
#         ans = st1.pop()
#         for i in range(len(st1)):
#             st2.append(st1.pop())
#         return ans
#     else:
#         for i in range(len(st1)):
#             st2.append(st1.pop())
#         ans = st2.pop()
#         for i in range(len(st2)):
#             st1.append(st2.pop())
#         return ans


# if __name__ == '__main__':
#     a = 0
#     st1, st2 = [], []
#     while a != 3:
#         a = int(input('enter 1 to enqueue 2 to dequeue 3 to exit'))
#         if a == 1:
#             b = int(input('enter value'))
#             enqueue(st1, st2, b)
#         if a == 2:
#             print(dequeue(st1, st2))