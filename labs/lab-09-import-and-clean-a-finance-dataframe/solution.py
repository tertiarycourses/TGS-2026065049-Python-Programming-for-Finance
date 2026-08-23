from pathlib import Path
import pandas as pd
BASE=Path(__file__).resolve().parent
def clean_prices(path=BASE/"dirty_prices.csv"):
    raw=pd.read_csv(path); before={"rows":len(raw),"duplicates":int(raw.duplicated("Date").sum()),"missing_close":int(raw["Close"].isna().sum())}
    df=raw.copy(); df["Date"]=pd.to_datetime(df["Date"],errors="coerce")
    for c in ["Open","High","Low","Close"]: df[c]=pd.to_numeric(df[c],errors="coerce")
    df=df.dropna(subset=["Date"]).drop_duplicates("Date",keep="last").sort_values("Date")
    df["Close"]=df["Close"].ffill(limit=2); after={"rows":len(df),"missing_close":int(df["Close"].isna().sum())}
    return df,before,after
if __name__=="__main__":
    df,before,after=clean_prices(); df.to_csv(BASE/"clean_prices.csv",index=False)
    (BASE/"quality_report.txt").write_text(f"before={before}\nafter={after}\n",encoding="utf-8"); print(before,after)
