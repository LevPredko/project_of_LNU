class Node:
    def __init__(self, data):
        if not isinstance(data, (int, float, str)):
            raise TypeError("Data must be of type int, float, or str.")
        self.value = data
