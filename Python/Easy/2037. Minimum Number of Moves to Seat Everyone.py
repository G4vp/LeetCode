from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        c = 0
        sea = sorted(seats)
        stu = sorted(students)
        for i in range(len(seats)):
            c += abs(sea[i] - stu[i])
        return c