def lin(elem):
    li = []
    try:
        iterator = iter(elem)
    except TypeError:
        return [elem]
    else:
        try:
            elem.isalpha()
            if len(elem) > 1:
                raise AttributeError
        except AttributeError:
            for obj in iterator:
                li = li + lin(obj)
            return li
        else:
            return [elem]


class linearize:

    def __init__(self, input_list):
        self.ret_val_pos = -1
        self.input_list = lin(input_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.ret_val_pos += 1
        if self.ret_val_pos >= len(self.input_list):
            raise StopIteration
        else:
            return self.input_list[self.ret_val_pos]
