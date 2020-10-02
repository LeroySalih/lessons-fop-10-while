import unittest
from subprocess import run

from main import *


class MyTest(unittest.TestCase):

    def test_starter(self):
        result = run(["python", "./lesson-files.py"], input=b"\n", capture_output=True)
        self.assertEqual(result, b'20,21,22,23,24,25,26,27,28,29,30\n')
"""
    def test_variable_exists(self):
        self.assertNotEqual(pupil_age, None, "The variable pupil age has not been declared.")    
        
    def test_fn(self):
        self.assertEqual(mySum(5, 4), 9)
            
    def test_output(self):
        result = run(["python", "main.py"], input=b"12\n", capture_output=True)
        self.assertEqual(result.stdout, b"Enter your age:You are 12 years old\n", "Returned: {0}".format(result.stdout))        
"""

if __name__ == "__main__":
    unittest.main()