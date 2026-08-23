import unittest,solution,numpy as np
class T(unittest.TestCase):
 def test_corr(self):
  *_,corr,rolling,dd=solution.analyse(); self.assertTrue(np.allclose(corr,corr.T)); self.assertTrue((np.diag(corr)==1).all()); self.assertLessEqual(dd.min().min(),0)
if __name__=='__main__': unittest.main()
