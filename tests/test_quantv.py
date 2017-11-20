import quantv
import unittest


class TestQuantV(unittest.TestCase):
    
    def setUp(self):
        self.hello_message = "Hello, Q User!"
        
    def test_prints_hello_QuantV(self):
        output = quantv.hello()
        assert(output == self.hello_message)
        
    def is_even(x):
        if x%2==0:
            return True
        else:
            return False