def findPeak(nums, left=None, right=None):

    #Sag ve sol degerlerin initialize edilmesi
    if left is None and right is None:
        left, right = 0, len(nums) -1

    #ortadaki elemanin bulunmasi. Overflow yapmak icin mid = left + (right-left) / 2
    mid = (left + right) //2

    #ortadaki elemanin, komsularindan buyuk olup olmadiginin kontrol edilmesi.
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid   

    #eger ki midin sol komsusu midden buyukse, sublistteki en buyuk degerin rekursive seklinde bulunmasi

    if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
        return findPeak(nums, left, mid -1)

    #eger ki midin sag komsusu midden buyukse, sublistteki en buyuk degerin rekursive seklinde bulunmasi

    return findPeak(nums, mid + 1, right)

def findPeakElement(nums):
    #base condition
    if not nums:
        exit(-1)

    index = findPeak(nums)
    return nums[index]

if __name__ == '__main__':
    nums = [5,20,40,60,80,100,101,99]
    print("En buyuk deger: ", findPeakElement(nums))

 
#https://www.techiedelight.com/find-peak-element-array/
