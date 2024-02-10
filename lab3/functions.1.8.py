def spy_game(nums):
    found_zero1 = False
    found_zero2 = False
    
    for num in nums:
        if num == 0 and not found_zero1:
            found_zero1 = True
        elif num == 0 and found_zero1 and not found_zero2:
            found_zero2 = True
        elif num == 7 and found_zero1 and found_zero2:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  
