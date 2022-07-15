# Problem 4 : Active Directory

## Reasoning for the used data structure
searching for the user in the groups using the recursion concept. 
the recursion is most simple and elegent solution i can see. 

## Time and space complixity 
### Time complexity 
Assuming that full legnth is n for all inputs
n  = k (number of all users for all groups) + g (number of all groups)

considering the worst case that the user isn't found , the time complexity will be :
O(k) to iterate on all users + O(g) to iterate all groups 
==> O(k+g) ===> O(n)

### Space complexity 
Assuming that full legnth is n for all inputs
n  = k (number of all users for all groups) + g (number of all groups)

considering the worst case that the user isn't found , the time complexity will be :

O(1) to iterate on all users + O(g) to iterate recursivelly all groups
===> O(g)