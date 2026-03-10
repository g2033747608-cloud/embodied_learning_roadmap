'''给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的 数组下标。'''
def twoSum(nums,target):
    num_dict={}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement],index]
        num_dict[num]=index
    return []
print(twoSum([2,7,11,15], 9))