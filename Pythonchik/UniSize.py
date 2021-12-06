class Handle:
    def __get__(self, obj, cls):
        return len(obj) if '__len__' in dir(cls) else int(obj)


def sizer(OldCls):
    class NewCls(OldCls):
        size = Handle()
    return NewCls
