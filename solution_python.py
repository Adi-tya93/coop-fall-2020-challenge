class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.stored = list()
        self.index = 0
        self.stored.append(self.value)

    def add(self, num: int):
        self.index += 1
        self.stored.insert(self.index, self.value+num)
        self.value = self.stored[self.index]
        print(val.value)
        pass

    def subtract(self, num: int):
        self.index += 1
        self.stored.insert(self.index, self.value - num)
        self.value = self.stored[self.index]
        print(val.value)
        pass

    def undo(self):
        if self.index == 0:
            print("nothing to undo")
        else:
            self.index -= 1
            self.value = self.stored[self.index]
            print(self.value)
        pass

    def redo(self):
        if self.index == len(self.stored)-1:
            print(self.value, "(nothing to redo)")
        else:
            self.index += 1
            self.value = self.stored[self.index]
            print(self.value)
        pass

    def bulk_undo(self, steps: int):
        if self.index - steps < 0:
            self.index = 0
            self.value = self.stored[self.index]
            print(self.value)
        else:
            self.index -= steps
            self.value = self.stored[self.index]
            print(self.value)
        pass

    def bulk_redo(self, steps: int):
        if self.index + steps > len(self.stored)-1:
            self.index = len(self.stored)-1
            self.value = self.stored[self.index]
            print(self.value)
        else:
            self.index += steps
            self.value = self.stored[self.index]
            print(self.value)
        pass
