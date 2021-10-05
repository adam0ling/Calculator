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


calculator = Calculator(memory = 0)
acceptable_inputs = [1, 2, 3, 4, 5, 6, 7, 8]
print('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Root \n6. Set Memory\n7. Clear Memory\n8. End Program')


while True:
    choice = int(input('What is your choice? '))

    if choice not in acceptable_inputs:
        print('Incorrect Input. Try again.')
    elif choice == 1:
        add_num = int(input('What number to add? '))
        calculator.add(add_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 2:
        sub_num = int(input('What number to subtract? '))
        calculator.sub(sub_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 3:
        mult_num = int(input('What number to multiply? '))
        calculator.mult(mult_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 4:
        div_num = int(input('What number to divide? '))
        calculator.div(div_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 5:
        root_num = int(input('What number for the root? '))
        calculator.root(root_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 6:
        set_num = int(input('What number to set the memory? '))
        calculator.set_memory(set_num)
        print(f'Result: {calculator.get_result()}')
    elif choice == 7:
        calculator.clear_memory()
        print(f'Result: {calculator.get_result()}')
    elif choice == 8:
        print(f'Result: {calculator.get_result()}. Good-Bye')
        break
