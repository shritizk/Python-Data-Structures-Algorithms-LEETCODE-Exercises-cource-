class Node :
    def __init__(self , value): 
        self.value = value 
        self.next = None

class LinkedList:
    def __init__(self , value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None :
            self.head =new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while(temp.next):
                pre = temp 
                temp = temp.next
            self.tail = pre 
            self.tail.next = None
            self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    def popFirst(self):
        if self.length == 0  :
            return False
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1
            if self.length == 0:
                self.tail = None
            return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            current = self.head
            while(index>0):
                current = current.next
                index -=1
            return current
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp : 
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index > self.length or index < 0:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length :
            self.append(value)
        else:
            temp = self.get(index -1) # pre node 
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length +=1
            return True
        
    def remove(self,index):
        if index > self.length or index < 0 :
            return False
        if index == 0:
            self.popFirst()
        if index == self.length : 
            self.pop()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next    
            temp.next - None
            self.length -=1
            return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp 
        before = None
        after = temp.next
        for i  in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True              




            
# practice      
my_ll = LinkedList(4)

