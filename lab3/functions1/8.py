"""
Write a function that takes in a list of 
integers and returns True if it contains 
007 in order
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""
def spy_game(nums):
    # Initialize a flag to track if we have seen '0' and '00' in order
    seen_0 = False
    seen_00 = False
    
    # Iterate through the list of numbers
    for num in nums:
        if num == 0:
            if not seen_0:
                seen_0 = True
            elif seen_0 and not seen_00:
                seen_00 = True
        elif num == 7:
            if seen_00:
                return True
    
    # If we finish iterating and never return True, return False
    return False

# Test cases
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False
