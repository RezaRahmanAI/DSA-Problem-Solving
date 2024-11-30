class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
        

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
        
    def all_item(self):
        for i in self.items:
            print(i)




stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)



# print(stack.peek())
# print(stack.pop())
# print(stack.pop())

stack.all_item()

