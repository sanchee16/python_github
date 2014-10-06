#code for stack in object oriented python 
class Stack:
    def __init__(self):
        self.items=[];
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item);
    def pop(self):
        if not self.isEmpty():
            return self.items.pop();
        else:
            return None
    def peek(self):
        return self.items[len(self.items)-1];
    def size(self):
        return len(self.items);
    def display(self):
        for each in self.items:
            print each       
