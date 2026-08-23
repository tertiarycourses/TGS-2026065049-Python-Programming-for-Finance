# Starter file: review the acceptance criteria, then complete the TODOs.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
def analyse():
    df=pd.read_csv(BASE/"dbs_prices.csv",parse_dates=["Date"]).sort_values("Date"); required={"Open","High","Low","Close"}
    if not required.issubset(df.columns): raise ValueError(f"Missing OHLC columns: {required-set(df.columns)}")
    df["MA10"]=df["Close"].rolling(10).mean(); df["MA50"]=df["Close"].rolling(50).mean(); diff=df["MA10"]-df["MA50"]
    cross=(diff.notna()&diff.shift().notna()&((diff>0)!=(diff.shift()>0))); crossovers=df.loc[cross,["Date","Close","MA10","MA50"]]
    out=BASE/"outputs"; out.mkdir(exist_ok=True); crossovers.to_csv(out/"crossover_dates.csv",index=False); df.to_csv(out/"technical_analysis.csv",index=False)
    fig,ax=plt.subplots(figsize=(10,5)); ax.plot(df["Date"],df["Close"],label="Close",color="#5B6372",lw=1); ax.plot(df["Date"],df["MA10"],label="MA10",color="#10B981"); ax.plot(df["Date"],df["MA50"],label="MA50",color="#7C3AED"); ax.scatter(crossovers["Date"],crossovers["Close"],color="#F59E0B",zorder=4,label="Crossover"); ax.set(title="DBS Close with 10-day and 50-day Moving Averages",ylabel="SGD",xlabel="Date"); ax.legend(); fig.tight_layout(); fig.savefig(out/"moving_average_crossover.png",dpi=160); plt.close(fig)
    return df,crossovers
# TODO: run the completed analysis
if __name__=="__main__": print(analyse()[1].to_string(index=False))
