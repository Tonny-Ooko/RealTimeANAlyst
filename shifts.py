import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = "shift_data.xlsx"
df = pd.read_excel(file_path, sheet_name="Shifts Data")
df.columns = df.columns.str.strip()

df["Shift Time"] = pd.to_timedelta(df["Shift Time"], unit="D")
df["Shift Time"] = df["Shift Time"].apply(lambda x: (pd.Timestamp("00:00") + x).time())


staffing_count = df["Shift Time"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
sns.barplot(x=staffing_count.index, y=staffing_count.values, palette="Blues_r")
plt.xlabel("Shift Time")
plt.ylabel("Number of Agents")
plt.title("Agent Staffing by Shift Time")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


df["Shift Start"] = pd.to_datetime(df["Shift Time"], format="%H:%M:%S")
df["Shift End"] = df["Shift Start"] + pd.Timedelta(hours=9)


time_range = pd.date_range("00:00", "23:00", freq="H").time
coverage = {time: 0 for time in time_range}


for _, row in df.iterrows():
    for time in time_range:
        if row["Shift Start"].time() <= time < row["Shift End"].time():
            coverage[time] += 1


coverage_df = pd.DataFrame(list(coverage.items()), columns=["Time", "Active Agents"])
coverage_df["Time"] = pd.to_datetime(coverage_df["Time"], format="%H:%M")


plt.figure(figsize=(12, 6))
sns.lineplot(x=coverage_df["Time"], y=coverage_df["Active Agents"], marker="o", color="b")
plt.xlabel("Time of Day")
plt.ylabel("Number of Active Agents")
plt.title("Intraday Agent Coverage")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()


