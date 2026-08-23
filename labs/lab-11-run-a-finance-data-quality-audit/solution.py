from pathlib import Path
import json
import pandas as pd
BASE=Path(__file__).resolve().parent
def audit(path=BASE/"loans_dirty.csv"):
    df=pd.read_csv(path); issues=[]
    for idx,row in df.iterrows():
        if pd.isna(row["Applicant_ID"]): issues.append((idx,"missing Applicant_ID"))
        if pd.isna(row["Annual_Income"]) or row["Annual_Income"]<=0: issues.append((idx,"invalid Annual_Income"))
        if pd.isna(row["Debt_to_Income"]) or not 0<=row["Debt_to_Income"]<=1: issues.append((idx,"invalid Debt_to_Income"))
        if pd.isna(row["Credit_Score"]) or not 300<=row["Credit_Score"]<=850: issues.append((idx,"invalid Credit_Score"))
    dup=df[df.duplicated("Applicant_ID",keep=False)&df["Applicant_ID"].notna()].index
    for idx in dup: issues.append((idx,"duplicate Applicant_ID"))
    ex=pd.DataFrame(issues,columns=["Row","Issue"]); summary={"rows":len(df),"exceptions":len(ex),"affected_rows":int(ex["Row"].nunique())}
    return ex,summary
if __name__=="__main__":
    ex,summary=audit(); ex.to_csv(BASE/"exceptions.csv",index=False); (BASE/"audit_summary.json").write_text(json.dumps(summary,indent=2)); print(summary)
