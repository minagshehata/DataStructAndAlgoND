from distutils.log import ERROR
import hashlib
from datetime import datetime
from logging import error
from tracemalloc import stop

#BlockData Class
class BlockData:
    # The constructor method of BlockData
    def __init__(self,sender,receiver,amount):
        if sender is not None and receiver is not None and amount > 0 :
            self.sender = str(sender) 
            self.receiver = str(receiver)
            self.amount = str(amount)
        else : 
            error ("Invalid input")
            raise SystemExit
    # Function to represent the block data in string format      
    def __repr__(self) -> str:
        return (self.sender + '\t'+  self.receiver +'\t'+ self.amount + '\n')

# Block Class        
class Block:
    # The constructor method of Block class
    def __init__(self, data ):
        if type(data) == BlockData : 
            # the timestamp of the block creation
            self.timestamp = str(self.calc_timestamp())
            self.data = data
            self.previous_hash = None
            # the hash of the block data 
            self.hash = self.calc_hash()
            self.next = None 
        else : 
            return -1 
        
    # Function to calculate hash of the block
    def calc_hash(self):
        sha = hashlib.sha256()
        # prepare the data that is included in the hash (time stamp and the BlockData)
        data_string = self.data.sender + '#'+ self.data.receiver + '#' + self.data.amount + '#' + str(self.timestamp) 
        hash_str = data_string.encode('utf-8')
        # update the hash
        sha.update(hash_str)
        return sha.hexdigest()
    
    # Function that return the timestamp of creation the block in GMT/UTC timing
    def calc_timestamp(self):
        return datetime.utcnow()
    
    # Function to represent the block in string format   
    def __repr__(self) -> str:
        string = "data is : \t" + str(self.data) +" the timestamp is \t" + str(self.timestamp) 
        string += "\n the hash is \t" + str(self.hash) + "\n the previous hash is \t" + str(self.previous_hash)
        return string

# Block Chain Class
class BlockChain: 
    # The constructor method of Block class
    def __init__(self):
        self.num_of_entries = 0
        self.genesis = None 
        self.tail = None
    
    #Function to add block to the chain
    def add_block(self,blockData):
        # create new Block
        block = Block(blockData)
        # Handle if the chain is empty
        if self.genesis is None : 
            # make the block as the genesis block  
            self.genesis = block
            # the tail is the same as the genesis
            self.tail = self.genesis
            #increment the number of blocks in the chain
            self.num_of_entries += 1
            return
        # update the hash of the previous block
        block.previous_hash = self.tail.hash
        # make the link from the tail to the current block
        self.tail.next = block
        #increment the number of blocks in the chain
        self.num_of_entries += 1
        # make the block as the tail
        self.tail = block 
        
    #Function to add block to the chain   
    def add_block(self,sender,receiver,amount):
        # create new Block
        block = Block(BlockData(sender,receiver,amount))
        # Handle if the chain is empty
        if self.genesis is None : 
            # make the block as the genesis block  
            self.genesis = block
            # the tail is the same as the genesis
            self.tail = self.genesis
            #increment the number of blocks in the chain
            self.num_of_entries += 1
            return
        
        # update the hash of the previous block
        block.previous_hash = self.tail.hash
        # make the link from the tail to the current block
        self.tail.next = block
        #increment the number of blocks in the chain
        self.num_of_entries += 1
        # make the block as the tail
        self.tail = block
        
    # Function to represent the chain in string format      
    def __repr__(self) -> str:
        string = "" 
        block = self.genesis
        
        while block is not None : 
            string += '\n=====================\n'
            string += str(block)
            block = block.next
        return string
        
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
block_chain = BlockChain()
sender = "mina"
receiver = "gamal"
amount = 10 

block_chain.add_block(sender,receiver,amount)

# Test Case 2
sender = "miray"
receiver = "gamal"
amount = 100 

block_chain.add_block(sender,receiver,amount)

# Test Case 3 for large data
sender = 'A'
receiver = 'a'
amount = 1

for i in range (100000) :  
    block_chain.add_block(sender,receiver,amount)
    amount += 1 
    
    
print(block_chain)
# expected to print 100002 number of entries with different timestamps and hashs

# Test Case 4 for empty data
sender = ""
receiver = ""
amount = 0 

block_chain.add_block(sender,receiver,amount)

print(block_chain)
# expected to raise an error