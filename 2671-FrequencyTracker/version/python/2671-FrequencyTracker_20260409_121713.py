# Last updated: 4/9/2026, 12:17:13 PM
1class FrequencyTracker:
2    def __init__(self):
3        self.count = defaultdict(int)
4        self.freq = defaultdict(int)
5
6    def add(self, number: int) -> None:
7        self.freq[self.count[number]] -= 1
8        self.count[number] += 1
9        self.freq[self.count[number]] += 1
10
11    def deleteOne(self, number: int) -> None:
12        if self.count[number] > 0:
13            self.freq[self.count[number]] -= 1
14            self.count[number] -= 1
15            self.freq[self.count[number]] += 1
16
17    def hasFrequency(self, frequency: int) -> bool:
18        return self.freq[frequency] > 0
19
20