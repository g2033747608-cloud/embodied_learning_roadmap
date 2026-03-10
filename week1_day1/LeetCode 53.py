def maxSubArray(nums):
    current_sum=max_sum=nums[0]
    for num in nums[1:]:
        current_sum = current_sum+num
        if num>current_sum:
            current_sum=num
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 输出6
