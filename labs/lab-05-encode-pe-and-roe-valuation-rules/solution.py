def classify_valuation(pe,roe):
    if pe <= 0 or roe < -1: return "INVALID", "Metrics outside accepted range"
    if pe < 15 and roe >= 0.12: return "BUY", "PE below 15 and ROE at least 12%"
    if pe <= 25 and roe >= 0.08: return "HOLD", "Fair PE band and adequate ROE"
    return "REVIEW", "Valuation or profitability outside preferred range"

if __name__=="__main__":
    for pe in (14.99,15,25,25.01): print(pe,classify_valuation(pe,0.13))
