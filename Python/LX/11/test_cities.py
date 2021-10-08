import unittest
from city_functions import city_functions as cf

class test(unittest.TestCase):
    """测试名字是否通过"""

    def test_city_country_population(self):
        """能够正确的处理城市和国家和人口"""
        name = cf('北京','中国','30000')
        self.assertEqual(name,'北京-中国-population 30000')

    def test_city_country(self):
        """能够正确的处理城市和国家"""
        name = cf('北京','中国')
        self.assertEqual(name,'北京 中国')

if __name__ == '__main__':
    unittest.main()