import unittest


class TestSearchusers(unittest.TestCase):
    def test_add(self):
        calculator.set_memory(0)
        calculator.add(10)
        result = calculator.get_result()
        self.assertEqual(result, 10)

    def test_subtract(self):
        calculator.set_memory(12)
        calculator.sub(2)
        result = calculator.get_result()
        self.assertEqual(result, 10)

    def test_multiply(self):
        calculator.set_memory(9)
        calculator.mult(2)
        result = calculator.get_result()
        self.assertEqual(result, 18)

    def test_divide(self):
        calculator.set_memory(40)
        calculator.div(10)
        result = calculator.get_result()
        self.assertEqual(result, 4)

    def test_root(self):
        calculator.set_memory(20)
        calculator.root(2)
        result = calculator.get_result()
        self.assertEqual(result, 4.47213595499958)


if __name__ == '__main__':

    from Calculator_Class import Calculator

    calculator = Calculator(memory = 0)

    unittest.main()
