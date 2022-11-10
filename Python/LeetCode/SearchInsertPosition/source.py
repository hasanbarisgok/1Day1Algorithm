class Position(object):
    def __init__(self,list:list,target) -> None:
        self.list = list
        self.target = target
        print(self.searchIndex())
        
    def searchIndex(self):
        left, right = 0, len(self.list) -1
        while (left < right):
            mid = (left + right) // 2
            if self.target <= self.list[mid]:
                right = mid
            else:
                left = mid + 1
        return left

