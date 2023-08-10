import numpy as np


class RleSequence:

    def __init__(self, input_sequence):

        if input_sequence.size == 0:
            raise TypeError
        self.values = \
            np.hstack((input_sequence[np.hstack((np.diff(input_sequence) != 0,
                                                 [False]))],
                       input_sequence[-1]))
        self.repeat = \
            np.hstack(((np.where(np.hstack((np.diff(input_sequence) != 0,
                                            [False]))))[0],
                       input_sequence.size - 1))\
            - np.hstack(([-1],
                         (np.where(np.hstack((np.diff(input_sequence) != 0,
                                              [False]))))[0]))

    def __getitem__(self, i):
        if type(i) == slice:
            return(np.array([self.values[sum(np.cumsum(self.repeat) <= j)]
                             for j in range(0 if i.start is None
                                            else sum(self.repeat) + i.start
                                            if i.start < 0
                                            else sum(self.repeat)
                                            if i.start > sum(self.repeat)
                                            else i.start,
                                            sum(self.repeat) if i.stop is None
                                            else sum(self.repeat) + i.stop
                                            if i.stop < 0
                                            else sum(self.repeat)
                                            if i.stop > sum(self.repeat)
                                            else i.stop,
                                            1 if i.step is None
                                            else i.step)]))
        elif type(i) == int:
            if i < 0:
                i = sum(self.repeat) + i
            return self.values[sum(np.cumsum(self.repeat) <= i)]
        else:
            raise TypeError

    def __contains__(self, target_elem):
        return target_elem in self.values
