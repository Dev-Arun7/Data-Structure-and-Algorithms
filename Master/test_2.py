class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enque(self, data):
        self.s1.append(data)

    def deque(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return None
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop(0)
                self.s2.append(temp)

            return self.s2.pop(0)
            
        else:
            return self.s2.pop(0)



