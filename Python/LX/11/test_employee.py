import unittest
from employee import Employee

class Text_employee(unittest.TestCase):
    """针对Employee的测试"""
    def setUp(self):
        self.name1 = Employee('zhu','zhenchao')
        self.name2 = Employee('zhu','zhenchao',5000)
    
    def test_give_difault_raise(self):
        self.assertEqual(self.name1.give_raise(),5000)

    def test_give_couston_raise(self):
        self.assertEqual(self.name2.give_raise(3000),8000)

if __name__ == "__main__":
    unittest.main()

    

