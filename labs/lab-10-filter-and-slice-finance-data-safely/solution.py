from pathlib import Path
import pandas as pd
BASE=Path(__file__).resolve().parent
def run():
    p=pd.read_csv(BASE/"portfolio.csv"); prices=pd.read_csv(BASE/"market_prices.csv",parse_dates=["Date"]).set_index("Date")
    p["Value"]=p["Shares"]*p["Price"]; banks=p.loc[(p["Sector"]=="Bank")&(p["Value"]>20000)].sort_values("Value",ascending=False)
    label_slice=prices.loc["2025-02-03":"2025-02-14"]; position_slice=prices.iloc[22:32]
    return banks,label_slice,position_slice
if __name__=="__main__":
    banks,label_slice,position_slice=run(); banks.to_csv(BASE/"filtered_positions.csv",index=False)
    print(banks[["Ticker","Value"]]); print("loc rows",len(label_slice),"iloc rows",len(position_slice))
