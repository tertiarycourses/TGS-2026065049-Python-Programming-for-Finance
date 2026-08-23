from pathlib import Path
required=['portfolio_analytics.csv','sector_exposure.csv','risk_summary.csv','sector_exposure.png','executive_report.html','validation_log.txt']
out=Path(__file__).resolve().parent/'outputs'
missing=[x for x in required if not (out/x).exists()]
if missing: raise SystemExit('MISSING: '+', '.join(missing))
print('CAPSTONE PASS')
