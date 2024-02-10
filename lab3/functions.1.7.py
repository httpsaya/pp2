def find(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
nums=[1,2,3,3,4,5,6]
print(find(nums))