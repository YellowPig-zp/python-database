import types

class Column:
    def __init__(self, items):
        assert len(items) > 0
        self.type = type(items[0])

    def join_column(self, col1, col2):
        pass


