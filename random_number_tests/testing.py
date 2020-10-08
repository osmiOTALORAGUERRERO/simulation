from distance_tester import DistanceT

class Testing(object):
    """docstring for Testing."""

    def __init__(self):
        super(Testing, self).__init__()
        self.__test = None

    def target(self, method, random_set):
        if method==1: #distance
            self.__test = DistanceT(random_set)
        elif method==2: #other in process
            pass
        else:
            print(':) Eso duele')
            exit()

        return self.__test
