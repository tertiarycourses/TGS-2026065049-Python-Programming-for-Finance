def safe_divide(a,b): return None if b==0 else a/b
def net_margin(net_profit,revenue): return safe_divide(net_profit,revenue)
def roe(net_profit,avg_equity): return safe_divide(net_profit,avg_equity)
def roa(net_profit,avg_assets): return safe_divide(net_profit,avg_assets)
def calculate_ratios(net_profit,revenue,equity,assets):
    return {"Net Margin":net_margin(net_profit,revenue),"ROE":roe(net_profit,equity),"ROA":roa(net_profit,assets)}

if __name__=="__main__":
    for k,v in calculate_ratios(11290000000,20180000000,62400000000,739000000000).items(): print(k,f"{v:.2%}")
