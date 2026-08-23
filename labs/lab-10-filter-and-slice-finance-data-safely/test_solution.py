import unittest,solution
class T(unittest.TestCase):
 def test_filter(self):
  b,_,_=solution.run(); self.assertTrue((b.Sector=='Bank').all()); self.assertTrue((b.Value>20000).all())
if __name__=='__main__': unittest.main()
