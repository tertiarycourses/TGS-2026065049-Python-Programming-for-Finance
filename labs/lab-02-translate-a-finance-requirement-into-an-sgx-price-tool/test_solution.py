import unittest,solution
class T(unittest.TestCase):
 def test_report(self):
  self.assertIn('NO DATA',solution.format_report([{'Ticker':'BAD','Company':'Invalid','Close':''}]))
if __name__=='__main__': unittest.main()
