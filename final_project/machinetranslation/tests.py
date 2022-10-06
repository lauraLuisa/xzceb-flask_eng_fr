import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(null, null) # test when null is given as input the output is null.
        self.assertEqual('Hello', 'Bonjour')  # test when 'Hello' is given as input the output is 'Bonjour'.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(null, null) # test when null is given as input the output is null.
        self.assertEqual('Bonjour', 'Hello')  # test when 'Bonjour' is given as input the output is 'Hello'.

unittest.main()