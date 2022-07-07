from locale import currency
from logging import root
import sys

# Node Class Definition
class Node:
    # The constructor method od the Node 
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
        
class MinHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.root = 0
        self.heap = [None]*self.capacity   
        
    def getParentIndex (self , index) :
        if index is not self.root :
            return (index-1)//2
        else:
            return self.root
    
    def swap(self , index1 , index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2] 
        self.heap[index2] = temp
        return
    
    def insert(self,node) : 
        if self.size >= self.capacity :
            return "Min-Heap is Full" 
        
        self.size += 1 
        self.heap[self.size-1] = node
        
        current = self.size -1 
        
        while self.heap[current].frequency_counter < self.heap[self.getParentIndex(current)].frequency_counter : 
            self.swap(current, self.getParentIndex(current) )
            current = self.getParentIndex(current)
            

    def getLeftChild(self, index):
        return ( 2 * index) + 1 
  
    def getRightChild(self, index):
        return (2 * index) + 2
  
    def isLeaf(self, index):
        return index*2 >= self.size -1
    
    def heapifyNode(self, nodeIndex) : 
        
        if not self.isLeaf(nodeIndex) : 
            if (self.heap[nodeIndex].frequency_counter > self.heap[self.getLeftChild(nodeIndex)].frequency_counter ) or \
                (self.heap[nodeIndex].frequency_counter > self.heap[self.getRightChild(nodeIndex)].frequency_counter ):
                    if self.heap[self.getLeftChild(nodeIndex)].frequency_counter > self.heap[self.getRightChild(nodeIndex)].frequency_counter :
                        self.swap(nodeIndex , self.getRightChild(nodeIndex))
                        self.heapifyNode( self.getRightChild(nodeIndex) )
                    else  :
                        self.swap(nodeIndex , self.getLeftChild(nodeIndex))
                        self.heapifyNode( self.getLeftChild(nodeIndex) )
                        
    def heapifyObject(self)  :
        for nodeIndex in range( (self.size - 1) // 2  , 0 , -1 ) : 
            self.heapifyNode(nodeIndex)
            
    def removeNode(self) :
        if self.size == 0  :
            return "Min Heap is already Empty"
        popped = self.heap[self.root]
        self.heap[self.root] = self.heap[self.size - 1 ]
        self.size-= 1
        self.heapifyNode(self.root)
        self.heap[self.size ] = None
        return popped
    # Function to print the contents of the heap
    def Print(self):
        for i in range(0, ((self.size-1) //2)):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+ 
                                str(self.heap[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.heap[2 * i + 2]))
# O(n)                    
def BuildFrequencyTable(data):
    frequency_table= {}
    
    for char in data :
        if char in frequency_table :
            frequency_table[char].frequency_counter += 1
        else : 
            node = Node(char)
            frequency_table[char] = node
            frequency_table[char].frequency_counter += 1
            
    return frequency_table

def buildHuffmanTree(frequencyTable):
    
    rootNode = None
    minHeapQ = MinHeap(len(frequencyTable))
    # n log n
    for char in frequencyTable : 
        # log n
        minHeapQ.insert(frequencyTable[char])
    # n * 3 log n
    while minHeapQ.size >= 1 :
        if minHeapQ.size == 1 : 
            rootNode = minHeapQ.removeNode()
            break
        left_node = minHeapQ.removeNode()
        right_node = minHeapQ.removeNode()
        new_node = Node()
        left_node.parent = new_node
        right_node.parent = new_node
        new_node.left = left_node
        new_node.right = right_node
        new_node.frequency_counter = left_node.frequency_counter + right_node.frequency_counter
        # log n
        minHeapQ.insert(new_node)
    
    return rootNode

# O (n log n)
def generateCodesforHuffmanTree(root_node, frequencyTable) : 
    
    for char in frequencyTable :
        if len(frequencyTable) == 1 : 
            frequencyTable[char].code = '1'
            return
        node = frequencyTable[char]
        code = ""
        # O ( log n)
        while node is not root_node : 
            if node.parent.left == node: 
                code = '0' + code 
            else : 
                code = '1' + code 
            node = node.parent
            
        frequencyTable[char].code = code
    
def printHuffmanTree(root_node):
    
    print ("parent is " + str(root_node) +" ------left child is " + str(root_node.left) +" ------right child is " + str(root_node.right) )
    if root_node.left is not None : 
        printHuffmanTree(root_node.left)
    if root_node.right is not None : 
        printHuffmanTree(root_node.right)
    
def huffman_encoding(data):
    if data is None:
        return 
    frequency_table = BuildFrequencyTable(data)
    root_node = buildHuffmanTree(frequency_table)
    generateCodesforHuffmanTree(root_node , frequency_table)
    binary_code_string = ""
    for char in data :
        binary_code_string += frequency_table[char].code
        
    return binary_code_string , root_node
    pass

def huffman_decoding(data,tree):
    
    string = ""
    node = tree
    
    if data is None or data == "": 
        return ""
    
    if node.left is None and node.right is None :
        string = node.value * node.frequency_counter
        return string

    for char in data :
        if char == '0':
           node = node.left 
        elif char == '1':
            node = node.right 
        if node is None : 
            return
        if node.left is None and node.right is None :
            string += node.value
            node = tree
        
    return string
            
    pass

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
