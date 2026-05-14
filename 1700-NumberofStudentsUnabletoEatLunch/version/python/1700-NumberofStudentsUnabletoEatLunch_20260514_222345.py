# Last updated: 5/14/2026, 10:23:45 PM
1class Solution:
2    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
3        circle_student_count = 0
4        square_student_count = 0
5
6        for student in students:
7            if student == 0:
8                circle_student_count += 1
9            else:
10                square_student_count += 1
11
12        for sandwich in sandwiches:
13            if sandwich == 0 and circle_student_count == 0:
14                return square_student_count
15
16            if sandwich == 1 and square_student_count == 0:
17                return circle_student_count
18
19            if sandwich == 0:
20                circle_student_count -= 1
21            else:
22                square_student_count -= 1
23
24        return 0