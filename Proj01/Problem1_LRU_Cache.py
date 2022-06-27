class Node:
    def __init__(self,key,value):
        # key for the value
        self.key = key
        # the value 
        self.value = value 
        # link to the next node
        self.next = None
        # link to the previous node
        self.previous = None
        
class QueueWithDoublyLinkedlist:
    def __init__(self,capacity=5): 
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    # method to add new element to the tail of the Queue
    def enqueue(self,node): 
        # check if the Queue is empty
        if self.head is None:
            # the new node would be the head and the tail
            self.head = node
            self.tail = self.head
        else:
            # make link from the new node to the tail 
            node.previous = self.tail
            # make link from the tail to the new node
            self.tail.next = node
            # mark the new node as the tail 
            self.tail = self.tail.next
        # incremetn the number of elements in the Queue
        self.num_elements+=1
    
    # method to pop element from the head of the Queue
    def dequeue(self):
        # if the Queue is empty terminate with None
        if self.is_empty():
            return None
        # get the head Node as the node to be returned
        node = self.head 
        # remove any links to the head 
        self.head.next.previous = None    
        # make the next node as the head one in the Queue
        self.head = self.head.next       
        #decrement the size of the Queue
        self.num_elements -= 1
        # return the node 
        return node
    
    def remove(self, node) : 
        # Terminate for the invalid cases  
        if node is None or self.is_empty == True : 
            return -1
        
        # handle if the node is the head of the Queue 
        if node == self.head:
            self.head = self.head.next
        
        # handle if the node is the tail of the Queue
        if node == self.tail: 
            self.tail = self.tail.previous
        
        # make the next node linked to the previous node
        if node.next is not None : 
           node.next.previous = node.previous 
        
        # make the previous node linked to the next node
        if node.previous is not None :
            node.previous.next = node.next 
        
        # decrement the number of the elements 
        self.num_elements -= 1
        
        return
    
    # method the return the maximum capacity of the Queue
    def capacity(self):
        return self.capacity
    
    # method to return the current size of the Queue
    def size(self) :
        return self.num_elements
    
    # method to check if the Queue empty 
    def is_empty(self):
        return self.num_elements == 0

class LRU_Cache(object):
    
    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity = capacity
        self.table= {}
        self.DbleLinkedList = QueueWithDoublyLinkedlist(capacity)
        
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.table:
            # get the original node of the key
            old_node = self.table[key]
            # get the value of the key that should be returned 
            value = old_node.value
            # construct the new node to have the same key and value
            new_node = Node(key,value)
            # remove the old node from The Queue
            self.DbleLinkedList.remove(old_node)
            # add the new node to be on the tail of the Queue
            self.DbleLinkedList.enqueue(new_node)
            # return the value of the key
            return value
        else :
            # if the key is not found return -1
            return -1
        

    def set(self, key, value):
        # if key is None, terminate
        if key is None :
            return -1
        # construct Node with key and value parameter. 
        node = Node(key,value)
        # check if queue is not full : 
        if not self.DbleLinkedList.size() == self.capacity : 
            # check if key is not in dictionary :
            if not key in self.table :
            # append the dictionary with key , Node
                self.table[key] = node 
            # enqueue node to the tail of the queue
                self.DbleLinkedList.enqueue(node)

            else : 
                # remove old node of this key
                old_node = self.table[key]
                # remove the old node from the Queue
                self.DbleLinkedList.remove(old_node)
                # update the dictionary with the new node reference 
                self.table[key] = node
                # add the new node on the tail of the queue 
                self.DbleLinkedList.enqueue(node)
        else : 
            # dequeue the Queue and remove the least recent key 
            old_node = self.DbleLinkedList.dequeue()
            # remove the poped element from the dictionary 
            self.table.pop(old_node.key)
            # check if key is not in dictionary :
            if not key in self.table :
                #append the dictionary with key , Node
                self.table[key] = node
                # enqueue node to the top of the queue
                self.DbleLinkedList.enqueue(node)
            else : 
                # remove old node of this key
                old_node = self.table[key]
                # remove the old node from the Queue
                self.DbleLinkedList.remove(old_node)
                # update the dictionary with the new node reference 
                self.table[key] = node
                # add the new node on the tail of the queue 
                self.DbleLinkedList.enqueue(node)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache)
print (our_cache.get(1))       # returns 1
print (our_cache.get(2))       # returns 2
print (our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print (our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache_1 = LRU_Cache(10)
our_cache_1.set(0,1)
# testing negative value for key
our_cache_1.set(-1,2)
our_cache_1.set(3,3)
our_cache_1.set(4,4)
our_cache_1.set(5,5)
# testing None as a akey
our_cache_1.set(None,6)
our_cache_1.set(7,7)
our_cache_1.set(8,8)
# testing large number as a akey
our_cache_1.set(999999999999999999999999999999999999999.99999999999999999,9)
our_cache_1.set(10,10)
our_cache_1.set(10,11)
our_cache_1.set(12,12)


print("***\ntest cases \n")
print ( our_cache_1.DbleLinkedList.size())
print (our_cache_1.get(0))  
print (our_cache_1.get(-1))   
print (our_cache_1.get(3))
print (our_cache_1.get(4))
print (our_cache_1.get(5))
print (our_cache_1.get(None) ) 
print (our_cache_1.get(7))
print (our_cache_1.get(8))
print (our_cache_1.get(999999999999999999999999999999999999999.99999999999999999))
print (our_cache_1.get(999999999999999999999999999999999999999))
print (our_cache_1.get(10))
our_cache_1.set(12,13)
our_cache_1.set(12,14)
our_cache_1.set(13,15)
our_cache_1.set(4,16)
our_cache_1.set(14,17)
# the next two key should be removed from  the Queue
print (our_cache_1.get(0))   
print (our_cache_1.get(-1))   
# test the tenth element in the queue still Ok 
print (our_cache_1.get(3))   
