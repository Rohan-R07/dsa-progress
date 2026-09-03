class Solution:
    def segregateElements(self, arr):
        # code here
        
        negative = []
        positive = []
        for i in arr:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
    
        newArr = positive + negative
        for i in range(len(newArr)):
            arr[i] = newArr[i]
            
  