class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        # newList = []
        # newDict = {}
        # string = ""
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i] == list2[j]:
        #             newDict[list1[i]] = i+j

        # smallest = min(newDict.values())
        # newList = []
        # for key,value in newDict.items():
        #     if len(newDict) == 1:
        #         return [key]
            
        #     if smallest == value:
        #         newList.append(key)
            
        # return newList


        dict1 = {}
        newDict = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i
        
        for k in range(len(list2)):
            if list2[k] in dict1:
               newDict[list2[k]] = k + dict1[list2[k]]  
        smallest = min(newDict.values())
        newList = []
        for key,value in newDict.items():
            if len(newDict) == 1:
                return [key]
            
            if smallest == value:
                newList.append(key)
            
        return newList
