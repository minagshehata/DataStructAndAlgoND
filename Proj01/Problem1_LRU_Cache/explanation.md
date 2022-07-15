# Problem 1 : Least Recent Used Cache (LRU Cache)

## Reasoning for the used data structure
- Dictionary : to give the fastest searching and insertion complexity O(1)
- Queue : To handle the order of using as the most recent used element shall be in the tail of the queue.
- Doubly Linked List : that gives more flexibility to dequeue, enqueue and remove elements

## Time and space complixity 
- as required all operations have O(1) effeciency in terms of time and space, Thanks to dictionary that refrencing to the node in the list.