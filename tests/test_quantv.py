import quantv
import unittest


class TestQuantV(unittest.TestCase):
    
    def setUp(self):
        self.hello_message = "Hello, Q User!"
        
    def test_prints_hello_QuantV(self):
        quantv.say_hello()
        
    def test_prints_sayhello(self):
        output = quantv.hello()
        assert(output == self.hello_message)   
        
    def test_isEven(self):
        output = quantv.is_even(4)
        assert(output == True)
        
    def test_isNotEven(self):
        output = quantv.is_even(5)
        assert(output == False)
        