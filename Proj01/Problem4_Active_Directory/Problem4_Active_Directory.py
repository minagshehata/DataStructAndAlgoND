# Group Class
class Group(object):
    # The constructor method of Group 
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    # Function to add group 
    def add_group(self, group):
        self.groups.append(group)

    # Function to add user
    def add_user(self, user):
        self.users.append(user)

    # Function to get the group of this group object
    def get_groups(self):
        return self.groups

    # Function to get the user of this group object
    def get_users(self):
        return self.users

    # Function to get the name of this group object
    def get_name(self):
        return self.name

# Create Group with name parent 
parent = Group("parent")
# Create Group with name child 
child = Group("child")
# Create Group with name subchild 
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
# add user with name "sub_child_user"
sub_child.add_user(sub_child_user)
# add group "sub_child" to group "child"
child.add_group(sub_child)
# add group "child" to group "parent"
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # terminator condition if user is found 
    if user in group.get_users():
        return True
    
    # iterate on the sub groups
    for grp in group.get_groups() : 
        # recursive call till find the user or finish the list of groups
        if is_user_in_group(user,grp) : 
            return True
        
    # by default return False 
    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# prepare the test
group_1 = Group("group 1 ")
group_2 = Group("group 2 ")
group_3 = Group("group 3 ")
group_4 = Group("group 4 ")
group_5 = Group("group 5 ")

user_1 = "user 1 "
user_2 = "user 2 "
user_3 = "user 3 "
user_4 = "user 4 "
user_5 = "user 5 "

user_6 = "user 6 "
user_7 = "user 7 "
user_8 = "user 8 "
user_9 = "user 9 "
user_10 = "user 10 "

user_11 = "user 11 "
user_12 = "user 12 "
user_13 = "user 13 "
user_14 = "user 14 "
user_15 = "user 15 "

user_16 = "user 16 "

group_1.add_user(user_1)
group_1.add_user(user_2)
group_1.add_user(user_3)

group_2.add_user(user_4)
group_2.add_user(user_5)
group_2.add_user(user_6)

group_3.add_user(user_7)
group_3.add_user(user_8)
group_3.add_user(user_9)

group_4.add_user(user_10)
group_4.add_user(user_11)
group_4.add_user(user_12)

group_5.add_user(user_13)
group_5.add_user(user_14)
group_5.add_user(user_15)

group_1.add_group(group_2)
group_2.add_group(group_3)
group_2.add_group(group_4)
group_4.add_group(group_5)

# Test Case 1
print( is_user_in_group(user_15, group_1) )
# Expected True
print( is_user_in_group(user_1, group_1) )
# Expected True
print( is_user_in_group(user_10, group_1) )
# Expected True

# Test Case 2
print( is_user_in_group(user_16, group_1) )
# Expected False
print( is_user_in_group(user_1, group_2) )
# Expected False

# Test Case 3
print( is_user_in_group("", group_1) )
# Expected False
print( is_user_in_group(None, group_1) )
# Expected False