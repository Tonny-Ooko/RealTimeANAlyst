import pandas as pd


file_path = "Raw Data.csv"
df = pd.read_csv(file_path)


df["TimeStamp"] = pd.to_datetime(df["Date"] + " " + df["Start Time"], format="%m/%d/%Y %H:%M")


df["Hour"] = df["TimeStamp"].dt.floor("h")


df.rename(columns={
    "Offered Calls": "Offered_Calls",
    "ACD Calls": "Answered_Calls",
    "Aban Calls": "Abandoned_Calls",
    "ACD Time": "Handle_Time",
    "Service Level": "Service_Level",
    "Avg Speed Ans": "ASA",
}, inplace=True)


hourly_report = df.groupby("Hour").agg({
    "Offered_Calls": "sum",
    "Answered_Calls": "sum",
    "Abandoned_Calls": "sum",
    "Handle_Time": "mean",
    "Service_Level": "mean",
    "ASA": "mean"
}).reset_index()

hourly_report["Abandon %"] = (hourly_report["Abandoned_Calls"] / hourly_report["Offered_Calls"]) * 100
hourly_report["Service Level %"] = hourly_report["Service_Level"] * 100
hourly_report["AHT"] = hourly_report["Handle_Time"]
hourly_report["Occupancy %"] = (hourly_report["Handle_Time"] / (hourly_report["Handle_Time"] + df["Avail Time"].mean())) * 100


hourly_report.rename(columns={"ASA": "Average Speed of Answer (ASA)"}, inplace=True)


print(hourly_report)


hourly_report.to_csv("hourly_performance_report.csv", index=False)

print("\nHourly Performance Report saved as 'hourly_performance_report.csv'")
