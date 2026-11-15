# unittest and PEP 8 - Part 2
# Every cell of the notebook, in order, as one script (run: python unittest_and_PEP_8_-_Part_2.py)

# Import unittest again in a new notebook

import unittest
print("unittest ready:", unittest.TestCase.__name__)

# Messy code: it works but nobody can read it

def f(a,b):return a-b
x=f(60,5)
print(x)

# PEP 8 style: a clean function with a clear name

def lap_after_cut(lap, cut):
    return lap - cut


print(lap_after_cut(60, 5))

# A unittest test case for the clean function

class CutTest(unittest.TestCase):
    def test_cut(self):
        got = lap_after_cut(60, 5)
        self.assertEqual(got, 55)


print("defined:", CutTest.__name__)

# Run the test and check that it passed

case = CutTest("test_cut")
result = case.run()
print(result.wasSuccessful())

# A last real call with Asha's number

print(lap_after_cut(58, 3))
