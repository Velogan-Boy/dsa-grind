# Last updated: 2/27/2026, 10:34:57 PM
import random
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(i):
            return points[i][0]**2 + points[i][1]**2

        def partition(left, right):
            pivot_index = random.randint(left, right)
            points[pivot_index], points[right] = points[right], points[pivot_index]
            pivot_dist = distance(right)

            i = left
            for j in range(left, right):
                if distance(j) <= pivot_dist:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[right] = points[right], points[i]
            return i

        left, right = 0, len(points) - 1

        while True:
            pivot = partition(left, right)

            if pivot == k - 1:
                return points[:k]
            elif pivot < k - 1:
                left = pivot + 1
            else:
                right = pivot - 1