from ast import List
from pip import main


class Solution:
    #Problem 31
    def nextPermutation(self, nums):
        length = len(nums)
        highest_in_suffix_index = 0
        pivot = 0
        for i in range(1, length+1):
            if length-i == 0:
                nums.sort()
                return nums
            if nums[length-i-1] < nums[length-i]:
                print("Passed here")
                highest_in_suffix_index = length-i
                pivot = highest_in_suffix_index - 1
                break
        lowest_on_suffix_index = length - 1
        print(f"lowest : {lowest_on_suffix_index}, pivot : {pivot}")
        while(nums[lowest_on_suffix_index] <= nums[pivot]):
            lowest_on_suffix_index -= 1
        
        
        #Swapping
        nums[lowest_on_suffix_index], nums[pivot] = nums[pivot], nums[lowest_on_suffix_index] 

        j = length - 1
        #Arranging after lowest_on_suffix_index
       
        while(highest_in_suffix_index < j):
            nums[highest_in_suffix_index], nums[j] = nums[j], nums[highest_in_suffix_index]
            highest_in_suffix_index += 1
            j -= 1 
        return nums
    #Problem 2217
    def kthPalindrome(self, queries, intLength):
        isodd = intLength & 1
        k = 0
        if isodd:
            k = (intLength + 1) / 2
        else:
            k = intLength / 2
        base = int(10**(k-1))
        l = []
        for q in queries:
            base = int(10**(k-1))
            base = base + q - 1
            if isodd:
                base = str(base)
                num = base + base[::-1][1:]
                base = int(base)

            else:
                base = str(base)
                num = base + base[::-1]
                base = int(base)
            if len(num) == intLength:
                l.append(int(num))
            else:
                l.append(-1)        
        return l

if __name__ == "__main__":
    a = Solution()
    m = [3,2,1]
    print(a.kthPalindrome([1,2,5], 5))
   