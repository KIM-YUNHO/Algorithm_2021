from queue import PriorityQueue

class SSTNode:

    def __init__(self, level,profit, weight):
        self.level = level
        self.profit= profit
        self.weight=weight
        self.bound = 0

    def print(self):
        print(self.level, self.profit, self.weight, self.bound)


    