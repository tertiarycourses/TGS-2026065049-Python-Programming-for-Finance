from pathlib import Path
import csv
BASE=Path(__file__).resolve().parent

def analyse(path=BASE/"holdings.csv"):
    valid=[]; errors=[]
    with open(path,newline="",encoding="utf-8") as f:
        for n,row in enumerate(csv.DictReader(f),1):
            try:
                value=float(row["Shares"])*float(row["Price"]); valid.append({**row,"Value":value})
            except (ValueError,TypeError): errors.append(f"row {n}: invalid numeric value"); continue
    total=sum(r["Value"] for r in valid)
    weights={r["Ticker"]:r["Value"]/total for r in valid}; overweight=[k for k,v in weights.items() if v>0.20]
    return valid,errors,weights,overweight

if __name__=="__main__":
    valid,errors,weights,overweight=analyse(); print("valid",len(valid),"errors",errors)
    print("weight total",sum(weights.values()),"overweight",overweight)
