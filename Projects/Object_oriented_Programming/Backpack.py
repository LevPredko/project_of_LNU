class Backpack:

    ID_counter = 1

    def __init__(self, name, color, max_size=5):
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []
        self.ID = Backpack.ID_counter
        Backpack.ID_counter += 1

    def put(self, item):
        if len(self.contents) < self.max_size:
            self.contents.append(item)
        else:
            print("No Room!")

    def take(self, item):
        self.contents.remove(item)

    def dump(self):
        self.contents = []

    def __str__(self):
        return f"Owner: {self.name}\nColor: {self.color}\nSize: {len(self.contents)}\nMax Size: {self.max_size}\nContents: {self.contents} \n"

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.color == other.color
            and len(self.contents) == len(other.contents)
        )

    def __hash__(self):
        return hash(self.name) ^ hash(self.color) ^ hash(len(self.contents))

    @staticmethod
    def find_backpack_color(backpacks, color):
        for backpack in backpacks:
            if backpack.color == color:
                return backpack
        return None
