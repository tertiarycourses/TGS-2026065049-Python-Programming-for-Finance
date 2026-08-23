# Starter file: review the acceptance criteria, then complete the TODOs.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
def analyse():
    df=pd.read_csv(BASE/"dbs_prices.csv",parse_dates=["Date"]).sort_values("Date"); df["Daily_Return"]=df["Close"].pct_change()
    out=BASE/"outputs"; out.mkdir(exist_ok=True); df.to_csv(out/"returns.csv",index=False)
    fig,ax=plt.subplots(figsize=(9,4)); ax.plot(df["Date"],df["Daily_Return"]*100,color="#1F6FEB"); ax.axhline(0,color="#5B6372",lw=1); ax.set(title="DBS Daily Returns",ylabel="Return (%)",xlabel="Date"); fig.tight_layout(); fig.savefig(out/"daily_returns.png",dpi=160); plt.close(fig)
    r=df["Daily_Return"].dropna(); fig,ax=plt.subplots(figsize=(7,4)); ax.hist(r*100,bins=24,color="#10B981",edgecolor="white"); ax.axvline(r.mean()*100,color="#D92D20",label="Mean"); ax.legend(); ax.set(title="Distribution of DBS Daily Returns",xlabel="Daily return (%)",ylabel="Frequency"); fig.tight_layout(); fig.savefig(out/"return_histogram.png",dpi=160); plt.close(fig)
    return df,{"mean":r.mean(),"std":r.std(),"max_abs":r.abs().max()}
# TODO: run the completed analysis
if __name__=="__main__": print(analyse()[1])
