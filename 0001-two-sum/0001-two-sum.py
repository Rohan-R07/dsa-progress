
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        newDic = dict()

        for index,value in enumerate(nums):
            number = target - value


            if number in newDic:
                return [newDic[number],index]
            
            newDic[value] = index
        
