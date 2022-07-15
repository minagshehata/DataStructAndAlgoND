# Problem 3 : Huffman Coding 

## Reasoning for the used data structure
- min heap  : that gives prioity queue functionality with improved time complexity for the insertion and deletion 
- dictionary : used for the frequency table to give O(1) complexity for searching and insertion. 

## Time and space complixity 
### Time complexity 
- to decode the data : 
huffman_encoding() ===> 
---> buildFrequencyTable() ===> O(n) to read all the data and construct frequency table and dictionary.
---> buildHuffmanTree() ===> O(n log n) to insert all characters in min heap 
                            + O(n * 3 log n) to remove the nodes and build huffman tree
---> generateCodesforHuffmanTree() ===> O (n log n) to iterate on all characters in  the data and generate code for each character.
---> Loop on the data to prepare the full encoded data ===> O(n) to iterate on all characters and construct the full encoded data 


From the previous call hirearichy, we can say that the total complexity would be O(n + n log n + n * 3 log n + n log n + n) complexity -> O(2n + n (5 log n) ) 

- to decode the data  :
huffman_decoding()===> O(n) to iterate on the the encoded data bits and construct the decoded data
### Space complexity 
- to decode the data : 
huffman_encoding() ===> 
---> buildFrequencyTable() ===> O(n) to read all the data and construct frequency table and dictionary.
---> buildHuffmanTree() ===> O(n) + O(1) to insert all characters in min heap 
                            + O(n log n) to remove the nodes and build huffman tree
---> generateCodesforHuffmanTree() ===> O (n) to iterate on all characters in  the data and generate code for each character.



From the previous call hirearichy, we can say that the total complexity would be O(n + n + 1 + n log n + n ) complexity -> O(3n + log n) 

- to decode the data  :
huffman_decoding()===> O(n) to iterate on the the encoded data bits and construct the decoded data