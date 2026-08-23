from pathlib import Path
import pandas as pd
import numpy as np
BASE=Path(__file__).resolve().parent
def clean_data(df): return df.drop_duplicates("Applicant_ID").dropna(subset=["Annual_Income","Monthly_Debt","Credit_Score"]).copy()
def add_features(df):
    out=df.copy(); out["Monthly_Income"]=out["Annual_Income"]/12; out["DTI"]=out["Monthly_Debt"]/out["Monthly_Income"]; return out
def score_risk(df):
    out=df.copy(); out["Risk_Band"]=np.select([(out["DTI"]>0.5)|(out["Credit_Score"]<620),(out["DTI"]>0.35)|(out["Credit_Score"]<700)],["High","Medium"],default="Low"); return out
def summarise(df): return df.groupby("Risk_Band",dropna=False).agg(Applicants=("Applicant_ID","count"),Mean_DTI=("DTI","mean")).reset_index()
def run(raw): return raw.pipe(clean_data).pipe(add_features).pipe(score_risk)
if __name__=="__main__":
    raw=pd.read_csv(BASE/"loan_pipeline.csv"); scored=run(raw); scored.to_csv(BASE/"scored_loans.csv",index=False); print(summarise(scored))
