from pathlib import Path
import csv
BASE=Path(__file__).resolve().parent

def load_portfolio():
    with open(BASE/"portfolio.csv",newline="",encoding="utf-8") as f: return list(csv.DictReader(f))

def analyse(rows):
    values={r["Ticker"]:float(r["Shares"])*float(r["Price"]) for r in rows}; total=sum(values.values())
    weights={k:v/total for k,v in values.items()}; sectors={r["Sector"] for r in rows}
    return values,weights,sectors

if __name__=="__main__":
    values,weights,sectors=analyse(load_portfolio())
    for ticker in values: print(f"{ticker:<8} SGD {values[ticker]:>12,.2f} {weights[ticker]:>7.2%}")
    print("Total weight",f"{sum(weights.values()):.2%}","Sectors",sorted(sectors))
