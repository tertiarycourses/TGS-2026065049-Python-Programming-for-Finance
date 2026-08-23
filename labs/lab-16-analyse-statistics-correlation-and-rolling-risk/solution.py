from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
def analyse():
    prices=pd.read_csv(BASE/"multi_asset_prices.csv",parse_dates=["Date"]).set_index("Date"); returns=prices.pct_change().dropna()
    stats=returns.describe().T; cov=returns.cov(); corr=returns.corr(); rolling=returns.rolling(20).std()*np.sqrt(252)
    wealth=(1+returns).cumprod(); drawdown=wealth/wealth.cummax()-1
    out=BASE/"outputs"; out.mkdir(exist_ok=True); stats.to_csv(out/"statistics.csv"); corr.to_csv(out/"correlation.csv"); rolling.to_csv(out/"rolling_volatility.csv")
    fig,ax=plt.subplots(figsize=(10,4)); ax.plot(drawdown.index,drawdown); ax.set(title="Portfolio Component Drawdowns",ylabel="Drawdown",xlabel="Date"); fig.tight_layout(); fig.savefig(out/"drawdown.png",dpi=160); plt.close(fig)
    return returns,stats,cov,corr,rolling,drawdown
if __name__=="__main__":
    _,stats,_,corr,_,dd=analyse(); print(stats[["mean","std"]]); print(corr); print("max drawdown",dd.min().min())
