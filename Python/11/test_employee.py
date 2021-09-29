import unittest
from employee import Employee

class Text_employee(unittest.TestCase):
    """针对Employee的测试"""
    def setUp(self):
        self.name = Employee('zhu','zhenchao',5000)
        self.name.give_raise()

