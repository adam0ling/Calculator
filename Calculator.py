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


calculator = Calculator(memory = 0)
acceptable_inputs = [1, 2, 3, 4, 5, 6, 7]
print('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Root\n6. Clear Memory\n7. End Program')


while True:
    choice = int(input('What is your choice? '))

    if choice not in acceptable_inputs:
        print('Incorrect Input. Try again.')
    elif choice == 1:
        calculator.add(81)
        print(f'Result: {calculator.get_result()}')
    elif choice == 2:
        calculator.sub(2)
        print(f'Result: {calculator.get_result()}')
    elif choice == 3:
        calculator.mult(3)
        print(f'Result: {calculator.get_result()}')
    elif choice == 4:
        calculator.div(6)
        print(f'Result: {calculator.get_result()}')
    elif choice == 5:
        calculator.root(4)
        print(f'Result: {calculator.get_result()}')
    elif choice == 6:
        calculator.clear_memory()
        print(f'Result: {calculator.get_result()}')
    elif choice == 7:
        print(f'Result: {calculator.get_result()}. Good-Bye')
        break
