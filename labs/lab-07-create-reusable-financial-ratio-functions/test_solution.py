import unittest,solution
class T(unittest.TestCase):
 def test_ratios(self):
  r=solution.calculate_ratios(11290000000,20180000000,62400000000,739000000000); self.assertAlmostEqual(r['ROE'],.180929,places=5)
 def test_zero(self): self.assertIsNone(solution.roe(1,0))
if __name__=='__main__': unittest.main()
