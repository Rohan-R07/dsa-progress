class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = ""
        increment = ""
        for i in range(len(digits)):
            strings = strings + str(digits[i])
        
        increment = str(int(strings) + 1)
        newList = []
        for i in range(len(increment)):
            newList.append(int(increment[i]))

        return newList
 