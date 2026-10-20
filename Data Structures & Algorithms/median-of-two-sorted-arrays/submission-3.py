class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        n3 = []
        l = 0
        r = 0

        '''
        nums1 = [1,3]
      . 
        nums2 = [2,4]


                 .    
        while (l < n1 or r < n2):
            if nums1[l] <= nums2[r]:
                l += 1
                n3.append(nums1[l])
            else:
                n3.append(nums2[r])
                r += 1
            
        if l < n1: 
            n3.append(nums1[l])
            l += 1
        if r < n2:
            n3.append(nums2[r])
            r += 1

        print(n3)

        '''
        if nums1 == []:
            n3 = nums2
        elif nums2 == []:
            n3 = nums1
        else:
            while (l < n1 and r < n2):
                if nums1[l] <= nums2[r]:
                    n3.append(nums1[l])
                    l += 1
                else:
                    n3.append(nums2[r])
                    r += 1   
            while l < n1: 
                n3.append(nums1[l])
                l += 1
            while r < n2:
                n3.append(nums2[r])
                r += 1
        n = len(n3)
        l = 0
        r = n - 1
        m = (l + r) // 2
        if  n % 2 == 0:
            return (n3[m] + n3[m+1])/ 2
        else:
            return n3[m]



        


        