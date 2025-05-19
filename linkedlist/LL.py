class Node :
    def __init__(self , value): 
        self.value = value 
        self.next = None

class LinkedList:
    def __int__(self , value):
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
    


# practice
my_ll = LinkedList(4)

