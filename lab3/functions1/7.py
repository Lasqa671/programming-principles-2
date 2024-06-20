"""
Given a list of ints, return True if the 
array contains a 3 next to a 3 somewhere.
"""
def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has33([1, 3, 3]))      # True
print(has33([1, 3, 1, 3]))   # False
print(has33([3, 1, 3]))      # False