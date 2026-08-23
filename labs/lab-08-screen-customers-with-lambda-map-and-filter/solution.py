from pathlib import Path
import csv
BASE=Path(__file__).resolve().parent

def load_rows():
    with open(BASE/"applicants.csv",newline="",encoding="utf-8") as f: return list(csv.DictReader(f))
def risk_named(row): return float(row["Monthly_Debt"])/(float(row["Annual_Income"])/12)>0.45 or row["Missed_Payment"]=="True"
def screen(rows):
    enriched=list(map(lambda r:{**r,"Monthly_Income":float(r["Annual_Income"])/12},rows))
    ids_lambda=[r["Applicant_ID"] for r in filter(lambda r:float(r["Monthly_Debt"])/r["Monthly_Income"]>0.45 or r["Missed_Payment"]=="True",enriched)]
    ids_named=[r["Applicant_ID"] for r in enriched if risk_named(r)]
    return ids_lambda,ids_named
if __name__=="__main__": print(screen(load_rows()))
