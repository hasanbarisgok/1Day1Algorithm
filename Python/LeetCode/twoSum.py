#Problem Name: Two Sum <= LeetCode 
#When sum of two numbers of nums list equal target, we're printing the two nums on terminal.

nums = [1,2,3,4]
target = 6
for a in range(0,len(nums)):
    for b in range(a+1,len(nums)):
        sum = nums[a] + nums[b]
        if sum == target:
         print(f"{nums[a]},{nums[b]}")
