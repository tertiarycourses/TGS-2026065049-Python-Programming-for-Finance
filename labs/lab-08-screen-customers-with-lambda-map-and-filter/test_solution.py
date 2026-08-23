import unittest,solution
class T(unittest.TestCase):
 def test_equal(self):
  a,b=solution.screen(solution.load_rows()); self.assertEqual(a,b)
if __name__=='__main__': unittest.main()
