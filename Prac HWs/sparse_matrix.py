# -*- coding: utf-8 -*-


class CooSparseMatrix:

    def __init__(self, ijx_list, shape, antirec=True):
        self.ijx_dict = {}
        for i, j, x in ijx_list:
            if (i, j) in self.ijx_dict:
                raise TypeError
            if (type(i) != int) or (type(j) != int):
                raise TypeError
            elif x != 0:
                self.ijx_dict[(i, j)] = x
        if ((type(shape) != tuple) or (len(shape) != 2) or
                (type(shape[0]) != int) or (type(shape[1]) != int)):
            raise TypeError
        self.shape = shape
        if antirec:
            self.T = CooSparseMatrix([(key[1], key[0], self[key])
                                     for key in list(self.ijx_dict.keys())],
                                     (self.shape[1], self.shape[0]),
                                     antirec=False)
#         else:
#             self.T = None

    def __getitem__(self, index):
        if type(index) == int:
            if index >= self.shape[0]:
                raise TypeError
            my_mtr = []
            my_str = ()
            for j in range(self.shape[1]):
                if ((index, j) in self.ijx_dict):
                    my_str = (index, j, self.ijx_dict[(index, j)])
                else:
                    my_str = (index, j, 0)
                my_mtr.append(my_str)
            return CooSparseMatrix(ijx_list=my_mtr, shape=(1, self.shape[1]))

        elif type(index) == tuple:
            if (index[0] >= self.shape[0]) or (index[1] >= self.shape[1]):
                raise TypeError
            if (index[0], index[1]) in self.ijx_dict:
                return self.ijx_dict[index[0], index[1]]
            else:
                return 0

        else:
            raise TypeError

    def __setitem__(self, key, value):
        if value != 0:
            self.ijx_dict[key] = value
            self.T.ijx_dict[(key[1], key[0])] = value
        elif key in self.ijx_dict:
            del self.ijx_dict[key]

    def __add__(self, other):
        if self.shape != other.shape:
            raise TypeError
        else:
            return CooSparseMatrix([key + (self[key] + other[key],) for key
                                    in set(list(self.ijx_dict.keys()) +
                                           list(other.ijx_dict.keys()))],
                                   self.shape)

    def __sub__(self, other):
        if self.shape != other.shape:
            raise TypeError
        else:
            return CooSparseMatrix([key + (self[key] - other[key],) for key
                                    in set(list(self.ijx_dict.keys()) +
                                           list(other.ijx_dict.keys()))],
                                   self.shape)

    def __mul__(self, other):
        if type(other) != int:
            raise TypeError
        else:
            return CooSparseMatrix([key + (self[key]*other,) for key
                                    in list(self.ijx_dict.keys())], self.shape)

    def __rmul__(self, other):
        if type(other) != int:
            raise TypeError
        else:
            return CooSparseMatrix([key + (self[key]*other,) for key
                                    in list(self.ijx_dict.keys())], self.shape)

    def __setattr__(self, name, value):
        if name == 'T':
            if 'T' in self.__dict__:
                raise AttributeError
        if name == 'shape':
            if 'shape' in self.__dict__:
                if ((type(value) != tuple) or (len(value) != 2) or
                        (type(value[0]) != int) or (type(value[1]) != int)):
                    raise TypeError
                if (value[0] * value[1]) != (self.shape[0] * self.shape[1]):
                    raise TypeError
                else:
                    new_dict = {}
                    for key in list(self.ijx_dict.keys()):
                        new_dict[divmod(key[0] * self.shape[1] + key[1],
                                        value[1])] = self.ijx_dict[key]
                    self.ijx_dict = new_dict.copy()
                    self.__dict__[name] = value
                    for key in list(self.ijx_dict.keys()):
                        self.T.ijx_dict[(key[1], key[0])] = self[key]
            else:
                self.__dict__[name] = value
        else:
            self.__dict__[name] = value
