import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


adherence_file = "adherence_data.xlsx"
agents_file = "agents_roster.xlsx"

adherence_df = pd.read_excel(adherence_file, sheet_name="Raw Data Adherence")
agents_df = pd.read_excel(agents_file, sheet_name="Agents Roster")


adherence_df.columns = adherence_df.columns.str.strip()


adherence_df['Scheduled Time'] = pd.to_datetime(adherence_df['Scheduled Time'], errors='coerce')


if not adherence_df['Scheduled Time'].isnull().all():
    last_4_weeks = adherence_df['Scheduled Time'] >= (adherence_df['Scheduled Time'].max() - pd.Timedelta(weeks=4))
    adherence_df = adherence_df[last_4_weeks]

merged_df = adherence_df.merge(agents_df, on="Agent Name", how="left")


if 'Adherence Rate' in merged_df.columns:
    merged_df['Adherence Rate'] = pd.to_numeric(merged_df['Adherence Rate'], errors='coerce')
    df_filtered = merged_df[['Agent Name', 'Adherence Rate']].copy()
    df_filtered.dropna(inplace=True)


    df_sorted = df_filtered.groupby('Agent Name')['Adherence Rate'].mean().sort_values(ascending=False).reset_index()


    print(df_sorted)


    def adherence_color(value):
        if value >= 85:
            return "#4CAF50"
        elif 70 <= value < 85:
            return "#FF9800"
        else:
            return "#F44336"

    colors = df_sorted['Adherence Rate'].apply(adherence_color).tolist()

    # Plot
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Agent Name", y="Adherence Rate", data=df_sorted, palette=colors, dodge=False)
    plt.axhline(85, color='#4CAF50', linestyle='--', label='High Adherence (85%+)')
    plt.axhline(70, color='#FF9800', linestyle='--', label='Medium Adherence (70-84%)')
    plt.axhline(50, color='#F44336', linestyle='--', label='Low Adherence (<70%)')

    plt.xlabel("Agent Name")
    plt.ylabel("Adherence Rate (%)")
    plt.title("Agent Adherence Scores - Last 4 Weeks")
    plt.xticks(rotation=90)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

else:
    print("Error: 'Adherence Rate' column not found in merged DataFrame.")


plt.bar(['Agent 1', 'Agent 2'], [80, 90])
plt.show()
