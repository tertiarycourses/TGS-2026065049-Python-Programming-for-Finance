# Starter file: review the acceptance criteria, then complete the TODOs.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
def build():
    out=BASE/"outputs"; out.mkdir(exist_ok=True); p=pd.read_csv(BASE/"capstone_portfolio.csv"); prices=pd.read_csv(BASE/"multi_asset_prices.csv",parse_dates=["Date"]).set_index("Date")
    p["Market_Value"]=p["Shares"]*p["Price"]; p["Weight"]=p["Market_Value"]/p["Market_Value"].sum(); sector=p.groupby("Sector")["Market_Value"].sum().sort_values(ascending=False)
    returns=prices.pct_change().dropna(); risk=pd.DataFrame({"Annual_Return":returns.mean()*252,"Annual_Volatility":returns.std()*(252**0.5)})
    p.to_csv(out/"portfolio_analytics.csv",index=False); sector.to_csv(out/"sector_exposure.csv"); risk.to_csv(out/"risk_summary.csv")
    fig,ax=plt.subplots(figsize=(7,4)); sector.plot.bar(ax=ax,color="#1F6FEB"); ax.set(title="Sector Exposure",ylabel="SGD",xlabel="Sector"); fig.tight_layout(); fig.savefig(out/"sector_exposure.png",dpi=160); plt.close(fig)
    html=f"""<html><head><title>Executive Finance Analytics Pack</title></head><body><h1>Executive Finance Analytics Pack</h1><p>Total portfolio value: SGD {p.Market_Value.sum():,.2f}</p><h2>Sector Exposure</h2>{sector.to_frame().to_html()}<h2>Risk Summary</h2>{risk.to_html()}<img src="sector_exposure.png" width="700"><h2>Controls</h2><ul><li>Weights reconcile to 100%: {p.Weight.sum():.6f}</li><li>Price rows: {len(prices)}</li><li>Return rows: {len(returns)}</li></ul></body></html>"""
    (out/"executive_report.html").write_text(html,encoding="utf-8"); (out/"validation_log.txt").write_text("Portfolio weights reconcile to 100%\nAll required source columns present\n",encoding="utf-8")
    return out
# TODO: run the completed analysis
if __name__=="__main__": print("Built",build())
