
#Reference
# I find some source code in https://github.com/mugenen/LossyCounting/blob/master/lossy_counting.py
class LossyCounting(object):
    def __init__(self, e):
        self.N = 0
        self.count = {}
        self.bucketID = {}
        self.e = e
        self.b_current = 1

        # def getCount(self, item):
        # return self.count[item]

    def getBucketID(self, item):
        return self.bucketID[item]

    def trim(self):
        for item in self.count.keys():
            if self.count[item] <= self.b_current - self.bucketID[item]:
                del self.count[item]
                del self.bucketID[item]

    def addCount(self, item):
        self.N += 1
        if item in self.count:
            self.count[item] += 1
        else:
            self.count[item] = 1
            self.bucketID[item] = self.b_current - 1

        if self.N % int(1 / self.e) == 0:
            self.trim()
            self.b_current += 1

    def iterateOverThresholdCount(self, threshold_count):
        # assert threshold_count > self.e * self.N, "too small threshold"

        self.trim()
        for item in self.count:
            if self.count[item] >= threshold_count - self.e * self.N:
                yield (item, self.colsunt[item])

    def iterateOverThresholdRate(self, threshold_rate):
        return self.iterateOverThresholdCount(threshold_rate * self.N)


if __name__ == '__main__':

    counter = LossyCounting(1e-3)

    f = open('/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part4/queriesLarge.txt')
    readline=f.readlines()
    lines = filter(lambda t: t.strip(), readline)

    for line in lines:
        counter.addCount(line)

    for item, count in sorted(counter.iterateOverThresholdRate(0.01), key=lambda x: x[1]):
        print item.strip()  # , count, counter.getBucketID(item)