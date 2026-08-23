def monthly_payment(principal, annual_rate, years):
    if principal < 0 or years <= 0 or annual_rate < 0: raise ValueError("Invalid loan terms")
    n=years*12; r=annual_rate/100/12
    return principal/n if r==0 else principal*(r*(1+r)**n)/((1+r)**n-1)

def loan_summary(principal,annual_rate,years):
    payment=monthly_payment(principal,annual_rate,years); n=years*12
    return {"monthly_payment":payment,"total_repayment":payment*n,"total_interest":payment*n-principal}

if __name__=="__main__":
    s=loan_summary(500000,2.6,25)
    for k,v in s.items(): print(f"{k}: SGD {v:,.2f}")
