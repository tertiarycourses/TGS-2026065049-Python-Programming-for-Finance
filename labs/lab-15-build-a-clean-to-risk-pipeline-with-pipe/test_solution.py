import unittest,solution,pandas as pd
class T(unittest.TestCase):
 def test_immutable(self):
  raw=pd.read_csv(solution.BASE/'loan_pipeline.csv'); original=raw.copy(deep=True); scored=solution.run(raw); self.assertTrue(raw.equals(original)); self.assertEqual(len(scored),len(scored.Risk_Band))
if __name__=='__main__': unittest.main()
