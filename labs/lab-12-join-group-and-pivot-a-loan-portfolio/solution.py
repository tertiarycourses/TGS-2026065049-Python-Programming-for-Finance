from pathlib import Path
import pandas as pd
BASE=Path(__file__).resolve().parent
def analyse():
    apps=pd.read_csv(BASE/"loan_applications.csv"); ref=pd.read_csv(BASE/"sector_reference.csv")
    merged=apps.merge(ref,on="Sector_Code",how="left",validate="many_to_one",indicator=True)
    summary=merged.groupby("Sector",dropna=False).agg(Applications=("Applicant_ID","count"),Exposure=("Exposure","sum"),Mean_Credit_Score=("Credit_Score","mean")).reset_index()
    pivot=pd.pivot_table(merged,index="Region",columns="Risk_Band",values="Exposure",aggfunc="sum",fill_value=0)
    return merged,summary,pivot
if __name__=="__main__":
    merged,summary,pivot=analyse(); summary.to_csv(BASE/"sector_summary.csv",index=False); pivot.to_csv(BASE/"risk_pivot.csv")
    print(summary); print("reconcile",merged["Exposure"].sum(),summary["Exposure"].sum(),pivot.to_numpy().sum())
