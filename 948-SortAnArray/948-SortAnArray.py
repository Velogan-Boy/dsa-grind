# Last updated: 2/27/2026, 5:19:04 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums,0, len(nums) - 1)

    def mergeSort(self, arr, start, end):
        if start >= end:
            return [arr[start]]

        mid = (end + start) // 2

        left = self.mergeSort(arr, start, mid)
        right = self.mergeSort(arr, mid + 1, end)

        return self.merge(left,right)


    def merge(self, arr1, arr2):
        i, j, k = 0, 0, 0
        m,n = len(arr1), len(arr2)

        arr3 = [0] * (m + n)

        while i < m and j < n:
            if arr1[i] <= arr2[j]:
                arr3[k] = arr1[i]
                k+=1
                i+=1
            else:
                arr3[k] = arr2[j]
                k+=1
                j+=1

        while i < m:
            arr3[k] = arr1[i]
            k+=1
            i+=1

        while j < n:
            arr3[k] = arr2[j]
            k+=1
            j+=1

        return arr3






        