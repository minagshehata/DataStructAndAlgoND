# Problem 6 : Union and Intersection

## Reasoning for the used data structure

set : set is the best form of data we need as it's save the data unordered and keep the uniqueness of its element.
also search and add an element to the list is very fast as the set contain a hash table inside ~ O(1)
## Time and space complixity 
### Time complexity 
Union : 
is O(2n) ~ O(n) , as to_set function is iterating on the input to fill the set, the iterating on the set to construct the output linked list.\

Intersection : 
is O(2n) ~ O(n) , similarly,to_set function is iterating on the input to fill the set,
also searching in set is O(1) so we can exclude it from the analysis. and we keep iterating on one list as least. 
### Space complexity 
for both operations, the space complexity is O(n) as the memory consumed is expanding with long input.