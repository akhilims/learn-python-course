# unittest: the first test for the race program
# Every cell of the notebook, in order, as one script (run: python unittest__the_first_test_for_the_race_program.py)

# Import unittest: the testing tool that comes with Python

import unittest
print(unittest.TestCase.__name__, "is ready")

# The helper we will test: cut time from a lap

def faster(lap: int, cut: int) -> int:
    return lap - cut

print(faster(60, 5))

# A test case class with assertEqual

class FasterTest(unittest.TestCase):
    def test_cut(self):
        got = faster(60, 5)
        self.assertEqual(got, 55)

print(FasterTest.__name__, "defined")

# Run the test: case.run() and wasSuccessful()

case = FasterTest("test_cut")
result = case.run()
print(result.wasSuccessful())

# A volunteer breaks the helper by mistake

def faster(lap: int, cut: int) -> int:
    return lap + cut

print(faster(60, 5))

# Run the same test again: it catches the mistake

result = case.run()
print(result.wasSuccessful())
