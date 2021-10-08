class Calculator:

    def __init__(self, memory):
        self.memory = memory

    def add(self, num):
        self.memory = self.memory + num

    def sub(self, num):
        self.memory = self.memory - num

    def mult(self, num):
        self.memory = self.memory * num

    def div(self, num):
        self.memory = self.memory / num

    def root(self, root):
        self.memory = self.memory**(1/float(root))

    def get_result(self):
        return self.memory

    def clear_memory(self):
        self.memory = 0
        return self.memory

    def set_memory(self, num):
        self.memory = num
