import unittest,solution
class T(unittest.TestCase):
 def test_payment(self): self.assertAlmostEqual(solution.monthly_payment(500000,2.6,25),2268.35,places=2)
 def test_zero(self): self.assertAlmostEqual(solution.monthly_payment(1200,0,1),100)
if __name__=='__main__': unittest.main()
