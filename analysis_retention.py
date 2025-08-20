# analysis_retention.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention": [67.11, 68.79, 69.12, 74.59]
})

average = df["Retention"].mean()
print("Average (unrounded):", average)        # 69.9025
print("Average (rounded, 1 decimal):", round(average,1))  # 69.9

plt.figure(figsize=(10,4.5))
plt.plot(df["Quarter"], df["Retention"], marker="o")
plt.axhline(y=85, linestyle="--", linewidth=1)  # industry benchmark
plt.title("Customer Retention Rate - 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.ylim(min(df["Retention"]) - 5, 90)
plt.grid(True)
plt.tight_layout()
plt.savefig("retention_trend.png", dpi=150)
print("Saved: retention_trend.png")
# Uncomment plt.show() if running locally with GUI
# plt.show()
