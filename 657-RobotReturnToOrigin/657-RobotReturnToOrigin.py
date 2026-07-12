# Last updated: 7/12/2026, 6:18:47 PM
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        dMap = { "U": [0,1], "R": [1,0], "D": [0, -1], "L": [-1, 0] }

        origin = [0,0]
        for d in moves:
            origin[0] += dMap[d][0]
            origin[1] += dMap[d][1]

        return origin == [0,0]


        