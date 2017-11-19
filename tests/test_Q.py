import Q


class TestQ(unittest.TestCase):
    
    def setUp(self):
        self.hello_message = "Hello, Q User!"
        
    def test_prints_hello_Q(self):
        output = Q.hello()
        assert(output) == self.hello_message)