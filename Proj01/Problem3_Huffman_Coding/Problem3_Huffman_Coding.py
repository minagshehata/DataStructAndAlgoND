from locale import currency
from logging import root
import sys

# Node Class Definition
class Node:
    # The constructor method of the Node 
    def __init__(self,value=None):
        # the value or the character of the node 
        self.value = value
        # the occurance of this character in the data
        self.frequency_counter = 0
        # it's code from Huffman tree prospective
        self.code = ''
        # reference to the left Node in the Huffman tree
        self.left = None
        # reference to the right Node in the Huffman tree
        self.right = None
        # reference to the parent Node
        self.parent  = None
        
    # the string print method of the Node  
    def __repr__(self) -> str:
        string = str(self.value) + '\t'
        string += str(self.frequency_counter) + '\t'
        string += str(self.code) + '\n'
        return string
    
# min heap class        
class MinHeap:
    # The constructor method of the min heap class 
    def __init__(self,capacity):
        # the maximum capcity of the min heap queue
        self.capacity = capacity
        # the current size of the queue 
        self.size = 0
        # the root element of the tree
        self.root = 0
        # the list of the heap 
        self.heap = [None]*self.capacity   
    
    # Function that return the parent index     
    def getParentIndex (self , index) :
        if index is not self.root :
            return (index-1)//2
        else:
            return self.root
    
    # function that swap two elements given their indices
    def swap(self , index1 , index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2] 
        self.heap[index2] = temp
        return
    # insert new node in the min heap
    def insert(self,node) : 
        # handle if the min heap is full
        if self.size >= self.capacity :
            return "Min-Heap is Full" 
        
        #increment the size of the heap
        self.size += 1 
        self.heap[self.size-1] = node
        
        current = self.size -1 
        
        # re order the min heap after inserting the new node based on its frequency 
        # check the new node if it isrepeated in the input less than the parent node
        while self.heap[current].frequency_counter < self.heap[self.getParentIndex(current)].frequency_counter : 
            # swap the node with its parent 
            self.swap(current, self.getParentIndex(current) )
            # after swapping we need to validate the same check with the parent also.
            current = self.getParentIndex(current)
            
    # Function to return the left child index
    def getLeftChild(self, index):
        return ( 2 * index) + 1 
    
    # Function to return the right child index
    def getRightChild(self, index):
        return (2 * index) + 2

    # Function to check if the node with this index is leaf or not
    def isLeaf(self, index):
        return index*2 >= self.size -1
    
    # Function re-order the heap for specific node 
    def heapifyNode(self, nodeIndex) : 
        # ensure that the given node is not leaf
        if not self.isLeaf(nodeIndex) : 
            # ensure that node is in wrong position 
            if (self.heap[nodeIndex].frequency_counter > self.heap[self.getLeftChild(nodeIndex)].frequency_counter ) or \
                (self.heap[nodeIndex].frequency_counter > self.heap[self.getRightChild(nodeIndex)].frequency_counter ):
                    # if the left node is repeated more than the right one swap the right and the original node
                    if self.heap[self.getLeftChild(nodeIndex)].frequency_counter > self.heap[self.getRightChild(nodeIndex)].frequency_counter :
                        self.swap(nodeIndex , self.getRightChild(nodeIndex))
                        # recursively re-order the next level
                        self.heapifyNode( self.getRightChild(nodeIndex) )
                    # if the left node is repeated less than the right one swap the left and the original node
                    else  :
                        self.swap(nodeIndex , self.getLeftChild(nodeIndex))
                        # recursively re-order the next level
                        self.heapifyNode( self.getLeftChild(nodeIndex) )
                        

    # Function to re-order the full min heap                  
    def heapifyObject(self)  :
        for nodeIndex in range( (self.size - 1) // 2  , 0 , -1 ) : 
            self.heapifyNode(nodeIndex)
            
    # Function to remove the root node as it's the lowest frequent node    
    def removeNode(self) :
        # Handle the empty heap
        if self.size == 0  :
            return "Min Heap is already Empty"
        # return the root node 
        popped = self.heap[self.root]
        # make the root node with the largest node
        self.heap[self.root] = self.heap[self.size - 1 ]
        # decrement the heap size
        self.size-= 1
        # reorder the full heap
        self.heapifyNode(self.root)
        # clear the out of range element 
        self.heap[self.size ] = None
        # return
        return popped
    
    # Function to print the contents of the heap
    def Print(self):
        for i in range(0, ((self.size-1) //2)):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+ 
                                str(self.heap[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.heap[2 * i + 2]))
# O(n)                    
# Function to build frequency table of string input
def buildFrequencyTable(data):
    frequency_table= {}
    
    for char in data :
        # if the char already exist in the table 
        if char in frequency_table :
            # increment the frequency counter of the repeated character
            frequency_table[char].frequency_counter += 1
        else : 
            # create new node of the char
            node = Node(char)
            frequency_table[char] = node
            # increment the frequency counter of the character
            frequency_table[char].frequency_counter += 1
            
    return frequency_table

# Function to build huffman tree for specific frequency table
def buildHuffmanTree(frequencyTable):
    
    rootNode = None
    # create new min heap with the capacity of the frequency table
    minHeapQ = MinHeap(len(frequencyTable))
    
    # O(n log n)
    #  add all characters to the min heap 
    for char in frequencyTable : 
        # O(log n)
        minHeapQ.insert(frequencyTable[char])
        
    # O(n * 3 log n)
    # Build the huffman tree
    while minHeapQ.size >= 1 :
        # make the last node as the root of the tree
        if minHeapQ.size == 1 : 
            rootNode = minHeapQ.removeNode()
            break
        # pick the two least repeated nodes as the left and the right nodes
        left_node = minHeapQ.removeNode()
        right_node = minHeapQ.removeNode()
        # create new node as parent for the two nodes
        new_node = Node()
        # make up linkd
        left_node.parent = new_node
        right_node.parent = new_node
        # make down links
        new_node.left = left_node
        new_node.right = right_node
        # the frequency counter for the new node shall be the sum of the two nodes frequency 
        new_node.frequency_counter = left_node.frequency_counter + right_node.frequency_counter
        # O(log n)
        # insert the new node to the min heap
        minHeapQ.insert(new_node)
    
    return rootNode

# O (n log n)
# Function to generate code for each node in the tree
def generateCodesforHuffmanTree(root_node, frequencyTable) : 
    # loop on all characters and fill it's code 
    for char in frequencyTable :
        # Handle the data with one character legnth 
        if len(frequencyTable) == 1 : 
            frequencyTable[char].code = '1'
            return
        
        node = frequencyTable[char]
        code = ""
        # O ( log n)
        # follow the path from the node to the root
        while node is not root_node : 
            # add 0 if the link is left 
            if node.parent.left == node: 
                code = '0' + code 
            # add 1 if the link is right
            else : 
                code = '1' + code 
            node = node.parent
            
        # assign the resultant code to the the node 
        frequencyTable[char].code = code
    
# Function to print the Huffman tree if needed
def printHuffmanTree(root_node):
    
    print ("parent is " + str(root_node) +" ------left child is " + str(root_node.left) +" ------right child is " + str(root_node.right) )
    if root_node.left is not None : 
        printHuffmanTree(root_node.left)
    if root_node.right is not None : 
        printHuffmanTree(root_node.right)

# the main Function to encode the data
def huffman_encoding(data):
    # Handle None data
    if data is None:
        return 
    # Build frequency table for the data
    frequency_table = buildFrequencyTable(data)
    # Build Huffman tree for the data
    root_node = buildHuffmanTree(frequency_table)
    # generate the code for all characters in the tree
    generateCodesforHuffmanTree(root_node , frequency_table)
    # prepare the last encoded data
    binary_code_string = ""
    for char in data :
        binary_code_string += frequency_table[char].code
        
    return binary_code_string , root_node
    
# Function to decode the encoded data
def huffman_decoding(data,tree):
    
    string = ""
    # start with the root of the tree
    node = tree
    # handle the empty data
    if data is None or data == "": 
        return ""
    
    # Handle one character legnth data 
    if node.left is None and node.right is None :
        string = node.value * node.frequency_counter
        return string

    # form the encoded data
    for char in data :
        if char == '0':
           node = node.left 
        elif char == '1':
            node = node.right 
            
        # loop terminator 
        if node is None : 
            return
        # handle leaf nodes 
        if node.left is None and node.right is None :
            # append the output string
            string += node.value
            # make the node to the root again 
            node = tree
        
    return string


# ****************** Testing *************** 
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print (" ============== Test Case 1 ==============")
a_great_sentence = "AAAAABBBBBSSSSSDDDDDEEEEEDDDASSSSDDDFFFKKMGGMGMBKKTGaskdfnkjsdfnksjdnfkjsdfns==-r=--405io3ngdfgnkhsdbdfhbdsknf"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))

# Test Case 2
print (" ============== Test Case 2 ==============")
a_great_sentence = "T"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))

# Test Case 3
print (" ============== Test Case 3 ==============")
a_great_sentence = ""

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))



# Test Case 4
print (" ============== Test Case 4 ==============")
a_great_sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))
