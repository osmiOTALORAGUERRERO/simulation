class DistanceT(object):
    """docstring for DistanceT."""

    def __init__(self, random_set):
        super(DistanceT, self).__init__()
        self.__random_set = random_set
        self.__interval = {"alpha":0.3, "beta":0.5}
        self.__theta = self.__interval["beta"] - self.__interval["alpha"]

    def set_options(self, interval, random_set=None):
        if interval["beta"] > interval["alpha"]:
            self.__interval = interval
            self.__theta = self.__interval["beta"] - self.__interval["alpha"]
        if random_set != None:
            self.__random_set = random_set

    def outcome(self):
        sh = self.size_holes()
        sh.sort()
        OF = self.observed_frequency(sh)
        sum_OF = int(sum(OF.values()))
        EF = self.expected_frequency(sum_OF, OF)
        sum_EF = int(sum(EF.values()))

        X2 = self.statistical(OF, EF)

        return X2, OF, EF

    def expected_frequency(self, sum_OF, OF):
        b = {}
        for i in OF.keys():
            if i == 0:
                b[i] = b.get(i, 0) + (sum_OF*self.__theta)
            elif i == len(OF)-1:
                b[i] = b.get(i, 0) + (sum_OF*((1-self.__theta)**i))
            else:
                b[i] = b.get(i, 0) + (sum_OF*self.__theta*((1-self.__theta)**i))
        return b

    def observed_frequency(self, size_holes):
        b = {}
        i = 0
        while len(size_holes) != 0:
            b[i] = b.get(i, 0)
            for j in range(len(size_holes)):
                if i == size_holes[0]:
                    b[i] = b.get(i, 0) + 1
                    size_holes.pop(0)
                else:
                    break
            i += 1
        return b

    def size_holes(self):
        state = 0
        size_hole = 0
        count_holes=[]
        for i in self.__random_set:
            if not(i>self.__interval['alpha'] and i<self.__interval['beta']):
                size_hole += 1
                state = 0
            else:
                state = 1

            if size_hole == 0 and state == 1:
                count_holes.append(size_hole)
            elif size_hole != 0 and state == 1:
                count_holes.append(size_hole)
                size_hole = 0
                count_holes.append(size_hole)

        return count_holes

    def statistical(self, FO, FE):
        X2 = 0
        for i in range(len(FO)):
            X2 += ((FO[i]-FE[i])**2)/FE[i]
        return X2
