# Problem 2 : File recursion

## Reasoning for the used data structure
- List : that gives a high level of grouping and appending.
- Recursion concept as it provides simple functionality would be repeated again on another level.  

## Time and space complixity 
### Time complexity 
For the worst case that all the element in the given path are directories so the recursive function would be called n times. 
could be concluded as find_files function has O(n) time complexity 

### Space complexity 
for the memory, it differs a little, we can consider the worst case for the memory is the case that all directories are leveled. 
in other words that if we have n elements in the given path we also have n level of recursion, so the stack will expand n times * constant facto ----> O(kn) ----> O(n)