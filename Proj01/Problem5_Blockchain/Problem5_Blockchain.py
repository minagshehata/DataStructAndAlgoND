from distutils.log import ERROR
import hashlib
from datetime import datetime

class BlockData:
    def __init__(self,sender,receiver,amount):
        if sender is not None and receiver is not None and amount > 0 :
            self.sender = str(sender) 
            self.receiver = str(receiver)
            self.amount = str(amount)
        else : 
            return -1
            
    def __repr__(self) -> str:
        return (self.sender + '\t'+  self.receiver +'\t'+ self.amount + '\n')
        
class Block:
    def __init__(self, data ):
        if type(data) == BlockData : 
            self.timestamp = str(self.calc_timestamp())
            self.data = data
            self.previous_hash = None
            self.hash = self.calc_hash()
            self.next = None 
        else : 
            return -1 
      
    def calc_hash(self):
        sha = hashlib.sha256()

        data_string = self.data.sender + '#'+ self.data.receiver + '#' + self.data.amount + '#' + str(self.timestamp) 
        hash_str = data_string.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()
    
    def calc_timestamp(self):
        return datetime.utcnow()
    
    def __repr__(self) -> str:
        string = "data is : \t" + str(self.data) +" the timestamp is \t" + str(self.timestamp) 
        string += "\n the hash is \t" + str(self.hash) + "\n the previous hash is \t" + str(self.previous_hash)
        return string


class BlockChain: 
    def __init__(self):
        self.num_of_entries = 0
        self.genesis = None 
        self.tail = None
        
    def add_block(self,blockData):
        block = Block(blockData)
        
        if self.genesis is None : 
            self.genesis = block
            self.tail = self.genesis
            self.num_of_entries += 1
            return
        
        block.previous_hash = self.tail.hash
        self.tail.next = block
        self.num_of_entries += 1
        
    def add_block(self,sender,receiver,amount):
        block = Block(BlockData(sender,receiver,amount))
        
        if self.genesis is None : 
            self.genesis = block
            self.tail = self.genesis
            self.num_of_entries += 1
            return
        
        block.previous_hash = self.tail.hash
        self.tail.next = block
        self.num_of_entries += 1
        self.tail = block
        
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

sender = "miray"
receiver = "gamal"
amount = 100 

block_chain.add_block(sender,receiver,amount)

sender = 'A'
receiver = 'a'
amount = 1
test_dict = {}
for i in range (100000) :  
    block_chain.add_block(sender,receiver,amount)
    
    if block_chain.tail.hash  in test_dict :
        print ("fail") 
        break 
    test_dict[block_chain.tail.hash] =  i 
    
    
    #sender += 'A'
    #receiver += 'a'
    #amount += 1 
    
    
print(block_chain)
# Test Case 2

# Test Case 3