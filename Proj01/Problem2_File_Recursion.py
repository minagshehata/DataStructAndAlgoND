import os 

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # an empty list 
    out = [] 
    # list of all components (Files/Directories) under the original path 
    list_of_components = os.listdir(path)
    
    for component in list_of_components :
        # concatenate the component name to the original path name
        full_path = os.path.join(path,component)
        # check if the component is directory 
        if os.path.isdir(full_path):
            # call find_files recursively and append the result to the final list
            out += find_files(suffix,full_path)
        # check if the component is just a file not a directory  
        # note that this case also act as a terminator to the recursion process  
        elif os.path.isfile(full_path):
            # check if it end with the targeted suffix
            if full_path.endswith(suffix) :
                # apend the targeted file to the final list 
                out.append(full_path)
    
    return out

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("\n=========== test case 1 ===========\n")
for i in (find_files(".py","../../")):
    print(i)
# Test Case 2
print("\n=========== test case 2 ===========\n")
for i in (find_files("","../../")):
    print(i)
# Test Case 3
print("\n=========== test case 3 ===========\n")
for i in (find_files(".c","./testdir")):
    print(i)
    