import unittest,solution
class T(unittest.TestCase):
 def test_boundaries(self):
  self.assertEqual(solution.classify_valuation(14.99,.12)[0],'BUY'); self.assertEqual(solution.classify_valuation(15,.12)[0],'HOLD'); self.assertEqual(solution.classify_valuation(25.01,.12)[0],'REVIEW')
if __name__=='__main__': unittest.main()
