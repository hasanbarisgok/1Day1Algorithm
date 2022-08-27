# Remove Duplicates from Sorted Array <= LeetCode
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory. 
# So we'll solve the problem with only a original nums list.

nums = [0,0,1,1,1,2,2,3,3,4]
l = 1 #We've gave the 1 value for variable l. Because we'll use variable l both counter, and new duplicate value of the list other steps. 
      #Thanks to this, we'll use the memory really low.
      #And our code will work really faster than others. 
      #You can look at my Challange details at the end of the line.(Memory Usage, Runtime etc.)

for a in range(1,len(nums)):
    if nums[a] != nums[a-1]:
        nums[l] = nums[a]
        l += 1
print(l) 


# Runtime: 61 ms, faster than 97.36% of Python online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.9 MB, less than 32.31% of Python online submissions for Remove Duplicates from Sorted Array.
