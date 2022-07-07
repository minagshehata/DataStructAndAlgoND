class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_set(self,set_):
        node = self.head
        while node is not None :
            set_.add(node.value)
            node = node.next
        return 

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None and llist_2.head is None : 
        return  
    elif llist_1.head is None :
        return llist_2
    elif llist_2.head is None :
        return llist_1
    else :  
        values_set = set()
        llist_1.to_set(values_set)
        llist_2.to_set(values_set)

        output_list = LinkedList()
        for element in values_set : 
            output_list.append(element)
        return output_list
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1.head is None or llist_2.head is None : 
        return  
    
    values_set_1 = set()
    values_set_2 = set()
    
    llist_1.to_set(values_set_1)
    llist_2.to_set(values_set_2) 
        
    output_list = LinkedList()
    for element in values_set_1 : 
        if element in values_set_2 : 
            output_list.append(element)
    return output_list
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [0,0,0,0,0,0,0,00,0,0,0,0,0,0]
element_2 = [1,2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
# Test Case 2

# Test Case 3
