import pandas as pd

# 讀取資料
df = pd.read_csv("YRBS_2007.csv")

# 只保留需要的欄位
df_clean = df[["Sleep", "SadOrHopeless"]].copy()

# 刪除空白值 (NaN)
df_clean = df_clean.dropna()

# 刪除異常值
df_clean = df_clean[
    (df_clean["Sleep"].between(1, 7)) &
    (df_clean["SadOrHopeless"].between(1, 2))
]

# 轉成整數型態
df_clean["Sleep"] = df_clean["Sleep"].astype(int)
df_clean["SadOrHopeless"] = df_clean["SadOrHopeless"].astype(int)

# 顯示結果
print("清洗後資料筆數：", len(df_clean))
print(df_clean.head())

# 存成新的 CSV
df_clean.to_csv("sleep_sad_clean.csv", index=False)

print("已輸出 sleep_sad_clean.csv")