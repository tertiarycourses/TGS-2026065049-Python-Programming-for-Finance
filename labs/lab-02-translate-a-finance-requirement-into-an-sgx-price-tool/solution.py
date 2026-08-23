from pathlib import Path
import csv
BASE=Path(__file__).resolve().parent

def load_prices(path=BASE/"sgx_prices.csv"):
    with open(path,newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def format_report(rows):
    lines=[]
    for row in rows:
        try: lines.append(f"{row['Ticker']:<8} {row['Company']:<24} SGD {float(row['Close']):>8,.2f}")
        except (ValueError,TypeError): lines.append(f"{row.get('Ticker','UNKNOWN'):<8} NO DATA")
    return "\n".join(lines)

def main(): print(format_report(load_prices()))
if __name__=="__main__": main()
