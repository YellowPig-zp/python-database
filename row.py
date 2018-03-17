import types

class Row:
    def __init__(self, items):
        assert len(items) > 0
        self.type = type(items[0])

    def join_row(self, row1, row2):
        pass

