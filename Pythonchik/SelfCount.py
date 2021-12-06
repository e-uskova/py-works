class WeAre:
    quantity = 0
    
    def __init__(self):
        WeAre.quantity += 1

    def __del__(self):
        WeAre.quantity -= 1

    @property
    def count(self):
        return WeAre.quantity

    @count.setter
    def count(self, x):
        pass

    @count.deleter
    def count(self):
        pass
