class Solution:
    def minOperations(self, logs: list[str]) -> int:
        

        counter = 0
        for log in logs:
            if log == "../" :
                if counter > 0:
                    counter -= 1

            
            elif log == "./":
                pass
            else:
                counter += 1
        return counter