import unittest,solution
class T(unittest.TestCase):
 def test_reconcile(self):
  m,s,p=solution.analyse(); self.assertAlmostEqual(m.Exposure.sum(),s.Exposure.sum()); self.assertAlmostEqual(m.Exposure.sum(),p.to_numpy().sum())
if __name__=='__main__': unittest.main()
